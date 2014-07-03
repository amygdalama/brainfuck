import unittest

import brainfuck



class BrainfuckArrayTest(object):

    def setUp(self):
        self.array = brainfuck.BrainfuckArray()


class InvalidKeyTest(BrainfuckArrayTest, unittest.TestCase):

    def add_item(self, key, value):
        self.array[key] = value

    def test_non_int(self):
        self.assertRaises(TypeError, self.add_item, 'cat', 0)

    def test_too_high(self):
        self.assertRaises(IndexError, self.add_item, 30000, 0)

    def test_too_low(self):
        self.assertRaises(IndexError, self.add_item, -1, 0)


class BrainfuckTest(object):

    def setUp(self):
        self.bf = brainfuck.BrainfuckExec()


class IncrementPointerTest(BrainfuckTest, unittest.TestCase):

    def test(self):
        self.bf.increment_pointer()
        self.assertEqual(self.bf.get_pointer(), 1)


class DecrementPointerTest(BrainfuckTest, unittest.TestCase):

    def test(self):
        self.bf.increment_pointer()
        self.bf.decrement_pointer()
        self.assertEqual(self.bf.get_pointer(), 0)


class IncrementByteTest(BrainfuckTest, unittest.TestCase):

    def test(self):
        self.bf.increment_byte()
        self.assertEqual(self.bf.get_data()[0], 1)


class DecrementByteTest(BrainfuckTest, unittest.TestCase):

    def test(self):
        self.bf.decrement_byte()
        self.assertEqual(self.bf.get_data()[0], 255)


if __name__ == '__main__':
    unittest.main()