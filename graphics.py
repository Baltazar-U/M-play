#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from Tkinter import *
from revisions import *
from tkFileDialog import askopenfilenames, askdirectory
import sys
import mutagen
import files


class GUI(Tk):
    def __init__(self,parent):
        Tk.__init__(self,parent)
        self.parent = parent

        self.initialize()

    def Loadall(self):
        name='revisions\\revs.all'
        allfile=open(name,'r')
        for revision in allfile:
            entries=revision.split('&')
            self.revisions+=[entries]

    def updatemusicdata(self):
        self.authorlist.delete(0, END)
        self.albumlist.delete(0, END)
        self.songlist.delete(0, END)
        
        for author in sorted(self.current.musicdata):
            self.authorlist.insert(END, author)
        for author in self.current.musicdata:
            for album in sorted(self.current.musicdata[author]):
                self.albumlist.insert(END, album)
        for author in self.current.musicdata:
            for album in self.current.musicdata[author]:
                for song in sorted(self.current.musicdata[author][album]):
                    self.songlist.insert(END, song[0])

    def plusfile(self):
        newfiles=askopenfilenames()
        newfiles=newfiles.split('.')
        

    def plusdir(self):
        newfolder=askdirectory()
        listtoimport=files.listfiles(newfolder)
        for songimported in listtoimport:
            if songimported in self.current.songlist:
                listtoimport.remove(songimported)
        if(len(listtoimport)>0):
            self.mustsave=True
        self.current.add(listtoimport)
        self.updatemusicdata()
        print self.current.musicdata
        self.update()


    def initialize(self):
        
        self.revisions=[]
        self.Loadall()
        self.current=Revision(0)
        self.mustsave=False

        '''
        authors=['moi', 'U2']
        albums=['le 1','le 2', 'leucémie']
        songs=['je cours',  ' je danse', 'je chante mal']
        '''

        self.grid()

        self.currentrevlabel = StringVar()
        label = Label(self, textvariable=self.currentrevlabel,
                              anchor="w",fg="black",bg="grey")
        label.grid(column=0,row=0,columnspan=7,sticky='EW')
        self.currentrevlabel.set(u"Currently used :")
        

        self.revnumberlabel = StringVar()
        label = Label(self,textvariable=self.revnumberlabel,
                              anchor="w",fg="black",bg="grey")
        label.grid(column=0,row=1,columnspan=1,sticky='EW')
        self.revnumberlabel.set(u"Revision number : ")

        self.revdatelabel = StringVar()
        label = Label(self,textvariable=self.revdatelabel,
                              anchor="w",fg="black",bg="grey")
        label.grid(column=1,row=1,columnspan=1,sticky='EW')
        self.revdatelabel.set(u"Date of release : ")

        self.includeslabel = StringVar()
        label = Label(self,textvariable=self.includeslabel,
                              anchor="w",fg="black",bg="grey")
        label.grid(column=3,row=1,columnspan=2,sticky='EW')
        self.includeslabel.set(u"Includes "+str(len(self.current.songlist))+" songs.")
        self.emptylabel = StringVar()
        emptylabel = Label(self,textvariable=self.emptylabel,
                              anchor="w",fg="black",bg="grey")
        emptylabel.grid(column=5,row=1,columnspan=2,sticky='EW')

        self.seelabel = StringVar()
        label = Label(self,textvariable=self.seelabel,
                              anchor="w",fg="black")
        label.grid(column=4,row=2,columnspan=1,sticky='EW')
        self.seelabel.set(u"See a revision :")
        
        loadrevbutton = Button(self,text=u"Load", )
        loadrevbutton.grid(column=4,row=3)
        loadrevbutton = Button(self,text=u"Load active", )
        loadrevbutton.grid(column=4,row=4)
        if self.mustsave:
            saverevbutton = Button(self,text=u"Must be saved", fg="red")
        else:
            saverevbutton = Button(self,text=u"Saved", fg="black")

        saverevbutton.grid(column=4,row=5)

        self.chooselabel = StringVar()
        label = Label(self,textvariable=self.chooselabel,
                              anchor="w",fg="black")
        label.grid(column=4,row=6,columnspan=1,sticky='EW')
        self.chooselabel.set(u"Unable a revision :")
        
        activaterevbutton = Button(self,text=u"Activate",)
        activaterevbutton.grid(column=4,row=7)

        self.modifylabel = StringVar()
        label = Label(self,textvariable=self.modifylabel,
                              anchor="w",fg="black")
        label.grid(column=4,row=8,columnspan=1,sticky='EW')
        self.modifylabel.set(u"Modify the library :")

        addbutton = Menubutton ( self, text="Add", relief=RAISED)
        addbutton.grid(column=4, row=9)
        addbutton.buttons = Menu(addbutton, tearoff = 0)
        addbutton["menu"]=addbutton.buttons
        addbutton.buttons.add_cascade(label="Folder",  command = self.plusdir)
        addbutton.buttons.add_cascade(label="Files", command = self.plusfile)

        self.authorentry = Entry(self)
        self.authorentry.grid(column=4, row=10)
        self.albumentry = Entry(self)
        self.albumentry.grid(column=4, row=11)
        self.songentry = Entry(self)
        self.songentry.grid(column=4, row=12)

        revscrollbar = Scrollbar(self)
        revlist = Listbox(self, yscrollcommand = revscrollbar.set)
        for revision in self.revisions:
            revlist.insert(END, revision[0])
        revscrollbar.config(command=revlist.yview)
        revlist.grid(column=0, row=2,rowspan=6, columnspan=3, sticky='EWNS')
        revscrollbar.grid(column=3, row=2,rowspan=6, sticky='WNS')

        self.lastchangelabel = StringVar()
        label = Label(self,textvariable=self.lastchangelabel,
                              anchor="w",fg="black")
        label.grid(column=0,row=8,columnspan=4,sticky='NSEW')
        self.lastchangelabel.set(u"Changes since previous :")

        revchangescrollbar = Scrollbar(self)
        self.revchangelist = Listbox(self, yscrollcommand = revchangescrollbar.set)
        for change in self.current.changes:
            self.revchangelist.insert(END, change)
        revchangescrollbar.config(command=self.revchangelist.yview)
        self.revchangelist.grid(column=0, row=9,rowspan=4, columnspan=3, sticky='EWNS')
        revchangescrollbar.grid(column=3, row=9,rowspan=4, sticky='WNS')

        self.authorlabel = StringVar()
        authorlabel = Label(self,textvariable=self.authorlabel, anchor="w", fg="black")
        authorlabel.grid(column=5,row=2,columnspan=1,sticky='NW')
        self.authorlabel.set(u"Authors :")
        self.albumlabel = StringVar()
        albumlabel = Label(self,textvariable=self.albumlabel, anchor="w", fg="black")
        albumlabel.grid(column=5,row=8,columnspan=1,sticky='NW')
        self.albumlabel.set(u"Albums :")
        self.songlabel = StringVar()
        songlabel = Label(self,textvariable=self.songlabel, anchor="w", fg="black")
        songlabel.grid(column=5,row=13,columnspan=1,sticky='NW')
        self.songlabel.set(u"Songs :")

        authorscrollbar=Scrollbar(self)
        self.authorlist=Listbox(self, yscrollcommand=authorscrollbar.set)
        authorscrollbar.config(command=self.authorlist.yview)
        self.authorlist.grid(column=5, row=3,rowspan=5, sticky='EWNS')
        authorscrollbar.grid(column=6, row=3,rowspan=5, sticky='WNSE')

        albumscrollbar=Scrollbar(self)
        self.albumlist=Listbox(self, yscrollcommand=albumscrollbar.set)
        albumscrollbar.config(command=self.albumlist.yview)
        self.albumlist.grid(column=5, row=9,rowspan=4, sticky='EWNS')
        albumscrollbar.grid(column=6, row=9,rowspan=4, sticky='WNSE')

        songscrollbar=Scrollbar(self)
        self.songlist=Listbox(self, yscrollcommand=songscrollbar.set)
        songscrollbar.config(command=self.authorlist.yview)
        self.songlist.grid(column=5, row=14,rowspan=1, sticky='EWNS')
        songscrollbar.grid(column=6, row=14,rowspan=1, sticky='WNSE')

        self.updatemusicdata()
        
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=0)
        self.grid_columnconfigure(3,weight=0)
        self.grid_columnconfigure(4,weight=0)
        self.grid_columnconfigure(5,weight=2)
        self.grid_columnconfigure(6,weight=0)
        self.resizable(True,False)
        self.update()
#        self.geometry(self.geometry())



#    def OnButtonClick(self):
#        self.revnumberlabel.set("Nice try")

#    def OnPressEnter(self,event):
#        self.labelVariable.set( self.entryVariable.get()+" (You pressed ENTER)" )
#        self.entry.focus_set()
#        self.entry.selection_range(0, Tkinter.END)
        

'''
if __name__ == "__main__":
    app = Graphics(None)
    app.title('my application')
    app.mainloop()
'''
