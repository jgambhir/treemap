import pygame
from tree_file import *


def draw_tiles(screen, x, y, width, height, directory):
    '''(Surface, int, int, int, int, Directory) -> NoneType
    Draw a treemap on a pygame surface showing the relative sizes of files and
    sub-directories within a given directory. Files are depicted as colored
    rectangles, and directories are a white rectangular outline around the
    files they contain.
    '''

    sub_x = x
    sub_y = y
    for child in directory.children:
        try:
            # values are turned into floats because integer division
            # can lead to undesired results
            size_ratio = float(child.size) / float(directory.size)
        # Division by zero does not occur in most cases, but will pop up
        # with certain directories.
        except ZeroDivisionError:
            size_ratio = 0
        w = width * size_ratio
        h = height * size_ratio
        if isinstance(child, Directory):
            if width > height:
                draw_tiles(screen, sub_x, sub_y, w, height,\
                           child)
                # move starting point for next rectangle over to the right
                # of the rectangle just drawn
                sub_x += w
            else:
                draw_tiles(screen, sub_x, sub_y, width, h,\
                           child)
                # move starting point for next rectangle over to under the
                # rectangle just drawn
                sub_y += h
        else:  # child is a file to be drawn and coloured in, not a directory
            if width > height:
                pygame.draw.rect(screen, child.color, \
                                 (sub_x, sub_y, w, height))
                sub_x += w
            else:
                pygame.draw.rect(screen, child.color, \
                                 (sub_x, sub_y, width, h))
                sub_y += h
        # draw a white rectangular outline representing the directory
        pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height), 1)


def blit_path(screen, directory_path):
    '''(Surface, unicode) -> NoneType
    Blit a given directory path onto a pygame surface.
    '''

    white = (255, 255, 255)
    font = pygame.font.Font(None, 20)
    text = directory_path + '  [Click to open directory].'
    text_surface = font.render(text, 1, white)
    text_position = (0, screen.get_size()[1] - font.get_linesize())
    screen.blit(text_surface, text_position)
