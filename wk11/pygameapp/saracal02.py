import pygame


pygame.init()
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption("Pygame-01")
running = True
sara_sheet = pygame.image.load("sara\sara-cal1.png")
sara_rect = pygame.Rect(0,0,34,56)
sara_pos = pygame.Rect(50,50,34,56)

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        key = pygame.key.get_pressed()
        if key[pygame.K_d] and sara_pos.x+sara_rect.width < 400:
            sara_pos.x += 5
        elif key[pygame.K_a]and sara_pos.x > 0:
            sara_pos.x -= 5
        elif key[pygame.K_s]and sara_pos.y+sara_rect.height < 300:
            sara_pos.y += 5
        elif key[pygame.K_w]and sara_pos.y > 0:
            sara_pos.y -= 5
    
    clock.tick(90)
    screen.fill((255,255,255))
    font = pygame.font.SysFont("Arial",36)
    text = font.render(f'{clock.get_fps():.0f}',True,(0,0,0))
    screen.blit(text,(300,200))
    screen.blit(sara_sheet,sara_pos,sara_rect)

    
    pygame.display.update()

pygame.quit()