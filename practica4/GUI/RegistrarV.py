from Tkinter import * 
import sys
import threading
import thread
import time

class Registrar:
    def mostrar(ventana):
        ventana.deiconify()

    def ocultar(ventana):
        ventana.withdraw()

    def ejecutar(f):
        ventanaInicio.affter(200,f)
        
    def DaPuertos(self,texto,StringVar1,texto1,StringVar2,texto2,StringVar3):
        self.ventanaInicio.withdraw()
        self.ventanaInicio.destroy()
        
                
    def daAlta(self):
        self.ventanaInicio = Tk()
        self.ventanaInicio.resizable(0,0)
        self.ventanaInicio.geometry("400x200")
        
        self.nombre=StringVar()
        self.textoentry_1=StringVar()
        
        self.contra=StringVar()
        self.textoentry_2=StringVar()
        
        self.Puerto=StringVar()
        self.textoentry_3=StringVar()
        
        self.Labelnombre = Label(self.ventanaInicio, text="No estas registrado ingresa tu usuario").pack()
        
        self.entry1=Entry(self.ventanaInicio,textvar=self.textoentry_1).pack()
        self.label1=Label(self.ventanaInicio,textvar=self.nombre).pack()

        self.Labelnombre = Label(self.ventanaInicio, text="ingresa tu contrasena?").pack()

        self.entry2=Entry(self.ventanaInicio,textvar=self.textoentry_2).pack()
        self.label2=Label(self.ventanaInicio,textvar=self.contra).pack()
        
        self.Labelnombre = Label(self.ventanaInicio, text="ingresa tu puerto").pack()

        self.entry3=Entry(self.ventanaInicio,textvar=self.textoentry_3).pack()
        self.label3=Label(self.ventanaInicio,textvar=self.Puerto).pack()
        
        botonIngresar=Button(self.ventanaInicio,text="Acceder",command=lambda:
        self.DaPuertos(self.textoentry_1.get(),self.nombre,self.textoentry_2.get(),self.contra,self.textoentry_3.get(),self.Puerto)).pack()
        
        
        self.ventanaInicio.mainloop()
        res=[]
        res.append(self.textoentry_1.get())
        res.append(self.textoentry_2.get())
        res.append(self.textoentry_3.get())
        return res
