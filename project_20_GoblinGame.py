import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('Project_20_GoblinGame_R1.png'), pygame.image.load('Project_20_GoblinGame_R2.png'), pygame.image.load('Project_20_GoblinGame_R3.png'), pygame.image.load('Project_20_GoblinGame_R4.png'), pygame.image.load(
    'Project_20_GoblinGame_R5.png'), pygame.image.load('Project_20_GoblinGame_R6.png'), pygame.image.load('Project_20_GoblinGame_R7.png'), pygame.image.load('Project_20_GoblinGame_R8.png'), pygame.image.load('Project_20_GoblinGame_R9.png')]
walkLeft = [pygame.image.load('Project_20_GoblinGame_L1.png'), pygame.image.load('Project_20_GoblinGame_L2.png'), pygame.image.load('Project_20_GoblinGame_L3.png'), pygame.image.load('Project_20_GoblinGame_L4.png'), pygame.image.load(
    'Project_20_GoblinGame_L5.png'), pygame.image.load('Project_20_GoblinGame_L6.png'), pygame.image.load('Project_20_GoblinGame_L7.png'), pygame.image.load('Project_20_GoblinGame_L8.png'), pygame.image.load('Project_20_GoblinGame_L9.png')]
bg = pygame.image.load('Project_20_GoblinGame_bg.jpg')
char = pygame.image.load('Project_20_GoblinGame_standing.png')


x = 50
y = 425
width = 64
height = 64
vel = 5

isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0


def redrawGameWindow():
    global walkCount
    win.blit(bg, (0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()


# Main Loop
run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel

    if keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel

    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1

        else:
            isJump = False
            jumpCount = 10

    redrawGameWindow()

pygame.quit()
