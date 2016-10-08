from Tkinter import * 
import sys
import threading
import thread
import time

class Ventana:
    def mostrar(ventana):
        ventana.deiconify()

    def ocultar(ventana):
        ventana.withdraw()

    def ejecutar(f):
        ventanaInicio.affter(200,f)
        
    def DaPuertos(self,texto,StringVar1,texto1,StringVar2):
        self.ventanaInicio.withdraw()
        self.ventanaInicio.destroy()
        
                
    def Login(self,lista_c):
        self.ventanaInicio = Tk()
        self.ventanaInicio.resizable(0,0)
        self.ventanaInicio.geometry("400x600")
        
        self.miPuerto=StringVar()
        self.textoentry_1=StringVar()
        
        self.contra=StringVar()
        self.textoentry_2=StringVar()
        
        self.IPContacto=StringVar()
        self.textoentry_3=StringVar()
        
        self.LabelMiPuerto = Label(self.ventanaInicio, text="Cual es mi puerto?").pack()
        
        self.entry1=Entry(self.ventanaInicio,textvar=self.textoentry_1).pack()
        self.label1=Label(self.ventanaInicio,textvar=self.miPuerto).pack()

        self.LabelMiPuerto = Label(self.ventanaInicio, text="escribe un puerto de un contacto disponible").pack()
        
        for i in lista_c:
            self.LabelMiPuerto = Label(self.ventanaInicio, text=i).pack()

        self.entry2=Entry(self.ventanaInicio,textvar=self.textoentry_2).pack()
        self.label2=Label(self.ventanaInicio,textvar=self.contra).pack()
        
        self.LabelMiIP = Label(self.ventanaInicio, text="Cual es tu IP?").pack()

        self.entry3=Entry(self.ventanaInicio,textvar=self.textoentry_3).pack()
        self.label3=Label(self.ventanaInicio,textvar=self.IPContacto).pack()
        
        botonIngresar=Button(self.ventanaInicio,text="Acceder",command=lambda:
        self.DaPuertos(self.textoentry_1.get(),self.miPuerto,self.textoentry_2.get(),self.contra)).pack()
        
        
        self.ventanaInicio.mainloop()
        res=[]
        res.append(self.textoentry_1.get())
        res.append(self.textoentry_2.get())
        res.append(self.textoentry_3.get())
        return res


        
    
