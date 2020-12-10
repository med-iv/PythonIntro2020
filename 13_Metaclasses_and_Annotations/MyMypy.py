class checked(type):
    def __new__(metacls, name, parents, dct):
        from inspect import getfullargspec
        for methname, meth in dct.items():
            if callable(meth):
                insp = getfullargspec(meth)
                #print(methname, meth, insp)
                def fun(*args, meth=meth, insp=insp, **kwargs):
                    #print(args)
                    #print(kwargs)
                    kwargs_stack = []
                    i = 0
                    for i in range(min(len(args), len(insp.args))):
                        elem = insp.args[i]
                        if elem in insp.annotations and not isinstance(args[i], insp.annotations[elem]):
                            raise TypeError(f"Type mismatch: {elem}")
                        
                    for i in range(min(len(args), len(insp.args)), len(insp.args)):
                        elem = insp.args[i]
                        if elem in insp.annotations and elem in kwargs and not isinstance(kwargs[elem], insp.annotations[elem]):
                            #raise TypeError(f"Type mismatch: {elem}")
                            kwargs_stack.append(elem)
                    
                    i1 = i + 1
                    if insp.varargs:   
                        for i1 in range(i + 1, len(args)):
                            if insp.varargs in insp.annotations \
                            and not isinstance(args[i1], insp.annotations[insp.varargs]):
                                raise TypeError(f"Type mismatch: {insp.varargs}")
                            
                        if insp.varargs in kwargs:
                            from collections.abc import Iterable
                            item = kwargs[insp.varargs]
                            if isinstance(item, Iterable):
                                for elem in item:
                                    if not isinstance(elem, insp.annotations[insp.varargs]):
                                        #raise TypeError(f"Type mismatch: {insp.varargs}")
                                        kwargs_stack.append(insp.varargs)
                            else:
                                if not isinstance(item, insp.annotations[insp.varargs]):
                                    #raise TypeError(f"Type mismatch: {insp.varargs}")
                                    kwargs_stack.append(insp.varargs)
                        
                    for i2 in range(len(insp.kwonlyargs)):
                        if i2 + i1 < len(args):
                            elem = insp.kwonlyargs[i2]
                            if elem in insp.annotations and not isinstance(args[i2 + i1], insp.annotations[elem]):
                                raise TypeError(f"Type mismatch: {elem}")                            
                        else:
                            elem = insp.kwonlyargs[i2]
                            if elem in insp.annotations and elem in kwargs \
                               and not isinstance(kwargs[elem], insp.annotations[elem]):
                                #raise TypeError(f"Type mismatch: {elem}")
                                kwargs_stack.append(elem)
                        
                        
                    if insp.varkw:
                        for k, v in kwargs.items():
                            if insp.varkw in insp.annotations and not isinstance(v, insp.annotations[insp.varkw]):
                                #raise TypeError(f"Type mismatch: {insp.varkw}") 
                                kwargs_stack.append(insp.varkw)
                    
                    for k in kwargs.keys():
                        if k in kwargs_stack:
                            raise TypeError(f"Type mismatch: {k}")
                    
                    res = meth(*args, **kwargs)
                    
                    if 'return' in insp.annotations and not isinstance(res, insp.annotations['return']):
                        raise TypeError(f"Type mismatch: return") 
                    return res
                dct[methname] = fun
        cls = super().__new__(metacls, name, parents, dct)
        return cls
            
#class E(metaclass=checked):
    #def __init__(self, var: int):
        #self.var = var if var%2 else str(var)

    #def mix(self, val: int, opt) -> int:
        #return self.var*val + opt

    #def al(self, c: int, d:int=1, *e:int, f:int=1, **g:int):
        #return self.var*d

#e1, e2 = E(1), E(2)
#code = """
#e1.mix("q", "q")
#e1.mix(2, 3)
#e2.mix(2, "3")
#e1.al("q")
#e1.al(1, 2, 3, 4, 5, 6, foo=7, bar=8)
#e2.al(1, 2, 3, 4, 5, 6, foo=7, bar=8)
#e1.al("E", 2, 3, 4, 5, 6, foo=7, bar=8)
#e1.al(1, "E", 3, 4, 5, 6, foo=7, bar=8)
#e1.al(1, 2, "E", 4, 5, 6, foo=7, bar=8)
#e1.al(1, 2, 3, "E", 5, 6, foo="7", bar=8)
#e1.al(1, f="E", d=1)
#e1.al(1, f=1, d="E")
#e1.al(1, f="E", d="1")
#e1.al(1, d="E", f="1")
#e1.al(1, e="E")
#e1.al(1, g="E")
#"""

#for c in code.strip().split("\n"):
    #try:
        #res = eval(c)
    #except TypeError as E:
        #res = E
    #print(f"Run: {c}\nGot: {res}")

