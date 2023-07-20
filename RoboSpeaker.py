import os
import win32com.client
##
speaker = win32com.client.Dispatch("SAPI.SpVoice")#====>  Predefiend modulas whhich is use to interact with system heardwares.
def say(text):
    speaker.speak(text)

##

print("Welcome To RoboSpeaker 1.1 Created By Dyno")
while True:
    y = input("Enter what You want to speak")
    if y == "q":
        break
    else:
        say(y)
        
##