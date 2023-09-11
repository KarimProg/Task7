# Header Files
import time
from PID import PIDclass

# PID variables
kp = 31
ki = 0.001
kd = 5 # In a physical robot this would be too high most probably, due to excess noise

# Required positions
setpointX = 20
setpointy = 10
setpointtheta = 50

# Delay to increase readablity of readings in terminal
delay = 0.1

# Object calls of classes
PIDx = PIDclass(kp,ki,kd)
PIDy = PIDclass(kp,ki,kd)
PIDtheta = PIDclass(kp,ki,kd)

# Start position
position = [0, 0, 0]

# End position
destination = [setpointX, setpointy, setpointtheta]

# Time management variable
prevTime = 0

# Loop to update position using PID control
while position != destination:
    currTime = time.time()
    signalx = PIDx.update(position[0], destination[0])
    signaly = PIDy.update(position[1], destination[1])
    signaltheta = PIDtheta.update(position[2], destination[2])

    # Not needed in end product but can be used to debug rate of change
    print(signalx)
    print(signaly)
    print(signaltheta)

    # Calculate time for conversion from speed to position
    period = currTime - prevTime - delay

    # Update position
    position[0] = position[0] + (signalx * period)
    position[1] = position[1] + (signaly * period)
    position[2] = position[2] + (signaltheta * period)

    # Update previous time
    prevTime = currTime

    # Print current position
    print(position)

    # Delay to increase readbility of terminal
    time.sleep(delay)
