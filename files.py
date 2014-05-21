#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import os
from mutagen.mp4 import MP4
from mutagen.id3 import ID3

extensionlist=['.mp3', '.m4a']

def listfiles(folder):
    listtoimport = []
    for root, directories, contents in os.walk(folder):
        for song in contents:
            if song[-4:] in extensionlist:
                listtoimport+=[root+'\\'+song]
    return listtoimport

def getdata(song):
    entries=[]
    entries+=[song]
    if '.m4a' in song or '.mp4' in song:
        audio=MP4(song)
        try:
            artist= audio.get('\xa9ART')
        except:
            artist= ["Unknown artist"]
        try:
            album= audio.get('\xa9alb')
        except:
            album= ["Unknown album"]
        try:
            title= audio.get('\xa9nam')
        except:
            lengh=0
            c=''
            while(c<>'\\'):
                lengh+=1
                c=song[-lengh]
            title=[song[-lengh:-4]]
    elif '.mp3'in song:
        audio=ID3(song)
        try:
            artist= audio["TPE1"].text
        except:
            artist= ["Unknown artist"]
        try:
            album= audio["TALB"].text
        except:
            album= ["Unknown album"]
        try:
            title= audio["TIT2"].text
        except:
            lengh=0
            c=''
            while(c<>'\\'):
                lengh+=1
                c=song[-lengh]
            title=[song[-lengh:-4]]
            
    entries+=artist
    entries+=album
    entries+=title
    return entries
        
