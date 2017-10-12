import os
import pickle
from classes import Student, Session, TransactionRecord
import prettyCLI as pretty


def setup():
    """
    Setup function to checks if transaction data exists, otherwise create a
    new file. Returns either TransactionRecord object in pickled data or new
    TransactionRecord.
    """
    for (cdir, sdirs, fs) in os.walk("data"):
        if records.pkl not in fs:
            print("Data file not found... creating now.")
            with open("data\\records.pkl", "wb") as f:
                pass
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
    
