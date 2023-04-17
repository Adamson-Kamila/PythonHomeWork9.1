class RoadMeta(type):
    def __call__(cls, length, width, *args, **kwargs):
        if length < 1000:
            raise ValueError('Длина дороги должна быть не менее 1000 метров')
        return super().__call__(length, width, *args, **kwargs)


class Road(metaclass=RoadMeta):
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.mass1 = 25
        self.t = 0.05

    def math(self):
        sum = self._width * self._length * self.mass1 * self.t // 1000
        print(f'{int(sum)} т')


road = Road(1000, 20)
road.math()