#Kal 1000 testing.
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

#For velocity data
flight = vessel.flight(vessel.orbit.body.reference_frame)

#Get my coordinates
my_long = flight.longitude
my_lat = flight.latitude
heading = flight.heading
print(my_long)
print(my_lat)
print(heading)


#Functions
def locate():
    #Ask for destination longitude and latitude
    long = int(input("What longitude?\n"))
    lat = int(input("What latitude?\n"))
   
    #Get my coordinates
    my_long = flight.longitude
    my_lat = flight.latitude
    heading = flight.heading
    
    #Get longitude correct
    #Go right until at the longitude.
    if (my_long < long):
        while my_long < long:
            if (heading < 90):
                while heading < 90:
                    vessel.control.wheel_throttle = 0.25
                    vessel.control.wheel_steering = 1
                    time.sleep(.25)
                    vessel.control.wheel_throttle = 0
                    vessel.control.wheel_steering = 0
                    heading = flight.heading
            vessel.control.wheel_throttle = 0.25
            if heading > 90:
                vessel.control.wheel_steering = -0.25
                time.sleep(.25)
                vessel.control.wheel_steering = 0
            #Recalculate
            my_long = flight.longitude
            heading = flight.heading
            

    #Go left until at the longitude.
    if (my_long > long):
        while my_long > long:
            if (heading < 270):
                while heading < 270:
                    vessel.control.wheel_throttle = 0.25
                    vessel.control.wheel_steering = 1
                    time.sleep(.25)
                    vessel.control.wheel_throttle = 0
                    vessel.control.wheel_steering = 0
                    heading = flight.heading
            vessel.control.wheel_throttle = 0.25
            if heading > 270:
                vessel.control.wheel_steering = -0.25
                time.sleep(.25)
                vessel.control.wheel_steering = 0
            #Recalculate
            my_long = flight.longitude
            heading = flight.heading

            
    #Get latitude correct
    #Go up until at the latitude.
    if (my_lat < lat):
        while my_lat < lat:
            if (heading > 0) and (heading < 180):
                while (heading > 0) and (heading < 180):
                    vessel.control.wheel_throttle = 0.25
                    vessel.control.wheel_steering = -1
                    time.sleep(.25)
                    vessel.control.wheel_throttle = 0
                    vessel.control.wheel_steering = 0
                    heading = flight.heading
            vessel.control.wheel_throttle = 0.25
            if heading > 180:
                 vessel.control.wheel_steering = 0.25
                 time.sleep(.25)
                 vessel.control.wheel_steering = 0
            #Recalculate
            my_long = flight.longitude
            heading = flight.heading
            
    #Go down until at the latitude.
    if (my_lat > lat):
        while my_lat > lat:
            if (heading < 180):
                while heading < 180:
                    vessel.control.wheel_throttle = 0.25
                    vessel.control.wheel_steering = 1
                    time.sleep(.25)
                    vessel.control.wheel_throttle = 0
                    vessel.control.wheel_steering = 0
                    heading = flight.heading
            vessel.control.wheel_throttle = 0.25
            if heading > 180:
                vessel.control.wheel_steering = -0.25
                time.sleep(.25)
                vessel.control.wheel_steering = 0
            #Recalculate
            my_long = flight.longitude
            heading = flight.heading


def throttle():
   vessel.control.wheel_throttle = 0.25
      
def reverse():
   vessel.control.wheel_throttle = -0.25
    
def stop():
    while (0.1 < flight.speed) or (flight.speed < -0.1):
        print(flight.speed)
        if 0.1 < flight.speed:
            vessel.control.wheel_throttle = -1
        if flight.speed < -0.1:
            vessel.control.wheel_throttle = 1
    vessel.control.wheel_throttle = 0
    
    

def left():
    vessel.control.wheel_steering = 1
    time.sleep(.5)
    vessel.control.wheel_steering = 0

def right():
    vessel.control.wheel_steering = -1
    time.sleep(.5)
    vessel.control.wheel_steering = 0

def retract():
    vessel.control.toggle_action_group(1)
    

def extendo():
    vessel.control.toggle_action_group(2)
   
def fold():
    vessel.control.toggle_action_group(3)

def rotate():
    vessel.control.toggle_action_group(4)
    

#Button to move foreward
ttk.Button(frm, text="Throttle", command=lambda: throttle()).grid(column=0, row=0)

#Button to reverse
ttk.Button(frm, text="Reverse", command=lambda: reverse()).grid(column=2, row=0)

#Stop button
ttk.Button(frm, text="Stop", command=lambda: stop()).grid(column=1, row=0)

#Steer left
ttk.Button(frm, text="Left", command=lambda: left()).grid(column=0, row=1)

#Steer right
ttk.Button(frm, text="Right", command=lambda: right()).grid(column=1, row=1)

