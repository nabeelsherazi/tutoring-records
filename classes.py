import datetime
import prettyCLI as pretty

# TODO thoughts:
# 1) implement printing of student list and transaction records inside of class
# itself, like print_self function.
# 2) Make all object creations take strings only, so that main function only
# does CLI interfacing. All object creation should be handled inside of the class
# when it's passed a string. I should be able to pass Session a string for
# session date and have it create the datetime.date object within itself.


class Student:
    """
    Defines student type.

    Must provide (in order): first name, last name, phone nummber,
    email address, subject studying, and any notes, all as strings.
    """
    def __init__(self, fname, lname, pnum, eaddr, subj, notes):
        self.first = fname
        self.last = lname
        self.phone = pnum
        self.email = eaddr
        self.subject = subj
        self.notes = notes

    def __str__(self):
        return "{} {}".format(self.first, self.last)

    def __lt__(self, other):
        return self.first < other.first

    def __le__(self, other):
        return self.first <= other.first

    def __gt__(self, other):
        return self.first > other.first

    def __ge__(self, other):
        return self.first >= other.first

    def __eq__(self, other):
        return self.first == other.first

    def __ne__(self, other):
        return self.first != other.first

    def update(self, field, newval):
        """Updates student field, specified as string, to newval."""
        try:
            self.__dict__[field]
        except KeyError:
            return False
        else:
            self.__dict__[field] = newval
            return True


class Session:
    """
    Defines tutoring session data type.

    Must provide:
    date -> datetime.date object
    start_time, end_time -> datetime.time objects
    rate -> float
    pmt_method -> string
    pmt_recieved -> boolean
    notes -> string
    """
    def __init__(self, date, student, start_time, end_time, rate, pmt_method, pmt_recieved, notes):
        #  Variable assignments
        self.date = date
        self.student = student
        self.start = datetime.datetime.combine(date, start_time)
        self.end = datetime.datetime.combine(date, end_time)
        self.rate = rate
        self.method = pmt_method.upper()
        self.recieved = pmt_recieved
        self.notes = notes
        #  Subtracting two datetime.datetime objects creates a new
        #  datetime.timedelta, of which we take the number of seconds attribute
        #  and floor divide by 3600 to get the number of billable hours in the
        #  session.
        self.duration = ((self.end - self.start).seconds) // 3600
        self.charge = self.duration * self.rate

    def __str__(self):
        return "Session on {0} with {1} from {2} to {3} ({4} hours @ ${5}/hr), total charges ${6} by {7}, {8}. Notes: {9} ".format(str(self.date), str(self.student), str(self.start), str(self.end), self.duration, self.rate, self.charge, self.method, "payment recieved" if self.received else "payment NOT received", self.notes)

    def __lt__(self, other):
        return self.start < other.start

    def __le__(self, other):
        return self.start <= other.start

    def __gt__(self, other):
        return self.start > other.start

    def __ge__(self, other):
        return self.start >= other.start

    def __eq__(self, other):
        return self.start == other.start

    def __ne__(self, other):
        return self.start != other.start

    def update(self, field, newval):
        """Updates session field, specified as string, to newval."""
        try:
            self.__dict__[field]
        except KeyError:
            return False
        else:
            self.__dict__[field] = newval
            return True


