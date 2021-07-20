import pygame

# 초기화
pygame.init()
screen_width = 1280 # 가로크기
screen_heigth = 720 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_heigth)) # 튜플형태 = 테이블
pygame.display.set_caption("Memory game")

# 게임루프
# 게임 종료조건이 되면 탈출하는 loop
running = True # 게임 실행중 여부 확인
while running:
    # 이벤트 루프 : 사용자 동작(키보드, 마우스 동작)
    for event in pygame.event.get(): # 어떤 이벤트가 발생
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트?
            running = False # 게임진행중 아님을 설정

# 게임종료
pygame.quit()
