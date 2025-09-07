import unittest
from pfs_file import File, Folder

class FolderSizeTest(unittest.TestCase):
    def test_empty_folder(self):
        f = Folder()

        self.assertEqual(f.size, 0)

    def test_folder_with_one_file(self):
        f1 = File.of_size(5)
        self.assertEqual(f1.size, 5)

        folder1 = Folder.from_files(f1)

        self.assertEqual(folder1.size, 5)

    def test_simple_folder_size(self):  # add assertion here
        f1 = File.of_size(5)
        f2 = File.of_size(10)
        self.assertEqual(f1.size, 5)
        self.assertEqual(f2.size, 10)
        f3 = Folder()
        f3.add_files(f1, f2)

        self.assertEqual(f3.size, 15)

    def test_nested_folder_size(self):
        f1 = File.of_size(5)
        f2 = File.of_size(10)
        f3 = Folder.from_files(f1, f2)
        f4 = File.of_size(15)
        f5 = Folder.from_files(f3, f4)

        self.assertEqual(f5.size, 30)

if __name__ == '__main__':
    unittest.main()
