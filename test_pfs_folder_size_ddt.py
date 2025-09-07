import unittest
from ddt import ddt, data, unpack
from pfs_file import File, Folder

@ddt
class FolderSizeDdtTest(unittest.TestCase):
    @data((1, 2, 3), (0, 1, 1), (-1, 1, 0))
    @unpack
    def test_folder_size(self, f1_size, f2_size, expected_folder_size):
        f1 = File.of_size(f1_size)
        f2 = File.of_size(f2_size)
        f3 = Folder.from_files(f1, f2)

        self.assertEqual(f3.size, expected_folder_size)

if __name__ == '__main__':
    unittest.main()
