def check(source, sub_str):
    if (sub_str == ""):
        return True
    if len(source) == 1 or len(sub_str) == 1:
        return sub_str in source
    for i in range(1, len(source) // (len(sub_str) - 1) + 1):
        for j in range(i):
            if sub_str in source[j::i]:
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