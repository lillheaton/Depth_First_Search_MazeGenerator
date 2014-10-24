class Cell():	
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

	def get_walls(self):
		return self.walls