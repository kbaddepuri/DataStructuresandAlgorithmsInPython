"""
Backtracking Algorithm
Create an empty path array and add vertex 0 to it. Add other vertices, starting from the vertex 1. Before adding
a vertex, check for whether it is adjacent to the previously added vertex and not already added. If we find such
a vertex, we add the vertex as part of the solution. If we do not find a vertex then we return false.
"""
class Graph:
    def __init__(self, vertices):
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

        self.V = vertices


    def isSafe(self, v, pos, path):
        if self.graph[path[pos - 1]][v] == 0:
            return False
        # Check if current vertex not already in path
        for vertex in path:
            if vertex == v:
                return False

        return True

    def hamCycleUtil(self, path, pos):
        # base case: if all vertices are
        # included in the path
        if pos == self.V:
            # Last vertex must be adjacent to the
            # first vertex in path to make a cyle
            if self.graph[path[pos - 1]][path[0]] == 1:
                return True
            else:
                return False

        # Try different vertices as a next candidate
        # in Hamiltonian Cycle. We don't try for 0 as
        # we included 0 as starting point in hamCycle()
        for v in range(1, self.V):
            if self.isSafe(v, pos, path) == True:
                path[pos] = v

                if self.hamCycleUtil(path, pos + 1) == True:
                    return True
                # Remove current vertex if it doesn't
                # lead to a solution
                path[pos] = -1

        return False


    def hamCycle(self):
        path = [-1] * self.V
        ''' Let us put vertex 0 as the first vertex
            in the path. If there is a Hamiltonian Cycle,
            then the path can be started from any point
            of the cycle as the graph is undirected '''
        path[0] = 0

        if self.hamCycleUtil(path, 1) == False:
            print("Solution does not exist")
            return False

        self.printSolution(path)
        return True

    def printSolution(self, path):
        print("Solution exist on following path: ")
        for vertex in path:
            print(vertex, end= " ")
        print(path[0])




g1 = Graph(5)
g1.graph = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1],
            [0, 1, 0, 0, 1,],[1, 1, 0, 0, 1],
            [0, 1, 1, 1, 0], ]

g1.hamCycle()

g2 = Graph(5)
g2.graph = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1],
        [0, 1, 0, 0, 1,], [1, 1, 0, 0, 0],
        [0, 1, 1, 0, 0], ]

# Print the solution
g2.hamCycle()







