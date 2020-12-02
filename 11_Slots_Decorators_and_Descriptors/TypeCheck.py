def TypeCheck(type_params, type_result):
    type_params = list(type_params)
    def decorator(fun):
        def newfun(*args, **kwargs):
            if len(type_params) != (len(args) + len(kwargs)):
                raise TypeError(f"Function {fun.__name__} must have {len(type_params)} arguments")
            
            for i in range(len(args)):
                if type(args[i]) != type_params[i]:
                    raise TypeError(f"Type of argument {i + 1} is not {type_params[i]}")
                
            #key_params = list(type_params[len(args):])
            i = len(args)
            for key, value in kwargs.items():
                if type(value) != type_params[i]:
                    raise TypeError(f"Type of argument '{key}' is not {type_params[i]}")
                i += 1
                
            res = fun(*args, **kwargs)
            
            if (type(res) != type_result):
                raise TypeError(f"Type of result is not {type_result}")
            
            return res
        return newfun
    return decorator

#@TypeCheck((int, str, int), int)
#def valid(a, b, c=0):
    #return len(b*(a+1))+c

#@TypeCheck((int for i in range(4)), int)
#def variable(*args, **kwargs):
    #return len(args)+len(kwargs)

#@TypeCheck([int, int], int)
#def semivalid(a, b):
    #return a/b if a%2 else a*b

#valid(3, "--", 10)

#variable(1,2,a=100)

#@TypeCheck((int, str, int), int)
#def valid(a, b, c=0):
    #return len(b*(a+1))+c

#print(valid(3, "--", 10))
#try:
    #valid(3, 7, 10)
#except TypeError as E:
    #print(E)