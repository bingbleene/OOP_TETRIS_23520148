from grid import Grid
from blocks import *
import random

class Game:
	"""Lớp trò chơi Tetris.

	Thuộc tính:
		grid (Grid): Lưới trò chơi.
		blocks (list): Danh sách tất cả các khối tetromino.
		current_block (Block): Khối hiện tại người chơi đang điều khiển.
		next_block (Block): Khối tiếp theo sẽ xuất hiện trong trò chơi.
		game_over (bool): Trò chơi đã kết thúc hay chưa.
		game_win (bool): Người chơi đã thắng trò chơi hay chưa.
		score (int): Điểm của người chơi.

	Phương thức:
		update_score(lines_cleared, move_down_points): Cập nhật điểm của người chơi.
		get_random_block(): Trả về một khối ngẫu nhiên.
		move_left(): Di chuyển khối hiện tại sang trái.
		move_right(): Di chuyển khối hiện tại sang phải.
		move_down(): Di chuyển khối hiện tại xuống dưới.
		lock_block(): Khóa khối hiện tại vào lưới.
		reset(): Đặt lại trò chơi.
		block_fits(): Kiểm tra xem khối hiện tại có vừa với lưới hay không.
		rotate(): Xoay khối hiện tại.
		block_inside(): Kiểm tra xem khối hiện tại có nằm trong lưới hay không.
		draw(screen): Vẽ lưới trò chơi và các khối lên màn hình.
	"""

	def __init__(self):
		"""Phương thức khởi tạo, khởi tạo trò chơi."""
		self.grid = Grid()
		self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
		self.current_block = self.get_random_block()
		self.next_block = self.get_random_block()
		self.game_over = False
		self.game_win = False
		self.score = 0

	def update_score(self, lines_cleared, move_down_points):
		"""Cập nhật điểm của người chơi.

		Args:
			lines_cleared (int): Số dòng đã xóa.
			move_down_points (int): Điểm cho việc di chuyển khối xuống.
		"""
		if lines_cleared == 1:
			self.score += 100
		elif lines_cleared == 2:
			self.score += 300
		elif lines_cleared >= 3:
			self.score += 500
		self.score += move_down_points
		if self.score >= 10000: 
			self.game_over = True
			self.game_win = True

	def get_random_block(self):
		"""Trả về một khối ngẫu nhiên.

		Returns:
			Block: Khối ngẫu nhiên.
		"""
		if len(self.blocks) == 0:
			self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
		block = random.choice(self.blocks)
		self.blocks.remove(block)
		return block

	def move_left(self):
		"""Di chuyển khối hiện tại sang trái."""
		self.current_block.move(0, -1)
		if self.block_inside() == False or self.block_fits() == False:
			self.current_block.move(0, 1)

	def move_right(self):
		"""Di chuyển khối hiện tại sang phải."""
		self.current_block.move(0, 1)
		if self.block_inside() == False or self.block_fits() == False:
			self.current_block.move(0, -1)

	def move_down(self):
		"""Di chuyển khối hiện tại xuống dưới."""
		self.current_block.move(1, 0)
		if self.block_inside() == False or self.block_fits() == False:
			self.current_block.move(-1, 0)
			self.lock_block()

	def lock_block(self):
		"""Khóa khối hiện tại vào lưới."""
		tiles = self.current_block.get_cell_positions()
		for position in tiles:
			self.grid.grid[position.row][position.column] = self.current_block.id
		self.current_block = self.next_block
		self.next_block = self.get_random_block()
		rows_cleared = self.grid.clear_full_rows()
		if rows_cleared > 0:
			self.update_score(rows_cleared, 0)
		if self.block_fits() == False:
			self.game_over = True

	def reset(self):
		"""Đặt lại trò chơi."""
		self.grid.reset()
		self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
		self.current_block = self.get_random_block()
		self.next_block = self.get_random_block()
		self.score = 0
		self.game_win = False

	def block_fits(self):
		"""Kiểm tra xem khối hiện tại có vừa với lưới hay không.

		Returns:
			bool: True nếu khối vừa, False nếu không.
		"""
		tiles = self.current_block.get_cell_positions()
		for tile in tiles:
			if self.grid.is_empty(tile.row, tile.column) == False:
				return False
		return True

	def rotate(self):
		"""Xoay khối hiện tại."""
		self.current_block.rotate()
		if self.block_inside() == False or self.block_fits() == False:
			self.current_block.undo_rotation()

	def block_inside(self):
		"""Kiểm tra xem khối hiện tại có nằm trong lưới hay không.

		Returns:
			bool: True nếu khối nằm trong lưới, False nếu không.
		"""
		tiles = self.current_block.get_cell_positions()
		for tile in tiles:
			if self.grid.is_inside(tile.row, tile.column) == False:
				return False
		return True

	def draw(self, screen):
		"""Vẽ lưới trò chơi và các khối lên màn hình.

		Args:
			screen (pygame.Surface): Màn hình để vẽ trò chơi.
		"""
		self.grid.draw(screen)
		self.current_block.draw(screen, 11, 11)

		if self.next_block.id == 3:
			self.next_block.draw(screen, 255, 290)
		elif self.next_block.id == 4:
			self.next_block.draw(screen, 255, 280)
		else:
			self.next_block.draw(screen, 270, 270)