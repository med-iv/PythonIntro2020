def ADD(f, g):
    if callable(f) and callable(g):
        return lambda x: f(x) + g(x)
    elif callable(f) and not callable(g):
        return lambda x: f(x) + g
    elif not callable(f) and callable(g):
        return lambda x: f + g(x)
    else:
        return lambda x: f + g

def SUB(f, g):
    if callable(f) and callable(g):
        return lambda x: f(x) - g(x)
    elif callable(f) and not callable(g):
        return lambda x: f(x) - g
    elif not callable(f) and callable(g):
        return lambda x: f - g(x)
    else:
        return lambda x: f - g

def MUL(f, g):
    if callable(f) and callable(g):
        return lambda x: f(x) * g(x)
    elif callable(f) and not callable(g):
        return lambda x: f(x) * g
    elif not callable(f) and callable(g):
        return lambda x: f * g(x)
    else:
        return lambda x: f * g
    
def DIV(f, g):
    if callable(f) and callable(g):
        return lambda x: f(x) / g(x)
    elif callable(f) and not callable(g):
        return lambda x: f(x) / g
    elif not callable(f) and callable(g):
        return lambda x: f / g(x)
    else:
        return lambda x: f / g
    
    
    
#from math import *

#f = SUB(sin, cos)
#print(f(12), sin(12)-cos(12))

#g = DIV(sin, cos)
#print(g(pi/6), tan(pi/6))

#h = MUL(exp, 0.1)
#print(h(2), e**2/10)

#t = ADD(lambda s: len(s), sum)
#print(t(range(5)))