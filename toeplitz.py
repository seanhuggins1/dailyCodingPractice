def isToeplitz(matrix, M, N):
      #find the start (top-leftmost) index pair of each diagonal in the matrix
      diagonalStartIndices = []
      diagonalStartIndices.append([0,0])
      for i in range(1,M):
            diagonalStartIndices.append([i,0])
      for j in range(1,N):
            diagonalStartIndices.append([0,j])
      
      #traverse each diagonal starting from the top-leftmost index 
      for [i,j] in diagonalStartIndices:
            val = matrix[i][j]
            while True:
                  i+=1
                  j+=1
                  
                  #check that the value in this spot is the same as the value in the top-left
                  newval = matrix[i][j]
                  if (newval != val):
                        #not a toeplitz
                        return False

      #every diagonal has been checked
      return True

if __name__ == '__main__':
      matrix = [[1,2,3,4,8],[5,1,2,3,4],[4,5,1,2,3],[7,4,5,1,2]]
      M = 4
      N = 5
      print(isToeplitz(matrix, M, N))
