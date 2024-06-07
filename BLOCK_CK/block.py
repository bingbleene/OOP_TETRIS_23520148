from colors import Colors
import pygame
from position import Position

class Block:
    """
    Lớp đại diện cho một khối (block) trong trò chơi. Mỗi khối có thể di chuyển, xoay và vẽ lên màn hình.
    
    Thuộc tính:
    - id (int): Mã định danh của khối.
    - cells (dict): Các trạng thái xoay của khối, mỗi trạng thái chứa các ô của khối.
    - cell_size (int): Kích thước của mỗi ô trong khối.
    - row_offset (int): Độ dịch hàng của khối.
    - column_offset (int): Độ dịch cột của khối.
    - rotation_state (int): Trạng thái xoay hiện tại của khối.
    - colors (list): Danh sách các màu của ô trong khối.
    """
    
    def __init__(self, id):
        """
        Hàm khởi tạo cho lớp Block. Khởi tạo các thuộc tính của khối.
        
        Tham số:
        - id (int): Mã định danh của khối.
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
        Di chuyển khối theo hàng và cột chỉ định.
        
        Tham số:
        - rows (int): Số lượng hàng để di chuyển.
        - columns (int): Số lượng cột để di chuyển. """
        self.row_offset += rows
        self.column_offset += columns

    def get_cell_positions(self):
        """
        Lấy vị trí của các ô trong khối sau khi đã di chuyển.
        
        Trả về:
        - list: Danh sách các vị trí ô đã được di chuyển.
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
        Hoàn tác xoay khối, trở về trạng thái xoay trước đó.
        """
        self.rotation_state -= 1
        if self.rotation_state == -1:
            self.rotation_state = len(self.cells) - 1

    def draw(self, screen, offset_x, offset_y):
        """
        Vẽ khối lên màn hình với vị trí offset đã cho.
        
        Tham số:
        - screen (pygame.Surface): Màn hình để vẽ lên.
        - offset_x (int): Vị trí offset theo trục x.
        - offset_y (int): Vị trí offset theo trục y.
        """
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size, 
                                    offset_y + tile.row * self.cell_size, self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)
