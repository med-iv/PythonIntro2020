def main():
    l = [0]
    numb = int(input())
    while numb != 0:
        l.append(l[-1] + numb)
        numb = int(input())
    maxim = -float('Inf')
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if (maxim < l[j] - l[i]):
                maxim = l[j] - l[i]
    print(maxim)
    
if __name__ == "__main__":
    main()