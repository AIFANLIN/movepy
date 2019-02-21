# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 10:05:26 2018

@author: Administrator
"""
import serial
import time
from tkinter import *                         
from tkinter.ttk import *


root = Tk()
root.title('w-z-y-z-i 一键设定操作')
root.geometry('400x400+100+100')
style = Style()
style.configure("TCheckbutton",  foreground="blue",width=20, height=20,)

serialport1 = serial.Serial("com4",9600,timeout=1)
serialport1.close()
serialport2 = serial.Serial("com3",9600,timeout=1)
serialport2.close()
data2 = ["正转","反转"]
data_z = ["向下","向上"]
dataT=["ml","ul","nl","pl"]
datar=["ml/min","ul/min","nl/min","pl/min"]
sv1=StringVar()
sv1.set("0")

sv2=StringVar()
sv2.set("0")

sv3=StringVar()
sv3.set("0")

sv4=StringVar()
sv4.set("50")

sv5=StringVar()
sv5.set("100")

sv6=StringVar()
sv6.set("80")

sv7=StringVar()
sv7.set("30")

def entrytohex(entryhex):
    if entryhex <10:
        entryhex='0'+str(entryhex)+'00'
    elif entryhex < 16:
        entryhex=str(entryhex)+'00'
    else :
        if entryhex<256:
            speed1=hex(entryhex)
            entryhex=speed1[-2]+'00'
        else :
            speed1=hex(entryhex)
            speed2=speed1.replace( 'x','0' )
            speed3=speed2[-4:]
            entryhex=str(speed3[-2:])+str(speed3[-4:-2])
            #print ("entryhex",entryhex)
    return(entryhex)
    

def Entry1():   #x
    bintext=int(float(sv1.get())*1750)
    result=entrytohex(bintext)
    print ("Entry1:",result)
    return (result)

def Entry2():   #y
    bintext=int(float(sv2.get())*1600)
    result=entrytohex(bintext)
    print ("Entry2:",result)
    return (result)


def Entry3(): #z轴不须取余
    bintext=int(float(sv3.get())*1000)
    result=entrytohex(bintext)
    print ("Entry3:",result)
    return (result)

def set_steering1():
    # 在下拉列表里查找输入框中的文字，如果找到返回对应的索引值
    # 没有找到返回-1
    i=cb1.current()
    if i==0:
        motor='00'
    else:
        motor='01'
    return(motor)

def set_steering2():
    # 在下拉列表里查找输入框中的文字，如果找到返回对应的索引值
    # 没有找到返回-1
    i=cb2.current()
    if i==0:
        motor='00'
    else:
        motor='01'
    return(motor)

def set_steering3():
    #在下拉列表里查找输入框中的文字，如果找到返回对应的索引值
    # 没有找到返回-1
    i=cb3.current()
    if i==0:
        motor='00'
    else:
        motor='01'
    return(motor)

def tunit():
    i=cb4.current()
    if i==0:
        tu='ml'
    elif i==1:
        tu='ul'
    elif i==2:
        tu='nl'
    else: tu='pl'
          
    print("i",i)
    print("tu:",tu)
    return (tu)
def irunit():
    i=cb5.current()
    if i==0:
        iru='ml/min'
    elif i==1:  
        iru='ul/min'
    elif i==2:
        iru='nl/min'
    else: iru='pl/min'
    return(iru)
def rrunit():
    i=cb6.current()
    if i==0:
        rru='ml/min'
    elif i==1:  
        rru='ul/min'
    elif i==2:
        rru='nl/min'
    else: rru='pl/min'
    return(rru)   

def calculate_end(speed,axis):
#    speed=entry()
    speed1=speed[0:2]
    speed2=speed[2:]
    end2=str(hex(int('ff', 16)+int('aa',16)+int(axis,16)+int('03',16)+int(speed1,16)+int(speed2,16)))#截取后两位)
    end=end2[-2:]
    print ("axis:",axis,"end",end)
    return(end)
#cmd='03'
def x_axis():

    serialport1.open()
    speed=Entry1()
    axis='01'
    motor=set_steering1()
    calculate_end(speed,axis)
    writeangle='ffaa0001013200b40091'
    writefirst = bytes.fromhex(writeangle)
    serialport1.write(writefirst)  #细分角
    
    writehz ='ffaa00010240060000f2'
    writeData = bytes.fromhex(writehz)
    serialport1.write(writeData)#设置脉冲
    
    writespeed='ffaa0001053200c800a9'
    writeData = bytes.fromhex(writespeed)
    serialport1.write(writeData)#设置运行速度200RPM
    
    writecontent ='ffaa000103'+str(speed)+'00'+'00'+str(calculate_end(speed,axis))
    writeData = bytes.fromhex(writecontent)
    serialport1.write(writeData)
    #print(writecontent)
    
    if motor=='00':
        writecontent1 ='ffaa00010400320000e0'#正转
    else :
        writecontent1 ='ffaa00010401320000e1' #反转
    writeData = bytes.fromhex(writecontent1) 
    serialport1.write(writeData)
    
    
    writecontent2 = 'ffaa00010900000000b3'
    writeData = bytes.fromhex(writecontent2)
    serialport1.write(writeData)    #运行
    
    #print(writecontent1)
    serialport1.close()

    

                
def rx_axis(speed):

    serialport1.open()
    speed=Entry1()
    axis='01'
    motor=set_steering1()
    if motor=='00':
        motor='01'
    else: motor='00'  
    calculate_end(speed,axis)
    writeangle='ffaa0001010800b40067'
    writefirst = bytes.fromhex(writeangle)
    serialport1.write(writefirst)  #细分角
    
    writehz ='ffaa00010240060000f2'
    writeData = bytes.fromhex(writehz)
    serialport1.write(writeData)#设置脉冲
    
    writespeed='ffaa0001053200c800a9'
    writeData = bytes.fromhex(writespeed)
    serialport1.write(writeData)#设置运行速度200RPM
    
    writecontent ='ffaa000103'+str(speed)+'00'+'00'+str(calculate_end(speed,axis))
    writeData = bytes.fromhex(writecontent)
    serialport1.write(writeData)
    #print(writecontent)
    
    if motor=='00':
        writecontent1 ='ffaa00010400320000e0'#正转
    else :
        writecontent1 ='ffaa00010401320000e1' #反转
    writeData = bytes.fromhex(writecontent1) 
    serialport1.write(writeData)
    
    
    writecontent2 = 'ffaa00010900000000b3'
    writeData = bytes.fromhex(writecontent2)
    serialport1.write(writeData)    #运行
    
    #print(writecontent1)
    serialport1.close()

def y_axis():

    serialport1.open()
    
    speed=Entry2()
    axis='02'
    motor=set_steering2()
    calculate_end(speed,axis)
   # writeangle='ffaa0002046800b400B8'
    writeangle='ffaa0002013200b40092'
    writefirst = bytes.fromhex(writeangle)
    serialport1.write(writefirst)  #细分角
    
    writehz ='ffaa00020240060000f3'
    writeData = bytes.fromhex(writehz)
    serialport1.write(writeData)#设置脉冲

    writecontent1 ='ffaa000203'+str(speed)+'00'+'00'+str(calculate_end(speed,axis))
    writeData = bytes.fromhex(writecontent1)#距离
    serialport1.write(writeData)
    #print(writecontent1)
    
    if motor=='00':
        writecontent1 ='ffaa00020400320000e1'#正转
    else :
        writecontent1 ='ffaa00020401320000e2' #反转
    writeData = bytes.fromhex(writecontent1) 
    serialport1.write(writeData)
    writecontent2 = 'ffaa00020900000000b4'
    writeData = bytes.fromhex(writecontent2)
    #print(writecontent1)
    serialport1.write(writeData)
    serialport1.close()

        
        
        

        
     
def ry_axis(speed):

    serialport1.open()
    speed=Entry2()
    axis='02'
    motor=set_steering2()
    if motor=='00':
        motor='01'
    else: motor='00'  
    calculate_end(speed,axis)
    writeangle='ffaa0002010800b40068'
    writefirst = bytes.fromhex(writeangle)
    serialport1.write(writefirst)  #细分角
    
    writehz ='ffaa00020240060000f3'
    writeData = bytes.fromhex(writehz)
    serialport1.write(writeData)#设置脉冲

    writecontent1 ='ffaa000203'+str(speed)+'00'+'00'+str(calculate_end(speed,axis))
    writeData = bytes.fromhex(writecontent1)#距离
    serialport1.write(writeData)
    #print(writecontent1)
    
    if motor=='00':
        writecontent1 ='ffaa00020400320000e1'#正转
    else :
        writecontent1 ='ffaa00020401320000e2' #反转
    writeData = bytes.fromhex(writecontent1) 
    serialport1.write(writeData)
    writecontent2 = 'ffaa00020900000000b4'
    writeData = bytes.fromhex(writecontent2)
    #print(writecontent1)
    serialport1.write(writeData)
    serialport1.close()    
    
def z_axis(speed):

    serialport1.open()
    speed=Entry3()
    axis='03'
    motor=set_steering3()
    calculate_end(speed,axis)
    writeangle='ffaa0003010800b40069'
    writefirst = bytes.fromhex(writeangle)
    serialport1.write(writefirst)  #细分角
    
    writehz ='ffaa00030240060000f4'
    writeData = bytes.fromhex(writehz)
    serialport1.write(writeData)#设置脉冲
    
    writespeed='ffaa00030532007800a9'
    writeData = bytes.fromhex(writespeed)
    serialport1.write(writeData)#设置运行速度
    
    writecontent1 ='ffaa000303'+str(speed)+'00'+'00'+str(calculate_end(speed,axis))
    writeData = bytes.fromhex(writecontent1)
    serialport1.write(writeData)
    #print(writecontent1)
    
    if motor=='00':
        writecontent1 ='ffaa00030400320000e2'#正转
    else :
        writecontent1 ='ffaa00030401320000e3' #反转
    writeData = bytes.fromhex(writecontent1) 
    serialport1.write(writeData)
    writecontent2 = 'ffaa00030900000000b5'
    writeData = bytes.fromhex(writecontent2)
    serialport1.write(writeData)
    serialport1.close() 
 
def rz_axis(speed):

    serialport1.open()
    speed=Entry3()
    axis='03'
    motor=set_steering3()
    if motor=='00':
        motor='01'
    else: motor='00'   
    calculate_end(speed,axis)
    writeangle='ffaa0003010800b40069'
    writefirst = bytes.fromhex(writeangle)
    serialport1.write(writefirst)  #细分角
    
    writehz ='ffaa00030240060000f4'
    writeData = bytes.fromhex(writehz)
    serialport1.write(writeData)#设置脉冲
    
    writespeed='ffaa00030532007800a9'
    writeData = bytes.fromhex(writespeed)
    serialport1.write(writeData)#设置运行速度
    
    writecontent1 ='ffaa000303'+str(speed)+'00'+'00'+str(calculate_end(speed,axis))
    writeData = bytes.fromhex(writecontent1)
    serialport1.write(writeData)
    #print(writecontent1)
    
    if motor=='00':
        writecontent1 ='ffaa00030400320000e2'#正转
    else :
        writecontent1 ='ffaa00030401320000e3' #反转
    writeData = bytes.fromhex(writecontent1) 
    serialport1.write(writeData)
    writecontent2 = 'ffaa00030900000000b5'
    writeData = bytes.fromhex(writecontent2)
    serialport1.write(writeData)
    serialport1.close()

def irun():
    serialport2.open()
    writeintext='cvolume\r'
    serialport2.write(writeintext.encode())
    print("sv4.get():",sv4.get())
    writeintext='tvolume'+' '+str(sv4.get())+' '+str(tunit())+'\r'
    print(writeintext)
    serialport2.write(writeintext.encode())
    writeintext='irate'+' '+str(sv5.get())+' '+str(irunit())+'\r'
    print("sv5.get():",sv5.get())
    serialport2.write(writeintext.encode())
    writeintext='irun\r'
    serialport2.write(writeintext.encode())
    
        
    serialport2.close()

def wrun():
    serialport2.open()
    writeintext='cvolume\r'
    serialport2.write(writeintext.encode())
   # print("sv4.get():",sv4.get())
    writeintext='tvolume'+' '+str(sv7.get())+' '+str(tunit())+'\r'
    print(writeintext)
    serialport2.write(writeintext.encode())
    writeintext='wrate'+' '+str(sv6.get())+' '+str(rrunit())+'\r'
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
    
    
    
    
    
    
Label(root, text='3轴移动平台', font=('宋体', 20)).pack(side=TOP, fill=NONE, expand=NO)   
#1 
entry1 = Entry(root, textvariable=sv1)
entry1.var=sv1
entry1.pack(side=TOP, anchor=W, fill=NONE, expand=NO,padx=10, pady=10)

cb1=Combobox(root, height=6, values=data2)
# 设置输入框只读
cb1["state"] = "readonly"  
cb1.set('Y轴运动方向')
cb1.pack()

#2
entry2 = Entry(root, textvariable=sv2)
entry2.var=sv2
entry2.pack( anchor=W, fill=NONE, expand=NO,padx=10, pady=10)

cb2=Combobox(root, height=6, values=data2)
cb2["state"] = "readonly"  
cb2.set('X轴运动方向')
cb2.pack()

#3
entry3 = Entry(root, textvariable=sv3)
entry3.var=sv3
entry3.pack(anchor=W, fill=NONE, expand=NO,padx=10, pady=10)



cb3=Combobox(root, height=6, values=data_z)
cb3["state"] = "readonly"  
cb3.set('Z轴运动方向')
cb3.pack()

#4
entry4 = Entry(root, textvariable=sv4)
entry4.var=sv4
entry4.pack(anchor=W, fill=NONE, expand=NO,padx=10, pady=10)

cb4=Combobox(root, height=6, values=dataT)
cb4["state"] = "readonly"  
cb4.set('ul')
cb4.pack()

#5
entry5 = Entry(root, textvariable=sv5)
entry5.var=sv5
entry5.pack(anchor=W, fill=NONE, expand=NO,padx=10, pady=10)

cb5=Combobox(root, height=6, values=datar)
cb5["state"] = "readonly" 
cb5.set('ul/min')
cb5.pack()

#6
entry6= Entry(root, textvariable=sv6)
entry6.var=sv6
entry6.pack(anchor=W, fill=NONE, expand=NO,padx=10, pady=10)

cb6=Combobox(root, height=6, values=datar)
cb6["state"] = "readonly" 
cb6.set('ul/min')
cb6.pack()

#6
entry7= Entry(root, textvariable=sv7)
entry7.var=sv7
entry7.pack(anchor=W, fill=NONE, expand=NO,padx=10, pady=10)

cb7=Combobox(root, height=6, values=dataT)
cb7["state"] = "readonly" 
cb7.set('ul')
cb7.pack()

#选框
def foo2():
    full=[0,entrytohex(62137)]
    #x_axis(full)
    
    '''i=Entry1()[0]
    while i>0:
        x_axis(full)
        time.sleep(30)
        i=i-1
    x_axis(Entry1())
    time.sleep(30)
    print("x_axis done!")
    
    i=Entry2()[0]    
    while i>0:
        y_axis(full)
        print("i:",i)
        time.sleep(20)
        i=i-1
    y_axis(Entry2())
    time.sleep(20)
    print("y_axis done!")'''
    
   # x_axis(Entry1())
    #y_axis(Entry2())
   # z_axis(Entry3())
    
   # z_axis(Entry3())
  
    #serialport2.open(
    
    
    #time.sleep(100)
    #serialport2.close()
    '''z_axis(Entry3())
    wrun()
    serialport2.open()
    rm=serialport2.read()
    rmx='T'#要读取比较的结尾字符
    while rm!=rmx.encode(encoding='utf-8'):
        rm=serialport2.read()
        print("rm:",rm)
    print("irun() has done")
     
    serialport2.close() 
    
    irun()
    
    serialport2.open()
    rm=serialport2.read()
    while rm!=rmx.encode(encoding='utf-8'):
        rm=serialport2.read()
        print("rm3:",rm)
    
    print("wrun() has done")'''
    serialport2.open()
    writeintext='stp\r'
    serialport2.write(writeintext.encode())
    serialport2.close()
def xmove():
    for i in range(3):
        irun()
        comparestring('T')
        sv1.set(5)
        x_axis(Entry1())
        time.sleep(3)
        irun()
        comparestring('T')
def ymove():
    sv2.set(5)
    y_axis(Entry2())
    irun()
    comparestring('T')
        
        
        
        
        
            
    
    
    
    
    
def foo1():
    x_axis()
    y_axis()
    z_axis(Entry3())
   
        
   
    
    
    
    
    
       
   
    


buttonsp = Button(root, text='start',command=foo1)
buttonsp.pack()



root.mainloop()
