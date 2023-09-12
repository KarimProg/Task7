# This file used only to get the velocity of each wheel and convert from local frame to global frame
import numpy as np

def get_velocity(Vx, Vy, w,):
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
    sols = np.array([Vx, Vy, 0.2 * w])

    V1, V2, V3 = np.linalg.solve(arr, sols)
    return V1, V2, V3


Vx = float(input("Input Vx: "))
Vy = float(input("Input Vy: "))
w = float(input("Input omega(w): "))
print("\n\n")


V1, V2, V3 = get_velocity(Vx, Vy, w)
print("Local Frame : ")
print(f"V1: {np.round(V1,2)}")
print(f"V2: {np.round(V2,2)}")
print(f"V3: {np.round(V3,2)}")

phi = 45

Rot  = np.array([ [np.cos(phi * (np.pi/180)) , -np.sin(phi * (np.pi/180)), 0 ], 
                  [np.sin(phi * (np.pi/180)) ,  np.cos(phi * (np.pi/180)) , 0 ],
                  [           0              ,             0              , 1 ]])

VGx, VGy, Wg = Rot  @  [Vx, Vy, w]

VG1, VG2, VG3 = get_velocity(VGx, VGy, Wg)

print("\n\nGlobal Frame : ")
print(f"VG1: {np.round(VG1,2)}")
print(f"VG2: {np.round(VG2,2)}")
print(f"VG3: {np.round(VG3,2)}\n")
