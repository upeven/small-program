from class_IRC_BOT import IRC
import os 
import random

server = "10.10.10.10" # provide a valid IP
port = 5597
channel = "#python"
botnick = "techvbeamers"
botnickpass = "guido"
botpass = "<% = @guido_password %>"
irc = IRC()
irc.connect(server,port,channel,botnick,botpass,botnickpass)

while True:
    text = irc.get_response()
    print(text)

    if "PRIVMSG" in text and channel in text and "hello" in text:
        irc.send(channel,"hello!")