import pygame
import sys
from game import Game
from colors import Colors
from menu import MENU 

class TetrisGame:
    """
    Lớp TetrisGame quản lý trò chơi Tetris.
    """
    def __init__(self):
        """
        Hàm khởi tạo thiết lập các thành phần cần thiết cho trò chơi.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((500, 620))
        pygame.display.set_caption("Python Tetris")
        self.clock = pygame.time.Clock()
        self.__game = Game()  
        self.__menu = MENU(self.screen)
        
        self.__title_font = pygame.font.Font(None, 40)
        self.__score_surface = self.__title_font.render("Score", True, Colors.white)
        self.__next_surface = self.__title_font.render("Next", True, Colors.white)
        self.__game_over_surface = self.__title_font.render("GAME OVER", True, Colors.red)
        self.__game_win_surface = self.__title_font.render("YOU WIN", True, Colors.yellow)
        
        self.__score_rect = pygame.Rect(320, 55, 170, 60)
        self.__next_rect = pygame.Rect(320, 215, 170, 180)
        
        self.__GAME_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(self.__GAME_UPDATE, self.__menu.run_menu())

    def run(self):
        """
        Hàm chạy trò chơi, bao gồm vòng lặp chính để xử lý sự kiện và vẽ màn hình.
        """
        while True:
            self.handle_events()
            self.draw()

    def handle_events(self):
        """
        Hàm xử lý các sự kiện của trò chơi.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if self.__game.game_over:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.__game.reset()
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.__game.move_left()
                    elif event.key == pygame.K_RIGHT:
                        self.__game.move_right()
                    elif event.key == pygame.K_DOWN:
                        self.__game.move_down()
                        self.__game.update_score(0, 1)
                    elif event.key == pygame.K_UP:
                        self.__game.rotate()
                if event.type == self.__GAME_UPDATE:
                    self.__game.move_down()

    def draw(self):
        """
        Hàm vẽ các thành phần của trò chơi lên màn hình.
        """
        score_value_surface = self.__title_font.render(str(self.__game.score), True, Colors.black)

        self.screen.fill(Colors.black)
        self.screen.blit(self.__score_surface, (365, 20, 50, 50))
        self.screen.blit(self.__next_surface, (375, 180, 50, 50))

        if self.__game.game_over:
            if self.__game.game_win:
                self.screen.blit(self.__game_win_surface, (345, 450, 50, 50))
            else:
                self.screen.blit(self.__game_over_surface, (322, 450, 50, 50))
            self.screen.blit(pygame.font.Font(None, 20).render("Press SPACE to restart", True, Colors.white), (335, 500, 50, 50))

        pygame.draw.rect(self.screen, Colors.white, self.__score_rect, 0, 10)
        self.screen.blit(score_value_surface, score_value_surface.get_rect(centerx=self.__score_rect.centerx,
                                                                           centery=self.__score_rect.centery))
        pygame.draw.rect(self.screen, Colors.dark_grey, self.__next_rect, 0, 10)
        
        self.__game.draw(self.screen)

        pygame.display.update()
        self.clock.tick(60)

