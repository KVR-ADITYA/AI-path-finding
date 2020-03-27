import pygame
from maze_maker import MazeMaker

if __name__ == '__main__':
	maze = MazeMaker('./maze.txt')
	maze.printGrid()