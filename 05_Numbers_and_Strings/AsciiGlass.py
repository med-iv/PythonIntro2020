def main():
    s = input()
    window_w = len(s)
    window_h = 0
    glass_w = 0
    glass_h = 0
    water_count = 0
    while s:
        window_h += 1
        if '#' in s:
            glass_h += 1
            glass_w = s.count('#')
            water_count += s.count('*')
            
        s = input()
            
    water_h = (water_count + window_w - 1) // window_w
    
    for i in range(window_h, 0, -1):
        if (i <= water_h):
            print('*' * window_w)
        elif(i == glass_w or i == 1):
            print('#' * min(glass_h, window_w) + '.' * max(0, window_w - glass_h))
        elif (i < glass_w):
            print('#' + '.' * (window_w - 1))
        else:
            print('.' * window_w)
        
if __name__ == "__main__":
    main()