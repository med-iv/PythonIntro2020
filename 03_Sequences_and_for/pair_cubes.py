#import time

#time1 = 0

import math

def main():
    #global time1
    n = int(input())
    #time1 = time.time_ns()
    i = 1
    mini = 1
    while mini <= n // 2:
        j = (n - mini) ** (1/3)
        if math.ceil(j) ** 3 + mini == n:
            print("YES")
            return
        elif math.floor(j) ** 3 + mini == n:
            print("YES")
            return            
        i += 1
        mini = i ** 3
    print("NO")
    
            
    
if __name__ == "__main__":
    main()
    #time2 = time.time_ns()
    #print((time2 - time1) / 1000000000)