#Importancion de tkinter
from tkinter import Tk, Entry, Label, Button, Radiobutton, IntVar, messagebox



def imprimir():
    #Obtener informacion de los widgets
    #Obteniendo el valor de los raddiobutton
    valor = float(input1.get())
    #Obteniendo el valor del input
    txt= float(input2.get())
    sape= valor * txt
    valor = int(radio.get())
    texto = "El precio es: $"

    #Se crea un if para evaluar si pagara con tarjeta o efectivo
    if valor == 1:
      sape1= sape * 0.2
      final = sape - sape1
      x = " Con un descuento de 20%"


    elif valor == 2:
        final = sape
        x = " Sin descuento"
    
    final_f = str(final)
   
    messagebox.showinfo(title="Cantidad a pagar", message=str(texto)+final_f+str(x))


vent1= Tk()
vent1.geometry("400x200")

radio = IntVar()

labl1=Label(vent1, bg = "gray",text="cantidad de producto.")
input1=Entry(vent1)
labl2=Label(vent1,bg = "gray", text="precio.")
input2=Entry(vent1)
#Declaracion de los radio button
rdb1 = Radiobutton(vent1, bg = "gray",text="Con tarjeta", value=1, variable=radio)
rdb2 = Radiobutton(vent1, bg = "gray",text="Con efectivo", value=2, variable=radio)

btn1 = Button(vent1,text="Calcular",command=imprimir)


#Mapeo de widgets
#se agrega color a la ventana
vent1.configure(bg='gray')
#Se agrega titulo a la ventana
vent1.title("Cajero de Super mercado")
labl1.pack()
input1.pack()
labl2.pack()
input2.pack()
btn1.pack()
rdb1.pack()
rdb2.pack()


vent1.mainloop()