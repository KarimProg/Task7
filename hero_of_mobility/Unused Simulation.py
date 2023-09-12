# https://www.internationaljournalssrg.org/IJEEE/2019/Volume6-Issue12/IJEEE-V6I12P101.pdf
# https://pdfs.semanticscholar.org/ed22/2105a1e4c42d64c207bcc55dec5aacd70275.pdf

import numpy as np


def calculate_wheel_velocities_local(Vx, Vy, w, wheel_config):
    wheel_velocities = []
    
    for wheel_info in wheel_config:
        L = wheel_info['distance']
        theta = wheel_info['angle']
        
        V = Vx * np.cos(theta) + Vy * np.sin(theta)
        omega = -Vx * np.sin(theta) + Vy * np.cos(theta) + L * w
        
        wheel_velocities.append(V + omega)
    
    return wheel_velocities

def calculate_wheel_velocities_global(Vx, Vy, w, phi):
    wheel_velocities = []

    rot = np.array([ [-np.sin(phi * (np.pi/180)) , -np.sin(phi * (np.pi/180)) , -np.sin(phi * (np.pi/180)) ], 
                     [ np.cos(phi * (np.pi/180)) ,  np.cos(phi * (np.pi/180)) ,  np.cos(phi * (np.pi/180)) ],
                     [            1              ,             1              ,             1          ]])
    
    V = rot @ [[Vx], [Vy], [w]]
    wheel_velocities.extend(v[0] for v in V)
    
    return wheel_velocities


R = 0.2 # meters

theta1 =   0    # Degree
theta2 = 120    # Degree
theta3 = 240    # Degree

phi = np.radians(45)        # The angle between the robot’s x-axis and the global x-axis.

Vx = 10      # meter / sec
Vy = 10      # meter / sec
w = 20       # Rad   / sec

wheel_config = [
    {'distance': R, 'angle': theta1 *  (np.pi / 180)},                     # Wheel 1 configuration: distance = 0.2, angle = 0 degrees
    {'distance': R, 'angle': theta2 *  (np.pi / 180)},                     # Wheel 2 configuration: distance = 0.2, angle = 120 degrees (in radians)
    {'distance': R, 'angle': theta3 *  (np.pi / 180)}                      # Wheel 3 configuration: distance = 0.2, angle = 240 degrees (in radians)
]

Vl = wheel_velocities = calculate_wheel_velocities_local(Vx, Vy, w, wheel_config)

for i, v in enumerate(Vl, start = 1):
    v = "{:.2f}".format(v)
    print(f"Velocity of Wheel {i} in Local frame: {v}")

print("\n\n")

Vg = calculate_wheel_velocities_global(Vx, Vy, w, phi)

for i, v in enumerate(Vg, start = 1):
    v = "{:.2f}".format(v)
    print(f"Velocity of Wheel {i} in global frame: {v}")
