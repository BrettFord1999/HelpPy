#let's create a tool to help with helpdesk work
#The first thing I'd like to do is pull the system information from a windows computer

import wmi
import ctypes

wmi_block = wmi.WMI()    
systeminfo = wmi_block.Win32_ComputerSystem()[0]

#Manufacturer = systeminfo.Manufacturer
#Model = systeminfo.Model
print(systeminfo)
