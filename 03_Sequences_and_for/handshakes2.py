from functools import reduce

def main():
    s = input()
    sets = []
    while(s):
        verts = set(map(int, s.rstrip(',').split(',')))
        if len(sets) == 0:
            sets = [verts]
        else:
            res = []
            un = [verts]
            for i in range(len(sets)):
                if sets[i] & verts:
                    un.append(sets[i])
                else:
                    res.append(sets[i])
            to_ap = reduce(set.union, un, set())
            #print("to_ap", to_ap)
            res.append(to_ap)
            #print("un", un)
            #print("res", res)
            sets = res
        s = input()
    if len(sets) <= 1:
        print("YES")
    else:
        print("NO")
                       


if __name__ == "__main__":
    main()