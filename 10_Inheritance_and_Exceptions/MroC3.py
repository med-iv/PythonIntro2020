inp = []

s = input()
while s:
    if 'class' in s:
        idx = 0
        s = s.replace("pass", "")
        inp.append(s + "\n    pass")
    s = input()
inp = '\n'.join(inp)
try:
    exec(inp)
except TypeError:
    print("No")
else:
    print("Yes")