from itertools import islice, repeat, tee
from random import randrange


def YinYang(*seqs):
    lst = []
    for seq in seqs:
        t1, t2 = tee(seq, 2)
        lst.append(t2)
        for elem in t1:
            if elem % 2 == 0:
                yield elem
    for t2 in lst:
        for elem in t2:
            if elem % 2 == 1:
                yield elem        
        
    

        
#I=(repeat(randrange(1,5), randrange(5, 15)) for i in range(100000))
#P = 477700
#print(*islice(YinYang(*I), P, P+100, 7))