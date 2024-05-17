from tkinter import* 
variavel=Tk()
variavel2=StringVar()
lista=[]
def botoes(numero):
        return Button(variavel, text=str(numero), command=lambda: novo(str(numero)), width=6,height=4, padx=10, bg="lightgreen")

def novo(novo_texto):
        if novo_texto == "=":
                if "/" in variavel2.get():
                        lado = variavel2.get().split("/")
                        if len(lado) == 2:
                                lado1 = float(lado[0])
                                lado2 = float(lado[1])
                                resultado = lado1 / lado2
                                variavel2.set(str(resultado))
                        else:
                                variavel2.set("Apenas um calculo simples por vez")
                if "+" in variavel2.get():
                        lado=variavel2.get().split("+")
                        if len(lado)==2:
                                lado1=float(lado[0])
                                lado2=float(lado[1])
                                resultado=lado1+lado2
                                variavel2.set(str(resultado))
                        else:
                                variavel2.set("Apenas um calculo simples por vez")
                if "-" in variavel2.get():
                        lado=variavel2.get().split("-")
                        if len(lado)==2:
                                lado1=float(lado[0])
                                lado2=float(lado[1])
                                resultado=lado1-lado2
                                variavel2.set(str(resultado))
                        else:
                                variavel2.set("Apenas um calculo simples por vez")
                if "x" in variavel2.get():
                        lado=variavel2.get().split("x")
                        if len(lado)==2:
                                lado1=float(lado[0])
                                lado2=float(lado[1])
                                resultado=lado1*lado2
                                variavel2.set(str(resultado))
                        else:
                                variavel2.set("Apenas um calculo simples por vez")    
        else:
                                
                if "," in variavel2.get():
                        partes=variavel2.get().split(",")
                        if len(partes) == 2:
                                variavel2.set(".".join(partes))
                        
                        
                else:
                        variavel2.set(variavel2.get() + novo_texto)

#-----------------------------------------------------------------------------------
criar_espaco = Label(variavel, width=36, height=6, padx=10, textvariable=variavel2, relief=FLAT, bg="lightblue")
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
ac=Button(variavel, text=str("AC"), command=lambda:variavel2.set(""), width=6,height=4, padx=10, bg="lightgreen" ).grid(row=1, column=0)
divisao=Button(variavel,text="/", command=lambda: novo("/"), width=6,height=4, padx=10, bg="lightgreen").grid(row=1,column=2)
multiplicacao=Button(variavel, text="x", command=lambda: novo("x"), width=6,height=4, padx=10, bg="lightgreen").grid(row=1,column=3)
sub=Button(variavel, text="-", command=lambda: novo("-"), width=6,height=4, padx=10, bg="lightgreen").grid(row=2, column=3)
adicao=Button(variavel, text="+", command=lambda:novo("+"), width=6,height=4, padx=10, bg="lightgreen").grid(row=3, column=3)
igual=Button(variavel, text="=", command=lambda:novo("="), width=6,height=4, padx=10, bg="lightgreen").grid(row=4, column=3)
virgula=Button(variavel, text=",", command=lambda:novo(","), width=6,height=4, padx=10, bg="lightgreen").grid(row=1, column=1)
label1=Label(variavel,borderwidth=3, relief="raised", width=6,height=4, padx=10, bg="lightgreen").grid(row=5, column=0)
label2=Label(variavel,borderwidth=3, relief="raised", width=16,height=4, padx=10, bg="lightgreen").grid(row=5, column=2, columnspan=3)
variavel.title("calculadora")
variavel.geometry("280x447")
variavel.resizable(0,0)
variavel.state("zoomed")
variavel.state("iconic")
variavel.iconphoto(0,PhotoImage(file="C:\\Users\\Júlia\\Desktop\\tkinter\\icone.img\\icon.png"))
variavel['background']="lightpink"
variavel.mainloop()