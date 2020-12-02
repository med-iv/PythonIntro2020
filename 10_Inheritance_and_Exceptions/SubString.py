class SubString(str):
        
    def wrap(func, *args, **kwargs):
        res = func(*args, **kwargs)
        if (type(res) == str):
            return SubString(res)
        else:
            return res
        
    def decorator(func):
        def wrap(*args, **kwargs):
            res = func(*args, **kwargs)
            if (type(res) == str):
                return SubString(res)
            else:
                return res
        return wrap
    
    def __add__(self, *args, **kwargs):
        return SubString.wrap(str.__add__, self, *args, **kwargs)
    
    def __radd__(self, other):
        return SubString.wrap(str.__add__, other, self)
    
    def __mul__(self, *args, **kwargs):
        return SubString.wrap(str.__mul__, self, *args, **kwargs) 
    
    def __iter__(self, *args, **kwargs):
        return SubString.wrap(str.__iter__, self, *args, **kwargs) 
    
    def __len__(self, *args, **kwargs):
        return SubString.wrap(str.__len__, self, *args, **kwargs) 
    
    def __getitem__(self, *args, **kwargs):
        return SubString.wrap(str.__getitem__, self, *args, **kwargs)           
    
    def __sub__(self, other):
        from collections import Counter
        c = Counter(list(other))
        inp = list(self)
        res = []
        for elem in inp:
            if c[elem]:
                c[elem] -= 1
            else:
                res.append(elem)
        del Counter
        return SubString(''.join(res))
    
    def __getattribute__(self, name):
        return SubString.decorator(str.__getattribute__(self, name))
    
    
#print(SubString("qwertyerty")-SubString("ttttr"))    
#A, B = SubString(list(range(5,15))), SubString(list(range(8,17)))
#print(f"{A} // {B}\n'{A-B}'//'{B-A}'")
#S, T = SubString(list(range(15,27))), SubString(tuple(range(20,55,3)))
#print(S)
#print(T)
#print(S-T, T-S)
#print(S*2-T*3)
#print(S[2:-2]-T[6:-6])
#print(S.replace(",",";")-T)
#print(S.replace(SubString(","),SubString("-=-"))-T)
#print(T.count(S[-6]))
#print(T[3:5] in S)

#import string
#S=SubString("NOTE: gravity is a myth, the Earth sucks.")
#print(S-string.ascii_lowercase)
#print(string.digits+S-string.ascii_uppercase)

#S=SubString("NOTE: gravity is a myth, the Earth sucks.")
#for m in ("isprintable", "upper", "title", "swapcase", "capitalize", "isascii"):
    #print(getattr(S, m)())