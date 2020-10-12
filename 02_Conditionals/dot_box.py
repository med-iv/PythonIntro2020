def main():
    s = input()
    x_up = y_up = z_up = -float('Inf')
    x_down = y_down = z_down = float('Inf')
    while s != "":
        x, y, z = map(float, s.split(','))
        if (x > x_up):
            x_up = x
        if (x < x_down):
            x_down = x
        if (y > y_up):
            y_up = y
        if (y < y_down):
            y_down = y
        if (z > z_up):
            z_up = z
        if (z < z_down):
            z_down = z
        s = input()
    print((x_up - x_down) * (y_up - y_down) * (z_up - z_down))

if __name__ == "__main__":
    main()