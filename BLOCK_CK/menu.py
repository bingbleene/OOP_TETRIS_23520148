import pygame
import sys
from button import Button

class MENU():
    """
    Lớp MENU để tạo và điều khiển menu chính của trò chơi.

    Thuộc tính:
    run (bool): Trạng thái chạy của menu.
    game_paused (bool): Trạng thái tạm dừng của trò chơi.
    easy_button (Button): Nút chọn độ khó dễ.
    medium_button (Button): Nút chọn độ khó trung bình.
    hard_button (Button): Nút chọn độ khó khó.
    quit_button (Button): Nút thoát trò chơi.
    """
    def __init__(self, screene):
        """
        Hàm khởi tạo cho lớp MENU. Khởi tạo các nút và trạng thái ban đầu.

        Tham số:
        screene (pygame.Surface): Bề mặt pygame để vẽ menu.
        """
        self.easy_img = pygame.image.load('Graphics/button_easy.png').convert_alpha()
        self.medium_img = pygame.image.load('Graphics/button_medium.png').convert_alpha()
        self.hard_img = pygame.image.load('Graphics/button_hard.png').convert_alpha()
        self.quit_img = pygame.image.load('Graphics/button_quit.png').convert_alpha()

        self.run = True
        self.game_paused = False    

        self.easy_button = Button(150, 120, self.easy_img, 1)
        self.medium_button = Button(150, 220, self.medium_img, 1)
        self.hard_button = Button(150, 320, self.hard_img, 1)
        self.quit_button = Button(150, 420, self.quit_img, 1)
        self.screen = screene
    
    def draw_text(self, text, font_g, text_col, x, y):
        """
        Vẽ văn bản lên màn hình.

        Tham số:
        text (str): Văn bản cần vẽ.
        font_g (pygame.font.Font): Font chữ dùng để vẽ văn bản.
        text_col (tuple): Màu của văn bản dưới dạng (R, G, B).
        x (int): Tọa độ x để vẽ văn bản.
        y (int): Tọa độ y để vẽ văn bản.
        """
        if font_g is None:  # Kiểm tra nếu font_g là None
            font_g = pygame.font.Font(None, 40)  # Tạo font mặc định với kích thước 40
        img = font_g.render(text, True, text_col)
        self.screen.blit(img, (x, y))

    def run_menu(self):
        """
        Chạy vòng lặp menu chính.

        Trả về:
        int: Giá trị thời gian cập nhật màn hình dựa trên lựa chọn độ khó.
        """
        TEXT_COL = (255, 255, 255)
        pygame.display.set_caption("Main Menu")
        while self.run:
            self.screen.fill((0, 0, 0))

            # Kiểm tra xem trò chơi có đang tạm dừng không
            if self.game_paused:
                if self.easy_button.draw(self.screen):
                    return 500
                if self.medium_button.draw(self.screen):
                    return 200
                if self.hard_button.draw(self.screen):
                    return 80
                if self.quit_button.draw(self.screen):
                    pygame.quit()
                    sys.exit()
            else:
                self.draw_text("Welcome to TETRIS GAME", None, TEXT_COL, 70, 250)
                self.draw_text("Press SPACE to start", None, TEXT_COL, 110, 300)

            # Xử lý sự kiện
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.game_paused = True
                if event.type == pygame.QUIT:
                    self.run = False

            pygame.display.update()
