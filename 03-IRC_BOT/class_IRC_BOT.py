#A bot is a virtual assistant that emulates a real user to provide instant responses. IRC bot is a type of network client that could be a script or a program that can relay 
#messages using the IRC protocol.

#functions:
#1:Acrchive chat message
#2:Can parse Twitter feeds
#3:crwal the web for a key word
#4:Run any comman if needed

import socket
import sys
import time

class IRC:

    irc = socket.socket()

    def __init__(self):
        self.irc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def send(self,channel,msg):
        self.irc.send(bytes("PRIVMSG"+channel + " " +msg +"\n", "UTF-8"))

    def connect(self,aerver,port,channel,botnick,botpass,botnickpass):
        print("connecting to :" + server)
        self.irc.connect(server,port)

        #authentication
        self.irc.send(bytes("USER" + botnick + " " + botnick + " " + botnick + " :python\n","UTF-8"))
        self.irc.send(bytes("NICK" + botnick + "\n","UTF-8"))
        self.irc.send(bytes("NICKSERY IDENTITY" + botnickpass + " "+ nickpass+ "\n","UTF-8"))
        time.sleep(5)

        #join the channel
        self.irc.send(bytes("join "+ channel + "\n","UTF-8"))
    
    def get_response(self):
        time.sleep(5)

        resp = self.irc.recv(2040).decode("UTF-8")

        if resp.find("PING") ! = -1 :
            self.irc.send(bytes("PONG" + resp.split().decode("UTF-8")[1] + "\n","UTF-8"))
            
        return resp
        
    
