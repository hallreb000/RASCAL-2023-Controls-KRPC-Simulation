import time
import krpc
from tkinter import *
from tkinter import ttk


conn = krpc.connect(name = "Example")
vessel = conn.space_center.active_vessel
ir = conn.infernal_robotics

with open('readme.txt', 'w') as f:
    f.write('readme')

print(ir)
if ir.available:
    print('Infernal Robotics is available\n\n')
if ir.ready:
    print("IR is ready\n")

#ir.DetermineReady()
group = ir.servo_group_with_name(vessel, "GroupX")

if group is None:
    print('Group not found')
    exit(1)
else:
    print("Group is not empty")

#print(group)
myServo = {}
i =0; 
for servo in group.servos:
    print(servo.name, servo.position)
    myServo[i] = servo
    i=i+1

# string name of servo 
servo_1 = ir.servo_with_name(vessel, "Extendatron - Basic (Half)")
print("servo 1:", myServo[0].name)
myServos = ir.servo_groups(vessel)
servo_1.move_to(servo_1.min_position,4)

#group.move_next_preset()
##print(servo_1.name, "/'s pos:", servo_1.position)
#time.sleep(5)
print("Moving to previous preset")
for i in range(3):
    group.move_prev_preset()
    time.sleep(2)
    print(servo_1.name ,"'s pos:", servo_1.position)
    print(myServo[3].name, "'s pos:" , myServo[3].position)
    print(myServo[4].name, "'s pos:" , myServo[5].position)
  
print('Move right....\n')
servo_1.move_right
time.sleep(5)
#group.move_right 
##group.stop() 
print(servo_1.name, "/'s pos:", servo_1.position)
print('Move left....\n')
servo_1.move_left
time.sleep(5)
print(servo_1.name, "/'s pos:", servo_1.position)
servo.stop()
print("\n")
# Servo class: ServoGroup.servos, ServoGroup.servo_with_name(), or servo_with_name()
print("Servo Group moving right once...\n")
group.move_right
time.sleep(2)
Servos_in_group  = group.servos
for servo in Servos_in_group:
    print(servo.name, servo.position)
print('servo 1\'s max configuration posistion', servo_1.max_config_position)
     


if(servo_1.is_moving):
    print(servo_1.name, " is moving.\n")
if servo_1.is_locked:
    print(servo_1.name, " is locked.\n")
if servo_1.is_free_moving:
    print(servo_1.name, " is free-moving.\n")

#print(servo_1.acceleration, servo_1.speed)
print("Servo move to max/2 posiiton...\n")
servo_1.move_to(servo_1.max_position/2*3, 5)
time.sleep(5)
servo_1.stop()

servo_1.speed = 8
servo_1.acceleration= 4
print("servo group move right... (x3)\n")
for i in range(3):
    group.move_right
    time.sleep(2)
    print(servo_1.name, "'s pos:", servo_1.position)
    print(myServo[3].name, "'s pos:" , myServo[3].position)
    print(myServo[4].name, "'s pos:" , myServo[5].position)
#print(servo_1.speed)
group.stop()  
print("servo is moving to next present ...\n ")
servo_1.move_next_preset
print(servo_1.acceleration)
print(servo_1.name, "'s pos:", servo_1.position)

print("move to positions...\n")
servo_1.move_to(servo_1.min_position, 4)
myServo[3].move_to(myServo[3].max_position, 4)
myServo[4].move_to(myServo[5].max_position, 4)

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Finish!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()