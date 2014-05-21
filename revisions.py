#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import files

class Revision:
    def __init__(self, number=0):
        name='revisions\\rev_'+str(number)+'.lst'
        save=False
        self.musicdata={}
        self.songlist=[]
        files=[]
        self.doublets=False
        
        try:
            listfile=open(name,'r')
        except:
            listfile=open(name,'w')
            save=True
        if not save:
            for entry in listfile:
                entries=entry.split('&')
                if entries[1] not in self.musicdata:
                    self.musicdata[entries[1]]={}
                if entries[2] not in self.musicdata[entries[1]]:
                    self.musicdata[entries[1]][entries[2]]=[]
                if entries[3] in self.musicdata[entries[1]][entries[2]]:
                    self.doublets=True
                else:
                    self.musicdata[entries[1]][entries[2]]+=[[entries[3], entries[0]]]
                    self.songlist+=[entries[0]]
        listfile.close()

        self.changes=[]
        name='revisions\\rev_'+str(number)+'.chg'
        try:
            revisionfile=open(name,'r')
        except:
            revisionfile=open(name,'w')
            save=True
        if not save:
            for change in revisionfile:
                self.changes+=[change]
        revisionfile.close()

    def add(self, listtoimport):
        self.songlist+=listtoimport
        for song in listtoimport:

            entries=files.getdata(song)
            
            if entries[1] not in self.musicdata:
                self.musicdata[entries[1]]={}
            if entries[2] not in self.musicdata[entries[1]]:
                self.musicdata[entries[1]][entries[2]]=[]
            if entries[3] in self.musicdata[entries[1]][entries[2]]:
                self.doublets=True
            else:
                self.musicdata[entries[1]][entries[2]]+=[[entries[3], entries[0]]]
                self.songlist+=[entries[0]]
            print entries
        
            
