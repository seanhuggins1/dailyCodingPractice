# returns count of possible paths
# to reach cell at row number m and column number n
# from the topmost leftmost cell (cell at 1,1)
def numberOfPaths(p, q):
    # create a 1D array to store
    # results of subproblems
    dp = [1 for i in range(q)]
    for i in range(p - 1):
        for j in range(1, q):
            dp[j] += dp[j - 1]
    return dp[q - 1]

numberOfPaths(5,5)