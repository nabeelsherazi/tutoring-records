import os
import pickle
from classes import Student, Session, TransactionRecord, StudentList
import prettyCLI as pretty


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
    pretty.marquee("Welcome to Tutor Stuff (name pending)")
    while True:
        print("What would you like to do? (type either option number or [keyword])")
        pretty.options("[Students] List", "Transaction [Record]", "[Exit]")
        inp = input().lower()
        if inp == "1" or inp == "students":
            students_subroutine(student_list)
        elif inp == "2" or inp == "record":
            # TODO: Implement this shit.
            #  record_subroutine(transaction_record)
            print("Record intent in development.")
        elif inp == "3" or inp == "exit":
            #  Remember to do file saving stuff here
            raise SystemExit
        else:
            print("Input not understood. Type either an option number or a [keyword].")


def students_subroutine(student_list):
    """
    Subroutine for working with student list.
    """
    while True:
        pretty.bar(80)
        print("What would you like to do? (type either option number or [keyword])")
        pretty.options("[View] students", "[Add] student", "[Remove] student", "[Update] student info", "[Return]")
        inp = input().lower()

        if inp == "1" or inp == "view":
            pretty.bar(80)
            #  TODO: add spacing in phone desired length to avoid cutoff
            # Since with dashes phone #s are exactly 12, the function
            # will subtract 2 and abbreviate to create a space.
            pretty.table([("first", 10), ("last", 10), ("phone", 12), ("email", 20), ("subject", 15), ("notes", 13)], student_list.students)
            input("Press enter to return.")

        if inp == "2" or inp == "add":
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
                args.append(input("First name?\n"))
                args.append(input("Last name?\n"))
                args.append(input("Phone number?\n"))
                args.append(input("Email address?\n"))
                args.append(input("Class or subject?\n"))
                args.append(input("Notes?\n"))
            except KeyboardInterrupt:
                pass
            else:
                pretty.bar(80)
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
                pretty.bar(80)
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
                pretty.options("[First] name", "[Last] name", "[Phone] number", "[Email] address", "[Subject] or class", "[Notes]")
                field = input().lower()
                newval = input("New value of field?\n")
            except KeyboardInterrupt:
                pass
            else:
                pretty.bar(80)
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
            pretty.bar(80)
            print("Input not understood. Type either an option number or a [keyword].")


if __name__ == "__main__":
    data = setup()
    main(*data)
