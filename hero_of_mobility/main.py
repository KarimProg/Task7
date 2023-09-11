# Header Files
import time
from PID import PIDclass

# PID variables
kp = 40
ki = 20
kd = 4 # In a physical robot this could be too high, due to excess noise

# Required positions
setpointX = 20
setpointY = 10
setpointTheta = 50

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
