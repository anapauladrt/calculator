from tkinter import* 
janela=Tk()
mudar_texto=StringVar()
lista=[]

def botoes(numero):
        return Button(janela, text=str(numero), command=lambda: novo(str(numero)), width=6,height=4, padx=10, bg="lightgreen")


def calcular(expressao):
        if 1:
                resultado = eval(expressao)
                return resultado
        else:
                resultado = "Erro"


def novo(novo_texto):
        if novo_texto == "=":
                if "0/0" in mudar_texto.get():
                        calculo=0.0
                        mudar_texto.set(calculo)
                if "/" in mudar_texto.get() or "+" in mudar_texto.get() or "-" in mudar_texto.get() or "x" in mudar_texto.get():
                        expressao = mudar_texto.get().replace('x', '*').replace(',', '.')
                        resultado = calcular(expressao)
                        mudar_texto.set(resultado)
                if "/" in mudar_texto.get():
                        lado = mudar_texto.get().split("/")
                        if len(lado) == 2:
                                lado1 = float(lado[0])
                                lado2 = float(lado[1])
                                resultado = lado1 / lado2
                                mudar_texto.set(resultado)
                        else:
                                mudar_texto.set("Apenas um calculo simples por vez")
                if "+" in mudar_texto.get():
                        lado=mudar_texto.get().split("+")
                        if len(lado)==2:
                                lado1=float(lado[0])
                                lado2=float(lado[1])
                                resultado=lado1+lado2
                                mudar_texto.set(resultado)
                        else:
                                mudar_texto.set("Apenas um calculo simples por vez")
                if "-" in mudar_texto.get():
                        lado=mudar_texto.get().split("-")
                        if len(lado)==2:
                                lado1=float(lado[0])
                                lado2=float(lado[1])
                                resultado=lado1-lado2
                                mudar_texto.set(resultado)
                        else:
                                mudar_texto.set("Apenas um calculo simples por vez")
                if "x" in mudar_texto.get():
                        expressao = mudar_texto.get().replace('x', '*').replace(',', '.')
                        resultado = calcular(expressao)
                        mudar_texto.set(resultado)
        else:
                                
                if "," in mudar_texto.get():
                        partes=mudar_texto.get().split(",")
                        if len(partes) == 2:
                                mudar_texto.set(".".join(partes))
                        
                        
                else:
                        mudar_texto.set(mudar_texto.get() + novo_texto)

#-----------------------------------------------------------------------------------
criar_espaco = Label(janela, width=36, height=6, padx=10, textvariable=mudar_texto, relief=FLAT, bg="lightblue")
criar_espaco.grid(row=0,column=0, columnspan=4)
for numero in range(0,10):
        botao = botoes(numero)
        lista.append(botoes(numero))
botoes(1).grid(row=4, column=0) 
botoes(2).grid(row=4, column=1)
botoes(3).grid(row=4, column=2)
botoes(4).grid(row=3, column=0)
botoes(5).grid(row=3, column=1)
botoes(6).grid(row=3, column=2)
botoes(7).grid(row=2, column=0)
botoes(8).grid(row=2, column=1)
botoes(9).grid(row=2, column=2)
botoes(0).grid(row=5, column=1)
ac=Button(janela, text=str("AC"), command=lambda:mudar_texto.set(""), width=6,height=4, padx=10, bg="lightgreen" ).grid(row=1, column=0)
divisao=Button(janela,text="/", command=lambda: novo("/"), width=6,height=4, padx=10, bg="lightgreen").grid(row=1,column=2)
multiplicacao=Button(janela, text="x", command=lambda: novo("x"), width=6,height=4, padx=10, bg="lightgreen").grid(row=1,column=3)
sub=Button(janela, text="-", command=lambda: novo("-"), width=6,height=4, padx=10, bg="lightgreen").grid(row=2, column=3)
adicao=Button(janela, text="+", command=lambda:novo("+"), width=6,height=4, padx=10, bg="lightgreen").grid(row=3, column=3)
igual=Button(janela, text="=", command=lambda:novo("="), width=6,height=4, padx=10, bg="lightgreen").grid(row=4, column=3)
virgula=Button(janela, text=",", command=lambda:novo(","), width=6,height=4, padx=10, bg="lightgreen").grid(row=1, column=1)
label1=Label(janela,borderwidth=3, relief="raised", width=6,height=4, padx=10, bg="lightgreen").grid(row=5, column=0)
label2=Label(janela,borderwidth=3, relief="raised", width=16,height=4, padx=10, bg="lightgreen").grid(row=5, column=2, columnspan=3)
janela.title("calculadora")
janela.geometry("280x447")
janela.resizable(0,0)
janela.state("zoomed")
janela.state("iconic")
janela.iconphoto(0,PhotoImage(file="C:\\Users\\Júlia\\Desktop\\Nova pasta (2)\\calculadora.png"))
janela['background']="green"
janela.mainloop()
