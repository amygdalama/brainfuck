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


def tokenize(source):
    """Tokenizes brainfuck source code.

    Args:
        source (string): brainfuck source code

    Returns:
        list: a list of valid brainfuck characters
    """
    return [ch for ch in source if ch in GRAMMAR]


if __name__ == '__main__':
    print tokenize("""++++++++[>++++[>++>+++>+++>+<<<<-]
            >+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.
            +++.------.--------.>>+.>++.""")