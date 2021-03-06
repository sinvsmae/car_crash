"""
no iteration
fruitful function

successful vehicle module

UnboundLocalError: local variable 'pos_now' referenced before assignment
but v_now is ok.

change pos_now to Pos_now is ok.....

how to return function and seperate the result


"""


import math

t1 = 'Honda'
t2 = 'Toyota'
epsilon = 0.001
time_delta = 0.1
time_ini = 0

def E(t, m, v):
    E = m * pow(v, 2) / 2
    return E

def V(t, m, E):
    v = math.sqrt(2 * E / m)
    return v

def E_now(t, m, v_ini, brakeJ, time_delta):
    v = v_ini
    #print(v)
    #print(E(t,m,v))
    E_ini = E(t, m, v)
    #print(E_ini)
    E_delta = brakeJ * time_delta
    #print(E_delta)
    E_now = E_ini - E_delta
    #print(E_now)
    return E_now
    
def V_now(t, m, v_ini, brakeJ, time_delta):
    E = E_now(t, m, v_ini, brakeJ, time_delta)
    if E > epsilon:
        v_now = V(t, m, E)
    else:
        v_now = 0
    return v_now

def Pos_now(t, m, v_ini, brakeJ, pos_ini, time_delta):
    pos_delta = v_ini * time_delta
    pos_now = pos_ini + pos_delta
    return pos_now

def Time_now(time_ini, time_delta):
    time_now = time_ini + time_delta
    return time_now
    
def vehicle_now(t, m, v_ini, brakeJ, pos_ini, time_ini, time_delta):
    time_now = Time_now(time_ini, time_delta)
    v_now = V_now(t, m, v_ini, brakeJ, time_delta)
    pos_now = Pos_now(t, m, v_ini, brakeJ, pos_ini, time_delta)
    print(str(time_now)+' sec', t, 'v = '+str(v_now)+'m/s', 'pos = '+str(pos_now)+'m', sep=' | ')
    return time_now, v_now, pos_now

def vehicle_update(t, m, v_ini, brakeJ, pos_ini, time_ini, time_delta):
    while True:
        vehicle_now(t, m, v_ini, brakeJ, pos_ini, time_ini, time_delta)
        time_ini = Time_now(time_ini, time_delta)
        v_ini = V_now(t, m, v_ini, brakeJ, time_delta)
        pos_ini = Pos_now(t, m, v_ini, brakeJ, pos_ini, time_delta)
        if v_ini < epsilon:
            break
    print('stopped.')
