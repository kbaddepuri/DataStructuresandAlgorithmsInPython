from collections import defaultdict

class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        # Mark all vertices as not visited
        visited = [False] * len(self.graph)

        # Create a queue for bfs
        queue = []

        # Mark source Node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:
            # Dequeue it and print it
            s = queue.pop(0)
            print(s, end=" ")

            # Get all the adjecent of source and check whether they are visited,
            # if not enqueue it and mark it as visited
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


# Driver code

# Create a graph given in
# the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is Breadth First Traversal"
      " (starting from vertex 2)")
g.BFS(2)