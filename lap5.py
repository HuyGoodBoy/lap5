#Practical Exercises
class queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,x):
        self.queue.append(x)
    def dequeue(self):
        return self.queue.pop(0)
    def show(self):
        for q in self.queue:
            print(q)
    def is_empty(self):
        return self.queue==[]
class Graph:
    def __init__(self):
        self.a=[]
        self.label=[]
        self.n=0
    def setAMatrix(self,b,m):
        self.a=b
        self.n=m
    def setLabel(self,c):
        self.label=c
    def bfs(self,start):
        visited=[False]*self.n
        q=queue([start])
        visited[start]=True
        while q:
            vertex=q.dequeue()
            print(self.label[vertex],end=' ')
            for i in range(self.n):
                if self.a[vertex][i]==1 and visited[i]==False:
                    q.enqueue(i)
                    visited[i]=True
    def dfs(self,start,visited=None):
        if visited is None:
            visited=[False]*self.n
        visited[start]=True
        print(self.label[start],end=' ')
        for i in range(self.n):
            if self.a[start][i]==1 and visited[i]==False:
                visited[i]=True
                self.dfs(i,visited)
import sys

class WGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.weight_matrix = [[0] * num_vertices for _ in range(num_vertices)]
    def add_edge(self, u, v, weight):
        self.weight_matrix[u][v] = weight
        self.weight_matrix[v][u] = weight
    def dijkstra(self, start):
        visited = [False] * self.num_vertices
        distance = [sys.maxsize] * self.num_vertices
        distance[start] = 0
        for _ in range(self.num_vertices):
            min_dist = sys.maxsize
            min_index = -1
            for v in range(self.num_vertices):
                if not visited[v] and distance[v] < min_dist:
                    min_dist = distance[v]
                    min_index = v
            visited[min_index] = True
            for v in range(self.num_vertices):
                if not visited[v] and self.weight_matrix[min_index][v] != 0:
                    new_dist = distance[min_index] + self.weight_matrix[min_index][v]
                    if new_dist < distance[v]:
                        distance[v] = new_dist

        return distance
class WGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.weight_matrix = [[0] * num_vertices for _ in range(num_vertices)]
    def add_edge(self, u, v, weight):
        self.weight_matrix[u][v] = weight
        self.weight_matrix[v][u] = weight
    def min_key(self, key, mst_set):
        min_val = sys.maxsize
        min_index = -1
        for v in range(self.num_vertices):
            if key[v] < min_val and not mst_set[v]:
                min_val = key[v]
                min_index = v
        return min_index
    def prim_mst(self):
        parent = [-1] * self.num_vertices
        key = [sys.maxsize] * self.num_vertices
        mst_set = [False] * self.num_vertices
        key[0] = 0
        for _ in range(self.num_vertices - 1):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.num_vertices):
                if self.weight_matrix[u][v] > 0 and not mst_set[v] and self.weight_matrix[u][v] < key[v]:
                    key[v] = self.weight_matrix[u][v]
                    parent[v] = u
        return parent
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]
    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1
    def is_safe(self, v, color, colored):
        for i in range(self.num_vertices):
            if self.adj_matrix[v][i] == 1 and colored[i] == color:
                return False
        return True
    def assign_colors(self):
        colored = [-1] * self.num_vertices
        colored[0] = 0
        for v in range(1, self.num_vertices):
            for c in range(self.num_vertices):
                if self.is_safe(v, c, colored):
                    colored[v] = c
                    break
        return colored
