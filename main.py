from maze_maker import MazeMaker
from path_finder import PathFinder
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
PURPLE = (255,0,255)

WIDTH = 20
HEIGHT = 20
MARGIN = 5

WINDOW_SIZE = [255, 255]

goal_reached = False


if __name__ == '__main__':
	done = False
	file = input('Enter file name : ')
	
	maze = MazeMaker('./input/' + file)

	grid = maze.grid
	root = maze.start_pos
	goal = maze.end_pos
	visited = maze.visited
	path = PathFinder(grid,root,goal,visited)
	final_path = path.path
	print(final_path)
	node_stack = path.node_stack
	# for i in range(len(node_stack)):
	# 	print(node_stack[i])
	print(len(node_stack))
	pygame.init()
	
	screen = pygame.display.set_mode(WINDOW_SIZE)
	pygame.display.set_caption("Array Backed Grid")
	clock = pygame.time.Clock()
	i = 0
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
		screen.fill(BLACK)
		maze.drawGrid(screen)
		pygame.time.delay(500)
		if i<len(node_stack) and grid[node_stack[i][0]][node_stack[i][1]] == 0 :
			maze.grid[node_stack[i][0]][node_stack[i][1]] = 4
			i += 1
		elif i<len(node_stack):
			maze.grid[node_stack[i][0]][node_stack[i][1]] = 5
			i+=1
		# maze.grid[3][3] = 4
		pygame.display.flip()

	pygame.quit()