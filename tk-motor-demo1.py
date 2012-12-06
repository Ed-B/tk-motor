#! /usr/bin/python
#-------------------------------------------------------------------------------
# tk-motor-demo1.py
# Ed_Bennett 12-3-12
# Tk GUI code to run a motor connected to a Raspberry Pi
#
# License is in the accompanying file LICENSE.md
#
# Added 5 RPi-specific lines to the gui example code from the book
# 
# At the top:
#        import RPi.GPIO as GPIO
#
# In the constructor:
#        GPIO.setmode(GPIO.BCM)
#        GPIO.setup(4, GPIO.OUT)
#
# In the "run" button callback:
#        GPIO.output(4, GPIO.HIGH)
#
# In the "stop" button callback:
#        GPIO.output(4, GPIO.LOW)
# 
# An open collector switch on pin 4 switches the motor power
#
#-------------------------------------------------------------------------------
# tkdemo2.py 2nd Demostration of Tkinter and the grid placement method
#-------------------------------------------------------------------------------
# Example source code for the book "Real-World Instrumentation with Python"
# by J. M. Hughes, published by O'Reilly Media, December 2010,
# ISBN 978-0-596-80956-0.
#-------------------------------------------------------------------------------

from Tkinter import *
import time
import RPi.GPIO as GPIO


class demoGUI(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.createWidgets()
        # set up GPIO output channel
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(4, GPIO.OUT)


    def createWidgets(self):
        # get top level frame reference
        top=self.winfo_toplevel()
        # set the start location in the window manager
        top.wm_geometry('+50+100')

        # set the window title
        self.master.title("Demo 2")

        # create string objects for use with label widgets
        self.var1 = StringVar()
        self.var1.set("")
        self.var2 = StringVar()
        self.var2.set("")

        self.master.rowconfigure(0, weight = 1)
        self.master.columnconfigure(0, weight = 1)
        self.grid(sticky = W+E+N+S)
        
        self.text1 = Label(self, text="", width = 15, height = 4,
                           relief=RAISED, bg="white", fg="black",
                           textvariable=self.var1)
        self.text1.grid(rowspan = 2, sticky = W+E+N+S)
        
        self.button1 = Button(self, text = "RUN", width = 10, height = 2)
        self.button1.grid(row = 0, column = 1, sticky = W+E+N+S)
        self.button1.bind("<Button-1>", self.button1_Click)
        
        self.button2 = Button(self, text = "STOP", width = 10, height = 2)
        self.button2.grid(row = 0, column = 2, sticky = W+E+N+S)
        self.button2.bind("<Button-1>", self.button2_Click)
        
        self.button3 = Button(self, text = "Test", width = 10, height = 2)
        self.button3.grid(row = 1, column = 1,sticky = W+E+N+S)
        self.button3.bind("<Button-1>", self.button3_Click)
        
        self.button4 = Button(self, text = "Reset", width = 10, height = 2)
        self.button4.grid(row = 1, column = 2, sticky = W+E+N+S)
        self.button4.bind("<Button-1>", self.button4_Click)
        
        self.entry = Entry(self, relief=RAISED)
        self.entry.grid(row = 2, columnspan = 2, sticky = W+E+N+S)
        self.entry.insert(INSERT, "Command")
        
        self.text2 = Label(self, text="Stopped", width = 2, height = 2,
                           relief=RAISED, bg="white", fg="black",
                           textvariable=self.var2)
        self.text2.grid(row = 2, column = 2, sticky = W+E+N+S)
        
        self.rowconfigure(1, weight = 1)
        self.columnconfigure(1, weight = 1)


    def button1_Click(self, event):
        
        # set RPi board pin 12 high
        GPIO.output(4, GPIO.HIGH)
        self.var1.set("")
        self.var2.set("Running")

    def button2_Click(self, event):
        
        GPIO.output(4, GPIO.LOW)
        self.var1.set("")
        self.var2.set("Stopped")

    def button3_Click(self, event):
        time.sleep(1)
        self.var1.set("Test OK")
        self.var2.set("Stopped")



    def button4_Click(self, event):
        time.sleep(1)
        self.var1.set("Reset OK")
        self.var2.set("Stopped")


app = demoGUI()
app.mainloop()

