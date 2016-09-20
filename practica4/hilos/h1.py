import sys
import threading
import thread
import time

sys.path.append('/root/Desktop/Redes/practica4/Channel')
from c3 import Cliente
from s3 import FuncionS


class Corre:
    texto=''
    def __init__(self,puerto,mensaje):
        self.p=puerto
        self.m=mensaje
    
#servidor
    def Servi(self):
        self.ser=FuncionS() 
        self.ser.abre(self.p)

#cliente
    def Cli(self):
        global texto
        c=Cliente()        
        c.crea(self.p,self.m)
        texto= c.respuesta()

        self.Pantalla()
        

    def Pantalla(self):
        self.ser.cerrar()
    
    def Pri(self):
        global texto
        return texto   
        
    
class MisHilos:
    def Paquete(self,puerto,mensaje):
        x=Corre(puerto,mensaje)    
        
        #creo los hilos de servidor y cliente
        t1 = threading.Thread(target=x.Servi, args=())
        t = threading.Thread(target=x.Cli, args=())

        t1.start()
        time.sleep(1)
        t.start()
        time.sleep(1)
        return x.Pri()
        
