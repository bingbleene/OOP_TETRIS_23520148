import pygame

class Button:
    """
    Lớp Button đại diện cho một nút bấm trong trò chơi.

    Thuộc tính:
    - image (pygame.Surface): Hình ảnh của nút bấm.
    - rect (pygame.Rect): Hình chữ nhật bao quanh nút bấm, dùng để vẽ nút và kiểm tra va chạm.
    - clicked (bool): Trạng thái của nút bấm sau khi được nhấn.

    Phương thức:
    - __init__(self, x, y, image, scale): Khởi tạo một đối tượng Button.
    - draw(self, surface): Vẽ nút bấm lên một bề mặt và kiểm tra sự kiện nhấn nút.
    """

    def __init__(self, x, y, image, scale):
        """
        Khởi tạo một đối tượng Button.

        Tham số:
        - x (int): Tọa độ x của nút bấm.
        - y (int): Tọa độ y của nút bấm.
        - image (pygame.Surface): Hình ảnh của nút bấm.
        - scale (float): Tỉ lệ thay đổi kích thước của hình ảnh nút bấm.
        """
        # Thay đổi kích thước hình ảnh nút bấm
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        
        # Tạo hình chữ nhật bao quanh nút bấm
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        
        # Trạng thái ban đầu của nút bấm
        self.clicked = False

    def draw(self, surface):
        """
        Vẽ nút bấm lên một bề mặt và kiểm tra sự kiện nhấn nút.

        Tham số:
        - surface (pygame.Surface): Bề mặt để vẽ nút bấm.

        Trả về:
        - action (bool): Trả về True nếu nút bấm được nhấn, ngược lại trả về False.
        """
        action = False
        # Lấy vị trí của chuột
        pos = pygame.mouse.get_pos()

        # Kiểm tra va chạm với chuột
        if self.rect.collidepoint(pos):
            # Kiểm tra sự kiện nhấn chuột trái
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        # Kiểm tra sự kiện nhả chuột
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Vẽ nút bấm lên bề mặt
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
