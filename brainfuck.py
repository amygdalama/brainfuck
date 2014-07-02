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

    def __init__(self):
        self.data = {}
        self.pointer = 0

    def __repr__(self):
        return repr(self.data)

    def increment_pointer(self):
        if self.pointer < 30000:
            self.pointer += 1
        else:
            raise IndexError("pointer out of bounds")

    def decrement_pointer(self):
        if self.pointer > 0:
            self.pointer -= 1
        else:
            raise IndexError("pointer out of bounds")

    def increment_byte(self):
        self.data[self.pointer] = self.data.get(self.pointer, 0) + 1 % 256

    def decrement_byte(self):
        self.data[self.pointer] = self.data.get(self.pointer, 0) - 1 % 256

    def output_byte(self):
        print self.data.get(self.pointer, 0)


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