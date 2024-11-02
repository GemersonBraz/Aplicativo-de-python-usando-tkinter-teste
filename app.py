from tkinter import * 
import tkinter as tk
from tkinter import ttk
import openpyxl
from datetime import datetime

#Backend
def cadastrar(documento, nome, validade, militar, veiculo, placa, cor):
    print("Cadastro Realizado:")
    print(f"Documento: {documento}")
    print(f"Nome: {nome}")
    print(f"Validade: {validade}")
    print(f"É Militar: {militar}")
    print(f"Veículo: {veiculo}")
    print(f"Placa: {placa}")
    print(f"Cor: {cor}")



    

#---------------------------------------------------------------------------------------------

def mudar_tema():
    if botao_tema.instate(["selected"]):
        style.theme_use("forest-light")
    else:
        style.theme_use("forest-dark")


def formatar_placa(event,placa):

    # Obtém o valor da placa até agora
    texto = placa.get()

    # Remove caracteres não alfabéticos e não numéricos
    texto = ''.join(filter(lambda x: x.isalnum(), texto))

    # Verifica se a placa está nos formatos válidos
    if len(texto) <= 3:  # Se a entrada tem até 3 caracteres, mantém
        texto = texto.upper()  # Garante que as letras estejam em maiúsculas
    elif len(texto) == 4:  # Se a entrada tem 4 caracteres
        texto = texto[:3].upper() + texto[3]  # A 4ª letra pode ser minúscula
    elif len(texto) >= 5:  # Se a entrada tem 5 ou mais caracteres
        # Formata para 'xxx0x00' ou 'xxx0000'
        if len(texto) <= 7:
            texto = (
                texto[:3].upper() +  # 1ª, 2ª e 3ª letras maiúsculas
                texto[3].upper() +   # 4ª letra (número) deve ser mantida
                texto[4].upper() +   # 5ª letra maiúscula
                texto[5:7]           # 6ª e 7ª letras
            )
        else:
            texto = texto[:3].upper() + texto[3:7]  # Formato 'xxx0000'

    # Atualiza o campo com o texto formatado
    placa.delete(0, tk.END)
    placa.insert(0, texto)
    



def formatar_validade(event,validade):
    
    # Obtém o texto digitado até agora
    texto = validade.get()

    # Remove qualquer caractere que não seja dígito para simplificar
    texto = ''.join(filter(str.isdigit, texto))

    # Formata automaticamente no estilo DD/MM/AAAA
    if len(texto) > 2 and len(texto) <= 4:
        texto = texto[:2] + '/' + texto[2:]
    elif len(texto) > 4:
        texto = texto[:2] + '/' + texto[2:4] + '/' + texto[4:8]

    # Validação do mês e do dia
    if len(texto) >= 5:
        dia = int(texto[:2])
        mes = int(texto[3:5]) if len(texto) > 2 else 0  # O mês começa no índice 3

        # Verifica se o mês é maior que 12
        if mes > 12:
            mes = 12
            texto = f"{dia:02}/{mes:02}/{texto[6:]}"  # Corrige o mês

        # Verifica se o dia é maior que 31
        if dia > 31:
            dia = 31
            texto = f"{dia:02}/{mes:02}/{texto[6:]}"  # Corrige o dia

    # Atualiza o campo com o texto formatado
    validade.delete(0, tk.END)
    validade.insert(0, texto)

