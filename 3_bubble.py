# 버블 이미지 설정 / map 생성
import os
import pygame

# 버블 클래스 생성
class Bubble(pygame.sprite.Sprite):
    def __init__(self, image, color, position):
        super().__init__()
        self.image = image
        self.color = color
        self.rect = image.get_rect(center=position)

# 맵 만들기
# 전역공간으로 만들어서 다 쓸수 있게
def setup():
    global map
    map = [        
        #["R","R","Y","Y","B","B","G","G"]
        # list() : 문자열이 하나하나로 나눠진다!
        list("RRYYBBGG"),
        list("RRYYBBG/"), # / : 버블이 위치할 수 없는 곳
        list("BBGGRRYY"),
        list("BGGRRYY/"),
        list("........"),
        list("......./"),
        list("........"),
        list("......./"),
        list("........"),
        list("......./"),
        list("........")
        # 맵 크기 8*11

    ]


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

# 버블 이미지 불러오기
bubble_images = [
    # 충돌체크용 convert_alpha
    pygame.image.load(os.path.join(current_path, "red.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "yellow.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "blue.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "green.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "pupple.png")).convert_alpha(),
    # black : 화면 전체를 감싸는 게임종료시키는 용도
    pygame.image.load(os.path.join(current_path, "black.png")).convert_alpha()
]

map = [] # 맵

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