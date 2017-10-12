def bar(length, sym="="):
    """Creates a bar of length length with symbol sym."""
    print(sym * length)


def marquee(text, height=3, sym="="):
    """Prints a pretty marquee with symbol sym around text."""
    bar(80, sym)
    print((sym + (" " * 78) + sym + "\n") * (height // 2), end="")
    print(sym + (" " * ((78 - len(text)) // 2)) + (" " if len(text) % 2 != 0 else "") +
          text + (" " * ((78 - len(text)) // 2)) + sym)
    print((sym + (" " * 78) + sym + "\n") * (height // 2), end="")
    bar(80, sym)


def options(*items):
    """Prints a pretty list of options, with as many string arguments as you like
    passed in."""
    for (i, v) in enumerate(items):
        print("{0}.    {1}".format(i + 1, v))
    print()


def table(heads, objects):
    """Prints a table of objects.

    * heads must be given as a list of tuples, with the first element being the
    heading text, and the second element being the desired column span.
    The sum of all of the desired column spans may not exceed 80.

    * objects must be given as a list of objects. Each object must have a dict
    whose keys match heading texts from heads *exactly* (don't worry if this means
    your elements in heads will be lowercase - they will be capitalized automatically).

    Example:
    heads = [("first", 10), ("last", 10), ("email", 15)]
    objects = [Person1, Person2]
    Person1.__dict__ = \{"first": "John", "last": "Doe", "email": "johndoe@gmail.com"\}
    """
    # Check column span sum
    if sum(h[1] for h in heads) > 80:
        print("Error: cannot print table (heading size exceeds 80 chars).")
    # Print heads
    for h in heads:
        # Remember each h has both its text in h[0] and its desired length in h[1].
        trimmed_head = h[0][0:(h[1] - 2)] + ("." if len(h[0]) >= (h[1] - 2) else "")
        # Does nothing if desired size is greater than heading length + 2 spaces,
        # but slices and abbreviates with "." if not.
        print(trimmed_head.capitalize() + (" " * (h[1] - len(trimmed_head))), end="")
    print()
    bar(80)
    # Print student info
    for s in objects:
        for h in heads:
            info = s.__dict__[h[0]]
            trimmed_info = info[0:(h[1] - 2)] + ("-" if len(info) >= (h[1] - 2) else "")
            print(trimmed_info + (" " * (h[1] - len(trimmed_info))), end="")
        print()
