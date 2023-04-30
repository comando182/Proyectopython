from tkinter import *
#import tkinter as tk

# Formulario aplicar empleo
def send_data():
  Nombres = Nombres.get()
  Apellidos = Apellidos.get()
  Correoelectrónico = Correoelectrónico.get()
  Tipoynúmerodeidentificación = str(Tipoynúmerodeidentificación.get())
  print(Nombres,"\t", Apellidos,"\t", Correoelectrónico,"\t", Tipoynúmerodeidentificación)

#  
  file = open("user.txt", "a")
  file.write(Nombres)
  file.write("\t")
  file.write(Apellidos)
  file.write("\t")
  file.write(Correoelectrónico)
  file.write("\t")
  file.write(Tipoynúmerodeidentificación)
  file.write("\t\n")
  file.close()
  print(" New vacante registered. Nombres: {} | Correoelectrónico: {}   ".format(Nombres, Correoelectrónico))

#  Delete data from previous event
  Nombres.delete(0, END)
  Apellidos.delete(0, END)
  Correoelectrónico.delete(0, END)
  Tipoynúmerodeidentificación.delete(0, END)

# Create new instance - Class Tk()  
mywindow = Tk()
mywindow.geometry("650x550")
mywindow.title("Portal empresarial búsqueda de empleo.")
mywindow.resizable(False,False)
mywindow.config(background = "#213141")
main_title = Label(text = "Alerta de empleos.", font = ("Cambria", 14), bg = "#061609", fg = "white", width = "500", height = "2")
main_title.pack()

# Define Label Fields 
Nombres_label = Label(text = "Nombres", bg = "#FFEEDD")
Nombres_label.place(x = 22, y = 70)
Apellidos_label = Label(text = "Apellidos", bg = "#FFEEDD")
Apellidos_label.place(x = 22, y = 130)
Correoelectrónico_label = Label(text = "Correo electrónico", bg = "#FFEEDD")
Correoelectrónico_label.place(x = 22, y = 190)
Tipoynúmerodeidentificación_label = Label(text = "Tipo y número de identificación", bg = "#FFEEDD")
Tipoynúmerodeidentificación_label.place(x = 22, y = 250)

# Get and store data from users 
Nombres = StringVar()
Apellidos = StringVar()
Correoelectrónico = StringVar()
Tipoynúmerodeidentificación = StringVar()

Nombres = Entry(textvariable = Nombres, width = "40")
Apellidos = Entry(textvariable = Apellidos, width = "40")
Correoelectrónico = Entry(textvariable = Correoelectrónico, width = "40")
Tipoynúmerodeidentificación = Entry(textvariable = Tipoynúmerodeidentificación, width = "40")

Nombres.place(x = 22, y = 100)
Apellidos.place(x = 22, y = 160)
Correoelectrónico.place(x = 22, y = 220)
Tipoynúmerodeidentificación.place(x = 22, y = 280)

# Submit Button
submit_btn = Button(mywindow,text = "Aplicar vacante", width = "30", height = "2", command = send_data, bg = "#00CD63")
submit_btn.place(x = 22, y = 320)

mywindow.mainloop()
