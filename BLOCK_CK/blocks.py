from block import Block
from position import Position

class LBlock(Block):
    """
    Lớp LBlock đại diện cho khối hình chữ L trong trò chơi Tetris.

    Phương thức:
        - __init__(): Khởi tạo khối L với các trạng thái xoay khác nhau và di chuyển nó.
    """
    def __init__(self):
        super().__init__(id = 1)
        self.cells = {
            0: [Position(0, 2), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 2)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 0)],
            3: [Position(0, 0), Position(0, 1), Position(1, 1), Position(2, 1)]
        }
        self.move(0, 3)

class JBlock(Block):
    """
    Lớp JBlock đại diện cho khối hình chữ J trong trò chơi Tetris.

    Phương thức:
        - __init__(): Khởi tạo khối J với các trạng thái xoay khác nhau và di chuyển nó.
    """
    def __init__(self):
        super().__init__(id = 2)
        self.cells = {
            0: [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(0, 2), Position(1, 1), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 2)],
            3: [Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)]
        }
        self.move(0, 3)

class IBlock(Block):
    """
    Lớp IBlock đại diện cho khối hình chữ I trong trò chơi Tetris.

    Phương thức:
        - __init__(): Khởi tạo khối I với các trạng thái xoay khác nhau và di chuyển nó.
    """
    def __init__(self):
        super().__init__(id = 3)
        self.cells = {
            0: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],
            1: [Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)],
            2: [Position(2, 0), Position(2, 1), Position(2, 2), Position(2, 3)],
            3: [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)]
        }
        self.move(-1, 3)

class OBlock(Block):
    """
    Lớp OBlock đại diện cho khối hình vuông (O) trong trò chơi Tetris.

    Phương thức:
        - __init__(): Khởi tạo khối O với trạng thái duy nhất và di chuyển nó.
    """
    def __init__(self):
        super().__init__(id = 4)
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)]
        }
        self.move(0, 4)

class SBlock(Block):
    """
    Lớp SBlock đại diện cho khối hình chữ S trong trò chơi Tetris.

    Phương thức:
        - __init__(): Khởi tạo khối S với các trạng thái xoay khác nhau và di chuyển nó.
    """
    def __init__(self):
        super().__init__(id = 5)
        self.cells = {
            0: [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)],
            2: [Position(1, 1), Position(1, 2), Position(2, 0), Position(2, 1)],
            3: [Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)]
        }
        self.move(0, 3)

class TBlock(Block):
    """
    Lớp TBlock đại diện cho khối hình chữ T trong trò chơi Tetris.

    Phương thức:
        - __init__(): Khởi tạo khối T với các trạng thái xoay khác nhau và di chuyển nó.
    """
    def __init__(self):
        super().__init__(id = 6)
        self.cells = {
            0: [Position(0, 1), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 1)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 1)]
        }
        self.move(0, 3)

class ZBlock(Block):
    """
    Lớp ZBlock đại diện cho khối hình chữ Z trong trò chơi Tetris.

    Phương thức:
        - __init__(): Khởi tạo khối Z với các trạng thái xoay khác nhau và di chuyển nó.
    """
    def __init__(self):
        super().__init__(id = 7)
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],
            1: [Position(0, 2), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(2, 1), Position(2, 2)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 0)]
        }
        self.move(0, 3)
