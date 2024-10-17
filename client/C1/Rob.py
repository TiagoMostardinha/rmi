from croblink import *
from utils.PID import PID

WINDOW_SIZE = 5

LPF_CONST = {
    "alpha": 2/(WINDOW_SIZE + 1),
    "sensors": ["front", "left", "right"]
}

PID_CONST = {
    "kp": 0.1,
    "ki": 0.1,
    "kd": 0.1,
    "h": 0.5
}


class Rob(CRobLinkAngs):
    def __init__(self, rob_name, rob_id, angles, host):
        CRobLinkAngs.__init__(self, rob_name, rob_id, angles, host)

        self.sensorWindows = {
            "front": [],
            "left": [],
            "right": []
        }

        self.last_lpf = {
            "front": 0,
            "left": 0,
            "right": 0
        }
        
        self.explore_pid = PID(PID_CONST)

    def run(self):
        if self.status != 0:
            print("Connection refused or error")
            quit()

        state = 'stop'
        stopped_state = 'run'

        while True:
            self.readSensors()

            # TODO: create a window of 5 measures of the sensors
            self.addToWindows()

            if not self.isAllWindowsFull():
                continue

            # TODO: implement Low Pass Filter to remove noise
            self.lowPassFilter()

            if self.measures.endLed:
                print(self.robName + " exiting")
                quit()

            if state == 'stop' and self.measures.start:
                state = stopped_state

            if state != 'stop' and self.measures.stop:
                stopped_state = state
                state = 'stop'

            if state == 'run':
                self.explore()

    # TODO: check if window is full
    def isWindowFull(self, window: str):
        return len(self.sensorWindows[window]) >= WINDOW_SIZE

    # TODO: check if all windows are full
    def isAllWindowsFull(self):
        for window in self.sensorWindows.keys():
            if not self.isWindowFull(window):
                return False
        return True

    # TODO: implement logic to add to window
    def addToWindows(self):
        def isFull(window: list):
            return len(window) > WINDOW_SIZE

        '''
        front_sensor    = 0
        left_sensor     = 1
        right_sensor    = 2
        back_sensor     = 3
        '''

        self.sensorWindows["front"].insert(0, self.measures.irSensor[0])
        self.sensorWindows["left"].insert(0, self.measures.irSensor[1])
        self.sensorWindows["right"].insert(0, self.measures.irSensor[2])

        if isFull(self.sensorWindows["front"]):
            self.sensorWindows["front"].pop()
        if isFull(self.sensorWindows["left"]):
            self.sensorWindows["left"].pop()
        if isFull(self.sensorWindows["right"]):
            self.sensorWindows["right"].pop()

    # TODO: Low Pass Filter

    def lowPassFilter(self):
        '''
        I'll be using Exponential Moving Average (EMA), instead of Kalman Filter
        because it is less computationally expensive
        '''
        def lpf(current_value: float, last_value: float, alpha: float):
            return alpha * current_value + (1 - alpha) * last_value

        for sensor in LPF_CONST["sensors"]:
            self.last_lpf[sensor] = round(
                lpf(self.sensorWindows[sensor][0],
                    self.last_lpf[sensor], LPF_CONST["alpha"]),
                5)

    # TODO: implement logic detect intersections

    def isAtIntersection(self):
        pass

    # TODO: implement logic to detect turns
    def isAtTurn(self):
        # TODO: might do specific use case where you can go straight instead of turning
        pass

    # TODO: implement logic to detect dead ends

    def isAtDeadEnd(self):
        pass

    # TODO: implement explore logic

    def explore(self):

        # TODO: implement logic about detecting intersections, turns and dead ends

        # TODO: Implement PID to keep on center
        error = self.last_lpf["left"] - self.last_lpf["right"]
        
        u = self.explore_pid.update(error)
        print("\n\nError:",error, "\nU:",u)

        self.driveMotors(0.1 + u, 0.1 - u)
    
    