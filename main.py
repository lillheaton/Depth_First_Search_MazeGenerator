import random

# Settings
mazeWidth = 10
mazeHeight = 10

class Vector2():
	"""docstring for Vector2"""
	def __init__(self, x, y):
		super(Vector2, self).__init__()
		self.x = x
		self.y = y

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y	
		

class Cell():
	"""docstring for Cell"""
	def __init__(self, x, y):
		super(Cell, self).__init__()
		self.walls = ["N", "S", "E", "W"]
		self.x = x
		self.y = y

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y


def create_grid():
	grid = [[None for x in range(0, mazeWidth)] for x in range(0, mazeHeight)]
	for x in range(0, mazeWidth):
		for y in range(0, mazeHeight):
			grid[x][y] = Cell(x, y)
	return grid


def calculate_maze(grid):
	n_cells = mazeWidth * mazeHeight
	current_cell = random.choice(random.choice(grid))
	visited_cells = []

	while len(visited_cells) < len(n_cells):
		neighbours = get_neighbours(grid, current_cell.get_x(), current_cell.get_y())
		if any(neighbours):
			choice_cell = random.choice(neighbours)



#"A function is not executed from the beginning every time a new value is requested; instead, it is resumed from the same place where it left off last time, which is the line after yield" - riv
def get_neighbours(grid, x, y):
	baseX = x-1 if x > 0 else x
	maxX = x+1 if x < mazeWidth else x
	baseY = y-1 if y > 0 else y
	maxY = y+1 if y < mazeHeight else y

	for i in range(baseX, maxX):
		for j in range(baseY, maxY):			
			yield grid[i][j]

grid = create_grid()