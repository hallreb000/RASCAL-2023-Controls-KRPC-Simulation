import krpc
import matplotlib.pyplot as plt

# Connect to KSP
conn = krpc.connect()
vessel = conn.space_center.active_vessel

# Create the matplotlib figure and axes
fig, axs = plt.subplots(3, 2)
fig.suptitle('Live Vessel Data')
axs[0, 0].set_title('Location')
axs[0, 1].set_title('Speed')
axs[1, 0].set_title('Roll')
axs[1, 1].set_title('Pitch')
axs[2, 0].set_title('Yaw')
axs[2, 1].set_title('Power')

# Initialize the data lists
x_data = []
y_data = [[], [], [], [], [], []]

# Define the function that updates the data and plots the graphs
def update_data():
    # Get the latest vessel data
    location = vessel.position(vessel.orbit.body.reference_frame)
    speed = vessel.flight(vessel.orbit.body.reference_frame).speed
    orientation = vessel.flight().direction
    roll, pitch, yaw = orientation[0], orientation[1], orientation[2]
    power = vessel.resources.amount('ElectricCharge')
    
    # Append the data to the lists
    x_data.append(len(x_data) + 1)
    y_data[0].append(location[0])
    y_data[1].append(speed)
    y_data[2].append(roll)
    y_data[3].append(pitch)
    y_data[4].append(yaw)
    y_data[5].append(power)
    
    # Plot the data
    axs[0, 0].plot(x_data, y_data[0], color='red')
    axs[0, 1].plot(x_data, y_data[1], color='green')
    axs[1, 0].plot(x_data, y_data[2], color='blue')
    axs[1, 1].plot(x_data, y_data[3], color='purple')
    axs[2, 0].plot(x_data, y_data[4], color='orange')
    axs[2, 1].plot(x_data, y_data[5], color='black')
    
    # Set the axes limits
    axs[0, 0].set_xlim(max(0, len(x_data) - 100), len(x_data) + 10)
    axs[0, 1].set_xlim(max(0, len(x_data) - 100), len(x_data) + 10)
    axs[1, 0].set_xlim(max(0, len(x_data) - 100), len(x_data) + 10)
    axs[1, 1].set_xlim(max(0, len(x_data) - 100), len(x_data) + 10)
    axs[2, 0].set_xlim(max(0, len(x_data) - 100), len(x_data) + 10)
    axs[2, 1].set_xlim(max(0, len(x_data) - 100), len(x_data) + 10)
    
    # Schedule the next update in 100 milliseconds
    plt.pause(0.1)
    update_data()

# Start the data update loop
update_data()

# Show the matplotlib window
plt.show()
