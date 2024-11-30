import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidField import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    lastframeTime = 0
    groupUpdatable = pygame.sprite.Group()
    groupDrawable = pygame.sprite.Group()
    groupAsteroid = pygame.sprite.Group()
    groupShot = pygame.sprite.Group()
    Player.containers = (groupDrawable,groupUpdatable)
    Asteroid.containers = (groupDrawable,groupUpdatable, groupAsteroid)
    AsteroidField.containers = (groupUpdatable)
    Shot.containers = (groupShot,groupDrawable, groupUpdatable)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroidField = AsteroidField()
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for updatable in groupUpdatable:
            updatable.update(dt)
        # collision check between astroids and player
        for asteroid in groupAsteroid:
            collided = asteroid.isCollided(player)
            if(collided):
                print("Game over!")
                return
        # collision check between astroids and bullets
        for asteroid in groupAsteroid:
            for shot in groupShot:
                collided = asteroid.isCollided(shot)
                if(collided):
                    asteroid.split()
                    shot.kill()
        for drawable in groupDrawable:
            drawable.draw(screen)
        pygame.display.flip()
        lastframeTime = clock.tick(60)
        dt = lastframeTime/1000

if __name__ == "__main__":
    main()

