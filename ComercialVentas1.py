import tkinter
from tkinter import *
from tkinter import font
from tkinter.font import BOLD
import time
from tkinter import ttk
from tkinter import messagebox
import subprocess
from INVENTORY import PC, Teclado, Monitor, Mouse
lista = []


#CREACION DE VENTANA PRINCIPAL
ventana = Tk()
ventana.title("ION SAC COMERCIAL")
ventana.config(bg="#191919")
ventana.iconbitmap("")
ventana.resizable(0,0)



#LOGO
logo = PhotoImage(file="")
Label(ventana, image=logo, bg="#191919" ,bd=0).grid(column=0,row=0,columnspan=2,sticky=EW, pady=5, padx=100)

lista_de_prods = []



#####################################################################################################
    
#FUNCIONES
def salida():
    subprocess.call("Salida Almacen.py", shell=True)
def registro():
    subprocess.call("Registro Almacen.py", shell=True)

   
def buscar():
    
    if get.get() == PC[0]:
        tree.insert(parent='', index=0, text='', values=(PC[0],PC[1],PC[2],PC[3]))
        get.set("")
        product1.focus()
        lista_de_prods.append("PC")
        #MENSAJE
        messagebox.showinfo("Aviso","Producto agregado satisfactoriamente")
    elif get.get() == Teclado[0]:
        tree.insert(parent='', index=1, text='', values=(Teclado[0],Teclado[1],Teclado[2],Teclado[3]))
        get.set("")
        product1.focus()
        lista_de_prods.append("Teclado")
        #MENSAJE
        messagebox.showinfo("Aviso","Producto agregado satisfactoriamente")
    elif get.get() == Monitor[0]:
        tree.insert(parent='', index=2, text='', values=(Monitor[0],Monitor[1],Monitor[2],Monitor[3]))
        get.set("")
        product1.focus()
        lista_de_prods.append("Monitor")
        #MENSAJE
        messagebox.showinfo("Aviso","Producto agregado satisfactoriamente")
    elif get.get() == Mouse[0]:
        tree.insert(parent='', index=3, text='', values=(Mouse[0],Mouse[1],Mouse[2],Mouse[3]))
        get.set("")
        product1.focus()
        lista_de_prods.append("Mouse")
        #MENSAJE
        messagebox.showinfo("Aviso","Producto agregado satisfactoriamente")            
    else:
        #MENSAJE ID NO ENCONTRADO
        messagebox.showinfo("Aviso","Producto no encontrado en almacén, verifique la lista de productos")
        get.set("")
        product1.focus()
    print(lista_de_prods)

#FUNCIONES DE IMPRESION DE ARCHIVO
 

def imprimir():
    namep = getname.get()
    lastnamep = getlastname.get()
    addressp = getaddress.get()
    dnip = getdni.get()
    phonep = getphone.get()
    lista.append("-----------------------------NUEVO CLIENTE-------------------------------------------")
    lista.append("Nombre:"+namep+" / "+"Apellidos:"+lastnamep+" / "+"DNI:"+dnip+" / "+"Direccion:"+addressp+" / "+"Telefono:"+phonep)
    lista.append("------------------------INFORMACION DEL PRODUCTO-------------------------------------")
    contador  = 0
    if "PC" in lista_de_prods:
        lista.append(f"Producto : {PC[1]}\nCantidad : {PC[2]} \nPrecio Unitario : S/.{PC[3]}\n")
        contador+=PC[3]
    if "Teclado" in lista_de_prods:
        lista.append(f"Producto : {Teclado[1]}\nCantidad : {Teclado[2]} \nPrecio Unitario : S/.{Teclado[3]}\n")
        contador+=Teclado[3]
    if "Monitor" in lista_de_prods:
        lista.append(f"Producto : {Monitor[1]}\nCantidad : {Monitor[2]} \nPrecio Unitario: S/.{Monitor[3]}\n")
        contador+=Monitor[3]
    if "Mouse" in lista_de_prods:
        lista.append(f"Producto : {Mouse[1]}\nCantidad : {Mouse[2]} \nPrecio Unitario : S/.{Mouse[3]}\n")
        contador+=Mouse[3]
    lista.append(f"Total a pagar : S/.{total}")
    lista.append("\n")
    lista.append("\n")
    
    escribirBoleta()
    messagebox.showinfo("información","La boleta de venta ha sido generada")
    getname.set("")
    getlastname.set("")
    getaddress.set("")
    getdni.set("")
    getphone.set("")

