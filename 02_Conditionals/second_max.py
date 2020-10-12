def main():
    """main function"""
    min_number = -float('Inf')
    maxim = min_number
    second_maxim = min_number
    numb = int(input())
    while numb != 0:
        if numb > maxim:
            maxim, second_maxim = numb, maxim
        elif numb != maxim and numb > second_maxim:
            second_maxim = numb
        numb = int(input())
    if second_maxim == min_number:
        print('NO')
    else:
        print(second_maxim)


if __name__ == "__main__":
    main()
