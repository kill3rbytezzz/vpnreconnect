from requests import get
import time
import os

#this will check your ip every 10 sec and will run the reconnect script if the ip changed (VPN Disconnect)
def checkip():
    ip = get('https://api.ipify.org').content.decode('utf8')
    ipadd = "10.10.10.1" #change this with your vpn server ip
    gateway = "192.168.100.1" #change this to your gateway ip (Router IP)
    i = 1
    j = 0
    while True :
            try:
                ip = get('https://api.ipify.org').content.decode('utf8')
            except:
                ip = ipadd #this exception if your internet got disconnected it wont stop the program and will get the ip from API after the internet reconnect again
            if ip == ipadd :
                print(str(i)+" | IP = " + str(ip) + " SAME | RECONNECT = "+str(j))
            else :
                print(str(i)+" | IP = " + str(ip) + " CHANGED | RECONNECT = "+str(j))
                os.system("./vpnreconnect.sh " + ipadd +" "+ gateway) 
                j+=1
            i+=1
            time.sleep(10)
checkip()