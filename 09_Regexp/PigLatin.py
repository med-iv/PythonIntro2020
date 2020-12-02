import re
word_pattern = r"[A-Za-z']+"
vowel = r"[euioaEUIOA]"
vowel_set = {'e', 'o', 'u', 'A', 'a', 'i', 'O', 'E', 'U', 'I'}
#consonant = r"[^euioaEUIOA]"

def process(match_obj) -> str:
    word = match_obj.group()
    is_cap = 'A' <= word[0] <= 'Z'
    word = word.lower()
    l = 0
    shift = 0
    m = re.search(vowel, word)
    if m:
        l += 1
        shift = m.start()
        m = re.search(vowel, word[shift+1:])
        if m:
            l += 1
    
    if l == 0:
        first = word[0]
        if is_cap:
            first = first.upper()           
        return first + word[1:]      
        
    if l == 1 and word[0] in vowel_set:
        first = word[0]
        if is_cap:
            first = first.upper()           
        return first + word[1:] + "yay"
    i = 0
    if i < len(word) and word[i] in vowel_set:
        i += 1
    while i < len(word) and word[i] not in vowel_set:
        i += 1
    first = word[i]
    if is_cap:
        first = first.upper()
    return first + word[i+1:] + word[:i] + "ay"
    
    

def main():
    #text = "This is an example of Hog Latin. As you can see, it’s silly, but lots of fun for children."
    text = input()
    #res = ""
    while text:
        print(re.sub(word_pattern, process, text), end = " ")
        text = input()
    
#import cProfile
if __name__ == "__main__":
    #cProfile.run('main()')
    main()
    