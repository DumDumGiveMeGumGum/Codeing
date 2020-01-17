import pygame
import os
import time
PlayerX=550
PlayerY=360
Loop =1
Mode1=False
Mode2=False
Mode3=False
Mode4=False
Mode5=False
pygame.init()
screen = pygame.display.set_mode((1280, 720))
done = False
clock = pygame.time.Clock()



while not done:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True
    
    mouse_pressed = pygame.mouse.get_pressed()
    mouseX, mouseY = pygame.mouse.get_pos()
    if mouse_pressed[0] and mouseX >= 550 and mouseX <= 699 and mouseY >= 360 and mouseY <= 408 and Mode5 == False:
        Mode1 = True
        print("What did you expect?")
        time.sleep(0.5)
    if mouse_pressed[0] and mouseX <= 10  and mouseY <= 10 and Mode4 == True:
        Mode5=True
            
    if mouse_pressed[0] and mouseX >= 700 and mouseX <= 750 and mouseY >= 30 and mouseY <= 80 and Mode1 == True:
        Mode2=True
        print ("Red")
        
    if mouse_pressed[0] and mouseX >= 600 and mouseX <= 650 and mouseY >= 30 and mouseY <= 80 and Mode2 == True:
        Mode3=True
        print ("Green")

    if mouse_pressed[0] and mouseX >= 500 and mouseX <= 550 and mouseY >= 30 and mouseY <= 80 and Mode3 == True:
        Mode4=True
        print ("Blue")
        
    if mouse_pressed[0] and mouseX >= 550 and mouseX <= 699 and mouseY >= 360 and mouseY <= 408 and Mode5 == True:
        print ("You made it do something")
            
    #print (mouseX, mouseY)
    screen.fill((100, 100, 255))
    
    pygame.draw.rect(screen, (100, 100, 250), pygame.Rect(-40, -40, 50, 50))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(545, 355, 160, 60))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(600, 30, 50, 50))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(700, 30, 50, 50))
    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(500, 30, 50, 50))
    pygame.draw.rect(screen, (255, 50, 0), pygame.Rect(PlayerX, PlayerY, 150, 50))

    pygame.display.flip()
    clock.tick(60)
