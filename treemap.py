import pygame
import Tkinter
from tkFileDialog import askdirectory
from tree_file import *
from tile import *
import sys


def get_directory():
    '''() -> unicode
    Return the path of a user-chosen directory. The directory and all of its
    contents must be accessible by Python; i.e. an attempt to access its
    contents through Python will not be rejected by the OS.
    '''

    root = Tkinter.Tk()
    dir_path = askdirectory(title='Choose a directory that does not have' + \
                            ' special access restrictions.', initialdir='.')
    root.destroy()
    if not dir_path:
        sys.exit('No directory was selected.')
    else:
        return dir_path

if __name__ == '__main__':

    dir_path = get_directory()

    pygame.init()
    screen_size = (800, 600)
    screen = pygame.display.set_mode(screen_size)

    directory = Directory(dir_path, os.path.dirname(dir_path))
    draw_tiles(screen, 0, 0, 800, 580, directory)
    blit_path(screen, dir_path)

    running = True
    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
        # Click area is anywhere in the bottom black box in the window
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and \
             event.pos[1] >= 580:
            # Open the directory in a new window
            os.startfile(dir_path)
        pygame.display.flip()
    # Upon closing, pygame window may freeze or not close without this line
    pygame.quit()
