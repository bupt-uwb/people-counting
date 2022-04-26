import os
import threading
from time import sleep

def T1():
    os.system("python detect.py --source 1")
    
def T2():
    os.system("python main.py")
    
t2 = threading.Thread(target = T2)
t2.start()

sleep(20)
t1 = threading.Thread(target = T1)
t1.start()


