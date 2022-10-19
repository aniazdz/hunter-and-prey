# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 


from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey):
    radius = 5

    def __init__(self, x, y):
        self._image = PhotoImage(file='ufo.gif')
        # self._color = 'red'
        Prey.__init__(self, x, y, 2 * Floater.radius, 2 * Floater.radius, 0, 5)
        self.randomize_angle()

    def update(self, model):
        if random() < 0.3:
            self.set_speed(self.get_speed() + (random()-0.5))
            self.set_angle(self.get_angle() + (random() - 0.5))
            if self.get_speed() >= 7:
                self.set_speed(7)
            elif self.get_speed() <= 3:
                self.set_speed(3)

        self.move()

    def display(self, canvas):
        # canvas.create_oval(self._x - Floater.radius, self._y - Floater.radius, self._x + Floater.radius, self._y + Floater.radius,
        #                    fill=self._color)
        canvas.create_image(*self.get_location(),image=self._image)
