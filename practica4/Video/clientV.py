#! /usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np
import cv2
import multiprocessing as mp
import time
import xmlrpclib
import numpy
from cStringIO import StringIO
import thread
CHUNK = 1024
CHANNELS = 1 
RATE = 44100
RECORD_SECONDS = 2 
cap = cv2.VideoCapture(0)
proxy = xmlrpclib.ServerProxy("http://localhost:9080/",allow_none = False)
from numpy.lib import format
queue = mp.Queue()

class cli:
    def toString(self,data):
        f= StringIO()
        format.write_array(f,data)
        return f.getvalue()
    
    def graba(self,q):
        while(True):
            ret, frame = cap.read()
            cv2.imshow('Cliente',frame) 
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            data = xmlrpclib.Binary(self.toString(frame))
            proxy.playVideo(data) 
        cap.release()   
        cv2.destroyAllWindows()

    def corre1(self):   
        
        p = mp.Process(target=self.graba, args=(queue,))
        p.start()
        


