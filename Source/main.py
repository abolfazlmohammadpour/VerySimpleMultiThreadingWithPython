import threading
import time

def FirstTask():
    print("Start First Task")
    time.sleep(float(2))
    print("End Of First Task")

def SecondTask():
    print("Start Second Task")
    time.sleep(float(1))
    print("End Of Second Task")

FirstThread = threading.Thread(target=FirstTask)
SecondThread = threading.Thread(target=SecondTask)

FirstThread.start()
SecondThread.start()