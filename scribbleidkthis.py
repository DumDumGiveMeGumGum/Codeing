#Its Still Incompleate
import pygame
import os
import time
PlayerX=10
PlayerY=640
BottemX=-500
BottemY=670
Cube1X=500
Loop =1
CubeTouch1= False
Jumping = False
Move = True


pygame.init()
screen = pygame.display.set_mode((1280, 720))
done = False
clock = pygame.time.Clock()


while Loop !=3:
    while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
    
        pressed = pygame.key.get_pressed()
        if PlayerX <= 470 and PlayerY < 640:
            PlayerY+=3
        if PlayerX >= 530 and PlayerY < 640:
            PlayerY+=3
        if PlayerX > 470 and PlayerX < 530:
            if PlayerY<= 610:
                PlayerY+=3
        
        
    
        
        print(Cube1X, "and", PlayerX, PlayerY)
        if pressed[pygame.K_UP]:
            Jumping = True
            if Jumping is True:
                PlayerY -= 20
        if PlayerX < 470 or PlayerX > 499:
            Move = True
            if Move == True:
                PlayerX+=1

        if PlayerX <499 and PlayerX >470 and PlayerY > 613:
            Move = False
            
        if pressed[pygame.K_RIGHT]:
            PlayerX += 3
        if pressed[pygame.K_LEFT]:
            PlayerX -= 3
        
        screen.fill((100, 100, 255))
        
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(PlayerX, PlayerY, 30, 30))
        pygame.draw.rect(screen, (50, 50, 50), pygame.Rect(BottemX, BottemY, 9999, 50))
        pygame.draw.rect(screen, (0, 0, 225), pygame.Rect(Cube1X,640 , 30, 30))
        pygame.display.flip()
        clock.tick(60)
        Jumping=False
