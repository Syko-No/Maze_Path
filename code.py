maze = [
    [1,1,0,0,0,0],
    [1,1,1,0,0,0],
    [0,1,1,0,0,0],
    [0,0,1,1,0,0],
    [0,0,0,1,1,0],
    [0,0,0,0,1,1],
]

def path_finder(maze):

    maze = maze
    visited = [[0 for _ in range(len(maze[0]))] for _ in range(len(maze))]
    n = len(maze)
    m = len(maze[0])
    i = j = 0
    paths = []

    def solve_maze(maze, n, m, visited, i, j, moves):     # D L R U 

        # time.sleep(0.75)
        # print(i,j)
        
        if(i==n-1 and j==m-1):
            # print(moves)
            paths.append(moves)
            return

        #Down
        if((i+1)<n and maze[i+1][j] and not visited[i+1][j]):
            visited[i][j] = 1
            solve_maze(maze, n, m, visited, i+1, j, moves+'D')
            visited[i][j] = 0
        #Left
        if((j-1)>=0 and maze[i][j-1] and not visited[i][j-1]):
            visited[i][j] = 1
            solve_maze(maze, n, m, visited, i, j-1, moves+'L')
            visited[i][j] = 0
        #Right
        if((j+1)<m and maze[i][j+1] and not visited[i][j+1]):
            visited[i][j] = 1
            solve_maze(maze, n, m, visited, i, j+1, moves+'R')
            visited[i][j] = 0
        #Up
        if((i-1)>=0 and maze[i-1][j] and not visited[i-1][j]):
            visited[i][j] = 1
            solve_maze(maze, n, m, visited, i-1, j, moves+'U')
            visited[i][j] = 0

    moves = ''
    solve_maze(maze, n, m, visited, i, j, moves)

    return paths

paths = path_finder(maze)
for path in paths:
    print(path)