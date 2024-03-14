import socket
from uuid import getnode as get_mac

mac=get_mac()
macString=':'.join(("%012X" % mac) [i:i+2] for i in range(0,12,2))

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

print("Computer Name : " + hostname)
print("IP Address : " + IPAddr)
print('MAC Address : ' + macString + '')