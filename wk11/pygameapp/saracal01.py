import pygame


pygame.init()
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption("Pygame-01")
running = True
sara = pygame.image.load("sara\sara-cal1.png")
squid = pygame.image.load("sara\squid-reef.png")
octopus_or = pygame.image.load("sara\octopus-reef.png").convert_alpha()
octopus = pygame.transform.scale(octopus_or, (150, 150))


clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    clock.tick(90)
    screen.fill((255,255,255))
    font = pygame.font.SysFont("Arial",36)
    text = font.render(f'{clock.get_fps():.0f}',True,(0,0,0))
    screen.blit(text,(300,200))
    screen.blit(sara,(50,50))
    screen.blit(squid,(350,250))
    screen.blit(octopus,(200,50))
    
    pygame.display.update()

pygame.quit()