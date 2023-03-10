import random
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH

class HeartUp(Sprite):
    def __init__(self, image):
        print("heart up")
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = random.randint(115,250)

    def update(self, game_speed, heartup):
        self.rect.x -= game_speed

        if self.rect.x < 0:
            heartup.pop()

    def draw(self, screen):
        screen.blit(self.image, self.rect)



