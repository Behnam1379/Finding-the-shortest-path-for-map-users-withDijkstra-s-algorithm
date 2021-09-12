import copy

from vertex import Vertex
from edge import Edge
from heap import MinHeap
class Router:

    def __init__(self,map_file_address):
        self.__edge = {}
        self.__vertices = []
        self.vertices_ = {}
        with open(map_file_address,"r") as read_map:

            try:
                a, b = read_map.readline().split()
                #creat vertices
                for i in range(int(a)):
                    line = read_map.readline().split()
                    ver_ = Vertex(int(line[0]), float(line[2]), float(line[1]))
                    self.__vertices.append(ver_)
                    self.vertices_[ver_.get_id()] = ver_

                #creat edges
                for i in range(int(b)):
                    line = read_map.readline().split()
                    self.__edge[int(line[0]), int(line[1])] = Edge(line[0], line[1], self.vertices_[int(line[0])], self.vertices_[int(line[1])])
                    self.__edge[int(line[1]), int(line[0])] = Edge(line[0], line[1], self.vertices_[int(line[0])], self.vertices_[int(line[1])])
                    self.vertices_[int(line[0])].adjacent_vertices.append(self.vertices_[int(line[1])])
                    self.vertices_[int(line[1])].adjacent_vertices.append(self.vertices_[int(line[0])])

            except ValueError:
                print("map is empty!!")

    def find_shortest_path(self, start_id, end_id):
        edges__ = copy.deepcopy(self.__edge)
        vertices_ = copy.deepcopy(self.__vertices)
        Heap = MinHeap(vertices_, self.vertices_)
        # Heap[start_id].set_value(0)
        Heap.__setitem__(start_id, 0)
        end_vertex = Heap[end_id]

        while end_id in Heap:
            v = Heap.pop()
            for neighbor in v.adjacent_vertices:
                if v.get_value() + edges__[v.get_id(), neighbor.get_id()].get_wieght() < neighbor.get_value():
                    Heap.modify(neighbor.get_id(), v.get_value() + edges__[v.get_id(), neighbor.get_id()].get_wieght())
                    neighbor.prev = v


        result = []
        current = end_vertex
        while current is not None:
            result.append(current.get_id())
            current = current.prev

        return result


