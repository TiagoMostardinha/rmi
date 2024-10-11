import numpy as np

# TODO: set sensor data in a dictionary


# TODO: get Error, the error will be the difference between left and right since you want to be at the center of panel
def calculateError(sensor_data:dict,irSensorData : list):
    return 0.8 * (irSensorData[1] - irSensorData[2])+ 0.2 * (np.mean(sensor_data[1]) - np.mean(sensor_data[2]))

# TODO: real distance is the inverse of the sensor data
def realDistance():
    pass

# TODO: the angle is in radians instead of degrees
def realAngle():
    pass

# TODO: the sensor data can have false positives, do the median of the last 3 values
def smoothSensorData(sensor_data:dict,irSensorData : list):
    for i in range(4):
        sensor_data[i].append(irSensorData[i])
        if len(sensor_data[i]) > 5:
            sensor_data[i].pop(0)
    return sensor_data

# TODO: check if the robot is at an intersection
def isAtIntersection():
    pass

def isAtDeadEnd():
    pass
