class Graph(object):
    def __init__(self):
        self.vertices = []
        self.edges = []

    def add_vertex(self, new_v):
        if len(self.vertices) == 0:
            self.vertices.append(new_v)
            return True
        i = 0
        while i < len(self.vertices):
            if self.vertices[i] == new_v:
                return False
            i += 1
        self.vertices.append(new_v)
        return True

    def add_edge(self, new_e):
        edge_added = False
        edge_in_g = False
        for e in self.edges:
            if new_e[0] == e[0] and new_e[1] == e[1]:
                edge_in_g = True
        if len(self.edges) == 0 or not edge_in_g:
            self.edges.append(new_e)
            edge_added = True
        return edge_added
