# data structure of graph
import unittest

class Edge:
    def __init__(self, v, w):
        self.v = v
        self.w = w

class Graph:
    def __init__(self, vertexs):
        self.vertexs = vertexs

    def setEdge(self, v, w):
        pass

    def hasPath(self, v, w):
        pass


# class GraphInMatrix(Graph):
#     # def __init__(self):
#     #     pass

#     def setEdge(self, v, w):
#         self.matrix = [[0 for col in range(cols)] for row in range(rows)]
#         pass

#     def hasPath(self, v, w):
#         return False

class GraphInList(Graph): 
    def __init__(self, vertexs):
        Graph.__init__(self, vertexs)
        self.edgeSet = []
        for i in range(0, vertexs):
            self.edgeSet.append([])

    def setEdge(self, v, w):
        exists = False
        for x in self.edgeSet[v]:
            if x == w:
                exists = True
                break
        if not exists:
            self.edgeSet[v].append(w)
            self.edgeSet[w].append(v)


    def edgeCount(self):
        cnt = 0
        for i in range(0, self.vertexs):
            cnt += len(self.edgeSet[i])
        return cnt/2
    
    def hasPath(self, v, w):
        return len(self.getPath(v, w))>0

    def getPath(self, v, w):
        path = []
        if self._getPath(v, w, [v,], path):
            path.insert(0, v)
        return path

    def _getPath(self, v, w, nodes, path):
        ns = self.edgeSet[v]
        for x in ns:
            if x == w:
                path.append(w)
                return True
        for x in ns:
            if not nodes.__contains__(x):
                nodes.append(x)
                if self._getPath(x, w, nodes, path):
                    path.insert(0, x)
                    return True
        return False

class GraphTest(unittest.TestCase):
    def setUp(self):
        vCnt = 10
        self.g = GraphInList(vCnt)
        self.g.setEdge(0, 1)
        self.g.setEdge(0, 5)
        self.g.setEdge(0, 8)
        self.g.setEdge(1, 3)
        self.g.setEdge(4, 9)
        self.g.setEdge(5, 6)
        self.g.setEdge(6, 9)
        self.g.setEdge(7, 8)

    def testInitGraphVertexs(self):
        assert self.g.vertexs == 10

    def testInitGraphEdges(self):
        assert self.g.edgeCount() == 8

    def testHasPath(self):
        assert self.g.hasPath(0, 2) == False
        assert self.g.getPath(0, 9) == [0, 5, 6, 9], self.g.getPath(0, 9)

if __name__ == '__main__':
    suite = unittest.makeSuite(GraphTest,'test')
    runner = unittest.TextTestRunner()
    runner.run(suite)
