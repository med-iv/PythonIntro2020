from collections import Counter

def sort_key(pair):
    return pair[1], pair[0]

n, w = map(int, input().split(','))
d = Counter()
s = input()
while s:
    to_be_removed = """.,:!'"?;-[]\\/@$%^&*()+=`~"""
    for elem in to_be_removed:
        s = s.replace(elem, ' ')
    tokens = [elem.lower() for elem in s.split() if elem.isalpha() and len(elem) >= w]
    d += Counter(tokens)
    s = input()
total_most = 0
set_most = set()
for elem in sorted(d.values(), reverse=True):
    if elem not in set_most and len(set_most) + 1 > n:
        break
    else:
        set_most.add(elem)
        total_most += 1        
    
for elem_1, elem_2 in sorted(d.most_common(total_most), reverse=False, key=sort_key):
    print(f"{elem_2}: {elem_1}")

    