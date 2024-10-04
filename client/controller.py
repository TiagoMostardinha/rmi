h = 0.05
type = "NONE"
Kp  = 1
Td = 0
max_u = 10




def controller(type: str ,r :float,y:float):
    e = r-y
    return Kp * e
