import sys
import threading
import thread
import time
from Tkinter import * 

sys.path.append('/root/Desktop/Redes/practica4/hilos')
from h1 import MisHilos


sys.path.append('/root/Desktop/Redes/practica4/GUI')
from LoginV import Ventana 
from ChatV import VentanaC


class Plantica:
    def __init__(self):
        print 'chat'
        arre=Ventana().Login()
        self.puerto1=arre[0]
        self.puerto2=arre[1]
        self.z=VentanaC(self.puerto1)
        self.z1=VentanaC(self.puerto2)
        
        
        print arre
   
    def Conversa1(self):
        self.z.Chat()
        self.coment=self.z.nuevo_mem()
        self.z1.insertar_comen_1(self.coment)
       
    def Conversa1_1(self):
        self.z1.Chat()
        self.z1.enfrente()
    
    
fin=Plantica()

hilo=threading.Thread(target=fin.Conversa1, args=())
hilo1=threading.Thread(target=fin.Conversa1_1, args=())

hilo.start()
time.sleep(.1)
hilo1.start()    
time.sleep(.1)
