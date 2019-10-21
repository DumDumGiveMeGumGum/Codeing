import pygame
import os
import time
x=10
y=10
speedX=21
speedY=21

Lives=0

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

while Lives !=3:
    while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        x=x+speedX
        y=y+speedY

        #screen.fill((255, 255, 255))
        
        screen.blit(get_image('Dvd.png'), (x,y,20, 20))
        
        pygame.display.flip()
        clock.tick(60)


        if x<=0:
                screen.fill((225, 225, 0))
                speedX=speedX*-1
                Lives=Lives+1
        if x>=(1020):
                screen.fill((225, 0, 0))
                speedX=speedX*-1
                Lives=Lives+1
        if y<=0:
                screen.fill((0, 225, 0))
                speedY=speedY*-1
                Lives=Lives+1
        if y>=(620):
                screen.fill((225, 111, 0))
                speedY=speedY*-1
                Lives=Lives+1
