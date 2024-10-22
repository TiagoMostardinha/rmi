class PID():
    def __init__(self, PID_CONST: dict):
        '''
        PID constants for the controller
        '''
        self.kp = PID_CONST["kp"]
        self.ki = PID_CONST["ki"]
        self.kd = PID_CONST["kd"]
        self.h = PID_CONST["h"]

        '''
        Parameter that multiplies the error at the time instant k, k-1 and k-2
        ---
        ke[0]: k
        ke[1]: k-1
        ke[2]: k-2
        '''
        self.ke = [
            self.kp * (1 + self.h / self.ki + self.kd / self.h),
            -self.kp * (1 + 2 * self.kd / self.h),
            self.kp * self.kd / self.h
        ]

        self.last_errors = [0, 0, 0]
        self.last_u = 0
    
    def update(self, error: float) -> float:
        '''
        Update the PID controller with the new error
        '''
        self.last_errors.insert(0,error)
        self.last_errors.pop()

        '''
        Compute the control signal
        '''
        u = self.last_u + self.ke[0] * self.last_errors[0] + self.ke[1] * self.last_errors[1] + self.ke[2] * self.last_errors[2]
        self.last_u = u

        return u
        

        
