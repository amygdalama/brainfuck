import unittest

import brainfuck


class BrainfuckTest(object):
    def setUp(self):
        self.bf = brainfuck.BrainfuckExec()


class IncrementPointerTest(BrainfuckTest, unittest.TestCase):

    def test(self):
        self.bf.increment_pointer()
        self.assertEqual(self.bf.get_pointer(), 1)

    def test_out_of_bounds(self):
        self.bf._pointer = 29999
        self.assertRaises(IndexError, self.bf.increment_pointer)


class DecrementPointerTest(BrainfuckTest, unittest.TestCase):

    def test(self):
        self.bf.increment_pointer()
        self.bf.decrement_pointer()
        self.assertEqual(self.bf.get_pointer(), 0)

    def test_out_of_bounds(self):
        self.assertRaises(IndexError, self.bf.decrement_pointer)


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