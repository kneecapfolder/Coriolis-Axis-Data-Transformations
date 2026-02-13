import math
import time
import threading
from GUI import AppInterface

r = .375 # 35.5cm

def transform(x_prime, y_prime, offset_theta):
    # x' = R*cos(theta)
    # y' = R*sin(theta)
    
    print(data['x'])

    R = math.hypot(x_prime, y_prime)
    theta = math.atan2(y_prime, x_prime)
    x = R*math.cos(theta - offset_theta) # + x_prime
    y = R*math.sin(theta - offset_theta) # + y_prime

    return x, y


def animate(data, index, gui : AppInterface):
    # w = 2*Pi/T
    # T = 1.867 [s]

    starting_angle = 61.8
    w = 3.365 # omega

    app.draw_point(app.canvas1, data['x'][index], data['y'][index], data['t'][index])
    x, y = transform(data['x'][index], data['y'][index], starting_angle-w*data['t'][index])
    app.draw_point(app.canvas2, x, y, data['t'][index])

    time.sleep(0.03)
    animate(data, index+1 if index+1 < len(data['t']) else 0, gui)




if __name__ == '__main__':
    t = []
    y = []
    x = []

    with open('mass_A.txt', 'r') as file:
        raw = file.read()
        rows = raw.split('\n')
        for row in rows:
            (_t, _y, _x) = row.split()
            t.append(float(_t))
            y.append(float(_y))
            x.append(float(_x))

    data = {
        't': t,
        'y': y,
        'x': x,
    }

    app = AppInterface()
    threading.Thread(target=animate, args=(data, 0, app)).start()
    app.start()