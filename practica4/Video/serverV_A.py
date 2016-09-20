#! /usr/bin/env python

from SimpleXMLRPCServer import SimpleXMLRPCServer
import pyaudio
import cv2
import numpy as np
import numpy 
import threading
CHUNK = 1024
CHANNELS = 1 
RATE = 44100
DELAY_SECONDS = 5 

frames = []
from cStringIO import StringIO
from numpy.lib import format
import sys
sys.path.append('/root/Desktop/Redes/practica4/Video')
from clientV import cli
import multiprocessing as mp


class miser:
    def toArray(self,s):
        f=StringIO(s)
        arr=format.read_array(f)
        return arr 


    def playAudio(self,audio):
        p = pyaudio.PyAudio()
        FORMAT = p.get_format_from_width(2)
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        output=True,
                        frames_per_buffer=CHUNK)
        data = audio.data
        stream.write(data)
        stream.close()
        p.terminate()

    def playVideo(self,video):
        frames.append(self.toArray(video.data))
    def reproduce(self):
        while True:
            if len(frames) > 0:
                cv2.imshow('Servidor',frames.pop(0))
            if cv2.waitKey(1) & 0xFF==ord('q'):
                break
        cv2.destroyAllWindows()
    
    def corre(self):
        server = SimpleXMLRPCServer(("localhost", 9080), allow_none = True)
        playVThread = threading.Thread(target=self.reproduce)
        playVThread.start()

        server.register_function(self.playAudio, 'playAudio') 
        server.register_function(self.playVideo, 'playVideo') 
        
        y=cli()
        y.corre1()
        print "escuchando ......"
        server.serve_forever()

