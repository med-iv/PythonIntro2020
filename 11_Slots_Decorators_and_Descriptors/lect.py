#def fun(a, b):
    #return a*2 + b

#def dfun(f, *args):
    #print(">", *args)
    #res = f(*args)
    #print("<", res)
    #return res
#print(fun(2,3))
#print(dfun(fun, 2, 3)) # Not convinient

#def genf(f):
    #def newfun(*args):
        #print(">", *args)
        #res = f(*args)
        #print("<", res)
        #return res
    #return newfun

#newf = genf(fun)
#print(newf(2, 3))
#fun = genf(fun)

#@genf
#def fun(a, b):
    #return a*2+b


class Timer:
    from time import time
    from sys import stderr
    
    def __init__(self, fun):
        self.function = fun
    
    def __call__(self, *args, **kwargs):
        start_time = self.time()
        result = self.function(*args, **kwargs)
        end_time = self.time()
        print(f"Duration: {end_time-start_time} seconds", file=self.stderr)
        return result
@Timer
def payload(delay):
    return sorted(sum(range(i)) for i in range(delay))

print(payload(10000)[-1])