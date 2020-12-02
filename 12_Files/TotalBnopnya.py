 

codings = list(input().split())
proced = bytes.fromhex(input())



variants = [proced]

for cod1 in codings:
    for cod2 in codings:
        for cod3 in codings:
            for cod4 in codings:
                try:
                    s = proced.decode(cod1).encode(cod2).decode(cod3).encode(cod4).decode("koi8-r")#.encode(cod3).decode()#.encode(cod3).decode()
                    if s[0:4] == 'ПРОЦ':
                        print(cod1, cod2, cod3, cod4, s)
                except:
                    pass
