"""
Adjacency List:
An array of lists is used. Size of the array is equal to the number of vertices. Let the array be array[].
An entry array[i] represents the list of vertices adjacent to the ith vertex. This representation can also be used to
represent a weighted graph. The weights of edges can be represented as lists of pairs. Following is adjacency list
representation of the above graph.
"""

class AdjNode(object):
    def __init__(self, value):
        self.vertex = value
        self.next = None

class Graph(object):
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [None]*self.vertices

    def add_edge(self, src, dest):
        # Adding node to source node
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        # Adding node to destination node
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def print_graph(self):
        for i in range(self.vertices):
            print("Adjacency list of vertex from {}\n head".format(i), end=" ")
            temp = self.graph[i]
            while temp:
                print("-> {}".format(temp.vertex), end=" ")
                temp = temp.next
            print("\n")

    def bfs(self, s):
        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))

        # Create a queue for BFS
        queue = []

        # Mark th sourc node as visited and enqueue it
        visited[s] = True
        queue.append(s)

        while queue:
            # Dequeue a vertex from queue and print it
            s = queue.pop(0)
            print(s, end=" ")

            # Get all adjacent of vertices of the dequeued vertex s.
            # If adjacent has not visited, then mark it as visited and enqueue it
            node = self.graph[s]
            while node:

            #for i in self.graph[s]:
                if visited[node.vertex] == False:
                    queue.append(node.vertex)
                    visited[node.vertex] = True
                node = node.next


# Driver program to the above graph class
if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)

    graph.print_graph()
    print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
    graph.bfs(2)