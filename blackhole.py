# The Black_Hole class is derived from Simulton; for updating it finds+removes
#   objects (of any class derived from Prey) whose center is contained inside
#   its radius (returning a set of all eaten simultons), and displays as a
#   black circle with a radius of 10 (width/height 20).
# Calling get_dimension for the width/height (for containment and displaying)'
#   will facilitate inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    radius = 10

    def __init__(self, x, y):
        self._color = '#000000'
        Simulton.__init__(self, x, y, 2*Black_Hole.radius, 2*Black_Hole.radius)
    

    def update(self, model):
        self.eaten = set()
        # if self.contains(i.get_location()):
        x = model.find((lambda x : isinstance(x, Prey)))
        # if x:
        for i in x:
            if self.contains(i.get_location()):
                self.eaten.add(i)
                model.remove(i)
        # print(len(self.eaten))
        # print(len(x))
        return self.eaten

    def display(self, canvas):
        canvas.create_oval(self._x - self._width/2, self._y - self._height/2,
                           self._x + self._width/2, self._y + self._height/2,
                           fill = self._color)

    def contains(self, xy):
        return self.distance(xy) < Black_Hole.radius
