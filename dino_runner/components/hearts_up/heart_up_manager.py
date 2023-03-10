import random
import pygame
from dino_runner.components.hearts_up.extra_heart import ExtraHeart

class HeartUpManager:

    def __init__(self):
        self.hearts_up = [] 
        self.points = 0
        self.when_appears = 0

    def generate_extra_hearts(self, points):
        self.points = points

        if len(self.hearts_up) == 0:
            if self.when_appears == self.points:
                print("generating extra heart")
                self.when_appears = random.randint(self.when_appears + 500, 750 + self.when_appears)
                self.hearts_up.append(ExtraHeart())


    def update(self, points, game_speed, game):
        self.generate_extra_hearts(points)    
        for heart_up in self.hearts_up:
            heart_up.update(game_speed, self.hearts_up)

            if game.player.dino_rect.colliderect(heart_up.rect):
                game.heart_manager.increase_heart()
                pygame.time.delay(300)
                self.hearts_up.remove(heart_up)



    def draw(self, screen):
        for heart_up in self.hearts_up:
            heart_up.draw(screen)