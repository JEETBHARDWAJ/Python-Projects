import requests
import json
import win32com.client
##

city = input("Enter name of city    ")
url=f"https://api.weatherapi.com/v1/current.json?key=99494812ce0445568a0121727231307&q={city}"
r = requests.get(url)#===>method of the request in python. use to send a get request a specified URl
print(r.text)
weather = json.loads(r.text)#=====>r.text in string,  json.loads change string to dictionary

##

speaker = win32com.client.Dispatch("SAPI.SpVoice")
a =weather["location"]["name"]
b=weather["current"]["temp_c"]

print(f" The current temprature in {a} is {b} degree celcius")
speaker.speak(f" The current temprature in {a} is {b} digre celcius")

##