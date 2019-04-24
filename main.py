import pygame
import pytmx
import random
from sprites import *
from settings import *
from tilemap import*
import time

def makeBorder(thickness):
    top = Edge(0,-(thickness/2),WIDTH,thickness)
    trails.add(top)
    all_sprites.add(top)
    bot = Edge(0,HEIGHT-(thickness/2),WIDTH,thickness)
    trails.add(bot)
    all_sprites.add(bot)
    left = Edge(-(thickness/2),0, thickness, HEIGHT)
    trails.add(left)
    all_sprites.add(left)
    right = Edge(WIDTH-(thickness/2),0, thickness, HEIGHT)
    trails.add(right)
    all_sprites.add(right)

def genScoreText(scores):
    text = str(scores[0]) + " : " + str(scores[1])
    return text

def drawText(text, offset,small):
    if small:
        surf  = myfontsmall.render(text, True, WHITE)
    else:
        surf  = myfont.render(text, True, WHITE)
    screen.blit(surf, ((WIDTH/2)-(surf.get_width()/2), int(HEIGHT/2)-(surf.get_height()/2)+ offset))


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("LightBike")
clock = pygame.time.Clock()

pygame.font.init()
myfont = pygame.font.SysFont('chalkboard', 70)
myfontsmall = pygame.font.SysFont('chalkboard', 15)

map = TiledMap("stage.tmx")
map_img = map.make_map()
map_rect = map_img.get_rect()

blankscreen = pygame.Surface((WIDTH,HEIGHT))
blankscreen.fill(BLACK)
blankscreen_rect = blankscreen.get_rect()
#create player sprite and add it to group

#textsurface = myfont.render('LIGHTBIKE', True, WHITE)
updatingText = "LIGHTBIKE"
pressSpace = myfontsmall.render('Press Space to Continue...', True, WHITE)

player1wins = myfont.render('Player 1 Wins!',True, WHITE)
player2wins = myfont.render('Player 2 Wins!',True, WHITE)



player = None
player2 = None

running = True
makeBorder(8)

scores = [0,0]
loadmap = False
textscreen = True


while running:
    if textscreen:
        screen.fill(BLACK)
        drawText(updatingText,0,False)
        drawText('Press Space to Continue...',50,True)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            loadmap = True
            textscreen = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if loadmap:
        all_sprites.empty()
        trails.empty()
        players.empty()
        for tile_object in map.tmxdata.objects:
            if tile_object.name == 'player1':
                    player = Player1(tile_object.x, tile_object.y,3,3)
            if tile_object.name == 'player2':
                    player2 = Player2(tile_object.x, tile_object.y,3,3)
        loadmap = False
        all_sprites.add(player)
        all_sprites.add(player2)
        players.add(player)
        players.add(player2)
        makeBorder(8)



    if textscreen == False:
        all_sprites.update()
        screen.blit(map_img, map_rect)

        for sprite in all_sprites:
            screen.blit(sprite.image, sprite.rect)

        if scores[0]==3:
            player.movement = [0,0]
            player2.movement = [0,0]
            screen.fill(BLACK)
            drawText('Player 1 Wins!',0,False)
        elif scores[1]==3:
            player.movement = [0,0]
            player2.movement = [0,0]
            screen.fill(BLACK)
            drawText('Player 2 Wins!',0,False)

        if pygame.sprite.collide_rect(player,player2):
            textsurface = myfont.render(genScoreText(scores), True, WHITE)
            textscreen = True

        hits = pygame.sprite.spritecollide(player,trails,False)

        if len(hits)>0:
            scores[1]+=1
            #textsurface = myfont.render(genScoreText(scores), True, WHITE)
            updatingText = genScoreText(scores)
            textscreen = True

        hits = pygame.sprite.spritecollide(player2,trails,False)

        if len(hits)>0:
            scores[0]+=1
            textscreen = True
            updatingText = genScoreText(scores)
            #textsurface = myfont.render(genScoreText(scores), True, WHITE)


    clock.tick(FPS)/1000
    pygame.display.flip()

pygame.quit()
