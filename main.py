import os
import pickle
import datetime
from classes import Student, Session, TransactionRecord, StudentList
import prettyCLI as pretty
import field_validation as valid

# Constants
program_width = 80


def setup():
    """
    Setup function to checks if transaction data exists, otherwise create a
    new file. Returns either TransactionRecord object in pickled data or new
    TransactionRecord.
    """
    for (cdir, sdirs, fs) in os.walk("data"):
        if "records.pkl" not in fs:
            print("Records file not found... creating now.")
            with open("data\\records.pkl", "wb") as f:
                pass
        if "students.pkl" not in fs:
            print("Students file not found... creating now.")
            with open("data\\students.pkl", "wb") as f:
                pass
        break
    try:
        with open("data\\students.pkl", "rb") as f:
            active_students = pickle.load(f)  # Might add feature for more student lists later.
            print("Student list loaded successfully.")

        with open("data\\records.pkl", "rb") as f:
            active_record = pickle.load(f)  # Might add feature for more records later.
            print("Transaction record loaded successfully.")
    except EOFError:
        # If first time running, pickle file will be blank, so return new
        # empty student list and transaction record.
        print("New student list and transaction record created successfully.")
        return (StudentList(), TransactionRecord())
    else:
        return (active_students, active_record)


def main(student_list, transaction_record):
    """
    Main function. Accepts an active record and provides a nice walk through to
    faciliate recordkeeping actions.
    """
    pretty.print_marquee("Tutor Tracker v0.3")
    # TODO: Include last opened date?
    while True:
        print("What would you like to do? (type either option number or [keyword])")
        pretty.print_options("[Students] List", "[Record] of Transactions", "[Exit]")
        inp = input().lower()
        if inp == "1" or inp == "students":
            students_subroutine(student_list)
        elif inp == "2" or inp == "record":
            record_subroutine(student_list, transaction_record)
        elif inp == "3" or inp == "exit":
            save(student_list, transaction_record)
            input("Press enter to close program.\n")
            raise SystemExit
        else:
            print("Input not understood. Type either an option number or a [keyword].")


def save(student_list, transaction_record):
    """
    Save function. Dumps active student list and transaction record to pickle objects.
    """
    try:
        with open("data\\students.pkl", "wb") as f:
            pickle.dump(student_list, f)
            print("Student list saved successfully.")

        with open("data\\records.pkl", "wb") as f:
            pickle.dump(transaction_record, f)  # Might add feature for more records later.
            print("Transaction record saved successfully.")
    except FileNotFoundError:
        print("Data files corrupted. Hoo boy.")


def students_subroutine(student_list):
    """
    Subroutine for working with student list.
    """
    while True:
        pretty.print_bar(program_width)
        print("What would you like to do? (type either option number or [keyword])")
        pretty.print_options("[View] students", "[Add] student", "[Remove] student", "[Update] student info", "[Return]")
        inp = input().lower()

        if inp == "1" or inp == "view":
            start = end = None
            start_inp = input("First letter to start at? (Leave blank to start at beginning)\n")
            if start_inp and valid.is_letter(start_inp):
                start = start_inp
            else:
                start = "a"
            end_inp = input("First letter to end at? (Leave blank to go until end)\n")
            if end_inp and valid.is_letter(end_inp):
                end = end_inp
            else:
                end = "z"
            pretty.print_bar(program_width)
            try:
                student_list.print_table(start, end)
            except ValueError as e:
                print(e)
            input("Press enter to return.")

        elif inp == "2" or inp == "add":
            # Add new student to student list.
            # Basic flow: ask for all arguments in a try/except block listening
            # for KeyboardInterrupts. If any are raised, exit add subroutine
            # and continue looping. Otherwise, create a new Student with given
            # parameters and add to students list. Report success.
            print("Press CTRL+C at any time to cancel.")
            args = []
            try:
                # Got all of the arguments at once in a list and then just expanded them
                # into the parameters for new Student. Less readable, but more compact.
                args.append(input("First name?\n").strip(' '))
                args.append(input("Last name?\n").strip(' '))
                args.append(input("Phone number?\n"))
                args.append(input("Email address?\n"))
                args.append(input("Class or subject?\n"))
                args.append(input("Notes?\n"))
            except KeyboardInterrupt:
                pass
            else:
                pretty.print_bar(program_width)
                student_list.add(Student(*args))
                print("Student {0} added successfully.".format(args[0] + " " + args[1]))

        elif inp == "3" or inp == "remove":
            # Remove student by name from student list.
            # Basic flow: Ask for name of student to remove in try/except block
            # listening for KeyboardInterrupts. If any are raised, exit remove
            # subroutine and continue looping. Else use StudentList method to
            # remove student with given name and report success or failure
            # (returned by method).
            print("Press CTRL+C at any time to cancel.")
            try:
                name = input("Full name of student to remove?\n")
            except KeyboardInterrupt:
                pass
            else:
                pretty.print_bar(program_width)
                removed = student_list.remove(name)
                if removed:
                    print("Student {0} removed successfully.".format(name))
                else:
                    print("Student {0} not found (check spelling?).".format(name))

        elif inp == "4" or inp == "update":
            # Update student info in student list.
            # Basic flow: Ask for name of student to update in try/except block
            # listening for KeyboardInterrupts. If any are raised, exit remove
            # subroutine and continue looping. Else use StudentList method to
            # update student with given name. Ask for field and new value to update
            # to. Report success or failure (returned by method). Student field
            # updates have no type checking for values.
            print("Press CTRL+C at any time to cancel.")
            try:
                name = input("Full name of student to update?\n")
                print("Field to update? (type by [keyword])")
                pretty.print_options("[First] name", "[Last] name", "[Phone] number", "[Email] address", "[Subject] or class", "[Notes]")
                field = input().lower()
                newval = input("New value of field?\n")
            except KeyboardInterrupt:
                pass
            else:
                pretty.print_bar(program_width)
                #  This works because update method returns True or False for successful update or not.
                updated = student_list.update(name, field, newval)
                if updated:
                    #  A little magic in format to make update to field "first" or "last" show as "first name" or "last name."
                    print("Student {0} {1} successfully updated to {2}.".format(name, field + ("name" if field == "first" or name == "last" else ""), newval))
                else:
                    print("Student {0} or field {1} not found (check spelling?).".format(name, field))

        elif inp == "5" or inp == "return":
            # Finishes method and returns to place in main() stack loop.
            return
        else:
            pass


