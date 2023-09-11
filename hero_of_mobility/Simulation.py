# https://www.internationaljournalssrg.org/IJEEE/2019/Volume6-Issue12/IJEEE-V6I12P101.pdf
# https://pdfs.semanticscholar.org/ed22/2105a1e4c42d64c207bcc55dec5aacd70275.pdf

import numpy as np

r = 0.2 # meters

theta1 =   0    #Rad
theta2 = 120    #Rad
theta3 = 240    #Rad


Vx = 10      # meter / sec
Vy = 10      # meter / sec
w = 20       # Rad   / sec


Vl = np.array([[ -np.sin(theta1 * (np.pi/180)) * Vx + np.cos(theta1 * (np.pi/180)) * Vy],
               [ -np.sin(theta2 * (np.pi/180)) * Vx + np.cos(theta2 * (np.pi/180)) * Vy],
               [ -np.sin(theta3 * (np.pi/180)) * Vx + np.cos(theta3 * (np.pi/180)) * Vy]])

Wl = Vl / r

print(Wl)

rot = np.array([ [-np.sin(theta1 * (np.pi/180)) , -np.sin(theta2 * (np.pi/180)) , -np.sin(theta3 * (np.pi/180)) ], 
                [ np.cos(theta1 * (np.pi/180)) ,  np.cos(theta2 * (np.pi/180)) ,  np.cos(theta2 * (np.pi/180)) ],
                [               1              ,                1              ,                1          ]])


Vg = np.linalg.inv(rot) @ [[Vx], [Vy], [w]]

Wg = Vg / r

print(Wg)