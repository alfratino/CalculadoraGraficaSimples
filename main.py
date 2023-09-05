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
janela.geometry("350x450")
janela.config()  #atribuir cor a janela

#divisao tela
frame_tela = Frame(janela, width=350, height=80, bg=cor4) #tamanho da segunda janela dentro da janela principal
frame_tela.grid(row=0, column=0) #posicao da divisao, row = linha, column = coluna

frame_corpo = Frame(janela, width=350, height=400)
frame_corpo.grid(row=1, column=0)

#criando botoes

b_1 = Button(frame_corpo, text="C", width=15, height=3, font=("Arial 9 bold"), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, text="%", width=15, height=3, font=("Arial 9 bold"), relief=RAISED, overrelief=RIDGE)
b_2.place(x=119, y=0)
b_3 = Button(frame_corpo, text="/", width=15, height=3, font=("Arial 9 bold"), relief=RAISED, overrelief=RIDGE)
b_3.place(x=235, y=0)

janela.mainloop()

