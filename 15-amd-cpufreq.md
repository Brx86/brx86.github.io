# AMD CPU 调频

## `amd_pstate`​ 驱动 [[1]](https://wiki.archlinux.org/title/CPU_frequency_scaling)

> amd_pstate: This driver implements a scaling driver with an internal governor for AMD Ryzen (some Zen 2 and newer) processors.
>
> The `amd_pstate`​ CPU power scaling driver can be manually enabled when using a supported CPU (Zen 2 and newer) by adding `amd_pstate=passive`​ as a kernel parameter.

*amd_pstate*：该驱动为 AMD Ryzen（一些 Zen 2 和更新的处理器）实现了一个带有内部调节器的缩放驱动程序。当使用支持的 CPU（Zen 2 和更新版本）时，可以通过添加 `amd_pstate=passive`​ 内核参数来手动启用 *amd_pstate* CPU 频率驱动（默认为 *acpi-cpufreq*）。

经实测，启用该驱动时 R7-5800H 闲时频率由 1.2GHz 降低至 400MHz，功耗也有所降低。

‍

## `cpupower`​ 工具 [[1]](https://wiki.archlinux.org/title/CPU_frequency_scaling)

*cpupower* 是一组为辅助 CPU 调频而设计的用户空间工具。该软件包并非必须，但强烈建议安装，因为它提供了方便的命令行实用程序，并且内置 *systemd* 服务，可在启动时更改调频器。

*cpupower* 的配置文件位于 `/etc/default/cpupower`​​。此配置文件由 `/usr/lib/systemd/scripts/cpupower`​​ 中的 bash 脚本读取，而该脚本由 *systemd* 通过 `cpupower.service`​​ 激活。若要在启动时启用 *cpupower*，请执行：`systemctl enable cpupower.service`​​

可用的调速器 [[2]](https://www.kernel.org/doc/Documentation/cpu-freq/governors.txt)：

| 调速器       | 描述                                                                                                |
| ------------ | --------------------------------------------------------------------------------------------------- |
| performance  | 运行于最大频率（见 `/sys/devices/system/cpu/cpuX/cpufreq/scaling_max_freq`​​）                      |
| powersave    | 运行于最小频率（见 `/sys/devices/system/cpu/cpuX/cpufreq/scaling_min_freq`​​）                      |
| userspace    | 运行于用户指定的频率（可设置 `/sys/devices/system/cpu/cpuX/cpufreq/scaling_setspeed`​​）            |
| ondemand     | 按需快速动态调整 CPU 频率， 一有 cpu 计算量的任务，就会立即达到最大频率运行，空闲时间增加就降低频率 |
| conservative | 按需快速动态调整 CPU 频率， 但比 ondemand 的调整更保守，优雅地增加与减少频率而不是跳跃              |
| schedutil    | 基于调度程序调整 CPU 频率，旨在与 Linux 内核调度程序更好地集成                                      |

根据实际硬件，以下的调速器可能被默认启用：

* ​`ondemand`​ ：AMD 及旧款 Intel CPU。
* ​`schedutil`​ ：AMD 新款 CPU。
* ​`powersave`​ ：Intel 使用 `intel_pstate`​ 驱动的 CPU(Sandy Bridge 和更新的 CPU)。

常用命令 [[3]](https://man.archlinux.org/man/cpupower-frequency-set.1)：

```bash
# 查看所有CPU的频率
grep MHz /proc/cpuinfo
# 查看所有cpu的详细信息
cpupower -c all frequency-info
# 设置最大频率为1600MHz
cpupower frequency-set -u 1600MHz
# 设置conservative调度模式以省电
cpupower frequency-set -g conservative

# cpupower frequency-set 参数
-d --min <FREQ>
    设置最低CPU频率。
-u --max <FREQ>
    设置最低CPU频率。
-g --governor <GOV>
    设置CPU缩放调节器。选项：conservative|ondemand|userspace|powersave|performance|schedutil
-f --freq <FREQ>
    要设置的特定频率。需要启用userspace调节器。
-r --related
    同时修改所有与硬件关联的CPU。

```

---

1. [Arch Wiki：CPU 调频](https://wiki.archlinux.org/title/CPU_frequency_scaling)
2. [Kernel：cpu-freq/governors.txt](https://www.kernel.org/doc/Documentation/cpu-freq/governors.txt)
3. [Arch Man Pages：cpupower-frequency-set](https://man.archlinux.org/man/cpupower-frequency-set.1)
