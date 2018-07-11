"""
stopped using 'for' statement
stopped loop finally 
print 'bang' twice, don't konw why

"""

import math

time_delta = 0.1
time_reaction = 20

def vehicle(time_now, name1, m1, v1, brakeJ1, name2, m2, v2, brakeJ2, pos2_now, gap):
    if gap > 0: 
        if time_now <= time_reaction:
            time_now += time_delta
            E1 = m1 * pow(v1, 2) / 2
            E1_delta = brakeJ1 / 10
            print(name1, 'speed1 = '+str(v1), 'E1 = '+str(E1), 'E1_delta ='+str(E1_delta))
            E1 -= E1_delta
            if E1 > 0:
                print(name1, 'E1 = '+str(E1))
                v1 = math.sqrt(2 * E1 / m1)
                print(name1, 'speed1 = '+str(v1), 'E1 = '+str(E1))
                pos1_now = pos2_now + gap
                pos1_delta = time_delta * v1
                pos1_now += pos1_delta
                print(name1, 'speed1 = '+str(v1), 'distance1 = '+str(pos1_now))
                pos2_delta = time_delta * v2
                pos2_now += pos2_delta
                print(name2, 'speed2 = '+str(v2), 'distance2 = '+str(pos2_now))
                print('distance1 = '+str(pos1_now), 'distance2 = '+str(pos2_now))
                gap = pos1_now - pos2_now
                print('gap = '+str(gap))
                print('time = '+str(time_now)+'sec', name1, 'speed = ' +str(v1)+' m/s', 'distance = '+str(pos1_now)+' m', name2, 'speed = ' +str(v2)+' m/s', 'distance = '+str(pos2_now)+' m', 'gap = '+str(gap), sep = ' | ')
                vehicle(time_now, name1, m1, v1, brakeJ1, name2, m2, v2, brakeJ2, pos2_now, gap)
    while True:
        if gap < 0.0:
            print('BANG!')
            break
        

vehicle(time_now =0.0, name1 = 'Honda', m1 = 2500, v1 = 27, brakeJ1 = 250000, name2 = 'Toyota', m2 = 3000, v2 = 27, brakeJ2 = 450000, pos2_now = 0.0, gap = 2)
