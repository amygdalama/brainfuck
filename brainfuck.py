import sys


class BrainfuckError(SyntaxError): pass


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


class BrainfuckInterpreter(object):
    """Execution of brainfuck interpreter.

    Attributes:
        data (dict): index -> value
        pointer (int): current index
    """

    def __init__(self):
        self._data = BrainfuckArray()
        self._pointer = 0
        self._grammar = {
            '>' : 'INCREMENT_POINTER',
            '<' : 'DECREMENT_POINTER',
            '+' : 'INCREMENT_BYTE',
            '-' : 'DECREMENT_BYTE',
            '.' : 'OUTPUT_BYTE',
            ',' : 'INPUT_BYTE',
            '[' : 'JUMP_FORWARD',
            ']' : 'JUMP_BACKWARD'
        }
        self._exec_tokens = {
            'INCREMENT_POINTER' : self.increment_pointer,
            'DECREMENT_POINTER' : self.decrement_pointer,
            'INCREMENT_BYTE' : self.increment_byte,
            'DECREMENT_BYTE' : self.decrement_byte,
            'OUTPUT_BYTE' : self.output_byte,
            'INPUT_BYTE' : self.input_byte,
            'JUMP_FORWARD' : None,
            'JUMP_BACKWARD' : None
        }

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
        sys.stdout.write(chr(self._data.get(self._pointer, 0)))

    def input_byte(self):
        # I don't like this
        byte = raw_input()
        if len(byte) > 1:
            raise ValueError("only one character per byte")
        self._data[self._pointer] = ord(byte)

    def tokenize(self, source):
        """Tokenizes brainfuck source code."""
        return [self._grammar[ch] for ch in source if ch in self._grammar]

    def parse(self, tokens):
        """Parse the brainfuck tokens.

        Args:
            tokens (list): tokens, output from tokenize function

        Returns:
            dict: mapping the indexes of [ to their corresponding ]
        """
        loop_map = {}
        stack = []
        for i, token in enumerate(tokens):
            if token == 'JUMP_FORWARD':
                stack.append(i)
            elif token == 'JUMP_BACKWARD':
                if stack:
                    beginning_index = stack.pop()
                    loop_map[beginning_index] = i
                else:
                    raise BrainfuckError("unexpected ]")
        if stack:
            raise BrainfuckError("missing ]")
        return loop_map

    def execute(self, tokens, loop_map):
        program_loc = 0
        stack = []
        while program_loc < len(tokens):
            token = tokens[program_loc]
            if token == 'JUMP_FORWARD':
                if self._data[self._pointer] == 0:
                    program_loc = loop_map[program_loc]
                else:
                    stack.append(program_loc)
            elif token == 'JUMP_BACKWARD':
                program_loc = stack.pop() - 1
            elif token in tokens:
                self._exec_tokens[token]()
            else:
                raise BrainfuckError("invalid token")
            program_loc += 1


if __name__ == '__main__':
    source = """++++++++[>++++[>++>+++>+++>+<<<<-]
            >+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.
            +++.------.--------.>>+.>++."""
    bf = BrainfuckInterpreter()
    tokens = bf.tokenize(source)
    loop_map = bf.parse(tokens)
    bf.execute(tokens, loop_map)