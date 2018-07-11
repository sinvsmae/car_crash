import math

t = 'Honda'
m = 1500
v = 27
brakeJ = 250000

def v(t,m, v, brakeJ):
    E = m * pow(v, 2) / 2
    E_delta = brakeJ / 10
    E -= E_delta
    v = math.sqrt(2 * E / m)
    return v

def pos_now(t, v, pos_now):
    time_delta = 0.1
    pos_delta = time_delta * v
    pos_now += pos_delta
    return pos_now

def vehicle(t, m, v, brakeJ, pos_now):
    time_delta = 0.1
    E = m * pow(v, 2) / 2
    #print(E)
    E_delta = brakeJ / 10
    E -= E_delta
    #print(E)
    v = math.sqrt(2 * E / m)
    pos_delta = time_delta * v
    pos_now += pos_delta
    return v
    print(t, v, pos_now)
    print(vehicle(t, m, v, brakeJ, pos_now))


    
#print(pos_now(t, v = 27, pos_now = 0))

vehicle(t, m = 1500, v = 27, brakeJ = 25000, pos_now = 0.0)
print(vehicle(t, m, v, brakeJ, pos_now))
