import pygame

pygame.init()

width = 700
height = 900

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Foodrush")

chefnumber = 0

class player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)

    def draw(self, win):    #draw display window
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):     #movement of the character by WASD and within boundary
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and self.x - 3 > 0:
            self.x -= 3
        if keys[pygame.K_d] and self.x + 3 + self.width < width:
            self.x += 3
        if keys[pygame.K_w] and self.y - 3 > 0:
            self.y -= 3
        if keys[pygame.K_s] and self.y + 3 + self.height < height:
            self.y += 3
        
        self.rect = (self.x, self.y, self.width, self.height)

def redrawWindow(ppl, win):
    win.fill((255, 253, 208))
    ppl.draw(win)
    pygame.display.update()

def main():
    running = True
    ppl = player(350, 450, 50, 60, (255, 0, 255))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        ppl.move()
        redrawWindow(ppl, win)

main()