import multiprocessing as mp
import sys
import threading
import thread
import time
from SimpleXMLRPCServer import SimpleXMLRPCServer

sys.path.append('/root/Desktop/Redes/practica4/Video')
from clientV import cli

sys.path.append('/root/Desktop/Redes/practica4/Video')
from serverV_A import miser 

class aux:
    def __init__(self):
        s=miser()
        c=cli()
        
        t1 = threading.Thread(target=s.corre(), args=())
        t = threading.Thread(target=x.corre(), args=())

        t1.start()
        time.sleep(1)
        t.start()
        time.sleep(1)
