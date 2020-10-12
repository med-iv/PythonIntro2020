def check(source, sub_str):
    if (sub_str == ""):
        return True
    if len(source) == 1:
        return source == sub_str
    sub_source = []
    for i in range(len(source) // 2):
        for j in range(i + 1, len(source)):
            if sub_str in source[i::j]:
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