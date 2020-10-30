def printAllHamiltonianPaths(graph, vertex, visited, path, numNodes):
    if len(path) == numNodes: 
        print(path)
        return

    #check if every edge starting from vertex v leads to a solution or not
    for w in graph[vertex]:
        if not visited[w]:
            
            visited[w] = True
            path.append(w)
            
            printAllHamiltonianPaths(graph, w, visited, path, numNodes)

            #backtrack
            visited[w] = False
            path.pop()


def printAllGreyCodes(n):
      #create a graph with all possible binary numbers as nodes
      #each node has an adjancency list with the binary numbers it can reach, by changing one bit
      #finding all the hamiltonian paths through this graph will yield all the possible grey codes for n bits
      graph = {}
      
      #prepare the graph with adjacency lists
      for i in range(0, pow(2,n)):
            adjacentNums = []
            for j in range(0, n):
                  #flip one bit and store that new number in the adjacentNums array
                  adjacentNums.append(i ^ (1 << j))
            graph[i] = adjacentNums

      #prepare for the hamiltonian path traversals
      #used my code from knights tour problem
      visited = {}
      for i in range(0, pow(2,n)):
            start = i
            path = [start]
            for j in range(0, pow(2,n)):
                  visited[j] = False
            visited[start] = True
            printAllHamiltonianPaths(graph, start, visited, path, pow(2, n))

if __name__ == '__main__':
      printAllGreyCodes(3)