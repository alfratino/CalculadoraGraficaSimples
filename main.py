from tkinter import *
from tkinter import ttk

#cores
cor1 = "#080708" #preto
cor2 = "#1507e0" #azul
cor3 = "#e01507" #vermelho
cor4 = "#706b6f" #cinza
cor5 = "#ffffff" #branco


#janela maior
janela = Tk()
janela.title("Calculadora")
janela.geometry("349x351")
janela.config()  #atribuir cor a janela

#divisao tela
frame_tela = Frame(janela, width=350, height=80, bg=cor4) #tamanho da segunda janela dentro da janela principal
frame_tela.grid(row=0, column=0) #posicao da divisao, row = linha, column = coluna

frame_corpo = Frame(janela, width=350, height=400)
frame_corpo.grid(row=1, column=0)

#criando label

cal_label = Label(frame_tela, text="123456789", width=22, height=3, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=("Ivy 18"))
cal_label.place(x=0, y=0)

#criando botoes

b_1 = Button(frame_corpo, text="C", width=15, height=3, font=("Arial 9 bold"), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, text="%", width=15, height=3, font=("Arial 9 bold"), relief=RAISED, overrelief=RIDGE)
b_2.place(x=119, y=0)
b_3 = Button(frame_corpo, text="/", width=15, height=3, font=("Arial 9 bold"), relief=RAISED, overrelief=RIDGE)
b_3.place(x=240, y=0)

b_4 = Button(frame_corpo, text="7", width=10, height=3, font=("Arial 8 bold"), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=55)
b_5 = Button(frame_corpo, text="8", width=10, height=3, font=("Arial 8 bold"), relief=RAISED, overrelief=RIDGE)
b_5.place(x=80, y=55)
b_6 = Button(frame_corpo, text="9", width=10, height=3, font=("Arial 8 bold"), relief=RAISED, overrelief=RIDGE)
b_6.place(x=160, y=55)

b_7 = Button(frame_corpo, text="4", width=10, height=3, font=("Arial 8 bold"), relief=RAISED, overrelief=RIDGE)
b_7.place(x=0, y=108)
b_8 = Button(frame_corpo, text="5", width=10, height=3, font=("Arial 8 bold"), relief=RAISED, overrelief=RIDGE)
b_8.place(x=80, y=108)
b_9 = Button(frame_corpo, text="6", width=10, height=3, font=("Arial 8 bold"), relief=RAISED, overrelief=RIDGE)
b_9.place(x=160, y=108)

b_10= Button(frame_corpo, text="1", width=10, height=3, font=("Arial 8 bold"), relief=RAISED, overrelief=RIDGE)
b_10.place(x=0, y=161)
b_11 = Button(frame_corpo, text="2", width=10, height=3, font=("Arial 8 bold"), relief=RAISED, overrelief=RIDGE)
b_11.place(x=80, y=161)
b_12 = Button(frame_corpo, text="3", width=10, height=3, font=("Arial 8 bold"), relief=RAISED, overrelief=RIDGE)
b_12.place(x=160, y=161)

b_13 = Button(frame_corpo, text="X", width=14, height=3, font=("Arial 8 bold"), relief=RAISED, overrelief=RIDGE)
b_13.place(x=240, y=55)
b_14 = Button(frame_corpo, text="-", width=14, height=3, font=("Arial 8 bold"), relief=RAISED, overrelief=RIDGE)
b_14.place(x=240, y=108)
b_15 = Button(frame_corpo, text="+", width=14, height=3, font=("Arial 8 bold"), relief=RAISED, overrelief=RIDGE)
b_15.place(x=240, y=161)

b_16 = Button(frame_corpo, text="0", width=15, height=3, font=("Arial 9 bold"), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=214)
b_17 = Button(frame_corpo, text=".", width=15, height=3, font=("Arial 9 bold"), relief=RAISED, overrelief=RIDGE)
b_17.place(x=119, y=214)
b_18 = Button(frame_corpo, text="=", width=15, height=3, font=("Arial 9 bold"), relief=RAISED, overrelief=RIDGE)
b_18.place(x=240, y=214)

janela.mainloop()

