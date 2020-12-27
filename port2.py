import socket,sys
from time import sleep

def inicio():
    print("\033[1;32m")
    print("="*28)
    print("{:^28}".format("\033[1;32mportscan 1.0 by uzi "))
    print("=" *28)
    print("")

def scan():
   inicio()
   ip = input(("digite o ip alvo: "))
   sec = 5
   print("")
   print("\033[1;95mfazendo a varredura, aguarde...")
   sleep(sec)
   for porta in range(21,65535):
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      if s.connect_ex((ip,porta)) == 0:
         print(porta, "\033[1;32mABERTA!")
         s.close()
      
scan()