#ARCHIVO TXT    
def escribirBoleta():
    archivo = open("Boleta.txt","w")
    # lista.sort()
    for elemento in lista:
        archivo.write(elemento+"\n")
    archivo.close()
def salir():
    
    ventana.destroy()    
###########################################################################################    


#CONTENEDOR PRINCIPAL
contenedor1= Frame(ventana)
contenedor1.config(bg="#191919")
contenedor1.grid(column=0,row=1,sticky=NSEW,padx=(20,20),pady=(10,10))
contenedor1.columnconfigure(0,weight=1)
contenedor1.columnconfigure(0,weight=1)

def is_valid_text(text):
    return text in "aAbBcCdDeEfFgGhHiIjJkKlLmMnNñÑoOpPqQrRsStTuUvVwWxXyYzZ  "
validatecommand = contenedor1.register(is_valid_text)


#DESCRIPCIÓN
dcn=Label(contenedor1, text="ION SAC COMERCIAL")
dcn.config(bg="#191919", font=("Impact",18), fg="white")
dcn.grid(column=1,row=1, columnspan=5,sticky=NSEW, pady=10)

#DNI
dni=Label(contenedor1, text="DNI")
dni.config(bg="#191919", font=("Arial Black",8), fg="#6571DC")
dni.grid(column=1,row=2,sticky=NSEW,pady=10,padx=10)


#ENTRY DNI SOLO 8 DIGITOS
def is_valid_date(action, char, text):
    # Solo chequear cuando se añade un carácter.
    if action != "1":
        return True
    return char in "0123456789" and len(text) < 8

validatecommand = contenedor1.register(is_valid_date)

getdni = StringVar()
dni1=Entry(contenedor1,textvariable=getdni, fg="#191919", bg="#6571DC",validate="key",validatecommand=(validatecommand, "%d", "%S", "%s"))
dni1.grid(column=2,row=2,sticky=NSEW,pady=10,padx=10)

#NOMBRE
name=Label(contenedor1, text="NOMBRES")
name.config(bg="#191919", font=("Arial Black",8), fg="#6571DC")
name.grid(column=1,row=3,sticky=NSEW,pady=10,padx=10)


def is_valid_text(text):
    return text in "aAbBcCdDeEfFgGhHiIjJkKlLmMnNñÑoOpPqQrRsStTuUvVwWxXyYzZ  "
validatecommand = contenedor1.register(is_valid_text)

#ENTRY NOMBRE SOLO TEXTO
getname = StringVar()
name1=Entry(contenedor1,textvariable=getname,fg="#191919", bg="#6571DC",validate="key", validatecommand=(validatecommand, "%S"))
name1.grid(column=2,row=3,sticky=NSEW,pady=10,padx=10)

#APELLIDOS
lastname=Label(contenedor1, text="APELLIDOS")
lastname.config(bg="#191919", font=("Arial Black",8), fg="#6571DC")
lastname.grid(column=4,row=3,sticky=NSEW,pady=10,padx=10)

#APELLIDOS ENTRY
getlastname = StringVar()
lastname1=Entry(contenedor1,textvariable=getlastname,fg="#191919", bg="#6571DC",validate="key", validatecommand=(validatecommand, "%S"))
lastname1.grid(column=5,row=3,sticky=NSEW,pady=10,padx=10)

#DIRECCION
address=Label(contenedor1, text="DIRECCIÓN DE DOMICILIO")
address.config(bg="#191919", font=("Arial Black",8), fg="#6571DC")
address.grid(column=1,row=4,sticky=NSEW,pady=10,padx=10)

#DIRECCION ENTRY
getaddress = StringVar()
address1=Entry(contenedor1,textvariable=getaddress,fg="#191919", bg="#6571DC")
address1.grid(column=2,row=4,columnspan=4,sticky=NSEW,pady=10,padx=10)

