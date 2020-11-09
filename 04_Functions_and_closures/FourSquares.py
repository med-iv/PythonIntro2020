import math
#import time


res = set()
#obs = set()
n = int(input())
#time1 = time.time()
b = math.ceil(n ** 0.5)
for i in range(b + 1):
    i_2 = i ** 2
    for j in range(i, b + 1):
        j_2 = j ** 2
        for k in range(j, b + 1):
            #t1 = tuple(sorted([i, j, k]))
            #if t1 in obs:
                #break
            #else:
                #obs.add(t1)
            k_2 = k ** 2
            s_2 = n - i_2 - j_2 - k_2
            if s_2 >= 0:
                s = s_2 ** 0.5
                #print(i, j, k, s)
                if math.floor(s) ** 2 + i_2 + j_2 + k_2 == n:
                    res.add(tuple(sorted([math.floor(s), i, j, k], reverse=True)))
                elif math.ceil(s) ** 2 + i_2 + j_2 + k_2 == n:
                    res.add(tuple(sorted([math.ceil(s), i, j, k], reverse=True)))
                    
for elem in sorted(res):
    print(' '.join(map(str, elem)))
    
#time2 = time.time()
#print(time2 - time1)