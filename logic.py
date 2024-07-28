import pygame

width = 700
height = 900
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chef")

chefnumber = 0

class player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        

def redrawWindow():
    win.fill((255, 253, 208))
    pygame.display.update()

def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        redrawWindow()