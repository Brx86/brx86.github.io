# 自动更新 v2raya 订阅，测速并选择最快的节点

## 使用方法：
1. 先安装依赖：
    ```bash
    sudo pacman -Sy python-httpx
    ```
2. 新建脚本，粘贴下面的[代码](https://fars.ee/js7z/py)，并在底部修改 user passwd 等参数

直接运行：
```bash
python autoaya.py
```

crontab 示例：
```bash
*/30 * * * * python /home/aya/autoaya.py
```

运行效果：

![图1](/pic/16.1.png)

## 代码：
```python
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   autoaya.py
@Time    :   2023/02/20 16:28:10
@Author  :   Ayatale 
@Version :   1.1
@Contact :   ayatale@qq.com
@Github  :   https://github.com/brx86/
@Desc    :   自动更新订阅，选择最快的节点连接
"""

import httpx, json


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
        r = httpx.post(
            f"{self.api}/login",
            json={
                "username": user,
                "password": passwd,
            },
        )
        r.raise_for_status
        token = r.json()["data"]["token"]
        self.client = httpx.Client(headers={"Authorization": token}, timeout=20)

    def get_sublist(self):
        """获取订阅的节点列表"""
        result = self.client.get(f"{self.api}/touch").json()
        sub_list = result["data"]["touch"]["subscriptions"][self.sub]["servers"]
        connected_list = result["data"]["touch"]["connectedServer"]
        return sub_list, connected_list

    def sort_list(self, http_list: list):
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
                if latency < self.limit:
                    test_result[p["id"]] = latency
        sorted_result = sorted(test_result.items(), key=lambda x: x[1])
        if not sorted_result:
            raise Exception(f"Limit: {self.limit}ms, no server available.")
        if len(sorted_result) < 5:
            return sorted_result
        return sorted_result[:5]

    def test_list(self, num: int):
        """节点测速

        Args:
            num (int): 节点数量

        Returns:
            list: 测速后延迟前五的节点列表
        """
        print(f"HTTP testing...", end="")
        plist = [
            {"id": i, "_type": "subscriptionServer", "sub": self.sub}
            for i in range(1, num + 1)
        ]
        result = self.client.get(
            f"{self.api}/httpLatency",
            params={"whiches": json.dumps(plist)},
        ).json()
        http_list = result["data"]["whiches"]
        print(f"Finished!")
        return self.sort_list(http_list)

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
                print(f"Disconnect server {pid}...")
            case _:
                print("Unknown Action!")

    def run(self):
        """开始运行"""
        self.v2raya("update")  # 更新订阅
        sub_list, connected_list = self.get_sublist()  # 获取订阅节点列表
        sorted_list = self.test_list(len(sub_list))  # 对节点进行测速排序
        self.v2raya("stop")  # 停止 v2raya
        if connected_list:
            for p in connected_list:
                self.v2raya("disconnect", pid=p["id"])  # 断开之前的节点
        for p in sorted_list:
            print(f"Server {p[0]}\tDelay: {p[1]}ms")
            self.v2raya("connect", pid=p[0])  # 连接新节点
        self.v2raya("start")  # 启动 v2raya


if __name__ == "__main__":
    user = "user"
    passwd = "passwd"
    AutoAya(user, passwd, sub=0).run()
```