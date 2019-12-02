class Rectangle:

    def __init__(self, posn, w, h):
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return ("{0},{1},{2}".format(self.corner, self.width, self.height))

    def area(self):
        return (self.height)*(self.width)

    def grow(self, dw, dh):
        self.width += dw
        self.height += dh

    def move(self, dx, dy):
        self.corner.x += dx
        self.corner.y += dy

    def flip(self):
        nw = self.height
        nh = self.width
        return(nw, nh)

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

box = Rectangle(Point(0,0), 100, 200)
bomb = Rectangle(Point(100,80), 5, 10)

r = Rectangle(Point(0,0), 15 ,5)
# r.grow(20,10)
print(r.flip())



p = Point(4,2)
s = Point(4,2)
# print(p == s)

a = [2,3]
b = [2,3]
# print(a == b)
