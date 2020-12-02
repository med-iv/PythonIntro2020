import re
bad_brace1 = re.compile(r"\w+\(")
bad_brace2 = re.compile(r"\)\w+")
allowed = set(r"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzабвг()+-*/%_")

class Assignment_error(Exception): pass
class Syntax_error(Exception): pass

global_dict = dict()



s = input()
while s:
    try:
        s = "".join(s.split())
        if s[0] != '#':
            s= s.replace("a", "б")
            s = s.replace("_", "в")
            #print(s)
            elems = s.split("=")
            #print(elems)
            if len(elems) > 2:
                raise Syntax_error
            elif len(elems) == 2:
                if not str.isidentifier(elems[0]):
                    raise Assignment_error
                if "**" in elems[1]:
                    raise Syntax_error                  
                for elem in elems[1]:
                    if elem not in allowed:
                        raise Syntax_error
                if re.match(bad_brace1, elems[1]) or re.match(bad_brace2, elems[1]):
                    raise Syntax_error
                #if not re.fullmatch(aripmetic, elems[1]):
                    #raise Syntax_error
                res_str0 = []
                for elem in elems[0]:
                    if "A" <= elem.upper() <= 'Z':
                        res_str0 += ['г', elem]
                    else:
                        res_str0 += [elem]
                res_str0 = ''.join(res_str0)
                
                res_str1 = []
                for elem in elems[1]:
                    if "A" <= elem.upper() <= 'Z':
                        res_str1 += ['г', elem]
                    else:
                        res_str1 += [elem]
                res_str1 = ''.join(res_str1)  
                res_str1 = res_str1.replace("/", "//")
                res = eval(res_str1, global_dict) 
                global_dict[res_str0] = res
            else:
                if "**" in elems[0]:
                    raise Syntax_error
                for elem in elems[0]:
                    if elem not in allowed:
                        raise Syntax_error
                if re.match(bad_brace1, elems[0]) or re.match(bad_brace2, elems[0]):
                    raise Syntax_error
                #if not re.fullmatch(aripmetic, elems[0]):
                    #raise Syntax_error
                res_str = []
                for elem in elems[0]:
                    if "A" <= elem.upper() <= 'Z':
                        res_str += ['г', elem]
                    else:
                        res_str += [elem]
                res_str = ''.join(res_str)
                res_str = res_str.replace("/", "//")
                #print(res_str)
                print(eval(res_str, global_dict))
            
    except Syntax_error:
        print("Syntax error")
    except SyntaxError:
        print("Syntax error")
    except Assignment_error:
        print("Assignment error")
    except NameError:
        print("Name error")
    except Exception:
        print("Runtime error")
        
    s = input()