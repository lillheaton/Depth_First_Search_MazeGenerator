import random
import time
import threading

from cell import Cell
from tkinter import *
from tkinter import ttk


# Settings
mazeWidth = 10
mazeHeight = 10
cell_size = 20

# Graphics
root = Tk()
width = str(cell_size * 2 + (mazeWidth * cell_size))
height = str(cell_size * 2 + (mazeHeight * cell_size))
root.geometry(width + "x" + height)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

canvas = Canvas(root, background='white')
canvas.grid(column=0, row=0, sticky=(N, W, E, S))


def create_grid():
	grid = [[None for x in range(mazeWidth)] for x in range(mazeHeight)]
	for y in range(0, mazeHeight):
		for x in range(0, mazeWidth):
			grid[x][y] = Cell(x, y)
	return grid

#"A function is not executed from the beginning every time a new value is requested; instead, it is resumed from the same place where it left off last time, which is the line after yield" - riv
def get_neighbours(grid, x, y):
	baseX = x-1 if x > 0 else x
	maxX = x+1 if x < (mazeWidth - 1) else x
	baseY = y-1 if y > 0 else y
	maxY = y+1 if y < (mazeHeight - 1) else y

	for i in range(baseY, maxY + 1):
		yield grid[x][i]

	for i in range(baseX, maxX + 1):
		yield grid[i][y]

def break_wall(current_cell, target_cell):
	# Break down targets East wall
	if current_cell.get_x() < target_cell.get_x():
		current_cell.remove_wall("W")
		target_cell.remove_wall("E")

	# Break down targets Weast wall
	if current_cell.get_x() > target_cell.get_x():
		current_cell.remove_wall("E")
		target_cell.remove_wall("W")

	# Break down targets North wall
	if current_cell.get_y() < target_cell.get_y():
		current_cell.remove_wall("S")
		target_cell.remove_wall("N")

	# Break down targets North wall
	if current_cell.get_y() > target_cell.get_y():
		current_cell.remove_wall("N")
		target_cell.remove_wall("S")

def print_cell(canvas, cell):
	x, y = (cell.get_x() + 1) * cell_size, (cell.get_y() + 1) * cell_size
	if "N" in cell.get_walls():
		draw_line(x, y, x + cell_size, y)

	if "S" in cell.get_walls():
		draw_line(x, y + cell_size, x + cell_size, y + cell_size)

	if "E" in cell.get_walls():
		draw_line(x, y, x, y + cell_size)

	if "W" in cell.get_walls():
		draw_line(x + cell_size, y, x + cell_size, y + cell_size)

def draw_line(x, y, endX, endY):
	canvas.create_line(x, y, endX, endY)

def assert_solution(solution):
	for y in range(0, mazeHeight):
		for x in range(0, mazeWidth):
			"If the solution was successful, then that means that every cell shuld have less then 4 walls"
			assert len(solution[x][y].get_walls()) < 4

	assert "N" and "E" in solution[0][0].get_walls()
	assert "N" and "W" in solution[mazeWidth-1][0].get_walls()
	assert "S" and "W" in solution[mazeWidth-1][mazeHeight-1].get_walls()
	assert "S" and "E" in solution[0][mazeHeight-1].get_walls()


"Calculate a solution and print it"
grid = create_grid()
n_cells = mazeWidth * mazeHeight
current_cell = random.choice(random.choice(grid))
cell_stack = []
visited_cells = []
tree = []

def calculate_maze(grid):
	global current_cell
	if len(visited_cells) < n_cells:
		neighbours = list(get_neighbours(grid, current_cell.get_x(), current_cell.get_y()))
		possible_neighbours = []
		if neighbours:
			possible_neighbours = [c for c in neighbours if c not in visited_cells]

		if possible_neighbours:
			choice_cell = random.choice(possible_neighbours)
			break_wall(current_cell, choice_cell)
			cell_stack.append(choice_cell)
			current_cell = choice_cell
			visited_cells.append(current_cell)
		else:
			if len(cell_stack) > all(path for path in tree):
				tree.append(cell_stack.copy())
			current_cell = cell_stack.pop()

		# Clear the window
		canvas.delete("all")

		# Print cells
		for y in range(0, mazeHeight):
			for x in range(0, mazeWidth):
				print_cell(canvas, grid[x][y])

		canvas.after(20, calculate_maze, grid)
	else:
		# When done assert solution
		assert_solution(grid)
		longest_path = sorted(tree, key=lambda path: len(path))[-1]

		# Draw start finish
		startX = (longest_path[0].get_x() + 1) * cell_size
		startY = (longest_path[0].get_y() + 1) * cell_size

		endX = (longest_path[-1].get_x() + 1) * cell_size
		endY = (longest_path[-1].get_y() + 1) * cell_size

		canvas.create_rectangle(startX + 2, startY + 2, (startX + cell_size) - 2, (startY + cell_size) - 2, fill="green")
		canvas.create_rectangle(endX + 2, endY + 2, (endX + cell_size) - 2, (endY + cell_size) - 2, fill="red")

		print("Calculation finished")

if __name__ == '__main__':
	solution = calculate_maze(grid)
	root.mainloop()