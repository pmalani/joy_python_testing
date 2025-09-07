import unittest
from unittest.mock import Mock

from pfs_file import File, Shortcut

class ShortcutOpenTest(unittest.TestCase):
    def test_open(self):
        # given
        f1 = File.of_size(5)
        f1.open = Mock()
        s1 = Shortcut(f1)

        # when
        s1.open()

        # then
        f1.open.assert_called_once()

if __name__ == '__main__':
    unittest.main()
