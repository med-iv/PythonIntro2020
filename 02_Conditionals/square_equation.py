def main():
    a, b, c = map(int, input().split(','))
    if (a == 0):
        if (b != 0):
            print(-c / b)
        else:
            if (c == 0):
                print(-1)
            else:
                print(0)
    else:
        disc = b ** 2 - 4 * a * c
        if (disc == 0):
            print(-b / (2 * a))
        elif (disc > 0):
            res = sorted(
                ((-b + disc ** 0.5) / (2 * a), (-b - disc ** 0.5) / (2 * a))
            )
            print(res[0], res[1])
        else:
            print(0)
                
            
            

if __name__ == "__main__":
    main()