#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 18:21:17 2023

@author: vargas
"""

import whisper
from pytube import YouTube
import os

def create_and_open_txt(text, filename):
    # create and write the text to a .txt file
    with open(filename, "w") as file:
        file.write(text)
    os.system('gedit ' + filename)
    
url = input("Enter the YouTube video URL: ")

yt = YouTube(url)
audio_stream = yt.streams.filter(only_audio=True).first()

output_path = "Youtubeaudios"
filename = "audio.mp3"

pathFile = output_path+"/"+filename
# If file exists, delete it.
if os.path.isfile(pathFile):
    os.remove(pathFile)
        
audio_stream.download(output_path=output_path, filename=filename)

print(f"Audio downloaded to {output_path}/{filename}")

model = whisper.load_model("base")
result = model.transcribe("Youtubeaudios/audio.mp3")
print(result["text"])

create_and_open_txt(result["text"], 'output.txt')

    