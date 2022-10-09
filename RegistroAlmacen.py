#IMPORTAR LIBRERIA TKINTER
import tkinter
from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import font
from tkinter.font import BOLD
import time
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import subprocess



lista = []

#CREACION DE VENTANA PRINCIPAL
ventana = Tk()
ventana.title("ION SAC REGISTRO")
ventana.config(bg="#191919")
ventana.iconbitmap("")
ventana.resizable(10,10)



#LOGO
logo = PhotoImage(file="")
Label(ventana, image=logo, bg="#191919" ,bd=0).grid(column=0,row=0,columnspan=2,sticky=EW, pady=5, padx=30)

lista_de_prods = []
#FUNCIONES
def salida():
    subprocess.run("SalidaAlmacen.py", shell=True)
def comercial():
    subprocess.run("ComercialVentas.py", shell=True)
    
def salir():
    
    ventana.destroy()

#FUNCIONES DE IMPRESION DE ARCHIVO

    
def guardar():
    archivo=open("INVENTORY.py","a")
    archivo.write("\n"+producto1.get()+"=['"+idproduct1.get()+"','"+str(producto1.get())+"',"+"'1',"+precio1.get()+"]")
    archivo.close()
    
def importlist():
    archivo= open('ComercialVentas1.py')
    text = archivo.read()
    archivo.close()
    
    archivo = open('ComercialVentas1.py', 'a')
    archivo.write("zero line\n\n")
    archivo.write("from INVENTORY import"+producto1.get())
    archivo.close()

    idproduct.set("")
    producto.set("")
    precio.set("")

###########################################################################################    


#CONTENEDOR PRINCIPAL
contenedor1= Frame(ventana)
contenedor1.config(bg="#191919")
contenedor1.grid(column=0,row=1,sticky=NSEW,padx=(20,20),pady=(10,10))
contenedor1.columnconfigure(0,weight=1)
contenedor1.columnconfigure(0,weight=1)


#DESCRIPCIÓN
dcn=Label(contenedor1, text="ION SAC ENTRADA DE PRODUCTOS")
dcn.config(bg="#191919", font=("Impact",18), fg="white")
dcn.grid(column=1,row=1, columnspan=6,sticky=NSEW, pady=5)

codproduct0=Label(contenedor1, text="COD_PROD")
codproduct0.config(bg="#191919", font=("Arial Black",8), fg="#6571DC")
codproduct0.grid(column=1,row=2,sticky=NSEW,pady=10,padx=5)

idproduct = StringVar()
idproduct1=Entry(contenedor1,textvariable=idproduct, fg="#191919", bg="#6571DC",validate="key")
idproduct1.grid(column=2,row=2,sticky=NSEW,pady=10,padx=5)


descriptionprod0=Label(contenedor1, text="NOMBRE DEL ARTICULO")
descriptionprod0.config(bg="#191919", font=("Arial Black",8), fg="#6571DC")
descriptionprod0.grid(column=1,row=3,sticky=NSEW,pady=10,padx=5)

producto = StringVar()
producto1=Entry(contenedor1,textvariable=producto,fg="#191919", bg="#6571DC",validate="key")
producto1.grid(column=2,row=3,sticky=NSEW,pady=10,padx=5)


precio0=Label(contenedor1, text="PRECIO")
precio0.config(bg="#191919", font=("Arial Black",8), fg="#6571DC")
precio0.grid(column=3,row=3,sticky=NSEW,pady=10,padx=5)

precio = StringVar()
precio1=Entry(contenedor1,textvariable=precio,fg="#191919", bg="#6571DC",validate="key")
precio1.grid(column=5,row=3,sticky=NSEW,pady=10,padx=5)


printbutton=Button(ventana, text="Guardar",font=("Arial Black",8),bg="#191919", fg="#6571DC",activebackground="#191919",activeforeground="white",command=guardar).grid(column=0,row=10,columnspan=2,sticky=NSEW, padx=600,pady=10)
printbutton=Button(ventana, text="Registrar Lista",font=("Arial Black",8),bg="#191919", fg="#6571DC",activebackground="#191919",activeforeground="white",command=importlist).grid(column=0,row=11,columnspan=2,sticky=NSEW, padx=600,pady=10)

Mi_Menu = Menu(ventana)
Mi_Menu.add_command(label="SALIDA ALMACEN", command =salida)
Mi_Menu.add_command(label="COMERCIAL", command =comercial)
Mi_Menu.add_command(label="SALIR", command =salir)
ventana.config(menu = Mi_Menu)

ventana.mainloop()
