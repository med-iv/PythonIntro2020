def is_prime(n):
    for i in range(2, int(n ** 0.5)):
        if n % i == 0:
            return False
    return n > 1

def main():
    n = int(input())
    for i in range(n, 1, -1):
        if is_prime(i):
            print(i)
            break
    
    
if __name__ == "__main__":
    main()