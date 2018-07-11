import math

name = 'honda'
m = 2500
v = 27
brakeJ = 250000
time_delta = 0.1    
time_ini = 0.0

def vehicle(name, m, v, brakeJ, pos_now, time_now):
    #print(v)
    time_now += time_delta
    E = m * pow(v, 2) / 2
    #print(E)
    E_delta = brakeJ / 10
    #print(E_delta)
    E -= E_delta
    if E > 0:
        #print(E)
        v = math.sqrt(2 * E / m)
        #print(v)
        pos_delta = time_delta * v
        pos_now += pos_delta
        #print(pos_now)
        #return name, v, pos_now
        print(name, 'time = '+str(time_now)+' sec', 'speed = ' +str(v)+' m/s', 'distance = '+str(pos_now)+' m', sep = ' | ')
        vehicle(name, m, v, brakeJ, pos_now, time_now)
    while True:
        if E <= 0:
            pos_delta = time_delta * v
            pos_now += pos_delta
            v = 0.0
            print(name, 'time = '+str(time_now)+' sec', 'speed = ' +str(v)+' m/s', 'distance = '+str(pos_now)+' m', sep = ' | ')
            print(name+' stopped.')
            break
    

vehicle(name, m, v, brakeJ, pos_now = 0.0, time_now = 0.0)
#print(vehicle(t, m, v, brakeJ, pos_now = 0.0))




    

    
