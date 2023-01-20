# 拯救者R9000P设置电池充电阈值

## 脚本
```bash
#!/usr/bin/bash

if [[ "$1" == "on" ]]; then
    sudo bash -c "echo 1 > /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode"
    echo "充电阈值已经设为60%"
elif [[ "$1" == "off" ]]; then
    sudo bash -c "echo 0 > /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode"
    echo "充电阈值已经设为100%"
elif [[ "$1" == "status" ]]; then
    status=$(cat /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode)
    if [ "$status" -eq 0 ]; then
        echo "充电阈值: 100%"
    else
        echo "充电阈值: 60%"
    fi
else
    echo -e "用法:\n    batsave on\t\t启用充电阈值\n    batsave off\t\t关闭充电阈值\n    batsave status\t查看电池状态"
    exit
fi

power_now=$(cat /sys/class/power_supply/BAT0/power_now)
if [ "$power_now" -gt 0 ];then
    power_now=${power_now::0-3}
fi
energy_now=$(cat /sys/class/power_supply/BAT0/energy_now)
energy_full=$(cat /sys/class/power_supply/BAT0/energy_full)
energy_status=$(acpi -i|head -1|cut -d' ' -f 3-)
echo "电池功率: ${power_now} mW"
echo "剩余电量: ${energy_now::0-3}/${energy_full::0-3} mWh"
echo "电池状态: ${energy_status}"
```

## 效果：
![图 1](/pic/14.1.png)