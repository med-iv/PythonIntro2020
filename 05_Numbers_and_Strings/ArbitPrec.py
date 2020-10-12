from decimal import Decimal, getcontext

def get_func_value(func, x):
    res = eval(func)
    return res

def main():
    func = input()
    d = int(input())
    getcontext().prec = d + 2
    
    left = Decimal('-1.5')
    left_value = get_func_value(func, left)
    right = Decimal('1.5')
    right_value = get_func_value(func, left)
    zero = Decimal('0')
    while right_value != zero and (right-left) > 10 ** (-d):
        mid = (right + left) / 2
        mid_value = get_func_value(func, mid)
        if mid_value > 0 and left_value > 0 or mid_value < 0 and left_value < 0:
            left = mid
            left_value = mid_value
        else:
            right = mid
            right_value = mid_value   
    print('{:.{prec}f}'.format(right, prec=d))
    
if __name__ == "__main__":
    main()