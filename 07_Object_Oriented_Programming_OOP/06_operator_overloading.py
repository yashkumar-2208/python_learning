class Point:

    def __init__(self, x,y ):
        self.x = x
        self.y = y

    def sum(self, p):
        return Point((self.x + p.x), self.y + p.x)
    
    def do_print(self):
        print(f"X is {self.x} and Y is {self.y}")


p1 = Point(4, 6)
p2 = Point(9, 3)
p = p1.sum(p2)
p.do_print()        

