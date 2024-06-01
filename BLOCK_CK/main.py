import pygame
import sys
from game import Game  
from colors import Colors  

pygame.init()

title_font = pygame.font.Font(None, 40)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)

screen = pygame.display.set_mode((320, 620))
pygame.display.set_caption("Tetris Game")

clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 500)

while True:
    """
    Vòng lặp chính của trò chơi. Xử lý các event, cập nhật trạng thái trò chơi, và vẽ màn hình.
    
    Event:
        - pygame.QUIT: Thoát trò chơi.
        - pygame.KEYDOWN: Xử lý các phím điều khiển trò chơi.
            - Mũi tên trái: Di chuyển tetromino sang trái.
            - Mũi tên phải: Di chuyển tetromino sang phải.
            - Mũi tên xuống: Di chuyển tetromino xuống.
            - Mũi tên lên: Xoay tetromino.
            - Nếu trò chơi kết thúc, bất kỳ phím nào được nhấn sẽ thiết lập lại trò chơi.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()

    screen.fill(Colors.black)

    if game.game_over == True:
        screen.blit(game_over_surface, (320, 450, 50, 50))

    game.draw(screen)

    pygame.display.update()
    clock.tick(60)
