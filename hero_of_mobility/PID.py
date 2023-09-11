import time

class PID:

    # Class constructor
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.integ = 0
        self.prevError = None
        self.prevTime = None

    # Function to be called to update PID control system
    def update(self, current, Setpoint):
        # New time
        currentTime = time.time()
        
        if self.prevTime is None:
            self.prevTime = currentTime
            return 0    # First iteration check
        
        # Calculate time passed
        period = currentTime - self.prevTime

        # Calculate error
        error = Setpoint - current

        # Calculate derivative
        if self.prevError is not None:
            derivative = (error - self.prevError) / period
        else:
            derivative = 0


        # Calculate integral
        self.integ += error * period

        # Reset values
        self.prevTime = currentTime
        self.prevError = error

        # Apply PID control system eqn
        return self.kp * error + self.ki * self.integ + self.kd * derivative