class TransactionRecord:
    """
    Defines record of transactions data type.

    Transactions are given as session object types and are stored as a list.
    """
    def __init__(self):
        self.transactions = []

    def __str__(self):
        return "{0} transactions on record.".format(len(self.transactions))

    def add(self, session):
        """Adds a new session to transaction record. Must supply Session object."""
        self.transactions.append(session)
        self.transactions.sort()

    def remove(self, date, name):
        """Removes a session specified by date and student name. Provide full
        student name a a single string, method will handle splitting."""
        try:
            fname, lname = name.split()[0], name.split()[1]
        except IndexError:
            return False
        for (i, s) in enumerate(self.transactions):
            if s.date == date and s.student.first == fname and s.student.last == lname:
                self.transactions.pop(i)
                return True
        return False

    def update(self, date, name, field, newval):
        """Updates a session's info specified by date and student name. Provide full
        student name a a single string, method will handle splitting."""
        try:
            fname, lname = name.split()[0], name.split()[1]
        except IndexError:
            return False
        for (i, s) in enumerate(self.transactions):
            if s.date == date and s.student.first == fname and s.student.last == lname:
                updated = s.update(field, newval)
                self.transactions.sort()
                return updated
        return False

    def get(self, date, name):
        """Returns a Session object specified by date and student name. Provide full
        student name a a single string, method will handle splitting."""
        try:
            fname, lname = name.split()[0], name.split()[1]
        except IndexError:
            return False
        for (i, s) in enumerate(self.transactions):
            if s.date == date and s.student.first == fname and s.student.last == lname:
                return s
        return False


class StudentList:
    """
    Defines list of students data type.

    Students are given as student object types and are stored as a list.
    """
    def __init__(self):
        self.students = []

    def add(self, student):
        """Adds a new student to student list. Must supply student object."""
        self.students.append(student)
        self.students.sort()

    def remove(self, name):
        """Removes a student specified by student name. Provide full
        student name a a single string, method will handle splitting."""
        try:
            fname, lname = name.split()[0], name.split()[1]
        except IndexError:
            return False
        for (i, s) in enumerate(self.students):
            if s.first == fname and s.last == lname:
                self.students.pop(i)
                return True
        return False

    def update(self, name, field, newval):
        """Updates a student's information, specified by name. Provide full
        student name a a single string, method will handle splitting."""
        try:
            fname, lname = name.split()[0], name.split()[1]
        except IndexError:
            return False
        for (i, s) in enumerate(self.students):
            if s.first == fname and s.last == lname:
                updated = s.update(field, newval)
                self.students.sort()
                return updated
        return False

    def get(self, name):
        """Returns a student object, specified by name. Provide full
        student name a a single string, method will handle splitting."""
        try:
            fname, lname = name.split()[0], name.split()[1]
        except IndexError:
            return False
        for (i, s) in enumerate(self.students):
            if s.first == fname and s.last == lname:
                return s
        return False

    def print_table(start="a", end="z"):
        """ Prints self """
        # Get subsection to print
        start, end = start.lower(), end.lower()
        if end < start:
            raise ValueError
        for i, s in enumerate(self.students):
            if s.first[0].lower() >= start:  # Start printing at the first name after our start point
                start_ix = i
                break
        for i, s in enumerate(self.students):
            if s.first[0].lower() > end:  # Stop printing at one before first name after end
                end_ix = i - 1
        to_print = self.students[start_ix:end_ix]

        # Print head
        col_spans = [10, 20, 10, 10, 5, 5, 5, 15]
        for student in to_print:  # Actually only need the first one
            for head, span in zip(student.__dict__, col_spans):
                assert len(col_spans) == len(student.__dict__)  # This is for you!
                # Remember each h has both its text in h[0] and its desired length in h[1].
                trimmed_head = head[0:(span - 2)] + ("." if len(head) > (span - 1) else "")
                # Does nothing if column span is greater than heading length + 2 spaces,
                # but slices and abbreviates with "." if not.
                print(trimmed_head.capitalize() + (" " * (span - len(trimmed_head))), end="")
            break
        print()
        pretty.print_bar(80)

        # Print student info
        for student in to_print:
            for head, span in zip(student.__dict__, col_spans):
                info = student.__dict__[head]
                # The trimmed info will be a slice plus a dash if the length of the original info
                # was greater than the column span.
                trimmed_info = info[0:(span - 2)] + ("-" if len(info) > (span - 2) else "")
                print(trimmed_info + (" " * (span - len(trimmed_info))), end="")
            print()
