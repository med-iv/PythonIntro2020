import random
from math import cos, sin, atan2, pi
from collections import namedtuple

Vector = namedtuple('Vector', ['x', 'y'])

def rotate(phi, v):
    return Vector( x = (v.x * cos(phi) - v.y * sin(phi)), y =  (v.x * sin(phi) + v.y * cos(phi)))


def randsquare(a, b):
    bias = Vector(x = (a[0] - b[0]), y = (a[1] - b[1]))
    angle = atan2(bias.y, bias.x)
    b_angle = (pi / 4) - angle
    norm_bias = rotate(b_angle, bias)
    #print(norm_bias)
    
    r1 = random.random()
    r2 = random.random()
    
    norm_rand_p = Vector(x = r1 * norm_bias.x, y = r2 * norm_bias.y)
    rand_p = rotate(-b_angle, norm_rand_p)

    return rand_p.x + b[0], rand_p.y + b[1]