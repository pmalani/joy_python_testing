class File:

    @classmethod
    def of_size(cls, size):
        ret = cls()
        ret.size = size
        return ret

    def open(self):
        print("opening file")

class Folder(File):

    def __init__(self):
        self.files = []

    @classmethod
    def from_files(cls, *files):
        ret = cls()
        ret.add_files(*files)
        return ret

    @property
    def size(self):
        return sum(file.size for file in self.files)

    def add_files(self, *files):
        for f in files:
            self.files.append(f)

class Shortcut(File):

    def __init__(self, file):
        self.file = file

    def open(self):
        print("opening shortcut")
        self.file.open()