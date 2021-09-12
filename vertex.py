class Vertex:

    def __init__(self, identity, y, x, value=float('inf')):
        self.__identity = identity
        self.x = x
        self.y = y
        self.adjacent_vertices = []
        self.__value = value
        self.prev = None

    # getter identity
    def get_id(self):
        return self.__identity

    # getter value
    def get_value(self):
        return self.__value

    # setter value
    def set_value(self, value):
        self.__value = value

    # equal
    def __eq__(self, other):
        if not isinstance(other, Vertex):
            raise TypeError(str(other) + ' is not and instance of ' + self.__class__.__name__)
        return self.__identity == other.__identity

    def __gt__(self, other):
        if not isinstance(other, Vertex):
            raise TypeError(str(other) + ' is not and instance of ' + self.__class__.__name__)
        return self.__value > other.__value

    def __lt__(self, other):
        if not isinstance(other, Vertex):
            raise TypeError(str(other) + ' is not and instance of ' + self.__class__.__name__)
        return other.__value > self.__value

    def __ge__(self, other):
        if not isinstance(other, Vertex):
            raise TypeError(str(other) + ' is not and instance of ' + self.__class__.__name__)
        return other.__value <= self.__value

    def __le__(self, other):
        if not isinstance(other, Vertex):
            raise TypeError(str(other) + ' is not and instance of ' + self.__class__.__name__)
        return other.__value >= self.__value

    def __str__(self):
        return str(self.__identity)

    def __repr__(self):
        return str(self.__identity)