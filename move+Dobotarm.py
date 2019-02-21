import serial
import time
from tkinter import *                         
from tkinter.ttk import *
import sys
from ctypes import *
import threading
import time
import os
#os.chdir('D:\pythonfile\DobotPython')
root = Tk()
root.title('机械臂光子晶体自动化实验平台')
root.geometry('400x400+100+100')
style = Style()
style.configure("TCheckbutton",  foreground="blue",width=20, height=20,)
serialport2 = serial.Serial("com8",9600,timeout=1)
serialport2.close()

sv2=StringVar()
#sv2.set("1.8 ul/s")
sv2.set("输入注射泵吸的速率")
sv3=StringVar()
sv3.set("输入注射泵吸的体积")

sv5=StringVar()
sv5.set("输入注射泵吐的速率")
sv6=StringVar()
sv6.set("输入注射泵吐的体积")
sv7=StringVar()
sv7.set("水槽吸的速率 ")
sv8=StringVar()
sv8.set("水槽吸的体积")
sv9=StringVar()
sv9.set("水槽吐的速率")
sv10=StringVar()
sv10.set("水槽吐的体积")
#sv11=StringVar()
#sv11.set("3 ul/s")
#sv12=StringVar()
#sv12.set("6 ul")

def irun1(x):
    serialport2.open()
    writeintext='cvolume\r'
    serialport2.write(writeintext.encode())
    writeintext='tvolume'+' '+str(x)+' '+'ul'+'\r'
    print(writeintext)
    serialport2.write(writeintext.encode())
    writeintext='irate'+' '+str(sv5.get())+'\r'
    serialport2.write(writeintext.encode())
    writeintext='irun\r'
    serialport2.write(writeintext.encode())
    serialport2.close()
def irun2(x):
    serialport2.open()
    writeintext='cvolume\r'
    serialport2.write(writeintext.encode())
    writeintext='tvolume'+' '+str(int(sv8.get())+x)+' '+'ul'+'\r'
    print(writeintext)
    serialport2.write(writeintext.encode())
    writeintext='irate'+' '+str(sv7.get())+'\r'
    serialport2.write(writeintext.encode())
    writeintext='irun\r'
    serialport2.write(writeintext.encode())
    serialport2.close()
def irun():
    serialport2.open()
    writeintext='cvolume\r'
    serialport2.write(writeintext.encode())
    writeintext='tvolume'+' '+str(sv6.get())+'\r'
    print(writeintext)
    serialport2.write(writeintext.encode())
    writeintext='irate'+' '+str(sv5.get())+'\r'
    serialport2.write(writeintext.encode())
    writeintext='irun\r'
    serialport2.write(writeintext.encode())
    serialport2.close()    
def irun1():
    serialport2.open()
    writeintext='cvolume\r'
    serialport2.write(writeintext.encode())
    writeintext='tvolume'+' '+str(sv10.get())+'\r'
    print(writeintext)
    serialport2.write(writeintext.encode())
    writeintext='irate'+' '+str(sv9.get())+'\r'
    serialport2.write(writeintext.encode())
    writeintext='irun\r'
    serialport2.write(writeintext.encode())
    serialport2.close()
def wrun(x):
    serialport2.open()
    writeintext='cvolume\r'
    serialport2.write(writeintext.encode())
    writeintext='tvolume'+' '+str(x)+' '+'ul'+'\r'
    print(writeintext)
    serialport2.write(writeintext.encode())
    writeintext='wrate'+' '+str(sv2.get())+'\r'
    serialport2.write(writeintext.encode())
    writeintext='wrun\r'
    serialport2.write(writeintext.encode())
    serialport2.close()
def wrun():
    serialport2.open()
    writeintext='cvolume\r'
    serialport2.write(writeintext.encode())
    writeintext='tvolume'+' '+str(sv3.get())+'\r'
    print(writeintext)
    serialport2.write(writeintext.encode())
    writeintext='wrate'+' '+str(sv2.get())+'\r'
    serialport2.write(writeintext.encode())
    writeintext='wrun\r'
    serialport2.write(writeintext.encode())
    serialport2.close()
