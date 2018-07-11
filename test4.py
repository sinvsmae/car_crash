"""
no iteration
fruitful function

UnboundLocalError: local variable 'pos_now' referenced before assignment
edit insid pos_now() change pos_now to pos does not work
but v_now is ok.

"""


import math

t = 'Honda'
epsilon = 0.001
time_delta = 0.1

def E(t, m, v):
    E = m * pow(v, 2) / 2
    return E

def V(t, m, E):
    v = math.sqrt(2 * E / m)
    return v

def E_now(t, m, v_ini, brakeJ, time_delta):
    v = v_ini
    print(v)
    print(E(t,m,v))
    E_ini = E(t, m, v)
    print(E_ini)
    E_delta = brakeJ * time_delta
    print(E_delta)
    E_now = E_ini - E_delta
    print(E_now)
    return E_now
    
def V_now(t, m, v_ini, brakeJ, time_delta):
    E = E_now(t, m, v_ini, brakeJ, time_delta)
    if E > epsilon:
        v_now = V(t, m, E)
    else:
        v_now = 0
    return v_now

def pos_now(t, m, v_ini, brakeJ, pos_ini, time_delta):
    pos_delta = v_ini * time_delta
    pos_now = pos_ini + pos_delta
    return pos_now

def update(t, m, v_ini, brakeJ, pos_ini, time_delta):
    v_now = V_now(t, m, v_ini, brakeJ, time_delta)
    pos_now = pos_now(t, m, v_ini, brakeJ, pos_ini, time_delta)
    print(v_now, pos_now)
    return v_now, pos_now

                       
update('honda', 2500, 27, 250000, 0, 0.1)        
