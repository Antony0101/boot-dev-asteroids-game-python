import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    lastframeTime = 0
    groupUpdatable = pygame.sprite.Group()
    groupDrawable = pygame.sprite.Group()
    Player.containers = (groupDrawable,groupUpdatable)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for updatable in groupUpdatable:
            updatable.update(dt)
        for drawable in groupDrawable:
            drawable.draw(screen)
        pygame.display.flip()
        lastframeTime = clock.tick(60)
        dt = lastframeTime/1000

if __name__ == "__main__":
    main()

