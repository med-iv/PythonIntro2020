from collections import OrderedDict
class Spiral:
    """Нужно будеть сделать свой индекс и хранить левый верхний и правый нижний угол в полях объекта,
    чтобы потом просто пройтись по нему"""
    
    def __init__(self, string):
        from collections import defaultdict
        
        self.string = string
        self.coord = defaultdict(lambda: defaultdict(lambda: " "))
        
        self.left_bound = 0
        self.upper_bound = 0
        
        self.right_bound = 0
        self.lower_bound = 0
        
        # current coordinations
        x = 0
        y = 0
        # counter while we should go in the same direction
        counter = 0
        # bound for counter
        bound = 1
        # 0 - right, 1 - up, 2 - left, 3 - down 
        direction = 0
        
        for elem in string:
            self[x, y] = elem
            #print(elem, x, y, "counter", counter, "bound", bound, "direction", direction)
            
            if direction == 0:
                x += 1
            elif direction == 1:
                y += 1
            elif direction == 2:
                x -= 1
            else:
                y -= 1
            counter += 1
            if counter == bound:
                counter = 0
                bound += 1
                direction = (direction + 1) % 4
            
            
        
    def __setitem__(self, pos, val):
        x, y = pos
        
        self.left_bound = min(self.left_bound, x)
        self.upper_bound = max(self.upper_bound, y)
        
        self.right_bound = max(self.right_bound, x)
        self.lower_bound = min(self.lower_bound, y)
        
        self.coord[x][y] = val
        
        
    def __getitem__(self, pos):
        x, y = pos
        return self.coord[x][y]
        
    def __str__(self):
        res = ""
        for y in range(self.upper_bound, self.lower_bound - 1, -1):
            for x in range(self.left_bound, self.right_bound + 1):
                res += self[x, y]
            res += '\n'
        return res[:len(res) - 1]
    
    
    def __add__(self, other):
        res_dict = OrderedDict()
        for elem in self.string:
            res_dict[elem] = res_dict.get(elem, 0) + 1
            
        for elem in other.string:
            if elem in res_dict:
                res_dict[elem] += 1
            else:
                res_dict[elem] = 1
                
        res_string = ""
        for key, value in res_dict.items():
            res_string += key * value
        return Spiral(res_string)
    
    def __sub__(self, other):
        res_dict = OrderedDict()
        for elem in self.string:
            res_dict[elem] = res_dict.get(elem, 0) + 1

        for elem in other.string:
            if elem in res_dict:
                res_dict[elem] -= 1
                
        res_string = ""
        for key, value in res_dict.items():
            res_string += key * value
        return Spiral(res_string)
    
    def __mul__(self, n):
        res_string = []
        for elem in self.string:
            res_string.extend([elem] * n)
        return Spiral(''.join(res_string))
    
    def __iter__(self):
        return iter(self.string)
    
#S = Spiral("abbcccddddeeeee")
#I = Spiral("abcdefghi")
#print(f"{S}\n")
#print(S+I, "\n")
#print(S-I, "\n")
#print(I*2, "\n")
#print(I*2-S, "\n")
#print(*list(S+I))