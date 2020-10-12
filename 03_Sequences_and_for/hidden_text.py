def primes(n):
    pr = []
    lp = [0 for i in range(n + 1)]
    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            pr.append(i)
        j = 0
        while j < len(pr) and pr[j] <= lp[i] and i * pr[j] <= n:
            lp[i * pr[j]] = pr[j]
            j += 1
    pr.insert(0, 1)
    return pr

def check(source, sub_str):
    if (sub_str == ""):
        return True
    if len(source) == 1:
        return source == sub_str
    
    sieve = primes(len(source) // 2)
    for elem in sieve:
        for j in range(elem, len(source)):
            if sub_str in source[(elem - 1)::j]:
                return True
    return False
        
def main():
    source = input()
    sub_str = input()
    if check(source, sub_str):
        print("YES")
    else:
        print("NO")
        
    
    
if __name__ == "__main__":
    main()