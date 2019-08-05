#!/usr/bin/python
#-*- coding: iso-8859-1 -*-
# Following Python GUI tutorial from http://sebsauvage.net/python/gui
# Basic GUI tutorial using Tkinter

# Import the Tkinter module - part of the standard Python dist.
import Tkinter
# Create a class for the application. In Tkinter, we inherit from Tkinter.Tk which is the 
# base class for standard windows.
class simpleapp_tk(Tkinter.Tk):

# Call the Tkinter.tk constructor
        def __init__(self,parent):
                Tkinter.Tk.__init__(self,parent)
# Create a reference to the parent, good practice for GUI building.
                self.parent = parent
# Initialise the GUI. It's usually best to have a portion of the code which creates the GUI elements
# seperate from the logic of the program.
                self.initialize()
        def initialize(self):
                self.grid()
                self.entryVariable = Tkinter.StringVar()
                self.entry = Tkinter.Entry(self,textvariable=self.entryVariable)
                self.entry.grid(column=0, row=0, sticky='EW')
                self.entry.bind("<Return>", self.OnPressEnter)
                self.entryVariable.set(u"Enter text here")

                button = Tkinter.Button(self, text=u"Click Me",command=self.OnButtonClick)
                button.grid(column=1,row=0)

                self.labelVariable = Tkinter.StringVar()
                label = Tkinter.Label(self,textvariable=self.labelVariable,anchor="w", fg="white",bg="blue")
                label.grid(column=0,row=1,columnspan=2,sticky='EW')
                self.labelVariable.set(u"Hello")

                self.grid_columnconfigure(0,weight=1)
                self.resizable(True,False)
                self.update()
                self.geometry(self.geometry())
                self.entry.focus_set()
                self.entry.selection_range(0, Tkinter.END)

        def OnButtonClick(self):
                self.labelVariable.set( self.entryVariable.get()+" (Button clicked!)" )
                print "Button Clicked"
                self.entry.focus_set()
                self.entry.selection_range(0, Tkinter.END)

        def OnPressEnter(self,event):
                self.labelVariable.set( self.entryVariable.get()+" (Enter pressed!)" )
                print "Enter Pressed"
                self.entry.focus_set()
                self.entry.selection_range(0, Tkinter.END)


# Create a main class which is executed when the program is run.
        if __name__ == "__main__":
# In Tkinter we instanciate our class (app=simpleapp_tk()). We give it no parent (None) as it's the first
# GUI element we build.
                app = simpleapp_tk(None)
# Add a title to the Window
                app.title('Test GUI 01')
                app.mainloop()


