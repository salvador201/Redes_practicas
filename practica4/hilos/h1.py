import sys
import threading
import thread
import time

sys.path.append('/root/Desktop/Redes/practica4/Channel')
from c3 import Cliente
from s3 import FuncionS


class Corre:
    
    def __init__(self,puerto,mensaje,IP):
        self.p=puerto
        self.m=mensaje
        self.IP=IP
    
#servidor
    def Servi(self):
        self.ser=FuncionS() 
        self.ser.abre(self.p,self.IP)

#cliente
    def Cli(self):
        
        c=Cliente()        
        c.crea(self.p,self.m,self.IP)
        self.texto= c.respuesta()

        self.Pantalla()
        

    def Pantalla(self):
        self.ser.cerrar()
    
    def Pri(self):
        self.texto='a'
        return self.texto   
        
    
class MisHilos:
    def Paquete(self,puerto,mensaje,IP):
        x=Corre(puerto,mensaje,IP)    
        
        #creo los hilos de servidor y cliente
        t1 = threading.Thread(target=x.Servi, args=())
        t = threading.Thread(target=x.Cli, args=())

        t1.start()
        time.sleep(1)
        t.start()
        time.sleep(1)
        return x.Pri()
        
