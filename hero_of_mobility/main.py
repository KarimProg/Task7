# Header Files
import time
import numpy as np
from PID import PIDclass
import matplotlib.pyplot as plt

# PID variables
kp = 6
ki = 5
kd = 2 # In a physical robot this could be too high, due to excess noise

# Required positions
setpointX = 200
setpointY = 100
setpointTheta = 200

# Wheel angles
theta1 = 0 
theta2 = 120
theta3 = 240

# Global angle
phi = 45

# Delay to increase readablity of readings in terminal
delay = 0.1

# Object calls of classes
PIDx = PIDclass(kp,ki,kd)
PIDy = PIDclass(kp,ki,kd)
PIDtheta = PIDclass(kp,ki,kd)

# Start position (x, y, theta)
position = [0, 0, 0]

# End position
destination = [setpointX, setpointY, setpointTheta]

# Time management variable
prevTime = 0

def get_velocity(Vx, Vy, Vtheta):
    # Wheel angles
    theta1 = 0 
    theta2 = 120
    theta3 = 240

    arr = np.array(
        [
            [-np.sin(theta1 * np.pi / 180), -np.sin(theta2 * np.pi / 180), -np.sin(theta3 * np.pi / 180)],
            [ np.cos(theta1 * np.pi / 180),  np.cos(theta2 * np.pi / 180),  np.cos(theta3 * np.pi / 180)],
            [               1             ,                1             ,                1             ]
        ]
    )
    sols = np.array([Vx, Vy, 0.2 * Vtheta])

    V1, V2, V3 = np.linalg.solve(arr, sols)
    return V1, V2, V3


# Initialize the graph
plt.figure()
plt.xlim(-100, 100)  # Set the x-axis limits based on your requirements
plt.ylim(-100, 100)  # Set the y-axis limits based on your requirements
plt.gca().set_aspect('equal', adjustable='box')  # Ensure aspect ratio is equal for x and y axes

# Create a scatter plot for the dot
dot, = plt.plot([], [], 'ro')  # 'ro' means red color, round marker
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Position Plot')

# Create an arrow to represent direction
arrow = plt.arrow(0, 0, 0, 0, head_width=5, head_length=10, fc='blue', ec='blue')  # Adjust head_width and head_length as needed

# Function to update the dot position
def update_plot(x, y, dx, dy):
    global arrow
    dot.set_xdata(x)
    dot.set_ydata(y)
    arrow.remove()  # Remove the previous arrow
    arrow = plt.arrow(x, y, dx, dy, head_width=5, head_length=10, fc='blue', ec='blue')  # Create a new arrow

# Loop to update position using PID control
while True:


    currTime = time.time()
    Vx = PIDx.update(position[0], destination[0])
    Vy = PIDy.update(position[1], destination[1])
    Vtheta = PIDtheta.update(position[2], destination[2])

    # Not needed in end product but can be used to debug rate of change
    print(f"Velocity X: {Vx}")
    print(f"Velocity Y: {Vy}")
    print(f"Omega: {Vtheta}")

    arr = np.array(
    [
        [-np.sin(theta1 * np.pi / 180), -np.sin(theta2 * np.pi / 180), -np.sin(theta3 * np.pi / 180)],
        [ np.cos(theta1 * np.pi / 180),  np.cos(theta2 * np.pi / 180),  np.cos(theta3 * np.pi / 180)],
        [               1             ,                1             ,                1             ]
    ]
)

    sols = np.array([Vx, Vy, 0.2 * Vtheta])

    # Calculate V for each motor
    V1, V2, V3 = np.linalg.solve(arr, sols)

    # Output to motor
    print(f"V1: {np.round(V1,2)}")
    print(f"V2: {np.round(V2,2)}")
    print(f"V3: {np.round(V3,2)}")

    Rot  = np.array([ [np.cos(phi * (np.pi/180)) , -np.sin(phi * (np.pi/180)), 0 ], 
                    [  np.sin(phi * (np.pi/180)) ,  np.cos(phi * (np.pi/180)) , 0 ],
                    [             0              ,             0              , 1 ]])

    # Calculate velocities in global frame
    VGx, VGy, VGtheta = Rot  @  [Vx, Vy, Vtheta]

    VG1, VG2, VG3 = get_velocity(VGx, VGy, VGtheta)

    print("Global Frame : ")
    print(f"VG1: {np.round(VG1,2)}")
    print(f"VG2: {np.round(VG2,2)}")
    print(f"VG3: {np.round(VG3,2)}")


    # Calculate time for conversion from speed to position
    period = currTime - prevTime - delay - 0.01

    # Update position
    position[0] = position[0] + (Vx * period)
    position[1] = position[1] + (Vy * period)
    position[2] = position[2] + (Vtheta * period)

    # Update previous time
    prevTime = currTime

    # Print current position
    print(position)

    # Calculate direction (dx, dy) based on Vx and Vy
    dx, dy = 0.2 * np.cos(np.radians(position[2])), 0.2 * np.sin(np.radians(position[2]))

    # Update dot position
    update_plot(position[0], position[1], dx, dy)
    
    # Refresh the plot
    plt.pause(0.01)

    # Delay to increase readbility of terminal
    time.sleep(delay)