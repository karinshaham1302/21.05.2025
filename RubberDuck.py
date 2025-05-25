class RubberDuck:

    __color = 'yellow'

    def __init__(self, quack_volume=5):
        self.quack_volume = quack_volume

    @staticmethod
    def squeak():
        print('duck is squeaking...')

    @classmethod
    def get_color(cls):
        return cls.__color

    def boost_volume(self):
        self.__quack_volume *= 2

    @property
    def quack_volume(self):
        return self.__quack_volume

    @quack_volume.setter
    def quack_volume(self, value):
        if value < 0:
            self.__quack_volume = 0
        else:
            self.__quack_volume = value

    def __str__(self):
        return f"RubberDuck quack_volume={self.quack_volume} color='{RubberDuck.get_color()}'"