def wrun1():
    serialport2.open()
    writeintext='cvolume\r'
    serialport2.write(writeintext.encode())
    writeintext='tvolume'+' '+str(sv8.get())+'\r'
    print(writeintext)
    serialport2.write(writeintext.encode())
    writeintext='wrate'+' '+str(sv7.get())+'\r'
    serialport2.write(writeintext.encode())
    writeintext='wrun\r'
    serialport2.write(writeintext.encode())
    serialport2.close()    
def comparestring(s):
    serialport2.open()
    rm=serialport2.read()
    rmx=s #要读取比较的结尾字符
    while True:
        rm=serialport2.read()
        if rm==rmx.encode(encoding='utf-8'):
            break
    rm=serialport2.read()
    print("rm:",rm)     
    serialport2.close()
    
def Dobotarm(x,y,z):
           
    playbackCmd.x = x
    playbackCmd.y = y
    playbackCmd.z = z
    dll.SetPlaybackBufferCmd(byref(playbackCmd))
    #dll.DisconnectDobot()
def PeriodicTask():
    dll.PeriodicTask()
    threading.Timer(0.5, PeriodicTask).start()

def GetPoseTask():
    pose = Pose()
    dll.GetPose(byref(pose))
    print ('Pose:', pose.x, pose.y, pose.z, pose.rHead, pose.joint1Angle, pose.joint2Angle, pose.joint3Angle, pose.joint4Angle)
    threading.Timer(0.5, GetPoseTask).start()

# For initial pose
class InitialPose(Structure):
    _fields_ = [("joint2Angle", c_float), ("joint3Angle", c_float)]

# For pose
class Pose(Structure):
    _fields_ = [
        ("x", c_float),
        ("y", c_float),
        ("z", c_float),
        ("rHead", c_float),
        ("joint1Angle", c_float),
        ("joint2Angle", c_float),
        ("joint3Angle", c_float),
        ("joint4Angle", c_float),
        ("isGrab", c_byte),
        ("gripper", c_float)
        ]

# For jog
class JogStaticParams(Structure):
    _fields_ = [
        ("jointMaxVelocity", c_float), ("jointMaxAcceleration", c_float),
        ("servoMaxVelocity", c_float), ("servoMaxAcceleration", c_float),
        ("linearMaxVelocity", c_float), ("linearMaxAcceleration", c_float)
        ]

class JogDynamicParams(Structure):
    _fields_ = [("velocityRatio", c_float)]

class JogInstantCmd(Structure):
    _fields_ = [("isJoint", c_byte), ("cmd", c_int)]

class PlaybackStaticParams(Structure):
    _fields_ = [
        ("jointMaxVelocity", c_float), ("jointMaxAcceleration", c_float),
        ("servoMaxVelocity", c_float), ("servoMaxAcceleration", c_float),
        ("linearMaxVelocity", c_float), ("linearMaxAcceleration", c_float),
    ]

class PlaybackDynamicParams(Structure):
    _fields_ = [("velocityRatio", c_float), ("accelerationRatio", c_float)]


class PlaybackBufferCmd(Structure):
    _fields_ = [
        ("motionStyle", c_byte), ("isGrab", c_byte),
        ("x", c_float), ("y", c_float), ("z", c_float), ("rHead", c_float),
        ("gripper", c_float), ("pauseTime", c_float)
    ]


sys.path.append(sys.path[0])
dll = cdll.LoadLibrary('D://pythonfile//DobotPython//DobotDll.dll');
dll.DisconnectDobot()
#PeriodicTask()
#GetPoseTask()

errorString = [
        'Success',
        'Warning:Long arm angle not good!',
        'Warning:Short arm angle not good!',
        'Both long & short arm angle not good!',
        'Error:Dobot not found!',
        "Error:COM port occupied!",
        "Error:No data uploaded!"
        ]

result = dll.ConnectDobot()
#print (errorString[result])


    
    # Set command timeout
dll.SetCmdTimeout(3000)
    # Set initial pose
     
'''initialPose = InitialPose()
initialPose.joint2Angle = 45
initialPose.joint3Angle = 45
dll.SetInitialPose.argtypes = [POINTER(InitialPose)]
dll.SetInitialPose(byref(initialPose))'''
    

pbsParam = PlaybackStaticParams()
pbsParam.jointMaxVelocity = 200
pbsParam.jointMaxAcceleration = 200
pbsParam.servoMaxVelocity = 200
pbsParam.servoMaxAcceleration = 200
pbsParam.linearMaxVelocity = 800
pbsParam.linearMaxAcceleration = 1000
pbsParam.pauseTime = 100
pbsParam.jumpHeight = 20
dll.SetPlaybackStaticParams(byref(pbsParam))

