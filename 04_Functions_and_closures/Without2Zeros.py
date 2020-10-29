def No_2Zero(N, K):
    def f(n):
        if n == 1:
            return K - 1
        elif n == 2:
            return K ** 2 - K
        else:
            return (K-1) * f(n-1) + (K-1) * f(n-2)
    return f(N)
        
            
            
#print(No_2Zero(6, 3))