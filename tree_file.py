import os
from random import randint


class File(object):
    '''A file, based on an existing file on the hard drive.'''

    def __init__(self, path, parent):
        '''(File, unicode, Directory) -> NoneType
        Create a new File object from a specified path.
        '''
        self.path = path
        self.parent = parent
        self.size = os.path.getsize(path)
        # random color assigned to file; full 0-255 range not used so
        # black and white are not possible as tile colors
        self.color = (randint(10, 200), randint(10, 200), randint(10, 200))


class Directory(File):
    '''A directory, based on an existing directory on the hard drive.'''

    def __init__(self, path, parent):
        '''(Directory, unicode, Directory) -> NoneType
        Create a new Directory object from a specified path.
        '''
        File.__init__(self, path, parent)
        self.children = self.build_tree()
        # Define size of a directory as solely the size of its contents
        self.size = self.get_size()

    def build_tree(self):
        '''(Directory) -> List
        Build a tree of files and directories based on the contents of
        Directory, using File and Directory objects.
        '''

        children = []
        for filename in os.listdir(self.path):
            subitem = os.path.join(self.path, filename)
            if os.path.isdir(subitem):
                children.append(Directory(subitem, self))
            else:
                children.append(File(subitem, self))

        return children

    def get_size(self):
        '''(Directory) -> int
        Return the size of Directory in bytes.
        '''

        size = 0
        for subitem in self.children:
            if os.path.isdir(subitem.path):
                size += subitem.get_size()
            else:
                size += subitem.size
        return size
