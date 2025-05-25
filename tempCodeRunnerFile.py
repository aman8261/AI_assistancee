# import time
# print(time.time()) #prints currrent time -starts from exicution of code
# time.sleep(2)#wait program for 2 second

import pyttsx3

# Use 'nsss' for macOS or leave it blank to let pyttsx3 choose automatically
engine = pyttsx3.init('nsss')

voices = engine.getProperty('voices')
for voice in voices:
    print(f"Voice: {voice.name}, ID: {voice.id}")



