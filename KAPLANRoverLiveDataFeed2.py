import krpc
import tkinter as tk

# Connect to KSP
conn = krpc.connect(name='Live Data')
vessel = conn.space_center.active_vessel

# Create GUI
root = tk.Tk()
root.title('KSP Live Data')
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Create labels
location_label = tk.Label(canvas, text='Location: ')
speed_label = tk.Label(canvas, text='Speed: ')
roll_label = tk.Label(canvas, text='Roll: ')
pitch_label = tk.Label(canvas, text='Pitch: ')
yaw_label = tk.Label(canvas, text='Yaw: ')
power_label = tk.Label(canvas, text='Power: ')
error_label = tk.Label(canvas, text='')

# Add labels to canvas
location_label.pack()
speed_label.pack()
roll_label.pack()
pitch_label.pack()
yaw_label.pack()
power_label.pack()
error_label.pack()

# Update data function
def update_data():
    # Get vessel data
    location = vessel.position(vessel.orbit.body.reference_frame)
    speed = vessel.flight(vessel.orbit.body.reference_frame).speed
    roll, pitch, yaw = vessel.flight().roll, vessel.flight().pitch, vessel.flight().heading
    power = vessel.resources.amount('ElectricCharge')

    # Update labels
    location_label.config(text=f'Location: {location}')
    speed_label.config(text=f'Speed: {speed} m/s')
    roll_label.config(text=f'Roll: {roll:.2f}°')
    pitch_label.config(text=f'Pitch: {pitch:.2f}°')
    yaw_label.config(text=f'Yaw: {yaw:.2f}°')
    power_label.config(text=f'Power: {power:.2f}')

    # Check for errors
    if speed > 15:
        error_label.config(text='ERROR: Speed > 15 m/s')
    elif 80 < pitch < 100:
        error_label.config(text='')
    else:
        error_label.config(text='ERROR: Pitch out of range')

    # Schedule next update
    root.after(100, update_data)

# Start updating data
update_data()

# Run GUI
root.mainloop()
