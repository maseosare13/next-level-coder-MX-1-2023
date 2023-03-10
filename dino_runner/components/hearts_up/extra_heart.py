import random
from dino_runner.components.hearts_up.heart_up import HeartUp
from dino_runner.utils.constants import HEART


class ExtraHeart(HeartUp):
    def __init__(self):
        self.image = HEART
        super().__init__(self.image)
