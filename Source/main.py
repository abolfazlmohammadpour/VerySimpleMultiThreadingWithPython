import threading
import time


def FirstTask():
    Second = Minute = Hour = 0
    while True:
        Second += 1
        if Second >= 60:
            Second = 0
            Minute += 1
        if Minute >= 60:
            Minute = 0
            Hour += 1
        if Hour >= 24:
            Hour = 0

        print(f"FirstThread {Hour}:{Minute}:{Second}")
        time.sleep(1)


def SecondTask():
    Second = Minute = Hour = 0
    while True:
        Second += 1
        if Second >= 60:
            Second = 0
            Minute += 1
        if Minute >= 60:
            Minute = 0
            Hour += 1
        if Hour >= 24:
            Hour = 0

        print(f"SecondThread {Hour}:{Minute}:{Second}")
        time.sleep(1)


FirstThread = threading.Thread(target=FirstTask)
SecondThread = threading.Thread(target=SecondTask)

FirstThread.start()
SecondThread.start()