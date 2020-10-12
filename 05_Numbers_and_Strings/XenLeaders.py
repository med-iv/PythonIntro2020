import time
def sort_key(row):
    return [row[0], row[1][1], row[1][0], row[1][2]]

def main():
    s = input().split()
    lst = []
    while s:
        lst.append([time.strptime(s[-1], "%H:%M:%S"), [s[0], s[1], ' '.join(s[2:len(s) - 1]), s[-1]]])
        s = input().split()
    lst.sort(reverse=False, key=sort_key)
    
    res = [lst[0][1]]
    counter = 0
    index = 0
    while index < (len(lst) - 1) and counter < 3:
        index += 1
        if lst[index][0] != lst[index - 1][0]:
            counter += 1
        if counter < 3:
            res.append(lst[index][1])
            
    lens = [0] * len(res[0])
    for row in res:
        for i in range(len(row)):
            if len(row[i]) > lens[i]:
                lens[i] = len(row[i])
    for row in res:
        for i in range(len(row)):
            print('{:<{prec}}'.format(row[i], prec=lens[i]), end=' ')
        print()
if __name__ == "__main__":
    main()