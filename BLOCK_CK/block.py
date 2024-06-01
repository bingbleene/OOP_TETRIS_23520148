from colors import Colors
import pygame
from position import Position

class Block:
    """
    Lớp Block đại diện cho các khối trong trò chơi Tetris.

    Thuộc tính:
        - id: ID của khối, dùng để xác định màu sắc.
        - cells: Từ điển chứa vị trí của các ô trong các trạng thái xoay khác nhau.
        - cell_size: Kích thước của mỗi ô (pixel).
        - row_offset: Độ dịch hàng của khối.
        - column_offset: Độ dịch cột của khối.
        - rotation_state: Trạng thái xoay hiện tại của khối.
        - colors: Danh sách các màu sắc cho các ô của khối.

    Phương thức:
        - __init__(id): Khởi tạo một khối mới với ID được cung cấp.
        - move(rows, columns): Di chuyển khối theo số hàng và số cột.
        - get_cell_positions(): Lấy danh sách vị trí các ô của khối sau khi đã dịch chuyển.
        - rotate(): Xoay khối sang trạng thái xoay tiếp theo.
        - undo_rotation(): Hoàn tác lần xoay gần nhất.
        - draw(screen, offset_x, offset_y): Vẽ khối lên màn hình với offset đã cho.
    """

    def __init__(self, id):
        """
        Khởi tạo một khối mới với ID được cung cấp.

        Tham số:
            - id (int): ID của khối.
        """
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()

    def move(self, rows, columns):
        """
        Di chuyển khối theo số hàng và số cột.

        Tham số:
            - rows (int): Số hàng cần di chuyển.
            - columns (int): Số cột cần di chuyển.
        """
        self.row_offset += rows
        self.column_offset += columns

    def get_cell_positions(self):
        """
        Lấy danh sách vị trí các ô của khối sau khi đã dịch chuyển.

        Trả về:
            - List[Position]: Danh sách các vị trí của các ô.
        """
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles

    def rotate(self):
        """
        Xoay khối sang trạng thái xoay tiếp theo.
        """
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    def undo_rotation(self):
        """
        Hoàn tác lần xoay gần nhất.
        """
        self.rotation_state -= 1
        if self.rotation_state == -1:
            self.rotation_state = len(self.cells) - 1

    def draw(self, screen, offset_x, offset_y):
        """
        Vẽ khối lên màn hình với offset đã cho.

        Tham số:
            - screen (pygame.Surface): Bề mặt màn hình để vẽ.
            - offset_x (int): Độ dịch theo trục X.
            - offset_y (int): Độ dịch theo trục Y.
        """
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size, 
                                    offset_y + tile.row * self.cell_size, self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)
