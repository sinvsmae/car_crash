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
time_delta = 0.1    #unit = sec
time_ini = 0        #unit = sec
reaction_time = 2   #unit = sec

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

def Pos_now(t, m, v_ini, pos_ini, time_delta):
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
        
def pos_buffer(t, m, v_ini, pos_ini, time_ini, time_delta):
    time_buffer = int(reaction_time / time_delta)
    for i in range(time_buffer):
        pos_now = pos_ini
        pos_now = Pos_now(t, m, v_ini, pos_ini, time_delta)
    return pos_now

pos_buffer = pos_buffer(t = 'Toyota', m = 3000, v_ini = 27, pos_ini = 0, time_ini = 0, time_delta = 0.1)                  
print(pos_buffer)

def vehicles_now(t1, m1, v1_ini, brakeJ1, t2, m2, v2_ini, brakeJ2, pos_ini, gap, time_ini, time_delta):
    t = t2
    m = m2
    v_ini = v2_ini
    brakeJ = brakeJ2
    vehicle_now(t, m, v_ini, brakeJ, pos_ini, time_ini, time_delta)
    t = t1
    m = m1
    v_ini = v1_ini
    brakeJ = brakeJ1
    pos_ini = pos_ini + gap
    vehicle_now(t, m, v_ini, brakeJ, pos_ini, time_ini, time_delta)
 
    """here shall use list/turple to simplify the module
        or library shall work. so that i can create individual object.
    """


def vehicles_update(t1, m1, v1_ini, brakeJ1, t2, m2, v2_ini, brakeJ2, pos_ini, gap, time_ini, time_delta):
    while True:
           t = t2
           m = m2
           v_ini = v2_ini
           brakeJ = brakeJ2
           vehicle_now(t, m, v_ini, brakeJ, pos_ini, time_ini, time_delta)
           





#vehicles_now(t1 = 'Honda', m1 = 2500, v1_ini = 27, brakeJ1 = 250000, t2 = 'Toyota', m2 = 3000, v2_ini = 27, brakeJ2 = 450000, pos_ini = 0, gap = 2, time_ini = 0, time_delta = 0.1)

#update(t = "Toyota", m = 3000, v_ini = 27, brakeJ = 450000, pos_ini = 0, time_ini = 0, time_delta = 0.1)        
