import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD


class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game_speed, game):

        if len(self.obstacles) == 0:
            if random.randint(0, 2) == 0:
                cactus = Cactus(SMALL_CACTUS)
                self.obstacles.append(cactus) 
            elif random.randint(0, 2) == 1:
                large_cactus = Cactus(LARGE_CACTUS)
                self.obstacles.append(large_cactus)
            elif random.randint(0, 2) == 2:
                bird = Bird(BIRD)
                self.obstacles.append(bird) 

        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)

            if game.player.dino_rect.colliderect(obstacle.rect):
                print("Game Over")
                pygame.time.delay(300)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
