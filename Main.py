#let's create a tool to help with helpdesk work
import wmi
import os
import subprocess
from socket import *

# I am using c because that is what is used in the wmi documentation
# I may rewrite this later to be more descriptive
c = wmi.WMI()

def get_sysinfo():
    systeminfo = c.Win32_ComputerSystem()[0]

def get_startup(): 
    for s in c.Win32_StartupCommand ():
        print(f"{s.Location} - {s.Caption} - {s.Command}")

#the watcher function is going to need troubleshooting
def event_log_watcher():
    watcher = c.watch_for (
    notification_type="Creation",
    wmi_class="Win32_NTLogEvent",
    Type="error"
    )
    while 1:
        error = watcher ()
        print(f"Error in {error.Logfile} log: {error.Message}")

# I may just create a subprocess function and just have a convenient menu to run powershell commands
# when the tool is open
def gpupdate():
    subprocess.run(["powershell", "gpupdate /force"])



#print(get_startup())



ip = '192.168.160.1'
username = '********'
password = '********'


import winrm

# Create winrm connection.
sess = winrm.Session(f'https://{ip}', auth=(f'{username}', f'{password}'), transport='kerberos')
result = sess.run_cmd('ipconfig', ['/all'])


"""
try:
    print(f"Establishing connection to {ip}")
    connection = wmi.WMI(ip, user=username, password=password)
    print("Connection established")
except wmi.x_wmi:
    print(f"Your Username and Password of {getfqdn(ip)} are wrong.")
"""
