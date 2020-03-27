import pygame
from maze_maker import MazeMaker

goal_reached = False

class PathFinder():
	def __init__(self, grid,root,goal,visited):
		self.grid = grid
		self.root = root
		self.goal = goal
		self.visited = visited
		self.op_stack = []
		self.node_stack = []
		self.path = ''
		self.DFS(root[0],root[1],self.grid[goal[0]][goal[1]])
		self.makepathString()


	def DFS(self,rootx, rooty,goal):
		global goal_reached
		if not goal_reached:
			self.visited[rootx][rooty] = True
			self.node_stack.append((rootx,rooty))
			if(self.grid[rootx][rooty] == goal):
				goal_reached = True
				return
			else:
				if(rootx-1>=0 and not self.visited[rootx-1][rooty] and not goal_reached):
					self.op_stack.append('U')
					self.DFS(rootx-1,rooty,goal)
					if not goal_reached:	
						self.op_stack.append('D')
						self.node_stack.append((rootx,rooty))
				if(rooty-1>=0 and not self.visited[rootx][rooty-1] and not goal_reached):
					self.op_stack.append('L')
					self.DFS(rootx,rooty-1,goal)
					if not goal_reached:	
						self.op_stack.append('R')
						self.node_stack.append((rootx,rooty))
				if(rootx+1<len(self.grid) and not self.visited[rootx+1][rooty] and not goal_reached):
					self.op_stack.append('D')
					self.DFS(rootx+1,rooty,goal)
					if not goal_reached:	
						self.op_stack.append('U')
						self.node_stack.append((rootx,rooty))
				if(rooty+1<len(self.grid[rootx]) and not self.visited[rootx][rooty+1] and not goal_reached):
					self.op_stack.append('R')
					self.DFS(rootx,rooty+1,goal)
					if not goal_reached:	
						self.op_stack.append('L')
						self.node_stack.append((rootx,rooty))
		return

	def makepathString(self):
		for i in range(len(self.op_stack)):
			self.path += '('
			self.path +=	str(self.node_stack[i][0])
			self.path +=	','
			self.path +=	str(self.node_stack[i][1])
			self.path +=	','
			self.path +=	str(self.op_stack[i])
			self.path += ')'
			self.path += '->'

		self.path += '('+ str(self.goal[0])+','+str(self.goal[1]) + ')'
		return


if __name__ == '__main__':
	maze = MazeMaker('./maze.txt')

	grid = maze.grid
	root = maze.start_pos
	goal = maze.end_pos
	visited = maze.visited

	path = PathFinder(grid,root,goal,visited)

	final_path = path.path

	print(final_path)