#TELEFONO
phone=Label(contenedor1,text="TELÉFONO FIJO / CELULAR")
phone.config(bg="#191919", font=("Arial Black",8), fg="#6571DC")
phone.grid(column=1,row=5,sticky=NSEW,pady=10,padx=10)

#ENTRY TELEFONO CHECK SOLO NUMERO

def is_valid_char(char):
    return char in "0123456789" 
 
validatecommand = contenedor1.register(is_valid_char)
getphone = StringVar()
phone1=Entry(contenedor1,textvariable=getphone,fg="#191919", bg="#6571DC",validate="key", validatecommand=(validatecommand, "%S"))
phone1.grid(column=2,row=5,columnspan=2,sticky=NSEW,pady=10,padx=10)

#ID PRODUCTO
product=Label(contenedor1, text="ID DEL PRODUCTO")
product.config(bg="#191919", font=("Arial Black",8), fg="#6571DC")
product.grid(column=1,row=6,sticky=NSEW,pady=10,padx=10)

#ENTRY ID PRODUCTO
get=StringVar()
product1=Entry(contenedor1,textvariable=get,fg="#191919", bg="#6571DC")
product1.grid(column=2,row=6,sticky=NSEW,pady=10,padx=10)

#BOTON BUSCAR PRODUCTO POR ID
button=Button(contenedor1,font=("Arial Black",8),bg="#191919", fg="white",activebackground="#6571DC",activeforeground="#191919", text="AÑADIR",command=buscar).grid(column=3,row=6,sticky=NSEW,padx=10, pady=10)



#VIEWTREE
style = ttk.Style()
style.configure("Treeview",
                background="#6571DC",
                foreground="#191919",
                rowheight=25,
                fieldbackground="#191919")
style.map('Treeview', background=[('selected', '#191919')])

tree = ttk.Treeview(ventana)
tree['columns']=('cod_pro', 'Description','Cantidad','Precio')
tree.column('#0', width=0, stretch=NO)
tree.column('cod_pro', anchor=CENTER)
tree.column('Description', anchor=CENTER)
tree.column('Cantidad', anchor=CENTER)
tree.column('Precio', anchor=CENTER)



#CREACIÓN DE HEADING
tree.heading('#0', text='', anchor=CENTER)
tree.heading('cod_pro', text='Cod_Pro', anchor=CENTER)
tree.heading('Description', text='Description', anchor=CENTER)
tree.heading('Cantidad', text='Cantidad', anchor=CENTER)
tree.heading('Precio', text='Precio', anchor=CENTER)
tree.grid(column=0,row=7,columnspan=2,sticky=EW, pady=5, padx=50)





def generar():
    global total
    total = 0.0

    for child in tree.get_children():
        total += float(tree.item(child, 'values')[3])
    

    result['text'] = 'Total: {}'.format(total)
    print (total)


 

#BOTON IMPRIMIR
printbutton=Button(ventana, text="GENERAR BOLETA",font=("Arial Black",8),bg="#191919", fg="#6571DC",activebackground="#191919",activeforeground="white",command=imprimir).grid(column=0,row=10,columnspan=2,sticky=NSEW, padx=600,pady=10)
#BOTON TOTAL
add = Button(ventana, text='TOTAL A PAGAR',font=("Arial Black",8),bg="#191919", fg="#6571DC",activebackground="#191919",activeforeground="white", command=generar)
add.grid(column=0,row=8,columnspan=2,sticky=NSEW, padx=600,pady=10)
#TOTAL A PAGAR
result = Label(ventana, text='Total: 0',font=("Arial Black",8),bg="#6571DC", fg="#191919")
result.grid(column=0,row=9,columnspan=2,sticky=NSEW,pady=5,padx=600)
#MENU PARA INVENTARIO
Mi_Menu = Menu(ventana, bg="#191919")
Mi_Menu.add_command(label="REGISTRO ALMACEN", command = registro)
Mi_Menu.add_command(label="SALIDA ALMACEN", command = salida)
Mi_Menu.add_command(label="SALIR", command = salir)
ventana.config(menu = Mi_Menu)

ventana.mainloop()
