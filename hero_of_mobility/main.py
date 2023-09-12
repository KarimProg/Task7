# Header Files
import time
import numpy as np
from PID import PIDclass

# PID variables
kp = 40
ki = 20
kd = 4 # In a physical robot this could be too high, due to excess noise

# Required positions
setpointX = 200
setpointY = 100
setpointTheta = 200

# Wheel angles
theta1 = 0 
theta2 = 120
theta3 = 240

# Global angle
phi = 0

# Delay to increase readablity of readings in terminal
delay = 0.1

# Object calls of classes
PIDx = PIDclass(kp,ki,kd)
PIDy = PIDclass(kp,ki,kd)
PIDtheta = PIDclass(kp,ki,kd)

# Start position
position = [0, 0, 0]

# End position
destination = [setpointX, setpointY, setpointTheta]

# Time management variable
prevTime = 0

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
                    [np.sin(phi * (np.pi/180)) ,  np.cos(phi * (np.pi/180)) , 0 ],
                    [           0              ,             0              , 1 ]])

    VG1, VG2, VG3 = Rot  @  [V1, V2, V3]

    print("Global Frame : ")
    print(f"VG1: {np.round(VG1,2)}")
    print(f"VG2: {np.round(VG2,2)}")
    print(f"VG3: {np.round(VG3,2)}")


    # Calculate time for conversion from speed to position
    period = currTime - prevTime -delay

    # Update position
    position[0] = position[0] + (Vx * period)
    position[1] = position[1] + (Vy * period)
    position[2] = position[2] + (Vtheta * period)

    # Update previous time
    prevTime = currTime

    # Print current position
    print(position)

    # Delay to increase readbility of terminal
    time.sleep(delay)
