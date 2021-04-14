"""  movtomp3_app.py
     Credit: Rodrigo Sparrapan
     sparodrigo82@gmail.com  
     based on user manu. solution"""

import os
import speech_recognition as sr

command2mp3 = 'ffmpeg -i record1.mp3 record1.txt'


os.system(command2mp3)


r = sr.Recognizer()
audio = sr.AudioFile ('record1.mp3')

audio = r.record(source, duration=100)
print(r.recognize_google(audio))


