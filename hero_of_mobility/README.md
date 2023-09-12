# Hero Of Mobility

Omnidirectional is defined as simply being able to move 
any direction. The occupied robotic space consists of three 
dimensions in mobile robots: the x, y (point position on the 
robot) and the ω (robot orientation). Using 
omnidirectional motion method in geometry robotics as 
shown in Figure 1. The robot can move in any direction 
irrespective of position and orientation, so that the linear 
angular velocity 𝑉𝑥 and 𝑉𝑦 can be generated simultaneously. 

![The omnidirectional three-wheel](imgs/img_01.png)

For the robot -considered as a particle- as shown in Figure 2. the x and y components of 
the orientation of the robot are described as:

V1 * cos( 𝛼1 ) - V2 * sin( 𝛼2 ) - V3 * sin( 𝛼3 ) = Vx

V1 * sin( 𝛼1 ) + V2 * cos( 𝛼2 ) - V3 * cos( 𝛼3 ) = Vy

V1              +       V2        +         V3      = R * w

![Factorize the Velocities](imgs/img_02.png)

- After generalizing the matrix we use the coefficients of `sin` and `cos` to get the matrix.

- Solve the matrix equation using `Linear Algebra` to get the vector V which has the velocity of each wheel.
