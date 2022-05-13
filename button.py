import pygame

pygame.init()
pygame.font.init()

class Button:
    def __init__(self, screen , x, y, height, width, colour=None, text=None, textsize=None, font=None, textcolour=None) -> None:
        self.screen = screen
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.colour = colour
        self.textcolour = textcolour
        self.text = text
        self.textsize = textsize
        self.font = font

        self.colour = colour if self.colour else (255,0,0)
        self.textcolour = textcolour if self.textcolour else (255,255,255)
        self.text = text if self.text else "Button"
        self.font = font if self.font else 'arial.ttf'

    def draw(self):
        
        pygame.draw.rect(self.screen, self.colour, pygame.Rect(self.x, self.y, self.height, self.width))

        if self.text:            
            font = pygame.font.Font('freesansbold.ttf', self.textsize)
            if self.textcolour:
                text = font.render(self.text, True, self.textcolour) 
            self.screen.blit(text, (self.height/2,self.width/2))

    def detect_press(self , event:pygame.event.Event) -> bool:

        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                print(pos)
            
        
        return True


    




pygame.quit()