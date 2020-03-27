import pygame

class MazeMaker:
	def __init__(self,file_path = "custom"):
		self.start_pos = []
		self.end_pos = []
		self.obstacle = []
		self.file_path = file_path
		if file_path == "custom":
			print('custom')
		else:
			self.file = open(file_path, "r")
			self.makeGrid()

	def makeGrid(self):
		self.grid_str = self.file.read().split('\n')
		self.file.close()
		self.grid = []
		self.visited = []

		for row in range(len(self.grid_str)):
			self.grid.append([])
			self.visited.append([])
			for column in range(len(self.grid_str[row])):
				self.visited[row].append(False)
				if(self.grid_str[row][column] == '.'):
					self.grid[row].append(0)
				if(self.grid_str[row][column] == 'O'):
					self.grid[row].append(1)
					a = [row,column]
					self.obstacle.append(a)
					self.visited[row][column] = True
				if(self.grid_str[row][column] == 'X'):
					self.grid[row].append(2)
					self.start_pos.append(row)
					self.start_pos.append(column)
				if(self.grid_str[row][column] == 'Y'):
					self.grid[row].append(3)
					self.end_pos.append(row)
					self.end_pos.append(column)
		
		self.printGrid()

	def printGrid(self):
		for row in range(len(self.grid)):
			for column in range(len(self.grid[row])):
				print(self.grid[row][column], end=' ')
			print()

	def drawGrid(self, screen):
		screen.fill(BLACK)
		for row in range(len(self.grid)):
			for column in range(len(self.grid[row])):
				color = WHITE
				if self.grid[row][column] == 1:
					color = BLUE
				elif self.grid[row][column] == 2 or self.grid[row][column] == 3:
					color = GREEN
				elif self.grid[row][column] == 4:
					color = RED
				elif self.grid[row][column] == 5:
					color = PURPLE
				pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])


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

if __name__ == '__main__':
	done = False
	
	maze = MazeMaker('./maze.txt')
	pygame.init()
	
	screen = pygame.display.set_mode(WINDOW_SIZE)
	pygame.display.set_caption("Array Backed Grid")

	grid = maze.grid
	clock = pygame.time.Clock()
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
		screen.fill(BLACK)
		maze.drawGrid(screen)
		pygame.time.delay(2000)
		maze.grid[3][3] = 4
		pygame.display.flip()

	pygame.quit()
