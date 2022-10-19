# Special is a Hunter; Special updates by
# moving in a straight line, and when it runs across an instance
# of Prey it will eat it and then change color; additionally once the
# Special object decreased to size of width/height 10 it will increase in speed until it hits speed 10
# if it gets back to width/height between 10-20 it will be set back to speed 5
# but above width/height 20 it will be speed 3


from mobilesimulton import Mobile_Simulton
from hunter import Hunter
import random

class Special(Hunter, Mobile_Simulton):
    def __init__(self, x, y):
        Hunter.__init__(self, x, y)
        # Mobile_Simulton.__init__(self, x, y, 2*Hunter.radius, 2*Hunter.radius, 0, 5)
        self.randomize_angle()

    def update(self, model):
        s= self.get_speed()
        ea = Hunter.update(self, model)

        if len(ea) != 0:
            self._color = "#" + ''.join([random.choice('ABCDEF0123456789') for _ in range(6)])

        dx,dy = self.get_dimension()
        if dx <= 10 and dy <= 10:
            if self.get_speed() < 10:
                s += 1
                self.set_speed(s)
                self._color = '#000000'
            # print(self.get_speed(), self.get_dimension())
        elif dx > 20 and dy > 20:
            self.set_speed(3)
            # print(self.get_speed(), self.get_dimension())
        else:
            self.set_speed(5)
            # print(self.get_speed(), self.get_dimension())

        self.move()

        return ea

    def display(self, canvas):
        canvas.create_rectangle(self._x - self._width/2, self._y - self._height/2,
                           self._x + self._width/2, self._y + self._height/2,
                           fill = self._color)