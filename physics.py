import math

t = 'Honda'
m = 1500
v = 27
brakeJ = 250000

def v(t,m, v, brakeJ):
    k_engery = brakeJ
    v_delta = math.sqrt(2 * k_energy / m)
    v -= v_delta
    return v

def pos_now(t, v, pos_now):
    time_delta = 0.1
    pos_delta = time_delta * v
    pos_now += pos_delta
    return pos_now

def vehicle(t, m, v, brakeJ, pos_now):
    pos_now = pos_now(t, v, pos_now)
    v = v(t, m, v, brakeJ)
    print(t, pos_now, v)

    
#print(pos_now(t, v = 27, pos_now = 0))
vehicle(t, m = 1500, v = 27, brakeJ = 25000, pos_now = 0.0)
