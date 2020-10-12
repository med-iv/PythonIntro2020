source = ""
sub_str = ""

def check():
    global sub_str
    global source
    if (sub_str == ""):
        return True
    if (len(source) <= 1):
        return sub_str == source
    
    i = 0
    is_res = False
    
    while (not is_res) and i <= (len(source) - len(sub_str)):
        step = 1
        while (not is_res) and step < (len(source) - i):
            if check_sub(i, step):
                is_res = True
            step += 1
        i += 1
    return is_res

def check_sub(index, step):
    res = True
    for i in range(len(sub_str)):
        if not ((index + step * i) < len(source) and source[index + step * i] == sub_str[i]):
            res = False
            break
    return res
        
def main():
    global source
    global sub_str
    source = input()
    sub_str = input()
    if check():
        print("YES")
    else:
        print("NO")
        
    
    
if __name__ == "__main__":
    main()
  