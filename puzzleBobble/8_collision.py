# 충돌 처리 1 : 기본 충돌로직 설계
# 충돌 처리 2 : 버블이 양 끝 구석에 던져지면서 벽에 부딪히면서 바로 버블에 부딪힐 때
import os, random, math
import pygame

# 버블 클래스 생성
class Bubble(pygame.sprite.Sprite):
    # 버블 위치 기본값 지정
    def __init__(self, image, color, position=(0,0)):
        super().__init__()
        self.image = image
        self.color = color
        self.rect = image.get_rect(center=position)
        self.radius = 18 # 속도 지정변수

    # 버블 위치: 사각형 기준으로 중심에 버블을 둠
    def set_rect(self, position):
        self.rect = self.image.get_rect(center = position)

    # 화면에 버블을 출력
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    # 버블이 이동해야하는 각도 저장필요
    def set_angle(self, angle):        
        self.angle = angle
        self.rad_angle = math.radians(self.angle)

    def move(self):
        to_x = self.radius * math.cos(self.rad_angle)
        to_y = self.radius * math.sin(self.rad_angle) * -1 
        # pygame : 맨위가 0,0 > 아래로 내려올수록 (-)
    
        self.rect.x += to_x
        self.rect.y += to_y

        # 튕겨나오는 계산
        if self.rect.left < 0 or self.rect.right > screen_width: 
            self.set_angle(180 - self.angle)

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
                continue # . , / 이면 무시하고 지나간다 = 다음 줄 실행
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

def prepare_bubbles():
    global curr_bubble, next_bubble
    # 다음 버블이 있으면 다음 버블을 현재 버블로 바꿔준다
    if next_bubble:
        curr_bubble = next_bubble
    else:
        curr_bubble = create_bubble()

    curr_bubble.set_rect((screen_width // 2, 624)) # 화면기준 발사대 위쪽(화살표 끝)
    next_bubble = create_bubble()
    next_bubble.set_rect((screen_width // 4, 688))

def create_bubble():
    color = get_random_bubble_color()
    image = get_bubble_image(color)
    return Bubble(image, color)

# 랜덤으로 버블색깔 지정
def get_random_bubble_color():
    colors = []
    for row in map:
        for col in row: # RRYYBBGG
            if col not in colors and col not in [".", "/"]: # 아직 없는 색깔일때, 비어있는 위치가 아닐 경우
                colors.append(col)
    return random.choice(colors)

# 충돌함수
# 충돌 발생시 현재위치(센터기준), 어떤 컬럼에 있는지 맵에 추가하고 컬럼위치들도 바꿔주고 bubble_group에 추가해서 다음 충돌에 대비할
# 버블을 현재 맵에 업데이트 시켜준다
def process_collision(): 
    global curr_bubble, fire
    # 충돌한 버블 (충돌한버블, sprite그룹, 진짜이미지비교)
    hit_bubble = pygame.sprite.spritecollideany(curr_bubble, bubble_group, pygame.sprite.collide_mask)
    # 충돌이 있을 경우
    if hit_bubble:
        row_idx, col_idx = get_map_index(*curr_bubble.rect.center) # x,y
        # * : unpacking > 하나를 나눠서 2개의 매개변수로 준다
        # 1. 현재버블을 현재맵기준으로 이동 2. 버블을 버블 그룹에 넣어주면 끝
        place_bubble(curr_bubble, row_idx, col_idx)
        curr_bubble = None
        fire = False

def get_map_index(x, y):
    row_idx = y // CELL_SIZE
    col_idx = x // CELL_SIZE
    # 실제 위치 계산 (홀수줄의 경우: 위에서 홀수줄은 cell_size의 반만큼 이동시켜놨음)
    if col_idx % 2 == 1:
        col_idx = (x - (CELL_SIZE // 2)) // CELL_SIZE
        if col_idx < 0:
            col_idx = 0
        elif col_idx > MAP_COLUMN_COUNT - 2:
            col_idx = MAP_COLUMN_COUNT - 2    
    return row_idx, col_idx
    
def place_bubble(bubble, row_idx, col_idx):
    map[row_idx][col_idx] = bubble.color
    position = get_bubble_position(row_idx, col_idx)
    bubble.set_rect(position)
    bubble_group.add(bubble)

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
MAP_ROW_COUNT = 11
MAP_COLUMN_COUNT = 8

# 화살표 관련 변수
# to_angle = 0 # 좌우 각도
to_angle_left = 0 # 왼쪽으로 움직일 각도 정보
to_angle_right = 0 # 오른쪽으로 움직일 각도 정보
angle_speed = 1.5 # 1.5도씩 움직이게 됨

curr_bubble = None # 이번에 쏠 버블
next_bubble = None # 다음에 쏠 버블
fire = False

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
                to_angle_left += angle_speed                
            elif event.key == pygame.K_RIGHT:
                to_angle_right -= angle_speed
            elif event.key == pygame.K_SPACE: # 스페이스키 눌렀을 때
                # 버블 확인+발사상태 확인 / 발사
                if curr_bubble and not fire:
                    fire = True
                    # 쏠때 발사각도 지정
                    curr_bubble.set_angle(pointer.angle)

        #왼쪽 오른쪽 방향키를 때면 멈춘다
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_angle_left = 0
            elif event.key == pygame.K_RIGHT:
                to_angle_right = 0

    # 버블 유무 확인
    if not curr_bubble:
        prepare_bubbles()

    if fire:
        process_collision() # 충돌 함수

    screen.blit(background, (0,0))
    bubble_group.draw(screen) 
    pointer.rotate(to_angle_left + to_angle_right) # 동시 누르면 멈추지만,     
    pointer.draw(screen)

    if curr_bubble:
        if fire:
            curr_bubble.move() # 지정된 각도만큼 이동하고 프레임적용 이동하고 프레임 적용
        curr_bubble.draw(screen)
        if curr_bubble.rect.top <= 0:
            curr_bubble = None
            fire = False
    
    if next_bubble:
        next_bubble.draw(screen)


    pygame.display.update()

pygame.quit()