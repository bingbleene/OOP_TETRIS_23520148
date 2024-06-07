import pygame
from colors import Colors

class Grid:
    """
    Lớp Grid đại diện cho bảng trò chơi Tetris.

    Thuộc tính:
    - num_rows (int): Số hàng của bảng.
    - num_cols (int): Số cột của bảng.
    - cell_size (int): Kích thước của mỗi ô trong bảng.
    - grid (list): Ma trận biểu diễn bảng trò chơi.
    - colors (dict): Màu sắc tương ứng với giá trị của mỗi ô trong bảng.
    """

    def __init__(self):
        """
        Khởi tạo một bảng trống với số hàng và số cột được chỉ định trước.

        Khởi tạo một ma trận có kích thước (num_rows x num_cols) với tất cả các ô có giá trị ban đầu là 0.
        """
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = Colors.get_cell_colors()

    def print_grid(self):
        """
        In ma trận biểu diễn của bảng ra màn hình console.
        """
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end=" ")
            print()

    def is_inside(self, row, column):
        """
        Kiểm tra xem một ô có nằm trong bảng không.

        Tham số:
        - row (int): Số hàng của ô cần kiểm tra.
        - column (int): Số cột của ô cần kiểm tra.

        Trả về:
        - bool: True nếu ô nằm trong bảng, False nếu không.
        """
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        return False

    def is_empty(self, row, column):
        """
        Kiểm tra xem một ô có trống không.

        Tham số:
        - row (int): Số hàng của ô cần kiểm tra.
        - column (int): Số cột của ô cần kiểm tra.

        Trả về:
        - bool: True nếu ô trống, False nếu không.
        """
        if self.grid[row][column] == 0:
            return True
        return False

    def is_row_full(self, row):
        """
        Kiểm tra xem một hàng có đầy đủ không.

        Tham số:
        - row (int): Số hàng cần kiểm tra.

        Trả về:
        - bool: True nếu hàng đầy đủ, False nếu không.
        """
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True

    def clear_row(self, row):
        """
        Xóa một hàng trong bảng.

        Tham số:
        - row (int): Số hàng cần xóa.
        """
        for column in range(self.num_cols):
            self.grid[row][column] = 0

    def move_row_down(self, row, num_rows):
        """
        Di chuyển một hàng xuống dưới một số lượng hàng được chỉ định.

        Tham số:
        - row (int): Số hàng cần di chuyển.
        - num_rows (int): Số hàng cần di chuyển xuống.
        """
        for column in range(self.num_cols):
            self.grid[row + num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0

    def clear_full_rows(self):
        """
        Xóa các hàng đầy đủ và di chuyển các hàng phía trên xuống dưới.

        Trả về:
        - int: Số lượng hàng đã được xóa.
        """
        completed = 0
        for row in range(self.num_rows - 1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed

    def reset(self):
        """
        Đặt lại bảng trò chơi, tất cả các ô sẽ trở thành ô trống.
        """
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0

    def draw(self, screen):
        """
        Vẽ bảng trò chơi lên màn hình.

        Tham số:
        - screen (pygame.Surface): Màn hình pygame để vẽ bảng.
        """
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column * self.cell_size + 11, row * self.cell_size + 11,
                                        self.cell_size - 1, self.cell_size - 1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
