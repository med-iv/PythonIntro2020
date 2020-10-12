import sys
sys.setrecursionlimit(100000)

from collections import deque

g = dict()
used = dict()

def dfs(elem):
    global g
    global used
    used[elem] = True
    for vert in g[elem]:
        if not used[vert]:
            dfs(vert)
            
def bfs(elem):
    global g
    global used
    
    deq = deque()
    deq.append(elem)
    
    used[elem] = True
    
    while len(deq) != 0:
        elem = deq.popleft()
        for vert in g[elem]:
            if not used[vert]:
                used[vert] = True
                deq.append(vert)
        
    

def main():
    global g
    global used
    s = input()
    while(s):
        verts = set(map(int, s.strip(',').split(',')))
        for elem in verts:
            if elem in g:
                g[elem] |= verts
            else:
                g[elem] = verts
            used[elem] = False
        s = input()
    seed = list(used.keys())[-1]
    bfs(seed)
    
    if False in used.values():
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    main()