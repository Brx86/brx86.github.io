# 使用python批量处理ssh日志

> 在/var/log/secure可以看到登陆的情况
> 在/var/log/btmp中可以查看到登陆失败的记录（可通过**lastb**命令进行检查）
> 在/var/log/lastlog中可以查看最近登陆的记录 （可通过**last**命令进行检查）
> ssh防攻击可以增加IP白名单/etc/hosts.allow和黑名单/etc/hosts.deny

我在洛杉矶的一个vps几个月前曾被ssh暴力破解过，几天就跑完了4.4T的流量。当时的密码也确实过于简单，在此之后我就使用强密码与密钥了。即便如此，来自世界各地的暴力破解也从未停歇。（别问为什么不上防火墙，问就是太懒）

失败的尝试必然会留下记录，这些都在ssh日志里记的清清楚楚。这里我就使用python脚本对日志做一些简单处理。

### 使用lastb命令查看日志并保存到文件

```bash
sudo lastb > fail_ip.txt
```

#### 日志格式如图所示：

![图 1](/pic/6.1.webp)

不看不知道，一看吓一跳，这台vps开机不到两个月，就已经有将近1.5w行的ssh登陆失败记录了。



### 使用python对日志文本进行处理


```bash
import requests, re
from collections import Counter

#添加请求头
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
}

#定义空列表与正则表达式
ip_list = []
ip_pattern = re.compile('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}')
addr_pattern = re.compile('ASN归属地":"(.*?)"')

#读取导出的ssh登陆失败记录，加入到空列表
with open('./fail_ip.txt', 'r') as f:
    for line in f:
        ip_list.append(ip_pattern.findall(line)[0])

#对列表里的ip进行计数，生成字典
ip_count = dict(Counter(ip_list))

#依次读取字典中的ip，请求ip138，查询归属地并加入字典
for ip in ip_count:
    back = requests.get(
        f'https://www.ip138.com/iplookup.asp?action=2&ip={ip}',
        headers=headers)
    back.encoding = 'gb2312' #自动识别编码失败，手动指定gb2312
    ip_addr = addr_pattern.findall(back.text)[0]
    ip_count[ip] = [ip_count[ip], ip_addr]

#按照尝试次数，从高到底对字典元素进行排序
ip_sum = sorted(ip_count.items(),
                key=lambda ic: (ic[1][0], ic[0][0]),
                reverse=True)

#处理结果写入csv
with open('./sum_ip.csv', 'a+') as f:
    f.write('IP地址,尝试次数,IP归属地\n')
    for i in range(len(ip_sum)):
        f.write(f'{ip_sum[i][0]},{ip_sum[i][1][0]},{ip_sum[i][1][1]}\n')
        
#记录尝试登陆次数大于10次的ip
with open('./deny_ip.txt', 'a+') as f:
    for i in range(len(ip_sum)):
        if ip_sum[i][1][0] > 10:
            f.write(f'sshd: {ip_sum[i][0]}\n')
```

#### 最终得到csv如图（共300余行，仅展示一部分）

![图 2](/pic/6.2.webp)

#### 得到即将加入的黑名单如图：

![图 3](/pic/6.3.webp)

### 修改/etc/hosts.deny

```bash
sudo nano /etc/hosts.deny
```

把刚才导出的deny_ip.txt的内容加到hosts.deny里即可。
