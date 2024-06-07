from block import Block
from position import Position

class LBlock(Block):
    """
    Lớp đại diện cho khối hình chữ L trong trò chơi Tetris.
    Kế thừa từ lớp Block.
    """

    def __init__(self):
        """
        Hàm khởi tạo cho LBlock. Đặt các vị trí của ô cho các trạng thái xoay khác nhau
        và di chuyển khối đến vị trí ban đầu.
        """
        super().__init__(id=1)
        self.cells = {
            0: [Position(0, 2), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 2)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 0)],
            3: [Position(0, 0), Position(0, 1), Position(1, 1), Position(2, 1)]
        }
        self.move(0, 3)

class JBlock(Block):
    """
    Lớp đại diện cho khối hình chữ J trong trò chơi Tetris.
    Kế thừa từ lớp Block.
    """

    def __init__(self):
        """
        Hàm khởi tạo cho JBlock. Đặt các vị trí của ô cho các trạng thái xoay khác nhau
        và di chuyển khối đến vị trí ban đầu.
        """
        super().__init__(id=2)
        self.cells = {
            0: [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(0, 2), Position(1, 1), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 2)],
            3: [Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)]
        }
        self.move(0, 3)

class IBlock(Block):
    """
    Lớp đại diện cho khối hình chữ I trong trò chơi Tetris.
    Kế thừa từ lớp Block.
    """

    def __init__(self):
        """
        Hàm khởi tạo cho IBlock. Đặt các vị trí của ô cho các trạng thái xoay khác nhau
        và di chuyển khối đến vị trí ban đầu.
        """
        super().__init__(id=3)
        self.cells = {
            0: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],
            1: [Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)],
            2: [Position(2, 0), Position(2, 1), Position(2, 2), Position(2, 3)],
            3: [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)]
        }
        self.move(-1, 3)

class OBlock(Block):
    """
    Lớp đại diện cho khối hình chữ O trong trò chơi Tetris.
    Kế thừa từ lớp Block.
    """

    def __init__(self):
        """
        Hàm khởi tạo cho OBlock. Đặt các vị trí của ô cho trạng thái xoay duy nhất
        và di chuyển khối đến vị trí ban đầu.
        """
        super().__init__(id=4)
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)]
        }
        self.move(0, 4)

class SBlock(Block):
    """
    Lớp đại diện cho khối hình chữ S trong trò chơi Tetris.
    Kế thừa từ lớp Block.
    """

    def __init__(self):
        """
        Hàm khởi tạo cho SBlock. Đặt các vị trí của ô cho các trạng thái xoay khác nhau
        và di chuyển khối đến vị trí ban đầu.
        """
        super().__init__(id=5)
        self.cells = {
            0: [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)],
            2: [Position(1, 1), Position(1, 2), Position(2, 0), Position(2, 1)],
            3: [Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)]
        }
        self.move(0, 3)

class TBlock(Block):
    """
    Lớp đại diện cho khối hình chữ T trong trò chơi Tetris.
    Kế thừa từ lớp Block.
    """

    def __init__(self):
        """
        Hàm khởi tạo cho TBlock. Đặt các vị trí của ô cho các trạng thái xoay khác nhau
        và di chuyển khối đến vị trí ban đầu.
        """
        super().__init__(id=6)
        self.cells = {
            0: [Position(0, 1), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 1)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 1)]
        }
        self.move(0, 3)

class ZBlock(Block):
    """
    Lớp đại diện cho khối hình chữ Z trong trò chơi Tetris.
    Kế thừa từ lớp Block.
    """

    def __init__(self):
        """
        Hàm khởi tạo cho ZBlock. Đặt các vị trí của ô cho các trạng thái xoay khác nhau
        và di chuyển khối đến vị trí ban đầu.
        """
        super().__init__(id=7)
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],
            1: [Position(0, 2), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(2, 1), Position(2, 2)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 0)]
        }
        self.move(0, 3)
