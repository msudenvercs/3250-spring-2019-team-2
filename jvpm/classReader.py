import unittest
from unittest.mock import mock_open, patch

# TODO OPcode unittest and reading methods


class ClassFile:
    def __init__(self):
        with open('test.class', 'rb') as binary_file:
            self.data = binary_file.read()

    def get_magic(self):
        magic = ""
        for i in range(4):
            magic += format(self.data[i], '02X')
        print(magic)
        return magic

    def get_minor(self):
        print(self.data[4] + self.data[5])
        return self.data[4] + self.data[5]

    def get_major(self):
        print(self.data[6] + self.data[7])
        return self.data[6] + self.data[7]


class TestClassFile(unittest.TestCase):
    def setUp(self):
        m = mock_open(read_data=b'\xCA\xFE\xBA\xBE\x00\x01\x02\x03')
        with patch(__name__ + '.open', m):
            self.cf = ClassFile()

    def test_magic(self):
        self.assertEqual(self.cf.get_magic(), 'CAFEBABE')

    def test_minor(self):
        self.assertEqual(self.cf.get_minor(), 1)

    def test_major(self):
        self.assertEqual(self.cf.get_major(), 5)


if __name__ == '__main__':
    cf = ClassFile()
