import os
import win32com.client
import speech_recognition as sr
import webbrowser


## speaker function
speakar = win32com.client.Dispatch("SAPI.SpVoice")
def say(text1):
    speakar.speak(text1)
    
    
## mic function
def  takecmd():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold =  0.6
        print("listenig......")
        try:
            #Audio listenig
            audio = r.listen(source)
            #Audio---->Eng text
            quary = r.recognize_google(audio,language="en-in")#quary is the recorded audio in text formate
            
            print(f"user said:{quary}")
            return(quary)
        except:
            return "Try again"
        


## 
if __name__=='__main__':
    print("\t\t\t\t\tRa.ONE\t\t\t\t\t")
    say("Hello i am  Raawan")
    
    while True:
        
        quary =  takecmd()#quary--> is the recorded audio in text formate
        
        if(quary == "turn off"):
            break
        elif(quary == "open YouTube"):
            webbrowser.open("https://www.youtube.com/watch?")
            say("yes sir, oppning Youtube")
      
        
    