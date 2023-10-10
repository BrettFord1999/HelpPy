The goal of this project is to create a suite of tools to assist in the daily work of a Helpdesk technician in a Windows environment

requirements:
    python 3.10.12
    pip install WMI
    pip install pywinrm requests_kerberos
    pip install pykerberos
    https://visualstudio.microsoft.com/visual-cpp-build-tools/


Plans:
    Create useful functions that can gather information or perform tasks
    Create a GUI to make the functions more accessible


Resources:
    http://timgolden.me.uk/python/wmi/cookbook.html
    https://pypi.org/project/WMI/
    https://learn.microsoft.com/en-us/windows/win32/cimwin32prov/win32-computersystem
    https://stackoverflow.com/questions/18961213/how-to-connect-to-a-remote-windows-machine-to-execute-commands-using-python


#I'm leaving off troubleshooting kerberos 
# C:\Users\brett\AppData\Local\Temp\pip-install-tn7q94vk\pykerberos_20c8ac485f2d4faab3a18996df5c5b6e\src\kerberosbasic.h(17): fatal error C1083: Cannot open include file: 'gssapi/gssapi.h': No such file or directory
      error: command 'C:\\Program Files (x86)\\Microsoft Visual Studio\\2022\\BuildTools\\VC\\Tools\\MSVC\\14.37.32822\\bin\\HostX86\\x86\\cl.exe' failed with exit code 2