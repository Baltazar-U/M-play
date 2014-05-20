#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from Tkinter import *
import sys

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
            self.revisions.append([entries])

    def initialize(self):

        self.revisions=[]
        self.Loadall()        

        nbr_of_files=50
        authors=['moi', 'U2']
        albums=['le 1','le 2', 'leucémie']
        songs=['je cours',  ' je danse', 'je chante mal']
        self.grid()

        self.currentrevlabel = StringVar()
        label = Label(self, textvariable=self.currentrevlabel,
                              anchor="w",fg="black",bg="grey")
        label.grid(column=0,row=0,columnspan=6,sticky='EW')
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
        label.grid(column=3,row=1,columnspan=1,sticky='EW')
        self.includeslabel.set(u"Includes "+str(nbr_of_files)+" songs.")
        self.emptylabel = StringVar()
        emptylabel = Label(self,textvariable=self.emptylabel,
                              anchor="w",fg="black",bg="grey")
        emptylabel.grid(column=4,row=1,columnspan=2,sticky='EW')

        loadrevbutton = Button(self,text=u"Load", )
        loadrevbutton.grid(column=3,row=2)
        saverevbutton = Button(self,text=u"Save",)
        saverevbutton.grid(column=3,row=3)
        activaterevbutton = Button(self,text=u"Activate",)
        activaterevbutton.grid(column=3,row=4)

        revscrollbar = Scrollbar(self)
        revlist = Listbox(self, yscrollcommand = revscrollbar.set)
        for revision in revisions:
            revlist.insert(END, revision[0])
        revscrollbar.config(command=revlist.yview)
        revlist.grid(column=0, row=2,rowspan=4, columnspan=3, sticky='EWNS')
        revscrollbar.grid(column=3, row=2,rowspan=4, columnspan=1, sticky='WNS')

        self.authorlabel = StringVar()
        authorlabel = Label(self,textvariable=self.authorlabel, anchor="w", fg="black")
        authorlabel.grid(column=4,row=2,columnspan=1,sticky='NW')
        self.authorlabel.set(u"Authors :")
        self.albumlabel = StringVar()
        albumlabel = Label(self,textvariable=self.albumlabel, anchor="w", fg="black")
        albumlabel.grid(column=4,row=6,columnspan=1,sticky='NW')
        self.albumlabel.set(u"Albums :")
        self.songlabel = StringVar()
        songlabel = Label(self,textvariable=self.songlabel, anchor="w", fg="black")
        songlabel.grid(column=4,row=8,columnspan=1,sticky='NW')
        self.songlabel.set(u"Songs :")

        authorscrollbar=Scrollbar(self)
        authorlist=Listbox(self, yscrollcommand=authorscrollbar.set)
        for author in authors:
            authorlist.insert(END, author)
        authorscrollbar.config(command=revlist.yview)
        authorlist.grid(column=4, row=3,rowspan=3, sticky='EWNS')
        authorscrollbar.grid(column=5, row=3,rowspan=3, sticky='WNSE')

        albumscrollbar=Scrollbar(self)
        albumlist=Listbox(self, yscrollcommand=albumscrollbar.set)
        for album in albums:
            albumlist.insert(END, album)
        albumscrollbar.config(command=revlist.yview)
        albumlist.grid(column=4, row=7,rowspan=1, sticky='EWNS')
        albumscrollbar.grid(column=5, row=7,rowspan=1, sticky='WNSE')

        songscrollbar=Scrollbar(self)
        songlist=Listbox(self, yscrollcommand=songscrollbar.set)
        for song in songs:
            songlist.insert(END, song)
        songscrollbar.config(command=revlist.yview)
        songlist.grid(column=4, row=9,rowspan=1, sticky='EWNS')
        songscrollbar.grid(column=5, row=9,rowspan=1, sticky='WNSE')
        
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=0)
        self.grid_columnconfigure(3,weight=0)
        self.grid_columnconfigure(4,weight=2)
        self.grid_columnconfigure(5,weight=0)
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
