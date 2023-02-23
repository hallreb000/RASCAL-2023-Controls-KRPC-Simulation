#Rover Stuff
import krpc
from tkinter import *
from tkinter import ttk
import time

#Connections
connection = krpc.connect()
vessel = connection.space_center.active_vessel
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()


#Sets wheels to go foreward. -1 would make them go backward.
#vessel.control.wheel_throttle = 1

#Sets wheel to steer left. -1 to steer right.
#vessel.control.wheel_steering = 1

#Functions
def throttle():
    vessel.control.wheel_throttle = 1

def stop():
    vessel.control.wheel_throttle = 0
    vessel.control.wheel_steering = 0

def left():
    vessel.control.wheel_steering = 1

def right():
    vessel.control.wheel_steering = -1


#Button to move foreward
ttk.Button(frm, text="Throttle", command=lambda: throttle()).grid(column=0, row=0)

#Stop button
ttk.Button(frm, text="Stop", command=lambda: stop()).grid(column=1, row=0)

#Steer left
ttk.Button(frm, text="Left", command=lambda: left()).grid(column=0, row=1)

#Steer right
ttk.Button(frm, text="Right", command=lambda: right()).grid(column=1, row=1)

#Quit Button
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=2)

#Update panel
root.mainloop()
