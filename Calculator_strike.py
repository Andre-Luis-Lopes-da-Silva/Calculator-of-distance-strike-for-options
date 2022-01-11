from tkinter import *
from yahoo_fin import stock_info

def calcular():
    cotacao1 = float(stock_info.get_live_price(cotacao.get()+'.SA')) # get the new value of the stock
    
    strike1 = float(strike.get())

    distancia = ((strike1/cotacao1)-1)*100 

    resposta['text'] = distancia

janela = Tk()
janela.title('Calculator of strike price distance for options')
janela.geometry('450x100')
janela.resizable(False, False)

Label(janela, text='Estimate the distance in percent of the strike of an option').grid(row=0, column=0, columnspan=2)

Label(janela, text='Insert the stock ticket:').grid(row=1, column=0)

cotacao = Entry(janela)
cotacao.grid(row=1, column=1)

Label(janela, text='Insert the option strike:').grid(row=2, column=0)

strike = Entry(janela)
strike.grid(row=2, column=1)

Button(janela, text='Calculate', command=calcular).grid(row=3, column=0)

resposta = Label(janela, text='')
resposta.grid(row=3, column=1)

janela.mainloop()
