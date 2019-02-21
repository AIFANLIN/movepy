# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 13:28:30 2018

@author: linha
"""
import serial
serialport1 = serial.Serial("com7",9600,timeout=1)
serialport1.close()
#设置细分8
serialport1.open()
writesegment='010600010008D9CC'
writefirst = bytes.fromhex(writesegment)
serialport1.write(writefirst)  
#设置步距角2
writesangle='0106000000B489BD'
writesecond = bytes.fromhex(writesangle)
serialport1.write(writesecond)  
#设置启动频率50hz
writehz='010600020032A9DF'
writethrid=bytes.fromhex(writehz)
serialport1.write(writethrid)
#设置运行速度200
writespeed='0106001E00C8E85A'
writefourth = bytes.fromhex(writespeed)
serialport1.write(writefourth)
#设置运行距离1600
writelength='0106001F0640BA5C'
writefifth=bytes.fromhex(writelength)
serialport1.write(writefifth)
#设置测试方向
writedirection='0106000B0000F808'
writesixth=bytes.fromhex(writedirection)
serialport1.write(writesixth)

#电机运行状态显示
writerun='0106003000014805'
writeseventh=bytes.fromhex(writerun)
serialport1.write(writeseventh)
serialport1.close()
