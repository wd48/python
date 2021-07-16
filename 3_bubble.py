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
    # 이중리스트 순회
    # row : 각 줄, col : 각 줄을 짤라와서 index 처럼 씀
    for row_idx, row in enumerate(map):
        for col_idx, col in enumerate(row):
            # 버블 그리기 여부 : / .
            if col in [".", "/"]:
                continue # . / 이면 무시하고 지나간다 = 다음 줄 실행
            # 실제 좌표 계산
            position = get_bubble_position(row_idx, col_idx)
            # 버블 이미지 추가 : col
            image = get_bubble_image(col)
            # 버블 만들기 스프라이트 그룹 만들기 > 그룹을 통해서 버블 관리하기          
            bubble_group.add(Bubble(image, col, position))


    # x = col_idx * cell_size(가로) + (bubble_width / 2)
    # y = row_idx * cell_size(세로) + (bubble_heigth / 2)
    # row_idx % 2 == 1? < 홀수번째 row이다?
    # x += cell_size / 2 : 셀사이즈 절반만큼만 이동한다
def get_bubble_position(row_idx, col_idx):
    # // : 나누기 결과값의 정수형 반환
    pos_x = col_idx * CELL_SIZE + (BUBBLE_WIDTH // 2)
    pos_y = row_idx * CELL_SIZE + (BUBBLE_HEIGHT // 2)
    if row_idx % 2 == 1:
        pos_x += CELL_SIZE // 2
    return pos_x, pos_y

def get_bubble_image(color):
    if color == "R":
        return bubble_images[0]
    elif color == "Y":
        return bubble_images[1]
    elif color == "B":
        return bubble_images[2]
    elif color == "G":
        return bubble_images[3]
    elif color == "P":
        return bubble_images[4]
    else:
        return bubble_images[-1]
        # -1 : 리스트의 마지막값 반환

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
    pygame.image.load(os.path.join(current_path, "black.png")).convert_alpha()
    # black : 화면 전체를 감싸는 게임종료시키는 용도    
]

#게임관련 변수
CELL_SIZE = 56
BUBBLE_WIDTH = 56
BUBBLE_HEIGHT = 62

map = [] # 맵
bubble_group = pygame.sprite.Group()
setup()

# 참일동안 계속 계임 실행
running = True
while running:
    clock.tick(60) # FPS 60

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # x,y 0,0 좌표로 넣기
    screen.blit(background, (0,0))
    bubble_group.draw(screen) # 모든 스프라이트를 screen에 그려준다
    pygame.display.update()

pygame.quit()