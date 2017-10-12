import datetime


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
        self.note = notes

    def __str__(self):
        return "{} {}".format(self.first, self.last)

    def update(self, field, newval):
        """Updates student field, specified as string, to newval."""
        try:
            self.__dict__[field]
        except KeyError:
            return False
        else:
            self.__dict__[field] = newval


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
        return "Session on {0} with {1} from {2} to {3} ({4} hours @ ${5}/hr), "
               "total charges ${6} by {7}, {8}. Notes: {9} ".format(str(self.date),
               str(self.student), str(self.start), str(self.end), self.duration,
               self.rate, self.charge, self.method, "payment recieved" if self.received
               else "payment NOT received", self.notes)

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


class TransactionRecord:
    """
    Defines record of transactions data type.

    Transactions are given as session object types and are stored as a list.
    """
    def __init__(self):
        self.transactions = []

    def __str__(self):
        return "{0} transactions on record.".format(len(self.transactions))

    def add(session):
        """Adds a new session to transaction record. Must supply Session object."""
        self.transactions.append(session)
        self.transactions.sort()

    def remove(date, name):
        """Removes a session specified by date and student name. Provide full
        student name a a single string, method will handle splitting."""
        fname, lname = name.split()[0], name.split()[1]
        for (i, s) in enumerate(self.transactions):
            if s.date == date and s.student.first == fname and s.student.last = lname:
                self.transactions.pop(i)
                return True
        return False


class StudentList:
    """
    Defines list of students data type.

    Students are given as student object types and are stored as a list.
    """
    def __init__(self):
        self.students = []

    def add(student):
        """Adds a new student to student list. Must supply student object."""
        self.students.append(student)

    def remove(name):
        """Removes a student specified by student name. Provide full
        student name a a single string, method will handle splitting."""
        fname, lname = name.split()[0], name.split()[1]
        for (i, s) in enumerate(self.students):
            if s.first == fname and s.last = lname:
                self.students.pop(i)
                return True
        return False
