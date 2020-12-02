#class Timer:
    #from time import time
    #from sys import stderr
    
    #def __init__(self, fun):
        #self.function = fun
    
    #def __call__(self, *args, **kwargs):
        #start_time = self.time()
        #result = self.function(*args, **kwargs)
        #end_time = self.time()
        #print(f"Duration: {end_time-start_time} seconds", file=self.stderr)
        #return result


codings = list(input().split())
proced = bytes.fromhex(input())

codecs = []

variants = [proced]

alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ()[]+-*/%;.,>=<\"!: \t\n"

for i in range(len(codings)):
    for j in range(i + 1, len(codings)):
        try:
            alph.encode(codings[i]).decode(codings[j]).encode(codings[j]).decode(codings[i])
            codecs.append((codings[i], codings[j]))
            codecs.append((codings[j], codings[i]))
        except:
            pass
        
        #try:
            #alph.encode(codings[j]).decode(codings[i])
            #codecs.append((codings[i], codings[j]))
        #except:
            #pass
        
#@Timer
def main():
    global variants
    for _ in range(5):
        new_var = []
        for cods in codecs:
            for elem in variants:
                try:
                    res_b = elem.decode(cods[0]).encode(cods[1])
                    res = res_b.decode("koi8-r")
                    if res[0:4] == "ПРОЦ":
                        print(res)
                        return
                    new_var.append(res_b)
                except UnicodeEncodeError:
                    pass
                except UnicodeDecodeError:
                    pass
        variants = new_var


main()
# utf8 koi8-r CP866 CP1251