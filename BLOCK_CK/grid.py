import pygame
from colors import Colors

class Grid:
    """
    Lớp Grid đại diện cho lưới trò chơi Tetris.

    Thuộc tính:
        - num_rows: Số lượng hàng của lưới.
        - num_cols: Số lượng cột của lưới.
        - cell_size: Kích thước của mỗi ô trong lưới.
        - grid: Ma trận đại diện cho lưới, chứa các giá trị của từng ô.
        - colors: Bảng màu cho các ô.

    Phương thức:
        - __init__(): Khởi tạo lưới mới.
        - print_grid(): In ra lưới hiện tại.
        - is_inside(row, column): Kiểm tra xem một ô có nằm trong lưới hay không.
        - is_empty(row, column): Kiểm tra xem một ô có trống hay không.
        - is_row_full(row): Kiểm tra xem một hàng có đầy hay không.
        - clear_row(row): Xóa một hàng (tất cả các ô trong hàng trở thành trống).
        - move_row_down(row, num_rows): Di chuyển một hàng xuống dưới một số hàng nhất định.
        - clear_full_rows(): Xóa tất cả các hàng đầy và di chuyển các hàng phía trên xuống.
        - reset(): Thiết lập lại lưới.
        - draw(screen): Vẽ lưới lên màn hình.
    """

    def __init__(self):
        """Khởi tạo lưới mới."""
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = Colors.get_cell_colors()

    def print_grid(self):
        """In ra lưới hiện tại."""
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end=" ")
            print()

    def is_inside(self, row, column):
        """
        Kiểm tra xem một ô có nằm trong lưới hay không.

        Tham số:
            - row (int): Chỉ số hàng.
            - column (int): Chỉ số cột.

        Trả về:
            - bool: True nếu ô nằm trong lưới, False nếu không.
        """
        if 0 <= row < self.num_rows and 0 <= column < self.num_cols:
            return True
        return False

    def is_empty(self, row, column):
        """
        Kiểm tra xem một ô có trống hay không.

        Tham số:
            - row (int): Chỉ số hàng.
            - column (int): Chỉ số cột.

        Trả về:
            - bool: True nếu ô trống, False nếu không.
        """
        return self.grid[row][column] == 0

    def is_row_full(self, row):
        """
        Kiểm tra xem một hàng có đầy hay không.

        Tham số:
            - row (int): Chỉ số hàng.

        Trả về:
            - bool: True nếu hàng đầy, False nếu không.
        """
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True

    def clear_row(self, row):
        """
        Xóa một hàng (tất cả các ô trong hàng trở thành trống).

        Tham số:
            - row (int): Chỉ số hàng.
        """
        for column in range(self.num_cols):
            self.grid[row][column] = 0

    def move_row_down(self, row, num_rows):
        """
        Di chuyển một hàng xuống dưới một số hàng nhất định.

        Tham số:
            - row (int): Chỉ số hàng.
            - num_rows (int): Số hàng cần di chuyển xuống.
        """
        for column in range(self.num_cols):
            self.grid[row + num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0

    def clear_full_rows(self):
        """
        Xóa tất cả các hàng đầy và di chuyển các hàng phía trên xuống.

        Trả về:
            - int: Số lượng hàng đã bị xóa.
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
        """Thiết lập lại lưới."""
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0

    def draw(self, screen):
        """
        Vẽ lưới lên màn hình.
        """
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column * self.cell_size + 11, row * self.cell_size + 11,
                                        self.cell_size - 1, self.cell_size - 1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
