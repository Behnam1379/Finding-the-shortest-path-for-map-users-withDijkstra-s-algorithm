import math


class Edge:

    # Constructor
    def __init__(self, head, tail, ver_head, ver_tail):
        self.__head = int(head)
        self.__tail = int(tail)
        self.ver_head = ver_head
        self.ver_tail = ver_tail

    # getter head
    def get_head(self):
        return self.__head

    # getter tail
    def get_tail(self):
        return self.__tail

    # return long of street
    def get_wieght(self):
        # print(self.vertices_)
        x = self.ver_head.x - self.ver_tail.x
        y = self.ver_head.y - self.ver_tail.y
        return math.sqrt(x**2 + y**2)
