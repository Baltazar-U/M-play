#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from Tkinter import *
import sys

class Graphics(Tk):
    def __init__(self,parent):
        Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):

        nbr_of_files=50
        revisions=['la 1', 'La 2','Encore une autre', 'Brun', 'la 5', 'un truc à la con', 'ça devient lourd', 'encore un', 'pourle fun', 'toujours aps', 'atteint la limite', 'toujours pas non plus mais c\'est ultra long']
        
        self.grid()

        self.revnumberlabel = StringVar()
        label = Label(self,textvariable=self.revnumberlabel,
                              anchor="w",fg="black",bg="grey")
        label.grid(column=0,row=1,columnspan=1,sticky='EW')
        self.revnumberlabel.set(u"Revision number : ")

        self.revdatelabel = StringVar()
        label = Label(self,textvariable=self.revdatelabel,
                              anchor="w",fg="black",bg="grey")
        label.grid(column=1,row=1,columnspan=2,sticky='EW')
        self.revdatelabel.set(u"Date of release : ")

        self.revdatelabel = StringVar()
        label = Label(self,textvariable=self.revdatelabel,
                              anchor="w",fg="black",bg="grey")
        label.grid(column=3,row=1,columnspan=1,sticky='EW')
        self.revdatelabel.set(u"Includes "+str(nbr_of_files)+" songs.")

        loadrevbutton = Button(self,text=u"Load",)
        loadrevbutton.grid(column=2,row=2)
        saverevbutton = Button(self,text=u"Save",)
        saverevbutton.grid(column=2,row=3)
        activaterevbutton = Button(self,text=u"Activate",)
        activaterevbutton.grid(column=2,row=4)

        revscrollbar = Scrollbar(self)
        revlist = Listbox(self, yscrollcommand = revscrollbar.set)

        for revision in revisions:
            revlist.insert(END, revision)

        revlist.grid(column=0, row=2,rowspan=4, sticky='EWNS')
        revscrollbar.config(command=revlist.yview)
        revscrollbar.grid(column=1, row=2,rowspan=4, sticky='WNS')

        self.authorlabel = StringVar()
        authorlabel = Label(self,textvariable=self.authorlabel, anchor="w", fg="black", bg="grey")
        authorlabel.grid(column=3,row=2,columnspan=1,sticky='NW')
        self.authorlabel.set(u"Authors :")
        
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=0)
        self.grid_columnconfigure(2,weight=0)
        self.grid_columnconfigure(3,weight=1)
        self.resizable(True,False)
        self.update()
#        self.geometry(self.geometry())



#    def OnButtonClick(self):
#        self.revnumberlabel.set("Nice try")

#    def OnPressEnter(self,event):
#        self.labelVariable.set( self.entryVariable.get()+" (You pressed ENTER)" )
#        self.entry.focus_set()
#        self.entry.selection_range(0, Tkinter.END)

if __name__ == "__main__":
    app = Graphics(None)
    app.title('my application')
    app.mainloop()
