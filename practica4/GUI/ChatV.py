from Tkinter import * 
import sys
import threading
import thread
import time
import multiprocessing as mp
from SimpleXMLRPCServer import SimpleXMLRPCServer

sys.path.append('/root/Desktop/Redes/practica4/hilos')
from h1 import MisHilos

sys.path.append('/root/Desktop/Redes/practica4/Audio')
from comunica import Com

sys.path.append('/root/Desktop/Redes/practica4/Video')
from auxP import aux


class VentanaC:
    def __init__(self,p1):
        self.puerto=p1
        
    def recarga(self,ven):
        self.ventana=ven
        
    def insertar_comen(self):
        if  self.miTexto.get() != "":
            self.comentario.insert(END,'-----------')
            self.comentario.insert(END ,self.miTexto.get())
            self.enviarM(self.puerto)
        else:
            self.comentario.insert(END,' ////')
    
    def Chat(self):
        self.ventanaChat = Tk()
        self.ventanaChat.resizable(0,0)

        scrollbar = Scrollbar(self.ventanaChat)
        scrollbar.pack(side=RIGHT, fill=Y)
        # Cambia el tamanio de la ventana
        self.ventanaChat.geometry("300x500")

        # VENTANA CHAT
        self.comentario = Listbox(self.ventanaChat)
        self.comentario.pack()
        self.miTexto = StringVar()
        e1 = Entry(self.ventanaChat, textvar = self.miTexto).pack()

        self.comentario.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command=self.comentario.yview)

        # Creamos el boton de Responde
        botonResponde=Button(self.ventanaChat,text="Responde", command = self.insertar_comen)
        botonResponde.pack()
        
        
        botonAudio=Button(self.ventanaChat,text="Audio",command = self.voz)
        botonAudio.pack()
        
        botonVideo=Button(self.ventanaChat,text="Video",command = self.video)
        botonVideo.pack()
        self.ventanaChat.mainloop()
    
    def enviarM(self,p1):
        #abrimos los puertos y la comunicacion
        H=MisHilos()
        self.respuesta=H.Paquete(int(p1),self.miTexto.get())
        print self.respuesta
        #self.muere()
    
    def insertar_comen_1(self,nuevo):
        if  nuevo != "":
            self.comentario.insert(END,'-----------')
            self.comentario.insert(END ,nuevo)
            
        else:
            self.comentario.insert(END,' ////')
            
    def nuevo_mem(self):
        return self.respuesta
    
    def muere(self):
        self.ventanaChat.withdraw()
        self.ventanaChat.destroy()
        
    def enfrente(self):
        self.ventanaChat.mainloop()
        
    def voz(self):
        win=Toplevel(self.ventanaChat) 
        win.title("Voz")
        c=Com(self.puerto)
        
    def video(self):
        q=aux()
            
    
        
        

    
