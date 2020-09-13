#
# Knights tour program finds all the sequences of moves a knight can take around a chessboard such that every square is visited once 
#
#

moves = [
        [-2,-1],
        [-1,-2],
        [-2,+1],
        [-1,+2],
        [+1,-2],
        [+2,-1],
        [+2,+1],
        [+1,+2]
        ]

def getMovesFromHere(pos, N):
    [i,j] = pos.split('-')
    i = int(i)
    j = int(j)

    movesFromHere = []
    for move in moves:

        new_i = i + move[0]
        if new_i < 0 or new_i >= N: 
            continue

        new_j = j + move[1]
        if new_j < 0 or new_j >= N:
            continue

        newBoardSquare = '-'.join([str(move[0] + i), str(move[1] + j)])  
        movesFromHere.append(newBoardSquare)

    return movesFromHere

def printAllHamiltonianPaths(moveGraph, vertex, visited, path, numNodes):
    if len(path) == numNodes: 
        print(path)
        return

    #check if every edge starting from vertex v leads to a solution or not
    for w in moveGraph[vertex]:
        if not visited[w]:
            
            visited[w] = True
            path.append(w)
            
            printAllHamiltonianPaths(moveGraph, w, visited, path, numNodes)

            #backtrack
            visited[w] = False
            path.pop()

def knightsTour(N):
    #create a graph that represents all the possible moves that a knight could make on the chessboard
    moveGraph = {}
    visited = {}
    for i in range(N):
        for j in range(N):
            boardSquare = '-'.join([str(i),str(j)])
            moveGraph[boardSquare] = getMovesFromHere(boardSquare, N)
            visited[boardSquare] = False
    
    #find the number of hamiltonian paths in this graph
    start = '0-0'
    path = [start]
    visited[start] = True
    printAllHamiltonianPaths(moveGraph, start, visited, path, N*N)

    
    

knightsTour(6)

