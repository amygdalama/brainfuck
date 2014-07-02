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


class BrainfuckArray(object):
    """Internal representation for the 30,000 byte brainfuck array,
    implemented like a sparse array.

    Attributes:
        data (dict): index -> value
        pointer (int): current index
    """

    def __init__(self, bytes=30000, bits=8):
        self._data = {}
        self._pointer = 0
        self._bytes = bytes
        self._bits = bits

    def __repr__(self):
        return repr(self._data)

    def get_pointer(self):
        return self._pointer

    def get_data(self):
        return self._data

    def get_bytes(self):
        return self._bytes

    def get_bits(self):
        return self._bits

    def increment_pointer(self):
        if self._pointer < 29999:
            self._pointer += 1
        else:
            raise IndexError("pointer out of bounds")

    def decrement_pointer(self):
        if self._pointer > 0:
            self._pointer -= 1
        else:
            raise IndexError("pointer out of bounds")

    def increment_byte(self):
        self._data[self._pointer] = (self._data.get(self._pointer, 0) + 1) % 256

    def decrement_byte(self):
        self._data[self._pointer] = (self._data.get(self._pointer, 0) - 1) % 256

    def output_byte(self):
        print self._data.get(self._pointer, 0)


def tokenize(source):
    """Tokenizes brainfuck source code.

    Args:
        source (string): brainfuck source code

    Returns:
        list: a list of valid brainfuck characters
    """
    return [ch for ch in source if ch in GRAMMAR]


if __name__ == '__main__':
    bf = BrainfuckArray()
    print bf
    bf.increment_byte()
    bf.increment_byte()
    bf.decrement_byte()
    bf.increment_pointer()
    bf.increment_byte()
    print bf
    print tokenize("""++++++++[>++++[>++>+++>+++>+<<<<-]
            >+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.
            +++.------.--------.>>+.>++.""")