# Xstop 暂停/恢复 X11 窗口

> 轻点即可暂停/恢复 x11 窗口，以降低cpu占用，减少发热。
> 
> 受 xkill 和 xsuspender 启发。

## 1. Github地址
https://github.com/Brx86/Xstop

## 2. 使用方法
在 Archlinux 上安装：
```bash
paru -S xstop
```
然后在系统设置里添加一个快捷键，命令为 `xstop`

按下快捷键，光标变成十字形，鼠标左键点击任意 x11 窗口，即可暂停该窗口的进程与子进程；再次按下快捷键点击即可恢复。在暂停期间该窗口无响应，显示画面可能异常，操作会一直堵塞直到恢复。

## 3. 脚本内容
```python
#!/usr/bin/python3
import os, re

# 正则匹配窗口的 PID 和 CLASS 名
cmd = os.popen("xprop -notype _NET_WM_PID WM_CLASS")
info = re.findall(r"= (\d+)\n.+\"([\w\-]+)", cmd.read())
if info:
    pid, name = info[0]
    # 获取该父进程ID的所有直接子进程的 PID
    cmd = os.popen(f"pgrep -P {pid}")
    child_pids = cmd.read().replace("\n", " ")
    # 获取该进程当前状态（ T 为已暂停）
    cmd = os.popen(f"ps -p {pid} -o state=")
    state = cmd.read().strip()
    if state == "T":
        # 如果已暂停，则发送恢复信号
        os.popen(f"kill -CONT {pid} {child_pids}")
        os.popen(f"notify-send 'Resume: {name}' -i xstop-resume -t 5000")
    else:
        # 如果正在运行，则发送暂停信号
        os.popen(f"kill -STOP {pid} {child_pids}")
        os.popen(f"notify-send 'Pause: {name}' -i xstop-pause -t 5000")
```