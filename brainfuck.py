GRAMMAR = {
    '>' : 'INCREMENT_POINTER',
    '<' : 'DECREMENT_POINTER',
    '+' : 'INCREMENT_BYTE',
    '-' : 'DECREMENT_BYTE',
    '.' : 'OUTPUT_BYTE',
    ',' : 'INPUT_BYTE',
    '[' : 'JUMP_FORWARD',
    ']' : 'JUMP_BACKWARD'
}


class BrainfuckArray(dict):
    """An dictionary representing a sparse array of length 30,000
    with indices as keys, and integers representing 8-bit characters
    as values."""

    def __init__(self, bytes=30000, bits=8):
        self.bytes = bytes
        self.bits = bits
        super(BrainfuckArray, self).__init__()

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError("keys can only be ints from 0-29999")
        elif not 0 <= key < self.bytes:
            raise IndexError("keys can only be ints from 0-29999")
        elif not isinstance(value, int):
            raise TypeError("values must be ints")
        else:
            super(BrainfuckArray, self).__setitem__(key,
                    value % (2**self.bits))

    def __missing__(self, key):
        self.__setitem__(key, 0)
        return 0


class BrainfuckExec(object):
    """Execution of brainfuck interpreter.

    Attributes:
        data (dict): index -> value
        pointer (int): current index
    """

    def __init__(self):
        self._data = BrainfuckArray()
        self._pointer = 0

    def __repr__(self):
        return repr(self._data)

    def get_pointer(self):
        return self._pointer

    def get_data(self):
        return self._data

    def increment_pointer(self):
        self._pointer += 1

    def decrement_pointer(self):
        self._pointer -= 1

    def increment_byte(self):
        self._data[self._pointer] += 1

    def decrement_byte(self):
        self._data[self._pointer] -= 1

    def output_byte(self):
        print chr(self._data.get(self._pointer, 0))

    def input_byte(self):
        # I don't like this
        byte = raw_input()
        if len(byte) > 1:
            raise ValueError("only one character per byte")
        self._data[self._pointer] = ord(byte)


def tokenize(source):
    """Tokenizes brainfuck source code.

    Args:
        source (string): brainfuck source code

    Returns:
        list: a list of valid brainfuck characters
    """
    return [ch for ch in source if ch in GRAMMAR]


if __name__ == '__main__':
    bf = BrainfuckExec()
    print bf
    bf.increment_byte()
    bf.increment_byte()
    bf.decrement_byte()
    bf.increment_pointer()
    bf.increment_byte()
    print bf
    bf.input_byte()
    bf.output_byte()
    print tokenize("""++++++++[>++++[>++>+++>+++>+<<<<-]
            >+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.
            +++.------.--------.>>+.>++.""")