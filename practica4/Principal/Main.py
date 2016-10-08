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
from SessionV import Session
from RegistrarV import Registrar

class Plantica:
    def __init__(self):
        print 'chat'
        #inicia sesion
        datos=Session().inicia()
        #verifica si esta en la lista
        if self.Verfica(datos[0],datos[1])==1:
            arre=Ventana().Login(self.cargaLis())
        else :
            self.alta(Registrar().daAlta())
            arre=Ventana().Login(self.cargaLis())
            
        self.puerto1=arre[0]
        self.puerto2=arre[1]
        self.IP=arre[2]
        self.z=VentanaC(self.puerto1,self.IP)
        self.z1=VentanaC(self.puerto2,self.IP)
        
        print arre
   
    def Conversa1(self):
        self.z.Chat()
        self.coment=self.z.nuevo_mem()
        self.z1.insertar_comen_1(self.coment)
       
    def Conversa1_1(self):
        self.z1.Chat()
        self.z1.enfrente()
        
    def Verfica(self,u,c):
        texto='contra.txt'
        con=0
        infile = open(texto, 'r')
        for line in infile:
            varAux=line.split()
            if varAux[0]==u and varAux[1]==c:
                con=1
        infile.close()
        return con
        
    def alta(self,var):
        archivo=open('contra.txt','w')
        archivo.write( var[0] +" "+ var[1]+" "+var[2])        
        archivo.close()  
        
    def cargaLis(self):
        texto='contra.txt'
        infile = open(texto, 'r')
        list_c=[]
        lista_c=[]
        for line in infile:
            list_c.append(line.split())
        #print list_c[0][2]
        for i in list_c:
            lista_c.append(str(i[0])+" "+str(i[2]))
            
        return lista_c
    
    
fin=Plantica()

hilo=threading.Thread(target=fin.Conversa1, args=())
hilo1=threading.Thread(target=fin.Conversa1_1, args=())

hilo.start()
time.sleep(.1)
hilo1.start()    
time.sleep(.1)