#Retract
ttk.Button(frm, text="Retract", command=lambda: retract()).grid(column=0, row=2)

#Extending arms
ttk.Button(frm, text="Extend", command=lambda: extendo()).grid(column=1, row=2)

#Fold
ttk.Button(frm, text="Fold", command=lambda: fold()).grid(column=0, row=3)

#Rotate
ttk.Button(frm, text="Rotate", command=lambda: rotate()).grid(column=1, row=3)

#Button to locate
ttk.Button(frm, text="Locate", command=lambda: locate()).grid(column=0, row=4)

#Quit Button
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=5)

#Update panel
root.mainloop()








###Prints out parts list for the vessel.

##root = vessel.parts.root
##stack = [(root, 0)]
##while stack:
##    part, depth = stack.pop()
##    print(' '*depth, part.title)
##    for child in part.children:
##        stack.append((child, depth+1))






##Live updating data stream of speed into graph
##Copy this chunk of code but just change the data value input on y.append()for multiple data streams 

##while True:
##
##    ##print(vessel.flight(srf_frame).speed)
##
##    fig = plt.figure(figsize=(6, 3))  #Make plot
##    x = [0]
##    y = [0]
##    ln, = plt.plot(x, y, '-')
##
##    def update(frame):
##        ##x is the time unit
##        x.append(x[-1] + 1)
##        ##y is the data value 
##        y.append(vessel.flight(srf_frame).speed)
##
##        ln.set_data(x, y) 
##        fig.gca().relim()
##        fig.gca().autoscale_view() 
##        return ln,
##
##    animation = FuncAnimation(fig, update, interval=500)
##    plt.show()
##    time.sleep(0.2)
##





##def locate():
##   #Ask for destination longitude and latitude
##   long = int(input("What longitude?\n"))
##   lat = int(input("What latitude?\n"))
##   
##   #Get my coordinates
##   my_long = flight.longitude
##   my_lat = flight.latitude
##   heading = flight.heading
##
##   #Get longitude correct
##   #Go right until at the longitude.
##   if (my_long < long)
##      while my_long < long:
##         if (heading < 90):
##            while heading < 90:
##               vessel.control.wheel_throttle = 0.25
##               vessel.control.wheel_steering = 1
##               time.sleep(.25)
##               vessel.control.wheel_throttle = 0
##               vessel.control.wheel_steering = 0
##               heading = flight.heading
##         vessel.control.wheel_throttle = 0.25
##         if heading > 90:
##            vessel.control.wheel_steering = -0.25
##            time.sleep(.25)
##            vessel.control.wheel_steering = 0
##         #Recalculate
##         my_long = flight.longitude
##         heading = flight.heading
##
##   #Go left until at the longitude.
##   if (my_long > long)
##      while my_long > long:
##         if (heading < 270):
##            while heading < 270:
##               vessel.control.wheel_throttle = 0.25
##               vessel.control.wheel_steering = 1
##               time.sleep(.25)
##               vessel.control.wheel_throttle = 0
##               vessel.control.wheel_steering = 0
##               heading = flight.heading
##         vessel.control.wheel_throttle = 0.25
##         if heading > 270:
##            vessel.control.wheel_steering = -0.25
##            time.sleep(.25)
##            vessel.control.wheel_steering = 0
##         #Recalculate
##         my_long = flight.longitude
##         heading = flight.heading
##
##
##
##   #Get latitude correct
##   #Go up until at the latitude.
##   if (my_lat < lat)
##      while my_lat < lat:
##         if (heading > 0) and (heading < 180):
##            while (heading > 0) and (heading < 180):
##               vessel.control.wheel_throttle = 0.25
##               vessel.control.wheel_steering = -1
##               time.sleep(.25)
##               vessel.control.wheel_throttle = 0
##               vessel.control.wheel_steering = 0
##               heading = flight.heading
##         vessel.control.wheel_throttle = 0.25
##         if heading > 180:
##            vessel.control.wheel_steering = 0.25
##            time.sleep(.25)
##            vessel.control.wheel_steering = 0
##         #Recalculate
##         my_long = flight.longitude
##         heading = flight.heading
##
##   #Go down until at the latitude.
##   if (my_lat > lat)
##      while my_lat > lat:
##         if (heading < 180):
##            while heading < 180:
##               vessel.control.wheel_throttle = 0.25
##               vessel.control.wheel_steering = 1
##               time.sleep(.25)
##               vessel.control.wheel_throttle = 0
##               vessel.control.wheel_steering = 0
##               heading = flight.heading
##         vessel.control.wheel_throttle = 0.25
##         if heading > 180:
##            vessel.control.wheel_steering = -0.25
##            time.sleep(.25)
##            vessel.control.wheel_steering = 0
##         #Recalculate
##         my_long = flight.longitude
##         heading = flight.heading














   
