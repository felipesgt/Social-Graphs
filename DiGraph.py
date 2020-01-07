#
#  @author Felipe Soares Gonçalves
#  @date 03/09/2018
#
from heapq import heappush, heappop
import sys
class DiGraph(object):
    # Directed Graph Class
    class DiGraph(object):
        # Create an empty graph
        def __init__(self):
            ## A dictionary that stores an entry of a node, as the key, and a set of outgoing edges (destination node, weight) from the node, as its value.
            self.graph = {}
            ## A dictionary that stores immediate neighbors on the shortest path
            self.pathAnt = {}
            ## Number of Edges
            self.__numEdges = 0
            ## Number of Vertices
            self.__num_vertices = 0


        ##
        # Add an edge from the source node to the destination node
        # @param src Source node
        # @param dst Destination node
        # @param c weight of the edge
        #
        # @return False if src or dst  is None, <br>
        #         or c <= 0, <br>
        #         or src == dst, <br>
        #         True if a new edge is added with the weight
        #
        def addEdge(self, src, dst, c=1):
            if src == None:
                return False
            elif dst == None:
                return False
            elif c <= 0:
                return False
            elif src == dst:
                return False
            DiGraph.DiGraph.addVertex(self, src)
            edge = DiGraph.Edge(dst, c) 
            if self.graph[src].copy() == set(): 
                self.graph[src].add(edge)
                self.__numEdges += 1 
            else:
                if DiGraph.DiGraph.getEdge(self, src, dst, c, edge): 
                    return True
                else:
                    self.graph[src].add(edge)
                    self.__numEdges += 1


        ##
        # Add a vertex to the graph with an empty set as value
        # @param vertex vertex to be added
        #
        # @return False if vertex is None or already in the graph, <br>
        #         True otherwise
        #
        def addVertex(self, vertex):
            if vertex is None:
                return False
            if vertex in self.graph.keys():
                return False
            else:
                self.graph[vertex] = set()


        ##
        # Gets all vertices adjacent to a given vertex.
        # @param vertex vertex to be checked
        #
        # @return An empty set is returned if  the vertex is not in the graph, <br>
        #         or vertex is None, <br>
        #         or a Set of vertices in which there is and edge from the given vertex to each of these vertices.
        #         
        #
        def adjacentTo(self, vertex):
            if DiGraph.DiGraph.hasVertex(self, vertex) == False:
                return set()
            elif vertex == None:
                return set()
            else:
                adj = self.graph[vertex].copy()
                return adj


        ##
        # return all vertices in the graphs.
        # @return a dict with the vertices in the graph, when there are no vertices, return an empty set.
        def vertices(self): 
            if len(self.graph) == 0:
                return set()
            else:
                vertices = {}
                for k in self.graph.keys():
                    vertices[k] = 1
                    for x in self.graph[k].copy():
                        v = x.getVertex()
                        vertices[v] = 1
                return vertices


        ##
        # Returns the number of vertices in this graph.
        def numVertices(self): 
            self.__num_vertices = len(self.vertices(self))
            return  self.__num_vertices


        ##
        # Checks whether a given vertex is in the graph.
        # @param vertex given vertex
        # @return True if the vertex is in the graph, <br>
        # False otherwise, including the case of a None vertex
        def hasVertex(self, vertex):
            if vertex in self.graph.keys():
                return True
            if vertex == None:
                return False
            return False


        ##
        # Returns the number of Edges in this graph.
        def numEdges(self): 
            return DiGraph.DiGraph.__numEdges


        ##
        # Checks if an edge from src to dst exists, <br>
        # if there is already existing an edge from src to dst, replace the existing weight.
        #
        # @param src Source node
        # @param dst Destination node
        # @param c weight of the edge
        # @param edge to compare with others
        #
        # @return True if a Edge from src to dst exists, and it's replaced with the new weight <br>
        #         False otherwise, including when src or dst == None
        #         
        #         
        def getEdge(self, src, dst, c, edge):
            if src == None:
                return False
            if dst == None:
                return False
            if DiGraph.DiGraph.hasVertex(self, src):
                for x in self.graph[src].copy():
                    if x == edge:
                        x.setCost(c)
                        return True
            return False


        ##
        #Remove this vertex from the graph  and calculate the number of edges in the graph accordingly.
        #
        # @param vertex vertex to be removed
        #
        # @return False, if vertex is None or not in the graph.
        #         True, if removal is successful.
        def removeVertex(self, vertex):
            if vertex == None:
                return False
            elif DiGraph.DiGraph.hasVertex(self, vertex) == False:
                return False
            else:
                inc = DiGraph.DiGraph.incomingEdges(self, vertex)
                self.__num_vertices -= 1
                count = 0
                for j in self.graph[vertex]:
                    count += 1
                self.graph.pop(vertex)
                self.__numEdges -= count
                for i in inc.keys():
                    for j in self.graph[i].copy():
                        y = j.getVertex()
                        if y == vertex:
                            self.graph[i].discard(j)
                            self.__numEdges -= 1
            return True


        ##
        # Return a set of nodes with edges coming to this given vertex.
        #
        # @param vertex given vertex
        #
        # @return empty set if vertex is None or not in the graph, <br>
        #          Otherwise, return a dictionary which have the nodes with edges coming to this vertex.
        def incomingEdges(self, vertex):
            if vertex == None:
                return set()
            if DiGraph.DiGraph.hasVertex(self, vertex) == False:
                return set()
            else:
                incEd = dict()
                for i in self.graph.keys():    
                    for x in self.graph[i]:
                        v = x.getVertex()
                        if vertex == v:
                            incEd[i] = 1
                return incEd
        ##
        # Compute Dijkstra single source shortest path from the source node.
        #
        # @param source source node
        #
        # @return An empty dictionary if the vertex is none or is not in the graph <br>
        #         Otherwise, return a dict of  each having a vertex and smallest cost going from the source node to it.


        def Dijkstra(self, source):
            if source == None:
                return {}
            if DiGraph.DiGraph.hasVertex(self, source) == False:
                return {}
            distances = {}
            visited = {source: 0}
            priority = [(0, source)]    
            while priority:
                dist, v = heappop(priority)
                if self.graph.get(v) != None:
                    distances[v] = dist
                try:
                    for w in self.graph[v].copy():
                        x = [w.getVertex(), int(w.getCost())]
                        dist_vw = distances[v] + x[1]
                        try:
                            try:
                                if (dist_vw < visited[x[0]]):
                                    visited[x[0]] = dist_vw
                                    heappush(priority, (dist_vw, x[0]))
                                    self.pathAnt[x[0]] = v
                                    distances[x[0]] = dist_vw
                                    break
                            except:
                                pass
                            if x[0] not in visited:
                                    visited[x[0]] = dist_vw
                                    heappush(priority, (dist_vw, x[0]))
                                    self.pathAnt[x[0]] = v
                        except:
                            pass
                except:
                    pass 
            return distances
        ##
        # Compute the shorest path from the source to the destination node
        # 
        # @param source source node
        # @param dest destination node
        # 
        # @return Empty list if the source or dest are None, <br>
        #         Otherwise, return a list of edges from source to destination with the smallest cost
        def Dijkstra2(self, source, dest):
            if source == None:
                return set()
            if dest == None:
                return set()
            Path = []
            convert = []
            D = DiGraph.DiGraph.Dijkstra(DiGraph.DiGraph, source)
            while 1:
                    Path.append((dest, D[dest]))
                    if dest == source: break
                    dest = DiGraph.DiGraph.pathAnt[dest]
            
            Path.reverse()
            for i in Path:
                convert.append((DiGraph.Edge(i[0], i[1])))
            return convert
            



    # An edge holds the vertex it points to and its cost (or weight).
    class Edge(object):
        # Constructor from a node and its cost.
        def __init__(self, n, c):
            self.__node = str(n)
            self.__cost = int(c)

        # Get the target vertex.
        def getVertex(self):
            return self.__node

        # Get this edge cost.
        def getCost(self):
            return self.__cost
        # Set the cost of this edge.

        def setCost(self, c):
            self.__cost = c

        # Operator in
        def __contains__(self, obj):
            return True

        # Operator ==
        def __eq__(self, obj):
            if (self.__node == obj.__node):
                return True 

        # Representation of this Edge    
        def __repr__(self):
            return "<" + self.__node + ", " + str(self.__cost)+ ">"

        # An Edge object must be hashable.
        def __hash__(self):
            return hash((self.__node, self.__cost))

# Creates a simple graph.
def main():
    x = DiGraph.DiGraph
    DiGraph.DiGraph.__init__(x)
main()








