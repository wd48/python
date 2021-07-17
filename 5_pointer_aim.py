# 발사대 겨냥 (키보드 화살표 눌러서 움직임)
import os
import pygame

# 버블 클래스 생성
class Bubble(pygame.sprite.Sprite):
    def __init__(self, image, color, position):
        super().__init__()
        self.image = image
        self.color = color
        self.rect = image.get_rect(center=position)

# 발사대 클래스 생성
class Pointer(pygame.sprite.Sprite):
    def __init__(self, image, position, angle):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(center=position)
        self.angle = angle
        self.original_image = image
        self.position = position

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.circle(screen, RED, self.position, 3)

    # 회전
    def rotate(self, angle):
        # 원래 가진 각도에 angle을 더해주는 식
        self.angle += angle

        # 오른쪽 왼쪽 한계점 지정: 각도범위
        if self.angle > 170: # 왼쪽 끝
            self.angle = 170
        elif self.angle < 10:
            self.angle = 10

        # 원본이미지를 불러오는 변수에 담고 이를 움직이게한다
        # 원본이미지를 각도에 맞게 회전시킨 이미지를 update
        # rotozoom(회전시킬객체, 회전각도, 회전크기)
        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 1)
        # self.image의 각도정보는 계속 바뀐다 : 중심좌표가 바뀔수 있다
        self.rect = self.image.get_rect(center = self.position)
        
        

# 맵 만들기
def setup():
    global map
    map = [        
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
    ]
    for row_idx, row in enumerate(map):
        for col_idx, col in enumerate(row):
            if col in [".", "/"]:
                continue # . / 이면 무시하고 지나간다 = 다음 줄 실행
            position = get_bubble_position(row_idx, col_idx)
            image = get_bubble_image(col)
            bubble_group.add(Bubble(image, col, position))

def get_bubble_position(row_idx, col_idx):
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

pygame.init()
screen_width = 448
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Puzzle Bobble")
clock = pygame.time.Clock()

# 배경이미지 불러오기
current_path = os.path.dirname(__file__)
background = pygame.image.load(os.path.join(current_path, "background.png"))

# 버블 이미지 불러오기
bubble_images = [
    pygame.image.load(os.path.join(current_path, "red.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "yellow.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "blue.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "green.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "pupple.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "black.png")).convert_alpha()
]

# 발사대 이미지 불러오기
pointer_image = pygame.image.load(os.path.join(current_path, "pointer.png"))
pointer = Pointer(pointer_image, (screen_width // 2, 624), 90)


#게임관련 변수
CELL_SIZE = 56
BUBBLE_WIDTH = 56
BUBBLE_HEIGHT = 62
RED = (255,0,0)
# 화살표 관련 변수
to_angle = 0 # 좌우 각도
# 1.5도씩 움직이게 됨
angle_speed = 1.5

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
        # 키를 누를 때
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_angle += angle_speed
            elif event.key == pygame.K_RIGHT:
                to_angle -= angle_speed
        #왼쪽 오른쪽 방향키를 때면 멈춘다
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
                to_angle = 0

    screen.blit(background, (0,0))
    bubble_group.draw(screen) 
    # 회전 메소드
    pointer.rotate(to_angle)
    pointer.draw(screen)
    pygame.display.update()

pygame.quit()