# 自动更新 v2raya 订阅，测速并选择最快的节点

## 使用方法：
1. 先安装依赖：
    ```bash
    sudo pacman -Sy python-httpx
    ```
2. 新建脚本，粘贴下面的[代码](https://fars.ee/ggDq/py)，并在底部修改 user passwd 等参数

直接运行：
```bash
python autoaya.py
```

crontab 示例：
```bash
0 4 * * * python /home/aya/autoaya.py
```

运行效果：

![图1](/pic/16.1.webp)

## 代码：
```python
#!/usr/bin/env python
"""
@File    :   autoaya.py
@Time    :   2024/02/11 16:58:23
@Author  :   Ayatale 
@Version :   1.5
@Contact :   ayatale@qq.com
@Github  :   https://github.com/brx86/
@Desc    :   自动更新订阅，选择最快的节点连接
"""

import httpx
import json


class AutoAya:
    def __init__(
        self,
        user: str,
        passwd: str,
        port: int = 2017,
        sub: int = 0,
        limit: int = 800,
    ):
        """初始化参数

        Args:
            user (str): v2raya 的用户名
            passwd (str): v2raya 的密码
            port (int, optional): v2raya 的端口，默认为 2017
            sub (int, optional): 要自动更新的订阅，默认为 0（即第一个）
            limit (int, optional): 限制最大延迟，不会选中超过这个延迟的节点，默认为 800ms
        """
        self.api = f"http://127.0.0.1:{port}/api"
        self.sub, self.limit = sub, limit
        self.sublist = []
        r = httpx.post(
            f"{self.api}/login",
            json={
                "username": user,
                "password": passwd,
            },
        )
        r.raise_for_status
        token = r.json()["data"]["token"]
        self.client = httpx.Client(headers={"Authorization": token}, timeout=30)

    def get_sublist(self) -> set[int]:
        """获取订阅的节点列表"""
        result = self.client.get(f"{self.api}/touch").json()
        raw_list = result["data"]["touch"]["subscriptions"][self.sub]["servers"]
        self.sublist = {i["id"]: i["name"] for i in raw_list}
        connected_list = {_["id"] for _ in result["data"]["touch"]["connectedServer"]}
        return connected_list

    def sort_list(self, http_list: list) -> list[tuple[int, int]]:
        """对测速后的节点列表进行排序

        Args:
            http_list (list): 测速后的节点列表

        Raises:
            Exception: 所有节点都超出设定延迟则报错

        Returns:
            list: 测速后延迟前五的节点列表
        """
        test_result = {}
        for p in http_list:
            if p["pingLatency"].endswith("ms"):
                latency = int(p["pingLatency"][:-2])
                if (latency < self.limit) and ("GPT" not in self.sublist[p["id"]]):
                    test_result[p["id"]] = latency
        sorted_result = sorted(test_result.items(), key=lambda x: x[1])
        if not sorted_result:
            raise Exception(f"Limit: {self.limit}ms, no server available.")
        if len(sorted_result) < 5:
            return sorted_result
        return sorted_result[:5]

    def test_list(self) -> list[tuple[int, int]]:
        """节点测速

        Args:
            num (int): 节点数量

        Returns:
            list: 测速后延迟前五的节点列表
        """
        print("HTTP testing...")
        plist = [
            {"id": i + 1, "_type": "subscriptionServer", "sub": self.sub}
            for i in range(len(self.sublist))
        ]
        result = self.client.get(
            f"{self.api}/httpLatency",
            params={"whiches": json.dumps(plist)},
        ).json()
        try:
            http_list = result["data"]["whiches"]
            print("Finished!")
            return self.sort_list(http_list)
        except Exception as e:
            print(repr(e), result)
            exit(1)

    def v2raya(self, action: str, pid: int = 1):
        """对 v2raya 的操作

        Args:
            action (str): 要执行的操作名称
            pid (int, optional): 节点序号，默认为 1
        """
        match action:
            case "stop":
                self.client.delete(f"{self.api}/v2ray")
                print("V2ray stopped.")
            case "start":
                self.client.post(f"{self.api}/v2ray")
                print("V2ray started.")
            case "update":
                self.client.put(
                    f"{self.api}/subscription",
                    json={
                        "id": self.sub + 1,
                        "_type": "subscription",
                    },
                )
                print(f"Subscription {self.sub} updated.")
            case "connect":
                self.client.post(
                    f"{self.api}/connection",
                    json={
                        "id": pid,
                        "_type": "subscriptionServer",
                        "sub": self.sub,
                        "outbound": "proxy",
                    },
                )
            case "disconnect":
                self.client.request(
                    method="DELETE",
                    url=f"{self.api}/connection",
                    json={
                        "id": pid,
                        "_type": "subscriptionServer",
                        "sub": self.sub,
                        "outbound": "proxy",
                    },
                )
            case _:
                print("Unknown Action!")

    def run(self):
        """开始运行"""
        self.v2raya("update")  # 更新订阅
        connected_list = self.get_sublist()  # 获取订阅节点列表
        sorted_list = self.test_list()  # 对节点进行测速排序
        self.v2raya("stop")  # 停止 v2raya
        for pid, delay in sorted_list:
            print(f"Server {pid}\tDelay: {delay}ms\t{self.sublist[pid]}")
            self.v2raya("connect", pid)  # 连接新节点
        if disconnect_list := connected_list.difference({_[0] for _ in sorted_list}):
            for pid in disconnect_list:
                print(f"Disconnect server {pid}\t{self.sublist[pid]}")
                self.v2raya("disconnect", pid)  # 断开之前的节点
        self.v2raya("start")  # 启动 v2raya


if __name__ == "__main__":
    user = "aya"  # 此处填写 v2raya 的用户名
    passwd = "aya"  # 此处填写 v2raya 的密码
    autoaya = AutoAya(user, passwd, sub=0)
    autoaya.run()
```