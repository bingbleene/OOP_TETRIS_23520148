from grid import Grid
from blocks import *
import random

class Game:
    """
    Lớp Game đại diện cho trò chơi Tetris.

    Thuộc tính:
        - grid: Lưới trò chơi.
        - blocks: Danh sách các khối có thể xuất hiện trong trò chơi.
        - current_block: Khối hiện tại đang rơi.
        - next_block: Khối sẽ xuất hiện tiếp theo.
        - game_over: Trạng thái của trò chơi (kết thúc hay chưa).
        - score: Điểm số của người chơi.

    Phương thức:
        - __init__(): Khởi tạo trò chơi mới.
        - get_random_block(): Lấy một khối ngẫu nhiên từ danh sách các khối.
        - move_left(): Di chuyển khối hiện tại sang trái.
        - move_right(): Di chuyển khối hiện tại sang phải.
        - move_down(): Di chuyển khối hiện tại xuống dưới.
        - lock_block(): Khóa khối hiện tại vào lưới khi không thể di chuyển xuống dưới nữa.
        - reset(): Thiết lập lại trò chơi.
        - block_fits(): Kiểm tra xem khối hiện tại có thể nằm gọn trong lưới hay không.
        - rotate(): Xoay khối hiện tại.
        - block_inside(): Kiểm tra xem khối hiện tại có nằm trong lưới hay không.
        - draw(screen): Vẽ trò chơi lên màn hình.
    """

    def __init__(self):
        """Khởi tạo trò chơi mới."""
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0

    def get_random_block(self):
        """
        Lấy một khối ngẫu nhiên từ danh sách các khối.

        Trả về:
            - Block: Khối ngẫu nhiên được chọn.
        """
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    def move_left(self):
        """Di chuyển khối hiện tại sang trái."""
        self.current_block.move(0, -1)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(0, 1)

    def move_right(self):
        """Di chuyển khối hiện tại sang phải."""
        self.current_block.move(0, 1)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(0, -1)

    def move_down(self):
        """Di chuyển khối hiện tại xuống dưới."""
        self.current_block.move(1, 0)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(-1, 0)
            self.lock_block()

    def lock_block(self):
        """Khóa khối hiện tại vào lưới khi không thể di chuyển xuống dưới nữa."""
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()
        if not self.block_fits():
            self.game_over = True

    def reset(self):
        """Thiết lập lại trò chơi."""
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()

    def block_fits(self):
        """
        Kiểm tra xem khối hiện tại có thể nằm gọn trong lưới hay không.

        Trả về:
            - bool: True nếu khối nằm gọn, False nếu không.
        """
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_empty(tile.row, tile.column):
                return False
        return True

    def rotate(self):
        """Xoay khối hiện tại."""
        self.current_block.rotate()
        if not self.block_inside() or not self.block_fits():
            self.current_block.undo_rotation()

    def block_inside(self):
        """
        Kiểm tra xem khối hiện tại có nằm trong lưới hay không.

        Trả về:
            - bool: True nếu khối nằm trong lưới, False nếu không.
        """
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_inside(tile.row, tile.column):
                return False
        return True

    def draw(self, screen):
        """
        Vẽ trò chơi lên màn hình.
        """
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)

        if self.next_block.id == 3:
            self.next_block.draw(screen, 255, 290)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 255, 280)
        else:
            self.next_block.draw(screen, 270, 270)
