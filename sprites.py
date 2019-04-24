import pygame
import pygame
from settings import *
from tilemap import *

clock = pygame.time.Clock()
dt = clock.tick(FPS)/1000

def collision_test(rect,tiles):
    collisions = []
    for tile in tiles:
        if rect.colliderect(tile):
            collisions.append(tile)
    return collisions

class Player1(pygame.sprite.Sprite):
    #sprite for Player

    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.size = self.width, self.height = (width,height)
        self.image = pygame.Surface((width,height))
        self.image.fill(WHITE)
        #looks at image, copies rect
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.movement = [10,0]
        self.collision_types = {'top':False,'bottom':False,'right':False,'left':False}
        self.trails = []
        self.dir = 1
        self.trails.append(Trail(self.rect.topleft[0],self.rect.topleft[1],1,RED))


    def update(self):
        self.keys()
        self.move()
        self.updateTrail(False)

    def move(self): # movement = [5,2]
        self.collision_types['top'] = False
        self.collision_types['left'] = False
        self.collision_types['bottom'] = False
        self.collision_types['right'] = False

        self.rect.x += self.movement[0]
        collisions = collision_test(self.rect,obstacles)
        for tile in collisions:
            if self.movement[0] > 0:
                self.collision_types['right'] = True
                self.rect.right = tile.rect.left
            if self.movement[0] < 0:
                self.rect.left = tile.rect.right
                self.collision_types['left'] = True


        self.rect.y += self.movement[1]
        collisions = collision_test(self.rect,obstacles)
        for tile in collisions:
            if self.movement[1] > 0:
                self.collision_types['bottom'] = True
                self.rect.bottom = tile.rect.top
            if self.movement[1] < 0:
                self.rect.top = tile.rect.bottom
                self.collision_types['up'] = True

    def keys(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and self.movement[1]==0:
            self.movement = [0,-10]
            self.dir = 0
            self.trails.append(Trail(self.rect.midbottom[0],self.rect.midbottom[1],1,RED))

        elif keys[pygame.K_s] and self.movement[1]==0:
            self.movement = [0,10]
            self.dir = 2
            self.trails.append(Trail(self.rect.midtop[0],self.rect.midtop[1],1,RED))

        elif keys[pygame.K_d] and self.movement[0]==0:
            self.movement = [10,0]
            self.dir = 1
            self.trails.append(Trail(self.rect.topleft[0],self.rect.topleft[1],1,RED))

        elif keys[pygame.K_a] and self.movement[0]==0:
            self.movement = [-10,0]
            self.dir = 3
            self.trails.append(Trail(self.rect.topright[0],self.rect.topright[1],1,RED))



    def updateTrail(self,change):
        t = self.trails[len(self.trails)-1]
        if self.dir == 1:
            t.resize(1,self.rect)
            t.rect.midright = self.rect.midleft
        elif self.dir == 3:
            t.resize(3,self.rect)
            t.rect.midleft= self.rect.midright
        elif self.dir == 0:
            t.resize(0,self.rect)
            t.rect.midtop= self.rect.midbottom
        elif self.dir == 2:
            t.resize(2,self.rect)
            t.rect.midbottom = self.rect.midtop


class Player2(pygame.sprite.Sprite):
    #sprite for Player

    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.size = self.width, self.height = (width,height)
        self.image = pygame.Surface((width,height))
        self.image.fill(WHITE)
        #looks at image, copies rect
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.movement = [-10,0]
        self.collision_types = {'top':False,'bottom':False,'right':False,'left':False}
        self.trails = []
        self.dir = 3
        self.trails.append(Trail(self.rect.topleft[0],self.rect.topleft[1],2,BLUE))

    def update(self):

        self.keys()
        self.move()
        self.updateTrail()

    def move(self):

        self.collision_types['top'] = False
        self.collision_types['left'] = False
        self.collision_types['bottom'] = False
        self.collision_types['right'] = False

        self.rect.x += self.movement[0]
        collisions = collision_test(self.rect,obstacles)
        for tile in collisions:
            if self.movement[0] > 0:
                self.collision_types['right'] = True
                self.rect.right = tile.rect.left
            if self.movement[0] < 0:
                self.rect.left = tile.rect.right
                self.collision_types['left'] = True
        self.rect.y += self.movement[1]
        collisions = collision_test(self.rect,obstacles)
        for tile in collisions:
            if self.movement[1] > 0:
                self.collision_types['bottom'] = True
                self.rect.bottom = tile.rect.top
            if self.movement[1] < 0:
                self.rect.top = tile.rect.bottom
                self.collision_types['up'] = True


    def keys(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and self.movement[1]==0:
            self.movement = [0,-10]
            self.dir = 0
            #self.trails.append(Trail(self.rect.bottomleft[0],self.rect.bottomleft[0],1))
            self.trails.append(Trail(self.rect.midbottom[0],self.rect.midbottom[1],2,BLUE))

        elif keys[pygame.K_DOWN] and self.movement[1]==0:
            self.movement = [0,10]
            self.dir = 2
            self.trails.append(Trail(self.rect.midtop[0],self.rect.midtop[1],2,BLUE))


        elif keys[pygame.K_RIGHT] and self.movement[0]==0:
            self.movement = [10,0]
            self.dir = 1
            self.trails.append(Trail(self.rect.topleft[0],self.rect.topleft[1],2,BLUE))


        elif keys[pygame.K_LEFT] and self.movement[0]==0:
            self.movement = [-10,0]
            self.dir = 3
            self.trails.append(Trail(self.rect.topright[0],self.rect.topright[1],2,BLUE))



    def updateTrail(self):
        t = self.trails[len(self.trails)-1]
        if self.dir == 1:
            t.resize(1,self.rect)
            t.rect.midright = self.rect.midleft
        elif self.dir == 3:
            t.resize(3,self.rect)
            t.rect.midleft= self.rect.midright
        elif self.dir == 0:
            t.resize(0,self.rect)
            t.rect.midtop= self.rect.midbottom
        elif self.dir == 2:
            t.resize(2,self.rect)
            t.rect.midbottom = self.rect.midtop


class Trail(pygame.sprite.Sprite):

    def __init__(self, x, y, player,color):
        pygame.sprite.Sprite.__init__(self,all_sprites)

        self.color = color
        self.size = self.width, self.height = ((3,3))
        self.image = pygame.Surface((self.width,self.height))
        self.image.fill(self.color)
        #looks at image, copies rect
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        if player == 1:
            self.dir = 1
        else:
            self.dir = 3
        trails.add(self)

    def resize(self,dir,playerrect):

        if dir == 1:
            x = playerrect.topleft[0]
            self.image = pygame.Surface((x-(self.rect.topleft[0]),self.height))
        #    self.image
        if dir == 3:
            x = playerrect.topright[0]
            self.image = pygame.Surface((self.rect.topright[0]-x, self.height))

        if dir == 0:
             y = playerrect.midbottom[1]
             self.image = pygame.Surface((self.width,  (self.rect.midbottom[1]-y)))

        if dir == 2:
             y = playerrect.midtop[1]
             self.image = pygame.Surface((self.width,  (y-self.rect.midtop[1])))

        self.image.fill(self.color)
        self.rect = self.image.get_rect()



class Obstacle(pygame.sprite.Sprite):
    def __init__(self,x,y,w,h):
        pygame.sprite.Sprite.__init__(self,obstacles)
        self.rect = pygame.Rect(x,y,w,h)
        self.rect.x = x
        self.rect.y = y

class Edge(pygame.sprite.Sprite):
    def __init__(self,x,y,w,h):
        pygame.sprite.Sprite.__init__(self)
        self.size = self.width, self.height = ((w,h))
        self.image = pygame.Surface((self.width,self.height))
        self.image.fill(WHITE)
        #looks at image, copies rect
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
