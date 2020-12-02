import time
import re
vowel = r"[euioaEUIOA-]"
time1 = time.time()
re.search(vowel, "a")
time2 = time.time()
print(time2 - time1)


vowel = set("euioaEUIOA")
time1 = time.time()
"a" in vowel
time2 = time.time()
print(time2 - time1)