from maze_maker import MazeMaker

grid = []
visited = []
i = 1
for r in range(4):
	grid.append([])
	visited.append([])
	for c in range(4):
		grid[r].append(i)
		i +=1
		visited[r].append(False)

for row in range(len(grid)):
	for column in range(len(grid[row])):
		print(grid[row][column], end=' ')
	print()

node_stack = []
op_stack = []

# global goal_reached 
goal_reached = False

def DFS(rootx, rooty,goal):
	global goal_reached
	if not goal_reached:
		visited[rootx][rooty] = True
		node_stack.append((rootx,rooty))
		if(grid[rootx][rooty] == goal):
			goal_reached = True
			return
		else:
			if(rootx+1<len(grid) and not visited[rootx+1][rooty] and not goal_reached):
				op_stack.append('D')
				DFS(rootx+1,rooty,goal)
				if not goal_reached:	
					op_stack.append('U')
					node_stack.append((rootx,rooty))
			if(rooty+1<len(grid[rootx]) and not visited[rootx][rooty+1] and not goal_reached):
				op_stack.append('R')
				DFS(rootx,rooty+1,goal)
				if not goal_reached:	
					op_stack.append('L')
					node_stack.append((rootx,rooty))
			if(rootx-1>=0 and not visited[rootx-1][rooty] and not goal_reached):
				op_stack.append('U')
				DFS(rootx-1,rooty,goal)
				if not goal_reached:	
					op_stack.append('D')
					node_stack.append((rootx,rooty))
			if(rooty-1>=0 and not visited[rootx][rooty-1] and not goal_reached):
				op_stack.append('L')
				DFS(rootx,rooty-1,goal)
				if not goal_reached:	
					op_stack.append('R')
					node_stack.append((rootx,rooty))
		
	return

maze = MazeMaker('./maze.txt')
grid = maze.grid

visited = maze.visited

DFS(maze.start_pos[0],maze.start_pos[1],3)

# print(len(node_stack))
# print(len(op_stack))
# print()
# print(node_stack)
# print(op_stack)

path = ''

for i in range(len(op_stack)):
	path += '('
	path +=	str(node_stack[i][0])
	path +=	','
	path +=	str(node_stack[i][1])
	path +=	','
	path +=	str(op_stack[i])
	path += ')'
	path += '->'

path += '('+ str(maze.end_pos[0])+','+str(maze.end_pos[1]) + ')'
print(path)


