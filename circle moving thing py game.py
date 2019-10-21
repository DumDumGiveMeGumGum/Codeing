import pygame
import os
import time
x=10
y=10
speedX=3
speedY=3
Lives=0
Four_Lives=0

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image

        return image

pygame.init()
screen = pygame.display.set_mode((1280, 720))
done = False
clock = pygame.time.Clock()

while Four_Lives !=3:
    while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
    
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        screen.fill((255, 255, 255))
        
        screen.blit(get_image('ball.png'), (x,y,20, 20))
        
        pygame.display.flip()
        clock.tick(60)


        if x<=0:
                time.sleep(1)
                Lives=(Lives)+1
                print (Lives)
        if x>=(1230):
                time.sleep(1)
                Lives=(Lives)+1
                print (Lives)
        if y<=0:
                time.sleep(1)
                Lives=(Lives)+1
                print (Lives)
        if y>=(673):
                time.sleep(1)
                Lives=(Lives)+1
                print (Lives)
