import sys,os
import pygame
pygame.init()

from chars.sara import player

class saraAdventure:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400,300))
        self.caption = 'sara Adventure'
        self.font = pygame.font.SysFont("Arial",20)
        self.player = player('sara','sara\sara-cal1.png',150,150)
        pygame.display.set_caption(self.caption)
        self.clock = pygame.time.Clock()
        self.sound = pygame.mixer.Sound('sara\stepdirt_1.wav')
    
    def handle_close(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    def draw_text(self,text,position,color=(0,0,0)):
        surface = self.font.render(text,True,color)
        self.screen.blit(surface,position)
    
    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.left()
            self.sound.play()
        if keys[pygame.K_RIGHT]:
            self.player.right()
        if keys[pygame.K_UP]:
            self.player.up()
        if keys[pygame.K_DOWN]:
            self.player.down()
    
    def start(self):
        while True:
            elapsed_time = self.clock.tick(60)
            self.handle_close()
            self.handle_keys()
            self.screen.fill((255,255,255))
            self.draw_text('sara adventure',(100,100))
            self.player.update(elapsed_time)
            self.player.draw(self.screen)
            pygame.display.flip()
        
        pygame.quit()
            
if __name__ == '__main__':
    game = saraAdventure()
    game.start()