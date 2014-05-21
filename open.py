#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from Tkinter import *
import glob
import sys

class GUI(Tk):
    def __init__(self,parent):
        Tk.__init__(self,parent)
        self.parent = parent

        self.initialize()    

    def parentfolder(self):
        c=''
        while c<>'\\':
            self.folder=self.folder[:-1]
            c=self.folder[-1]
        
        self.folder=self.folder[:-1]
        self.currentfolderlabel.set(self.folder)
        self.displayfolder()
        self.update()

    def displayfolder(self):
        self.infolderlist.delete(0, END)
        for item in glob.glob(self.folder+'\\*'):
            self.infolderlist.insert(END, item[len(self.folder)+1:])

    def childfolder(self, event):
        if('\.' not in self.infolderlist.get(ACTIVE)):
            self.folder=self.folder+'\\'+self.infolderlist.get(ACTIVE)
            self.displayfolder()
            self.update()

    def initialize(self):
        self.folder='C:\\Users\Laurent\\Music'
        self.grid()
        self.geometry("400x250+200+200")
        infolderscrollbar = Scrollbar(self)
        self.infolderlist = Listbox(self, yscrollcommand = infolderscrollbar.set)
        infolderscrollbar.config(command=self.infolderlist.yview)
        self.infolderlist.grid(column=0, row=1,columnspan=5, sticky='EWNS')
        infolderscrollbar.grid(column=5, row=1,rowspan=1, sticky='WNSE')

        self.infolderlist.bind("<Double-Button-1>", self.childfolder)

        self.displayfolder()

        self.currentfolderlabel = StringVar()
        label = Label(self,textvariable=self.currentfolderlabel,
                              anchor="w",fg="black")
        label.grid(column=0,row=0,columnspan=1,sticky='NSEW')
        self.currentfolderlabel.set(self.folder)

        cancelbutton = Button(self,text=u"Cancel",)
        cancelbutton.grid(column=4,row=2, sticky='S')
        loadbutton = Button(self,text=u"Load",)
        loadbutton.grid(column=3,row=2, sticky='S')
        parentbutton = Button(self,text=u"Parent folder", command=self.parentfolder)
        parentbutton.grid(column=0,row=2, sticky='W')

        #self.grid_columnconfigure(0,weight=1)
        #self.grid_columnconfigure(1,weight=0)
        #self.resizable(True,False)



if __name__=="__main__":
    app = GUI(None)
    app.title('Open')
    app.mainloop()