def record_subroutine(student_list, transaction_record):
    """
    Subroutine for working with transaction record.
    """
    while True:
        pretty.print_bar(program_width)
        print("What would you like to do? (type either option number or [keyword])")
        pretty.print_options("[View] record", "[Add] transaction", "[Remove] transaction", "[Update] transaction", "[Return]")
        inp = input().lower()

        if inp == "1" or inp == "view":
            try:
                pretty.print_bar(program_width)
                print("Enter starting date of transactions.")
                start = datetime_builder("date")
                print("Enter ending date of transactions.")
                end = datetime_builder("date")
            except KeyboardInterrupt:
                pass
            else:
                transaction_record.print_table(start, end)
                input("Press enter to return.")


        elif inp == "2" or inp == "add":
            # Add new transaction to transaction record.
            # Basic flow: ask for all arguments in a try/except block listening
            # for KeyboardInterrupts. If any are raised, exit add subroutine
            # and continue looping. Otherwise, verify types of all entered data
            # and create a new Session with given parameters. Add to transaction
            # record. Report success.
            print("Press CTRL+C at any time to cancel.")
            try:
                date = datetime_builder("date")
                name = input("Enter full name of student\n")
                student = student_list.get(name)
                if not student:
                    raise ValueError("Student {0} not found (check spelling?).".format(name))
                start = datetime_builder("time", "start")
                end = datetime_builder("time", "end")
                rate = float(input("Hourly rate charged?\n"))
                method = input("Payment method?\n")
                pmt_received = input("Payment receieved? (Yes/No)\n").lower()
                if pmt_received == "yes" or pmt_received == "y" or pmt_received == "1":
                    pmt_received = True
                elif pmt_received == "no" or pmt_received == "n" or pmt_received == "0":
                    pmt_received = False
                else:
                    raise ValueError("Payment received must be yes or no.")
                notes = input("Notes?\n")
            except ValueError as e:
                print(e)
            except KeyboardInterrupt:
                pass
            else:
                pretty.print_bar(program_width)
                s = Session(date, student, start, end, rate, method, pmt_received, notes)
                transaction_record.add(s)
                print("Transaction on date {0} with {1} from {2} to {3} added successfully.".format(s.date, s.student, pretty.time(s.start), pretty.time(s.end)))

        elif inp == "3" or inp == "remove":
            # Remove transaction by name and date from transaction record.
            # Basic flow: Ask for name of student to remove in try/except block
            # listening for KeyboardInterrupts. If any are raised, exit remove
            # subroutine and continue looping. Else use StudentList method to
            # remove student with given name and report success or failure
            # (returned by method).
            print("Press CTRL+C at any time to cancel.")
            try:
                name = input("Full name of student to remove?\n")
            except KeyboardInterrupt:
                pass
            else:
                pretty.print_bar(program_width)
                removed = student_list.remove(name)
                if removed:
                    print("Student {0} removed successfully.".format(name))
                else:
                    print("Student {0} not found (check spelling?).".format(name))

        elif inp == "4" or inp == "update":
            # Update session info in transaction record.
            # Basic flow: Ask for date of session to update in try/except block
            # listening for KeyboardInterrupts. If any are raised, exit update
            # subroutine and continue looping. Else, ask for what field to update
            # and direct flow to specific input type builders. This has to be
            # done because the Session data type stores hetergeneous objects, which
            # may or may not be enterable as a pure string (the Session class
            # does no type checking. Using the helper module, each branch determines
            # if its entered input is valid and then stores the data correctly
            # formed as newval, which is finally passed to the Session update
            # method. A new approach I'm trying is using specific error messages
            # to pass up what went wrong.
            print("Press CTRL+C at any time to cancel.")
            try:
                print("Date of session to update?")
                date_of_session = datetime_builder("date")
                name = input("Enter full name of student in session to update.\n")
                print("Field to update? (type by [keyword])")
                pretty.print_options("[Date]", "[Student]", "[Start] time", "[End] time", "[Rate]", "Payment [method]", "Payment [received]", "[Notes]")
                field = input().lower()
                if field == "date":
                    newval = datetime_builder("date")
                elif field == "start":
                    newval = datetime_builder("time", "start")
                elif field == "end":
                    newval = datetime_builder("time", "end")
                elif field == "rate":
                    inp = input("New value of field?\n")
                    if valid.is_rate(inp):
                        newval = float(inp)
                    else:
                        raise ValueError("Invalid entry: rate must be a number.")
                elif field == "received":
                    inp = input("New value of field?\n")
                    if valid.is_bool(inp):
                        newval = True if inp in ["yes", "y", "1"] else False
                    else:
                        raise ValueError("Invalid entry: payment received must be either yes or no")
                else:
                    newval = input("New value of field?\n")
            except ValueError as e:
                print(e)
            except KeyboardInterrupt:
                pass
            else:
                pretty.print_bar(program_width)
                #  This works because update method returns True or False for successful update or not.
                updated = transaction_record.update(date_of_session, name, field, newval)
                if updated:
                    #  A little magic in format to make update to field "first" or "last" show as "first name" or "last name."
                    print("Field {0} in session on {1} with {2} successfully updated to {3}.".format(field, pretty.date(date_of_session), name, newval))
                else:
                    print("Session on {0} with {1} or field {2} not found (check spelling?).".format(pretty.date(date_of_session), name, field))

        elif inp == "5" or inp == "return":
            # Finishes method and returns to place in main() stack loop.
            return
        else:
            pass


