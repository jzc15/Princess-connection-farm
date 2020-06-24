# Princess connection 公主连结农场脚本v0.3

![](https://img.shields.io/badge/license-GPL--3.0-blue)![](https://img.shields.io/badge/opencv-2.0-blue)![](https://img.shields.io/badge/UIAutomator-2-blue)

## 简介

此项目为国服公主连结脚本，使用opencv图像识别进行按钮分析。本项目基于公主连接opencv高级脚本(https://github.com/bbpp222006/Princess-connection) 开发。

## 特点

- [x] 多线程多开 **new**
- [x] 家园领取
- [x] 行会点赞
- [x] 自动捐赠
- [x] 地下城 农场/大号
- [x] 收取任务
- [x] 收取礼物
- [x] 免费扭蛋
- [x] 自动刷经验
- [x] 自动刷10图
- [x] 自动购买体力
- [x] 自动探索(额外脚本)

功能详解

1. 模拟器多开管理 ← new!!
2. 账号批量登录/退出；
3. 收取所有礼物；
4. 检测行会捐赠请求并捐赠；
5. 地下城自动刷支援，默认第一个人，请确保支援角色不大于农场号等级+30；
6. 购买3次体力；
7. 收取所有任务报酬；
8. 刷全部10图3次（请确保你的农场号已经全部3星通关）；
10. 家园自动收取；
11. 公会给副会长（默认排序第二位）自动点赞；
11. 自动刷经验关(1-1，内含自动购买体力)
12. 自动免费扭蛋
13. 自动刷完第三个地下城（断崖的遗迹）及自动探索（主程序中没有包含，为额外脚本）。
14. 购买70次mana（主程序中没有包含，为额外脚本）；


## 环境

需要安装下列python包:

```
pip install opencv-python==3.* -i https://pypi.tuna.tsinghua.edu.cn/simple/
pip install matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple/
pip install uiautomator2 -i https://mirrors.aliyun.com/pypi/simple/
```

windows端需要adb工具，在adb文件夹，请自行手动添加到path中。

若使用模拟器，则需要将模拟器设置为桥接模式，同时需要打开usb调试。具体参考这个项目(https://github.com/Jiahonzheng/JGM-Automator)

建议使用雷电模拟器，本项目中均以雷电模拟器为示例。

**重要：模拟器分辨率要求540*960**


## 使用方式

1. 在main.py中定制自己需要的功能，不需要的用#号注释，或直接跳过本步骤
2. 启动雷电模拟器，安装b服版公主连结，设置分辨率为540*960   **注意不是960 * 540**
3. 启动雷电多开器，用复制模拟器功能 根据电脑性能酌情多开
4. 然后在终端中输入

```
cd main.py文件所在的目录（自己复制）
例如：cd C:\Users\Administrator\Documents\Princess-connection-farm
```

5. 再输入

```
python main.py
```

程序将按顺序自动完成简介中功能1-11。

**第二次使用只需**

1. 启动雷电多开器，多开复数个模拟器；
2. 然后在终端中输入

```
cd main.py文件所在的目录（自己复制）
例如：cd C:\Users\Administrator\Documents\Princess-connection-farm
```

3. 再输入

```
python main.py
```

## 额外说明

1. **本项目下zhanghao.txt为待刷账号与密码**;
   账号与密码之间用tab键作为分割，不要用空格；

   不同账号之间按行分割；

   第一行的zhanghao mima请也改成自己的账号密码。

2. **本项目下goumaimana.py为购买70次mana**，执行方法参照main.py

3. **本项目下juanzeng.py为行会捐赠装备**；

   建议每天上午跑一次main.py，8小时后请求新的装备后再跑juanzeng.py

4. **本项目下dixiacheng.py为自动刷完第三个地下城（断崖的遗迹）及自动探索**；

   请在zhanghao2.txt中输入账号密码；

   请把”我的队伍“中1队设为打boss队，2队设为aoe队；

   探索默认打第5级；

5. 一些剧情由于识别率问题需要手动跳过，例如公会之家的剧情。如果不想手动跳过，请在主程序尝试自行添加识别，或直接注释相关函数；

6. 请不要用于商业用途。代码交流和bug反馈请联系qq 2785242720

7. 感谢CyiceK(https://github.com/1076472672) 对本项目的倾力帮助。

8. 来个 star 吧(*/ω＼*)

9. 您的一点支持会是我们完善本项目的强大动力！(*/ω＼*)

   <img src="https://s1.ax1x.com/2020/06/22/NYtMHs.jpg" alt="image" style="zoom:25%;" />

## 更新计划

- [ ] 改进地下城和刷图逻辑，更加效率
- [ ] 识别卡死会自动跳转
- [ ] 39对1农场的行会管理功能
- [ ] 代码优化整理

## 更新历史

2020/6/18

- 修复了issue中地下城撤退时可能截图到撤退按钮的问题
- 修复了地下城双倍期间无法识别地下城图标问题
- 修复了登录时可能因控件未能及时弹出而失败的问题
- 收取礼物函数优化了逻辑，去掉了全部收取按钮的锁定
- 行会捐赠函数优化了逻辑，现在大概不会捐赠失败了
- 地下城函数优化了逻辑增加了鲁棒性，加入跳过剧情/首次进入时已经进了地下城 两种情况的初始号的处理法

2020/6/20  By:1076472672

- 添加家园收取和公会点赞功能
- 更替maoxian文件名为dixiacheng
- 优化一小点代码 XD

2020/6/20

* 增加了供大号使用的自动刷完第三个地下城及探索的功能

2020/6/21  By:1076472672

- 添加自动免费扭蛋功能
- 添加刷经验关(1-1)功能

2020/6/22

* 增加了对雷电模拟器多开的支持
* 免除了在终端中手动输入命令的步骤
* 脚本函数均移到了Automator.py
* 修改协议为GPL 3.0
