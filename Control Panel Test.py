#Some tkinter stuff.
#This code gives a window with a button to launch a rocket and shows
#   the current altitude of the rocket.
from tkinter import *
from tkinter import ttk
from time import time
import krpc

#Connections
connection = krpc.connect()
vessel = connection.space_center.active_vessel
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

#Set throttle to turn on at full speed.
vessel.control.throttle = 1
#tkinter variable to track altitude
h = IntVar()


while True:
    #Label and Button to activate rocket
    ttk.Label(frm, text="Activate Rocket").grid(column=0, row=0)
    ttk.Button(frm, text="Launch", command=lambda: vessel.control.activate_next_stage()).grid(column=1, row=0)

    #Keep track of altitude as an integer
    h.set(int(vessel.flight().mean_altitude))
    ttk.Label(frm, text="Altitude").grid(column=0, row=1)
    ttk.Label(frm, textvariable=h).grid(column=1, row=1)

    #Quit Button stops code
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=2)

    #Update panel
    root.after(1,root.update())


