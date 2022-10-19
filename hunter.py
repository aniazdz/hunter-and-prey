# The Hunter class is derived (in order) from both Pulsator and Mobile_Simulton.
#   It updates/displays like its Pulsator base, but is also mobile (moving in
#   a straight line or in pursuit of Prey), like its Mobile_Simultion base.


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):
    dist = 200

    def __init__(self, x, y):
        Pulsator.__init__(self, x, y)
        Mobile_Simulton.__init__(self, x, y, 2*Pulsator.radius, 2*Pulsator.radius, 0, 5)
        self.randomize_angle()

    def update(self, model):
        ea = Pulsator.update(self, model)
        p = model.find((lambda x: isinstance(x, Prey) and int(self.distance(x.get_location()) <= self.dist)))
        preydist = 300

        for i in p:
            if self.distance(i.get_location()) < preydist:
                preydist = self.distance(i.get_location())
                ix, iy = i.get_location()
                self.set_angle(atan2(iy - self._y, ix - self._x))
        self.move()
        return ea