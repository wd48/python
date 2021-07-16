# 배경 이미지 설정
import os
import pygame

pygame.init()
screen_width = 448
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Puzzle Bobble")
clock = pygame.time.Clock()

# 배경이미지 불러오기
# 실행하는 파일의 경로를 받아올것임 = PBW 나옴
current_path = os.path.dirname(__file__)
background = pygame.image.load(os.path.join(current_path, "background.png"))

# 참일동안 계속 계임 실행
running = True
while running:
    clock.tick(60) # FPS 60

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # x,y 0,0 좌표로 넣기
    screen.blit(background, (0,0))
    pygame.display.update()

pygame.quit()