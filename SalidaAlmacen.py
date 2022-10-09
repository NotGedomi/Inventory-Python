import tkinter
from tkinter import *
from tkinter import font
from tkinter.font import BOLD
import time
from tkinter import ttk
from tkinter import messagebox
import subprocess
lista = []

#CREACION DE VENTANA PRINCIPAL
ventana = Tk()
ventana.title("ION SAC SALIDA")
ventana.config(bg="#191919")
ventana.iconbitmap("")
ventana.resizable(10,10)



#LOGO
logo = PhotoImage(file="")
Label(ventana, image=logo, bg="#191919" ,bd=0).grid(column=0,row=0,columnspan=2,sticky=EW, pady=5, padx=30)

lista_de_prods = []

#####################################################################################################

#FUNCIONES
def registro():
    subprocess.call("RegistroAlmacen.py", shell=True)
def comercial():
    subprocess.call("ComercialVentas.py", shell=True)

def salir():
    
    ventana.destroy()

#FUNCIONES DE IMPRESION DE ARCHIVO
 
def iniciarArchivo():
    archivo = open("file.txt","a")
    archivo.close()
    
def guardar():
    archivo=open("D://BOLETACAB.TXT","a")
    archivo.write("ION"+idproduct1.get()+"-"+str(cantidad1.get())+"\n")
    archivo.close()  

###########################################################################################    


#CONTENEDOR PRINCIPAL
contenedor1= Frame(ventana)
contenedor1.config(bg="#191919")
contenedor1.grid(column=0,row=1,sticky=NSEW,padx=(20,20),pady=(10,10))
contenedor1.columnconfigure(0,weight=1)
contenedor1.columnconfigure(0,weight=1)



dcn=Label(contenedor1, text="ION SAC SALIDA DE PRODUCTOS")
dcn.config(bg="#191919", font=("Impact",18), fg="white")
dcn.grid(column=1,row=1, columnspan=5,sticky=NSEW, pady=10)


idproduct0=Label(contenedor1, text="ID DEL PRODUCTO")
idproduct0.config(bg="#191919", font=("Arial Black",8), fg="#6571DC")
idproduct0.grid(column=1,row=2,sticky=NSEW,pady=10,padx=10)

idproduct = StringVar()
idproduct1=Entry(contenedor1,textvariable=idproduct, fg="#191919", bg="#6571DC",validate="key")
idproduct1.grid(column=2,row=2,sticky=NSEW,pady=10,padx=10)


cantidad0=Label(contenedor1, text="CANTIDAD")
cantidad0.config(bg="#191919", font=("Arial Black",8), fg="#6571DC")
cantidad0.grid(column=1,row=3,sticky=NSEW,pady=10,padx=10)

cantidad = StringVar()
cantidad1=Entry(contenedor1,textvariable=cantidad,fg="#191919", bg="#6571DC",validate="key")
cantidad1.grid(column=2,row=3,sticky=NSEW,pady=10,padx=10)

#PRODUCTOS
PC = ["ION01","PC","1","1",1350.00,1350.00]
Teclado = ["ION02","Teclado","1","1",120.00,120.00]
Monitor = ["ION03","Monitor","1","1",400.00,400.00]
Mouse = ["ION04","Mouse","1","1",99.00,99.00]

printbutton=Button(ventana, text="Actualizar",font=("Arial Black",8),bg="#191919", fg="#6571DC",activebackground="#191919",activeforeground="white",command=guardar).grid(column=0,row=10,columnspan=2,sticky=NSEW, padx=700,pady=10)


Mi_Menu = Menu(ventana)
Mi_Menu.add_command(label="REGISTRO ALMACEN", command =registro)
Mi_Menu.add_command(label="COMERCIAL", command =comercial)
Mi_Menu.add_command(label="SALIR", command =salir)
ventana.config(menu = Mi_Menu)
ventana.mainloop()
