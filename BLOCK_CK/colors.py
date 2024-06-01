class Colors:
	dark_grey = (26, 31, 40)
	dark_green = (0, 100, 0)
	red = (232, 18, 18)
	carrot = (255, 69, 0)
	yellow = (237, 234, 4)
	purple = (166, 0, 247)
	cyan = (21, 204, 209)
	blue = (13, 64, 216)
	white = (255, 255, 255)
	dark_blue = (44, 44, 127)
	light_blue = (59, 85, 162)
	black = (0, 0, 0)
	pink = (199, 21, 133)

	@classmethod
	def get_cell_colors(cls):
		return [cls.dark_grey, cls.pink, cls.dark_green, cls.carrot, cls.yellow, cls.purple, cls.cyan, cls.blue]