pbdParam = PlaybackDynamicParams()
pbdParam.velocityRatio = 30
pbdParam.accelerationRatio = 30
dll.SetPlaybackDynamicParams(byref(pbdParam))

dll.SetPlaybackBufferCmd.argtypes = [POINTER(PlaybackBufferCmd)]
playbackCmd = PlaybackBufferCmd()
playbackCmd.motionStyle = 2
playbackCmd.isGrab = 0
playbackCmd.gripper = 0
playbackCmd.rHead = 0


#Dobotarm(168.5,19.4,-6.8)    
#dll.DobotExec()
dll.DisconnectDobot()

def one_turn(x,y):
    Dobotarm(157.5,0,-4.5) #起始位置
    time.sleep(2)
    Dobotarm(157.5,1.1)                          #起始位置向下
    time.sleep(2)
    wrun()                          #吸
    comparestring('T')
    time.sleep(2)
                              #起始位置
    irun()                    #吐
    comparestring('T') 
    time.sleep(3)
    Dobotarm(x,y,-4.5)                          #移动到玻璃片11点
    time.sleep(2)
    Dobotarm(x,y,2.1)                           #向下
    time.sleep(2)
    Dobotarm(x,y,-4.5)                          #移动到玻璃片11点
    time.sleep(2)
    Dobotarm(140.3,0,-4.5)                         #移动到水槽
    time.sleep(2)
    Dobotarm(140.3,0,1.1)                          #向下
    time.sleep(2)
    wrun1()                         #吸
    comparestring('T')  
    time.sleep(3)
    Dobotarm(140.3,0,-4.5)                          #向上
    time.sleep(2)
    irun1()
    comparestring('T')
    Dobotarm(157.5,0,-4.5)                          #移动到初始位置
    time.sleep(2) 
#foo()
def foo():
    one_turn(167.7,0)
    one_turn(174.7,0)
    one_turn(178,0)
    
    
Label(root, text='光子晶体自动化实验平台3*3', font=('宋体', 20)).pack(side=TOP, fill=NONE, expand=NO)
#2
entry2 = Entry(root, textvariable=sv2)
entry2.var=sv2
entry2.pack( anchor=CENTER, fill=NONE, expand=NO,padx=10, pady=10)
#3
entry3 = Entry(root, textvariable=sv3)
entry3.var=sv3
entry3.pack(anchor=CENTER, fill=NONE, expand=NO,padx=10, pady=10)
#5
entry5 = Entry(root, textvariable=sv5)
entry5.var=sv5
entry5.pack(anchor=CENTER, fill=NONE, expand=NO,padx=10, pady=10)
#6
entry6= Entry(root, textvariable=sv6)
entry6.var=sv6
entry6.pack(anchor=CENTER, fill=NONE, expand=NO,padx=10, pady=10)
#7
#entry7= Entry(root, textvariable=sv7)
#entry7.var=sv7
#entry7.pack(anchor=CENTER, fill=NONE, expand=NO,padx=10, pady=10)
#8
#entry8= Entry(root, textvariable=sv8)
#entry8.var=sv8
#entry8.pack(anchor=CENTER, fill=NONE, expand=NO,padx=10, pady=10)
#9
#entry9= Entry(root, textvariable=sv9)
#entry9.var=sv9
#entry9.pack(anchor=CENTER, fill=NONE, expand=NO,padx=10, pady=10)
#10
#entry10= Entry(root, textvariable=sv10)
#entry10.var=sv10
#entry10.pack(anchor=CENTER, fill=NONE, expand=NO,padx=10, pady=10)
#11
#entry11= Entry(root, textvariable=sv11)
#entry11.var=sv11
#entry11.pack(anchor=CENTER, fill=NONE, expand=NO,padx=10, pady=10)
#12
#entry12= Entry(root, textvariable=sv12)
#entry12.var=sv12
#entry12.pack(anchor=CENTER, fill=NONE, expand=NO,padx=10, pady=10)

buttonsp = Button(root, text='开始',command=foo)
buttonsp.pack()


#buttonsp = Button(root, text='单点测试',command=foo)
#buttonsp.pack()
root.mainloop()     
    
