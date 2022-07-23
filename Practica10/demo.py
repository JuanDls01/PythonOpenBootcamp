import tkinter

window = tkinter.Tk()

# Widget label: crea una etiqueta nomas
# tkinter.lable(ventana, texto descriptivo)

label_saludo = tkinter.Label(window, text='hola mundo', bg='yellow', fg='blue')
label_adios = tkinter.Label(window, text='Adios', bg='purple')

# Pack permite posicionar en mi ventana
label_saludo.pack(ipadx=50, ipady=50, fill='both', expand=True, side='left')
label_adios.pack(ipadx=100, ipady=75, fill='both', expand=True)

window.mainloop()
