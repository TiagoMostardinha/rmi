class PID:
    def __init__(self, kp, ki, kd, dt):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.dt = dt
        self.previous_error = 0
        self.integral = 0

    def update(self, error):
        # Proportional term
        P = self.kp * error

        # Integral term
        self.integral += error * self.dt
        I = self.ki * self.integral

        # Derivative term
        derivative = (error - self.previous_error) / self.dt
        D = self.kd * derivative

        # Update previous error
        self.previous_error = error

        return P + I + D
