import math, random, pygame
from pygame import mixer

pygame.init() # Inicializar o módulo pygame

screen = pygame.display.set_mode((800, 600)) # Define o tamanho da tela

background = pygame.image.load('background.png') # Carrega a imagem como plano de fundo

mixer.music.load("background.wav") # Seleciona a música de fundo
mixer.music.play(-1) #coloca a música para rodar em loop infinito

pygame.display.set_caption("Space Invader") #define o nome da janela
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon) #define o ícone do jogo na janela

playerImg = pygame.image.load('Nave.png') #carrega a imagem da nave
playerX = 370
playerY = 480
playerX_change = 0

# Inicialização dos inimigos
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 4

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('alien.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

bulletImg = pygame.image.load('bala.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "pronto" # pronto - você não vê a bala na tela e tiro- a bala está se movendo

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 24) #define a fonte e o tamanho da letra no score

#Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64) #define o tamanho da letra e a fonte no game over

score_position_x = 10
score_position_y = 10

def show_score(x, y):
    score = font.render("SCORE: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fogo"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

# Rodando o jogo
while True:

    screen.fill((0, 0, 0)) # RGB = Red, Green, Blue -> para limpar a tela

    screen.blit(background, (0, 0)) # Background Image

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN: #para saber se alguma tecla foi pressionada
            if event.key == pygame.K_a: #A move a nave para a esquerda
                playerX_change = -5
            if event.key == pygame.K_d: #D move a nave para a direita
                playerX_change = 5
            if event.key == pygame.K_SPACE: #barra de espaço atira
                if bullet_state == "pronto":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    bulletX = playerX # Obtém a coordenada x atual da nave espacial
                    bullet_state = "fogo"
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP: #para saber se a tecla pressionada foi solta
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0


    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Movimento dos aliens
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

        # Colisão
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            bulletY = 480
            bullet_state = "pronto"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Disparo
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "pronto"

    if bullet_state == "fogo":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(score_position_x, score_position_y)
    pygame.display.update()