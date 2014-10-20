import random

# Settings
mazeWidth = 10
mazeHeight = 10

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

	def remove_wall(self, wall):
		if wall in self.walls:
			self.walls.remove(wall)


def create_grid():
	grid = [[None for x in range(mazeWidth)] for x in range(mazeHeight)]
	for x in range(0, mazeWidth):
		for y in range(0, mazeHeight):
			grid[x][y] = Cell(x, y)
	return grid


def calculate_maze(grid):
	n_cells = mazeWidth * mazeHeight
	current_cell = random.choice(random.choice(grid))
	cell_stack = []
	visited_cells = 1

	while visited_cells < n_cells:
		neighbours = get_neighbours(grid, current_cell.get_x(), current_cell.get_y())
		if any(neighbours):
			choice_cell = random.choice(list(neighbours))
			break_wall(current_cell, choice_cell)
			cell_stack.append(current_cell)
			current_cell = choice_cell
			visited_cells += 1
		else:
			current_cell = cell_stack[-1]

	return cell_stack

#"A function is not executed from the beginning every time a new value is requested; instead, it is resumed from the same place where it left off last time, which is the line after yield" - riv
def get_neighbours(grid, x, y):
	baseX = x-1 if x > 0 else x
	maxX = x+1 if x < mazeWidth else x
	baseY = y-1 if y > 0 else y
	maxY = y+1 if y < mazeHeight else y

	for i in range(baseY, maxY):
		if grid[x][i] != grid[x][y]:
			yield grid[x][i]

	for i in range(baseX, maxX):
		if grid[x][i] != grid[x][y]:
			yield grid[x][i]

def break_wall(current_cell, target_cell):
	# Break down targets East wall
	if current_cell.get_x() > target_cell.get_x():
		target_cell.remove_wall("E")

	# Break down targets Weast wall
	if current_cell.get_x() < target_cell.get_x():
		target_cell.remove_wall("W")

	# Break down targets North wall
	if current_cell.get_y() > target_cell.get_y():
		target_cell.remove_wall("N")

	# Break down targets North wall
		if current_cell.get_y() < target_cell.get_y():
			target_cell.remove_wall("S")

grid = create_grid()
solution = calculate_maze(grid)

#Print a square!
m, n = 3, 3
for i in range(m):
    for j in range(n):
        print('*' if i in [0, n-1] or j in [0, m-1] else ' ', end='')
    print()