def nova_janela_cadastro():
    # Cria uma nova janela (janela secundária)
    nova_janela = tk.Toplevel(root)
    nova_janela.title("Cadastro")  # Título da janela (sem exibição na interface principal)

    # Frame principal com texto de instrução
    frame_principal = ttk.Frame(nova_janela)
    frame_principal.pack(padx=10, pady=10, fill="both")

    # Texto de instrução no topo
    label_instrucao = ttk.Label(frame_principal, text="Insira os Dados", font=("Arial", 14))
    label_instrucao.grid(row=0, column=0, columnspan=2, pady=(0, 10), sticky="ew")
    label_instrucao.config(anchor="center") # Centraliza o texto dentro do Label

    # Documento
    ttk.Label(frame_principal, text="Documento: ").grid(row=1, column=0, padx=(5), pady=5, sticky="w")
    documento = ttk.Entry(frame_principal)
    documento.insert(0, "Documento")
    documento.bind("<FocusIn>", lambda e: documento.delete(0, "end"))
    documento.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    # Nome
    ttk.Label(frame_principal, text="Nome: ").grid(row=2, column=0, padx=(5), pady=5, sticky="w")
    nome = ttk.Entry(frame_principal)
    nome.insert(0, "Nome")
    nome.bind("<FocusIn>", lambda e: nome.delete(0, "end"))
    nome.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

    # Validade do Documento
    ttk.Label(frame_principal, text="Validade do Documento:").grid(row=3, column=0, padx=(5), pady=5, sticky="w")
    validade = ttk.Entry(frame_principal)
    validade.insert(0, "Validade")
    validade.bind("<FocusIn>", lambda e: validade.delete(0, "end"))
    validade.bind("<KeyRelease>", lambda event: formatar_validade(event, validade))
    validade.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

    # É Militar (Sim ou Não)
    ttk.Label(frame_principal, text="Militar?").grid(row=4, column=0, padx=(5), pady=5, sticky="w")
    militar_var = tk.StringVar(value="N")  # Valor padrão "Não"
    radio_sim = ttk.Radiobutton(frame_principal, text="Sim", variable=militar_var, value="S")
    radio_nao = ttk.Radiobutton(frame_principal, text="Não", variable=militar_var, value="N")
    radio_sim.grid(row=4, column=1, padx=(5, 25), pady=5, sticky="e")
    radio_nao.grid(row=4, column=1, padx=(25, 0), pady=5, sticky="w")  # Alinhamento dos botões

    # Veículo
    ttk.Label(frame_principal, text="Veículo: ").grid(row=5, column=0, padx=(5), pady=5, sticky="w")
    veiculo = ttk.Entry(frame_principal)
    veiculo.insert(0, "Veículo")
    veiculo.bind("<FocusIn>", lambda e: veiculo.delete(0, "end"))
    veiculo.grid(row=5, column=1, padx=5, pady=5, sticky="ew")

    # Placa
    ttk.Label(frame_principal, text="Placa: ").grid(row=6, column=0, padx=(5), pady=5, sticky="w")
    placa = ttk.Entry(frame_principal)
    placa.insert(0, "Placa")
    placa.bind("<FocusIn>", lambda e: placa.delete(0, "end"))
    placa.bind("<KeyRelease>", lambda event: formatar_placa(event, placa))
    placa.grid(row=6, column=1, padx=5, pady=5, sticky="ew")

    # Cor
    ttk.Label(frame_principal, text="Cor: ").grid(row=7, column=0, padx=(5), pady=5, sticky="w")
    cor = ttk.Combobox(frame_principal, values=["Branco", "Preto", "Cinza", "Prata", "Vermelho", "Verde", "Amarelo", "Azul", "Dourado", "Vinho"])
    cor.grid(row=7, column=1, padx=5, pady=5, sticky="ew")

    # Botão para salvar o cadastro
    botao_salvar = ttk.Button(frame_principal, text="Salvar Cadastro", command=lambda: cadastrar(
        documento.get(),
        nome.get(),
        validade.get(),
        militar_var.get(),
        veiculo.get(),
        placa.get(),
        cor.get()
    ))
    botao_salvar.grid(row=8, column=0, columnspan=2, padx=5, pady=(10, 5), sticky="ew")


    



#---------------------------------------------------------------------------------


#iniciando nossa janela

root = tk.Tk()
#titulo do app
root.title("Cadastro de Entrada")

#configuração do nosso tema
style = ttk.Style(root)
root.tk.call("source", "forest-light.tcl")
root.tk.call("source", "forest-dark.tcl")

style.theme_use("forest-dark")

#criando o espacos para os objetos frame principal
frame_principal = ttk.Frame( root)
frame_principal.pack()

widgets_frame = ttk.LabelFrame( frame_principal, text="Insira os dados")
widgets_frame.grid(row=0, column=0, padx=10, pady=10)

#criando os campos do nosso formulario
inserir_cadastro = ttk.Entry(widgets_frame)
inserir_cadastro.insert(0,"Cadastro")
inserir_cadastro.bind("<FocusIn>", lambda e:inserir_cadastro.delete("0","end"))
inserir_cadastro.grid(row=0,column=0,padx=5,pady=5,sticky="ew")


#botao para cadastro
botao_novo_cadastro = tk.Button(widgets_frame, text="Novo Cadastro", command=nova_janela_cadastro)
botao_novo_cadastro.grid(row=1,column=0,padx=5,pady=5,sticky="ew")

#separador
separador = ttk.Separator(widgets_frame)
separador.grid(row=2,column=0,padx=5,pady=5,sticky="ew")

#switch do tema
botao_tema = ttk.Checkbutton(widgets_frame,text="Tema",style="Switch",command=mudar_tema)
botao_tema.grid(row=3,column=0,padx=50,pady=(5,10),sticky="ew")


#criando a treeview do banco de dados
treeFrame = ttk.Frame(frame_principal)
treeFrame.grid(row=0, column=1,padx=(0,20),pady=10)
treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side="right",fill="y")

colunas = ("Documento","Nome","Validade","Militar","Veiculo","Placa","Cor","Destino","Hora","OBS")
treeview = ttk.Treeview(treeFrame, show="headings", yscrollcommand=treeScroll.set, columns=colunas, height=20)

treeview.column("Documento",width=100)
treeview.column("Nome",width=100)
treeview.column("Validade",width=100)
treeview.column("Militar",width=100)
treeview.column("Veiculo",width=100)
treeview.column("Placa",width=100)
treeview.column("Cor",width=100)
treeview.column("Destino",width=100)
treeview.column("Hora",width=100)
treeview.column("OBS",width=100)


treeview.pack()
treeScroll.config(command=treeview.yview)





#rodando nossa janela
root.mainloop()
"""
#na segunda tela teremos o cadastro dos seguintes elementos


"""
#validade

#émilitar?
#veiculo
#cor
#placa
#destino
#hora





#botao editar cadastro
#
#
#
#


#
#
#
#
#

