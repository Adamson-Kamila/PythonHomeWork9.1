import time


class ColorDescriptor:
    def __init__(self, colors):
        self.colors = colors

    def __set__(self, instance, value):
        if value not in self.colors:
            raise ValueError(f"Invalid color: {value}. Allowed colors: {', '.join(self.colors)}.")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class TrafficLight:
    color = ColorDescriptor(["красный", "желтый", "зеленый"])

    def __init__(self):
        self.color = 'красный'

    def running(self):
        print('Светофор начинает работать. ')
        while True:
            print(f'Горит {self.color} сигнал светофора')
            if self.color == 'красный':
                time.sleep(7)
                self.color = 'желтый'
            elif self.color == 'желтый':
                time.sleep(2)
                self.color = 'зеленый'
            else:
                time.sleep(7)
                self.color = 'красный'
                break


traffic_light = TrafficLight()
traffic_light.running()