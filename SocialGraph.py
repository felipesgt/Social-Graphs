#
#  @author Felipe Soares Gonçalves
#  @date 03/09/2018
#
import sys
from DiGraph import DiGraph 

##
#Create a graph to model a social network of friendships.
class SocialGraph(object):
    # Constructor method, if 
    def __init__(self):
        if len(sys.argv) < 2:
            sys.exit("Erro")
        self.readGraphFile(self, sys.argv[1])
    ##
    # Create a graph from a file and read their commands
    def readGraphFile (self, file):
        with open(file, "r") as arq:
            line = arq.readline().split()
            while line:
                if line[0] == ("add"):
                    src = line[1]
                    dst = line[2]
                    cost = int(line[3])
                    DiGraph.DiGraph.addEdge(DiGraph.DiGraph, src, dst, cost)
                    print("AddEdge: (True) - ", DiGraph.DiGraph.numEdges(DiGraph.DiGraph), "edges", DiGraph.DiGraph.numVertices(DiGraph.DiGraph), "vertices")
                    print()
                elif line[0] == ("showFriends"):
                    src = line[1]
                    print("ShowFriends" + "" + src)
                    result = (DiGraph.DiGraph.adjacentTo(DiGraph.DiGraph, src))
                    print(result)
                elif line[0] == ("recommendFriends"):
                    src = line[1]
                    opt = line[2]
                    print("recommendFriends" + " " + src + " " + opt + " " + line[3])
                    number = int(line[3])
                    recommends = SocialGraph.recommendFriends(self, src, opt, number)
                elif line[0] == ("remove"):
                    src = line[1]
                    print("remove" + " " + src)
                    DiGraph.DiGraph.removeVertex(DiGraph.DiGraph, src)
                    print("remove: (True) - ", DiGraph.DiGraph.numEdges(DiGraph.DiGraph), "edges", DiGraph.DiGraph.numVertices(DiGraph.DiGraph), "vertices")
                    print()
                elif line[0] == ("shortestPath"):
                    src = line[1]
                    dst = line[2]
                    dij = DiGraph.DiGraph.Dijkstra2(self, src, dst)
                    print("shortestPath", src, dst)
                    print(dij)
                line = arq.readline().split()

    ##
    # Recommend topK (e.g., 5) best friend candidates who are not already a friend of personOfInterest. <br>
    #
    #  If dist option is used, find the shortest path from personOfInterest to all the other nodes in the graph using <br>
    #    Dijkstra's single source shortest path algorithm and friendship distances. The smaller the distance means the <br>
    #    closer the relationship.
    # 
    #  If weightedDist option is used, after computing the shortest path like in the dist option to all the other nodes <br>
    #     in the graph, multiply each distance with the total number of edges in the graph less the number of incoming <br>
    #     edges to that node.
    #
    #  This method also:
    #    If there are less than topK candidates, return only those candidates.
    #
    #    If there are more than topK candidates, return only the topK candidates, when there are no other candidates ith the same distance/weighted distance as the last candidate in the topK list.
    #
    #    If there are other candidates with the same distance/weighted distance as the last candidate in the topK list,
    #    return all the candidates with the same distance. In this case, more than topK candidates are included in the list.
    #
    # @param personOfInterest Name of the person to recommend new friend candidates for
    # @param Either dist or weightedDist, which indicates whether to use the friendship distance or the weighted friendship distance.
    # @param Desirable maximum number of candidate friends to recommend.
    #
    # @return List of candidate friends.
    #
    def recommendFriends(self, personOfInterest, option, topK):
        if option == "dist":
            D = DiGraph.DiGraph.Dijkstra(DiGraph.DiGraph, personOfInterest)
            
            D.pop(personOfInterest)
            for k in DiGraph.DiGraph.graph[personOfInterest]:
                Edges = k.getVertex()
                for x in D.copy().keys():
                    if x == Edges:
                        D.pop(x)

            final  = []
            for i in D.items():
                final.append(i)
            final.sort(key=lambda x: x[1])
        else:
            final = []
            recommend = DiGraph.DiGraph.Dijkstra(DiGraph.DiGraph, personOfInterest)
            
            recommend.pop(personOfInterest)
            for k in DiGraph.DiGraph.graph[personOfInterest]:
                Edges = k.getVertex()
                for x in recommend.copy().keys():
                    if x == Edges:
                        recommend.pop(x)
            
            numEdges = DiGraph.DiGraph.numEdges(DiGraph.DiGraph)
            for i in recommend.keys():
                incomingEdges = DiGraph.DiGraph.incomingEdges(DiGraph.DiGraph, i)
                shortest = recommend[i]
                final.append((i, shortest*(numEdges-len(incomingEdges))))
        
        if len(final) < topK:
            var = []
            for i in final:
                var.append((DiGraph.Edge(i[0], i[1])))
            print(var)
        elif len(final) > topK:
            var = []
            costs = []
            tam = len(final)
            for i in final:
                costs.append(i[1])
            for item in costs:
                if costs.count(item) > 1:
                    topK += 1
                    del final[topK:tam]
                    for i in final:
                        var.append((DiGraph.Edge(i[0], i[1])))
                    print(var)
                    return True
            print (final)
        return True

     
# Main method                
def main(argv=None):
    f = SocialGraph
    f.__init__(f)


if __name__ == "__main__":
    sys.exit(main())     