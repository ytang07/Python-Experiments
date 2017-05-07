from visual import *
ball = sphere(pos = (0,5,0), r = 1, color = color.red)
floor = box(pos = (0,-5,0), length = 8, h = 0.2, w = 4)

y, v, dt = 5.0, 0.0, 0.01   #initialize position, velocity, and time step
while True:
    rate(400)               #400 fps
    y = y + v*dt            #duh
    ball.pos.y = y
    if y > floor.y + ball.r:
        v = v- 9.8*dt
    else:
        v = -v
