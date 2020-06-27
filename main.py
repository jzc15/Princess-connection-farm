# coding=utf-8
import uiautomator2 as u2
import time
from utils import *
from cv import *
from Automator import *
from math import ceil
import matplotlib.pylab as plt
import os
import time
import threading


def runmain(address,account,password,work_no,shuatucl = ""):
    #主功能体函数
    #请在本函数中自定义需要的功能
    work_no = int(str(work_no))
    a = Automator(address)
    # a.start()

    #opencv识别可视化 无法在多线程中使用
    # plt.ion()
    # fig, ax = plt.subplots(1)
    # # plt.show()

    print('>>>>>>>即将登陆的账号为：',account,'密码：',password,'<<<<<<<')
    a.login_auth(account, password)#注意！请把账号密码写在zhanghao2.txt内
    a.init_home()#初始化，确保进入首页
    a.shuatucl = shuatucl
    for x in a.config['work'][work_no]:
        if ('(' in x):
            text = "a." + x
        else:
            text = "a." + x +"()"
        
        print(text)
        eval(text)
    # a.shouqurenwu()#收取任务
    # a.gonghuizhijia()  #家园一键领取
    # a.mianfeiniudan() # 免费扭蛋
    # a.shouqu()  # 收取所有礼物
    # a.dianzan()  # 公会点赞
    # a.shouqu()# 收取所有礼物
    
    # a.shuatu()
    # a.hanghui()#行会捐赠

    # a.dixiacheng()#地下城
    # a.goumaitili()#购买3次体力
    # a.shuatu()#刷全部10图3次
    # a.shuajingyan() # 刷1-1经验（自带体力购买）
    # a.shouqurenwu()  # 二次收取任务
    

    a.change_acc()#退出当前账号，切换下一个


def connect():#连接adb与uiautomator
    try:
        # os.system('adb connect 127.0.0.1:5554')#雷电模拟器
        os.system('adb connect 127.0.0.1:7555') #mumu模拟器
        os.system('python -m uiautomator2 init')
    except:
        print('连接失败')

    result = os.popen('adb devices')#返回adb devices列表
    res = result.read()
    lines=res.splitlines()[1:]

    for i in range(0,len(lines)):
        lines[i]=lines[i].split('\t')[0]
    lines=lines[0:-1]
    print(lines)
    emulatornum=len(lines)
    return(lines,emulatornum)

def read():#读取账号
    account_dic = {}
    wno = []
    cl = []
    with open('zhanghao.yaml','r') as f:#注意！请把账号密码写在zhanghao.csv
        lines = yaml.load(f)
        for i,line in enumerate(lines):
            account,password,work_no,shuatucl = line[0:4]
            account_dic[account]=password.strip()
            wno.append(work_no)
            cl.append(shuatucl)

    account_list=list(account_dic.keys())
    accountnum=len(account_list)
    return(account_list,account_dic,accountnum,wno,cl)



#主程序
if __name__ == '__main__':
    
    #连接adb与uiautomator
    lines,emulatornum = connect()
    #读取账号
    account_list,account_dic,accountnum,work_no,shuatucl = read()
    
    # runmain(lines[0],account_list[0],account_dic[account_list[0]])
    # 多线程执行
    count = 0 #完成账号数
    #完整循环 join()方法确保完成后再进行下一次循环
    for i in range(accountnum):#完整循环 join()方法确保完成后再进行下一次循环
        # for j in range(emulatornum-1):
        t = threading.Thread(target=runmain, args=(lines[0],account_list[i],account_dic[account_list[i]],work_no[i],shuatucl[i]))
        # runmain(lines[0],account_list[i],account_dic[account_list[i]],work_no[i],shuatucl[i])
        # count+=1
        t.setDaemon(True)
        t.start()

        for j in range(30):
            time.sleep(60)
            if(not t.is_alive()):
                break
        if(t.is_alive()):
            print('>>>>>>>出问题的账号为：',account_list[i],'密码：',account_dic[account_list[i]],'<<<<<<<')
            os.system('adb kill-server')
            exit(0)
        


    os.system('adb kill-server')