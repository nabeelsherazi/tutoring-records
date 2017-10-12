from classes import Student, Session
import pickle


if __name__ == '__main__':
    try:
        with open("data\\data.dat", "rb") as f:
            pass
    except FileNotFoundError:
        print("Data file not found... creating now.")
        with open("data\\data.dat", "wb") as f:
            pass

    with open("data\\data.dat", "rb") as f:
        data = pickle.load(f)
    
