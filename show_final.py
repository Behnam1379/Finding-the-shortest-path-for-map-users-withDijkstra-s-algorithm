import matplotlib.pyplot as plt
import numpy as np


#
class Show:

    def __init__(self, map_address_, arr_shorter_path):
        self.arr_shortest_path = arr_shorter_path
        self.read_map = open(map_address_)
        a, b = self.read_map.readline().split()
        self.__edge = {}
        self.dic = {}
        self.arr_x = []
        self.arr_y = []
        for i in range(int(a)):
            line = self.read_map.readline().split()
            data = [float(line[1]), float(line[2])]
            # creat_dic_shortest_path
            self.dic[int(line[0])] = data

        for i in range(int(b)):
            line = self.read_map.readline().split()
            try:
                if int(line[1]) not in self.__edge[int(line[0])]:
                    self.__edge[int(line[0])].append(int(line[1]))
            except KeyError:
                self.__edge[int(line[0])] = [int(line[1])]
                # self.__edge[int(line[1])] = [(int(line[0]))]


    def show(self):
        for i in self.__edge:
            for v in self.__edge[i]:
                x = [self.dic[i][0], self.dic[v][0]]
                y = [self.dic[i][1], self.dic[v][1]]
                plt.plot(x, y, color='green', marker='o')
                plt.annotate(str(i), self.dic[i])

        plt.plot(self.creat_x(), self.creat_y(), '-o', color='blue')
        plt.show()

    # creat_array_x ; shortest_path
    def creat_x(self):
        array_x = []
        for i in self.arr_shortest_path:
            array_x.append(self.dic[i][0])

        return array_x

    # creat_array_y ; shortest_path
    def creat_y(self):
        array_y = []
        for i in self.arr_shortest_path:
            array_y.append(self.dic[i][1])

        return array_y


# show = Show('Maps', [8, 20, 15, 30, 5])
# show.show()