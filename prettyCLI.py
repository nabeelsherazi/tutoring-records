def bar(length, sym="="):
    """Creates a bar of length length with symbol sym."""
    print(sym * length)


def marquee(text, height=3, sym="="):
    """Prints a pretty marquee with symbol sym around text."""
    bar(80, sym)
    print((sym + (" " * 79) + sym + "\n") * (height // 2), end="")
    print(sym + (" " * ((79 - len(text)) // 2)) + (" " if len(text) % 2 == 0 else "") +
          text + (" " * ((79 - len(text)) // 2)) + sym)
    print((sym + (" " * 79) + sym + "\n") * (height // 2), end="")
    bar(80, sym)


def options(*args):
    """ Prints a pretty list of options, with a list of args passed in as tuples
    containing action and its corresponding control word."""
    for (i, v) in enumerate(args):
        print("{0}.    {1} (type \"{2}\")".format(i + 1, v)
        
