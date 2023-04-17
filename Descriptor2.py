class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self._mass1 = 25
        self._t = 0.05

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def mass1(self):
        return self._mass1

    @mass1.setter
    def mass1(self, value):
        self._mass1 = value

    @property
    def t(self):
        return self._t

    @t.setter
    def t(self, value):
        self._t = value

    def math(self):
        sum = self._width * self._length * self._mass1 * self._t // 1000
        print(f'{int(sum)} т')

road = Road(5000, 20)
road.math()
road.length = 10000
road.width = 30
road.math()