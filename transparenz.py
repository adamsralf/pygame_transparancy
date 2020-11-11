import pygame
from pygame.constants import (
    QUIT, K_ESCAPE, KEYDOWN
)
import os

class Settings:
    window_width = 400
    window_height = 400
    file_path = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(file_path, "images")


class Cat(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        bitmap = pygame.image.load(os.path.join(Settings.image_path, "cat1.bmp"))
#        bitmap.set_colorkey((0, 0, 0))
        self.image = bitmap.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = Settings.window_width // 2
        self.rect.centery = Settings.window_height // 2



if __name__ == '__main__':
    os.environ['SDL_VIDEO_WINDOW_POS'] = "850, 100"
#pylint: disable=no-member
    pygame.init()
#pylint: enable=no-member
    screen = pygame.display.set_mode((Settings.window_width, Settings.window_height))

    cat = Cat()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        

        screen.fill((255, 255, 255))
        screen.blit(cat.image, cat.rect)
        pygame.display.flip()


#pylint: disable=no-member
    pygame.quit()
#pylint: enable=no-member
