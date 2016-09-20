import threading
import thread
import time
from Tkinter import * 
import pyaudio
import wave
import sys

sys.path.append('/root/Desktop/Redes/practica4/Audio')
from p1 import Cli
from p2 import Ser

class Com:
    def __init__(self,port):
        x=Cli()
        y=Ser()
        t1 = threading.Thread(target=x.va, args=(port,))
        t = threading.Thread(target=y.va, args=(port,))

        t1.start()
        time.sleep(.1)
        t.start()
        time.sleep(.1)

