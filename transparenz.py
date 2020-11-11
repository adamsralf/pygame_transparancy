"""Making background transparent with PyGame.

A short program which shows how to make the 
background of a sprite transparent with PyGame.
Two ways are possible:
 * Setting the "magic pink" manually by set_colorkey()
 * Using a bitmap with alpha-chanel and convert_alpha()

 Hint: the slow down using the clock is added later
"""
import pygame
from pygame.constants import (
    QUIT, K_ESCAPE, KEYDOWN
)
import os


class Settings:
    """Project global informations.

    This static class contains project global informations like window size and file directories.
    """
    window_width = 400
    window_height = 400
    file_path = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(file_path, "images")


class Cat(pygame.sprite.Sprite):
    """A cat sprite class.

    Short sprite example with no other function as showing how to make 
    the background color transparent. This class is derived from pygame.sprite.Sprite. 
    """

    def __init__(self):
        """Constructor function.

        Besides all other usual tasks of a constructor this function loads the 
        bitmap and center the position. 
        """
        super().__init__()
        bitmap = pygame.image.load(
            os.path.join(Settings.image_path, "cat1.bmp"))
#        bitmap.set_colorkey((0, 0, 0))
        self.image = bitmap.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = Settings.window_width // 2
        self.rect.centery = Settings.window_height // 2


if __name__ == '__main__':
    """Main function

    Starts and runs the the transparancy example. 

    Hint: This is not a testing main function.
    """

    # Preparation
    os.environ['SDL_VIDEO_WINDOW_POS'] = "850, 100"
#pylint: disable=no-member
    pygame.init()
#pylint: enable=no-member
    screen = pygame.display.set_mode(
        (Settings.window_width, Settings.window_height))
    clock = pygame.time.Clock()

    cat = Cat()

    # main loop
    running = True
    while running:
        clock.tick(60)
        # event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        #draw
        screen.fill((255, 255, 255))
        screen.blit(cat.image, cat.rect)
        pygame.display.flip()


    # bye bye
#pylint: disable=no-member
    pygame.quit()
#pylint: enable=no-member
