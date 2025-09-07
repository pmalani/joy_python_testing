import unittest
from unittest.mock import Mock

from pfs_file import Folder

class FolderSizeMockTest(unittest.TestCase):
    def test_folder_size(self):
        f1 = Mock()
        f1.size = 5
        f2 = Mock()
        f2.size = 10
        f3 = Folder.from_files(f1, f2)
        self.assertEqual(f3.size, 15)

if __name__ == '__main__':
    unittest.main()
