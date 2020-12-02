import re
reg = input()
text = input()

while text:
    match_obj = re.search(reg, text)
    if not match_obj:
        print("<NONE>")
    else:
        print(f"{match_obj.start()}: {match_obj.group()}")
        for i in range(1, len(match_obj.groups()) + 1):
            if match_obj.group(i):
                print(f"{i}/{match_obj.start(i)}: {match_obj.group(i)}")
        for k, v in match_obj.groupdict().items():
            if v:
                print(f"{k}/{match_obj.start(k)}: {v}")
    text = input()