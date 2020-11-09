def fcounter(CL, *args):
    class_methods = set([method_name for method_name in dir(CL) \
                  if method_name[0] != '_' and callable(getattr(CL, method_name))])
    class_fields = set([method_name for method_name in dir(CL) \
                  if method_name[0] != '_' and not callable(getattr(CL, method_name))])
    
    obj = CL(*args)
    object_methods = (set([method_name for method_name in dir(obj)
                  if method_name[0] != '_' and \
                  callable(getattr(obj, method_name))])).difference(class_methods)
    
    object_fields = (set([method_name for method_name in dir(obj)
                  if method_name[0] != '_' and \
                  not callable(getattr(obj, method_name))])).difference(class_fields)    
    return sorted(class_methods), sorted(class_fields), sorted(object_methods), sorted(object_fields)
    
#class C:
    #x, y, z = 1, 3, 5

    #def X(self): return self.x
    #def Y(self): return self.y

    #def __init__(self, dx, dy, dz):
        #self.x = dx
        #self.Y = dy
        #self.Z = dz
        
#cm, cf, om, of = fcounter(C, 6, 7, 8)
#print("Class: methods", *cm)
#print("Class: fields", *cf)
#print("Object: methods", *om)
#print("Object: fields", *of)