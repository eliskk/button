import pygame
import button


WIDTH = 360
HEIGHT = 480
FPS = 30

pygame.init()
pygame.mixer.init()  
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("<Your game>")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

## Game loop
running = True
while running:
    
    button1 = button.Button(screen, 10, 10, 60, 30, (0,0,128), "penis", 12)

    clock.tick(FPS)  
    for event in pygame.event.get():        
        if event.type == pygame.QUIT:
            running = False

    button1.detect_press(event)

    
    all_sprites.update()
    screen.fill((255,255,255))


    button1.draw()
    
    

    all_sprites.draw(screen)

    pygame.display.flip()       

pygame.quit()