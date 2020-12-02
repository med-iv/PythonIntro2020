def Stat(*args):
    if len(args) == 1:
        cl = args[0]
        fields = list(vars(cl))
        for i in range(len(fields)):
            if fields[i][0] != "_" and not callable(cl.__dict__[fields[i]]):
                field = fields[i]
                setattr(cl, f"vl_{field}", cl.__dict__[field])
                setattr(cl, f"rd_{field}", 0)
                setattr(cl, f"wt_{field}", 0)
                def set_getter_and_setter(field):
                    def getter(self):
                        #print(self, field)
                        self.__setattr__(f"rd_{field}", self.__getattribute__(f"rd_{field}") + 1)
                        return getattr(self, f"vl_{field}")
                    def setter(self, value):
                        #print(self, value, field)
                        self.__setattr__(f"wt_{field}", self.__getattribute__(f"wt_{field}") + 1)
                        return setattr(self, f"vl_{field}", value)
                    setattr(cl, field, property(getter, setter))
                set_getter_and_setter(field)
        return cl
    else:
        obj = args[0]
        field = args[1]
        return (obj.__dict__.get(f"rd_{field}", 0), obj.__dict__.get(f"wt_{field}", 0))

#@Stat
#class C:
    #A, B = 3, 4
    #def __init__(self, a=None):
        #if a:
            #self.A = a

#c, d = C(), C(123)
#print(Stat(c, "A"), Stat(d, "A"))
#d.A = c.A * 2 + c.B
#c.B = d.A - 1 - len([d.B, d.B, d.B])
#print(Stat(c, "A"), Stat(c, "B"))
#print(Stat(d, "A"), Stat(d, "B"))
#print(Stat(c, "Foo"))