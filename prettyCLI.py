"""
Helper module to prettify some common CLI printing tasks.
"""

from init import PROGRAM_WIDTH, BORDER_SYM, ALERT_SYM


def print_bar(length, sym=BORDER_SYM):
    """Creates a bar of length length with symbol sym."""
    print(sym * length)


def print_marquee(text, height=3, sym=BORDER_SYM):
    """Prints a pretty marquee with symbol sym around text."""
    print_bar(PROGRAM_WIDTH, sym)
    print((sym + (" " * (PROGRAM_WIDTH - 2)) + sym + "\n") * (height // 2), end="")
    print(sym + (" " * (((PROGRAM_WIDTH - 2) - len(text)) // 2)) + (" " if len(text) % 2 != 0 else "") +
          text + (" " * (((PROGRAM_WIDTH - 2) - len(text)) // 2)) + sym)
    print((sym + (" " * (PROGRAM_WIDTH - 2)) + sym + "\n") * (height // 2), end="")
    print_bar(PROGRAM_WIDTH, sym)


def print_options(*items):
    """Prints a pretty list of options, with as many string arguments as you like
    passed in."""
    for (i, v) in enumerate(items):
        print("{0}.    {1}".format(i + 1, v))
    print()


def print_table(heads, objects):
    """Prints a table of objects.

    * heads must be given as a list of tuples, with the first element being the
    heading text, and the second element being the desired column span.
    The sum of all of the desired column spans may not exceed PROGRAM_WIDTH.

    * objects must be given as a list of objects. Each object must have a dict
    whose keys match heading texts from heads *exactly* (don't worry if this means
    your elements in heads will be lowercase - they will be capitalized automatically).

    Example:
    heads = [("first", 10), ("last", 10), ("email", 15)]
    objects = [Person1, Person2]
    Person1.__dict__ = \{"first": "John", "last": "Doe", "email": "johndoe@gmail.com"\}
    """
    # Print heads
    for h in heads:
        # Remember each h has both its text in h[0] and its desired length in h[1].
        trimmed_head = h[0][0:(h[1] - 2)] + ("." if len(h[0]) > (h[1] - 1) else "")
        # Does nothing if column span is greater than heading length + 2 spaces,
        # but slices and abbreviates with "." if not.
        print(trimmed_head.capitalize() + (" " * (h[1] - len(trimmed_head))), end="")
    print()
    print_bar(PROGRAM_WIDTH)
    # Print student info
    for s in objects:
        for h in heads:
            info = s.__dict__[h[0]]
            # The trimmed info will be a slice plus a dash if the length of the original info
            # was greater than the column span.
            trimmed_info = info[0:(h[1] - 2)] + ("-" if len(info) > (h[1] - 2) else "")
            print(trimmed_info + (" " * (h[1] - len(trimmed_info))), end="")
        print()


def print_table(transaction_record, by_student=False, in_range=False, start=datetime.date.min, end=datetime.date.max, student=None):
    """
    Prints transaction_record. If by_student is True, prints only transactions
    where session.student is student. If in_range is True, prints only
    transactions in between start and end. Both may be True to increase
    specificity as desired.
    """
    if len(transaction_record.transactions) == 0:
        print("No transactions on record.")
        return
    # Get date range of transaction to print
    start_ix = end_ix = None
    if in_range:
        if end < start:
            raise ValueError("Invalid start/end pair.")
        for i, s in enumerate(transaction_record.transactions):
            if s.date >= start:  # Start printing at the first name after our start point
                start_ix = i
                break
        if start_ix is None:
            start_ix = len(transaction_record.transactions)
        for i, s in enumerate(transaction_record.transactions):
            if s.date > end:  # Stop printing at one before first name after end
                end_ix = i - 1
                break
        if end_ix is None:
            end_ix = len(transaction_record.transactions)
    to_print = [s in transaction_record[start_ix:end_ix] if s.student == student]
    range_of_transactions = transaction_record.transactions[start_ix:end_ix]
    to_print = []
    if by_student:
        for s in range_of_transactions:
            if s.student == student:
                to_print.append(s)
    else:
        to_print
    # Print head
    col_spans = [11, 20, 10, 10, 10, 7, 9, 8, 10, 25]
    heads = ["date", "student", "start", "end", "duration", "rate", "charge", "method", "received", "notes"]
    # Have to do it this way because dicts are unsorted :(
    for session in to_print:  # Actually only need the first one
        assert len(col_spans) == len(session.__dict__)  # This is for you!
        for head, span in zip(heads, col_spans):  # Zips each
            # heading and span length as a tuple and then unpacks it into the for loop
            # so they can be accessed together exclusively... I'm clever, see!
            trimmed_head = head[0:(span - 2)] + ("." if len(head) > (span - 1) else "")
            # Does nothing if column span is greater than heading length + 2 spaces,
            # but slices and abbreviates with "." if not.
            print(trimmed_head.capitalize() + (" " * (span - len(trimmed_head))), end="")
        break
    print()
    pretty.print_bar(PROGRAM_WIDTH)
    # Print student info
    for session in to_print:
        for head, span in zip(heads, col_spans):
            if head == "start" or head == "end":
                info = pretty.time(session.__dict__[head])
            elif head == "duration":
                info = str(session.__dict__[head]) + (" hour" if session.__dict__[head] == 1 else " hours")
            else:
                info = str(session.__dict__[head])
            # The trimmed info will be a slice plus a dash if the length of the original info
            # was greater than the column span.
            trimmed_info = info[0:(span - 2)] + ("-" if len(info) > (span - 2) else "")
            print(trimmed_info + (" " * (span - len(trimmed_info))), end="")
        print()


def time(datetime_obj):
    """Formats datetime.time or datetime.datetime objects into 12 hour time."""
    return datetime_obj.strftime("%I:%M %p")


def date(date_obj):
    """Formats datetime.date objects into MM/DD/YYYY syntax."""
    return date_obj.strftime("%m/%d/%Y")