def datetime_builder(output, of=None):
    """Builds datetime.date and datetime.time objects."""
    if output == "date":
        while True:
            date = input("Enter date in MM/DD/YYYY format (leave blank for today)\n")
            if not date:
                date_obj = datetime.date.today()
                return date_obj
            else:
                try:
                    date = date.split('/')
                    date_obj = datetime.date(int(date[2]), int(date[0]), int(date[1]))
                    return date_obj
                except IndexError:
                    print("Invalid entry (check format?)")
                except ValueError as e:
                    print("Invalid entry ({})".format(e))
    if output == "time":
        h = m = p = None
        while h is None or m is None or p is None:
            if h is None:
                try:
                    h = int(input("{0} hour?\n".format(of.capitalize())))
                    assert 1 <= h <= 12
                except (ValueError, AssertionError):
                    print("Invalid entry (hour must be range 1-12).")
                    continue
            if m is None:
                try:
                    m = input("{0} minute? (default :00)\n".format(of.capitalize()))
                    if m == "":
                        m = 0
                    m = int(m)
                    assert 0 <= m <= 59
                except (ValueError, AssertionError):
                    print("Invalid entry (minute must be range 0-59 or blank).")
                    m = None
                    continue
            if p is None:
                try:
                    p = input("AM or PM? (default PM)\n")
                    assert p.upper() in ["AM", "A", "PM", "P", ""]
                    if p.upper() in ["PM", "P", ""] and h != 12:
                        h += 12
                    if p.upper() in ["AM", "A"] and h == 12:
                        h -= 12
                except (ValueError, AssertionError):
                    print("Invalid entry (must be either AM, PM or blank).")
                    p = None
                    continue
        return datetime.time(h, m)



if __name__ == "__main__":
    data = setup()
    main(*data)
