import csv
from datetime import datetime


#escrevam o cógido abaixo do comentário com seu nome
#variaveis: tarefa, descricao, data, tipodetarefa
#objeto = agenda
#funcoes = imprimir_atrasadas(), cadastrar_tarefa(), editar_tarefa(), criar_arquivo(), ler_csv()

#DaNasser
def editar_tarefa(agenda):
    pesquisa = input("Digite o nome da sua tarefa que deseja atualizar: ")
    for  tarefa in agenda:
        if tarefa ['Tarefa'] == pesquisa:
            tarefa['Tarefa'] = input("Digite o nome da tarefa: ")
            tarefa['Lista'] = input("Digite a lista da sua tarefa: ")
            dia = int(input("Digite o dia de expiração: "))
            mes = int(input("Digite o mês de expiração: "))
            ano = int(input("Digite o ano de expiração: "))
            tarefa ['Data'] = datetime(ano,mes,dia)
            tarefa ['Status'] = input("Digite o status da atividade: ")
        else: 
            print("Tarefa não encontrada!")
    criar_arquivo()
        
#Vitotoso
def criar_arquivo():
    gravador = csv.writer(open('arquivo_agenda.csv', mode="w", newline='')) 
    gravador.writerow(["Tarefa","Lista","Data","Status"])
    
    for tarefa in agenda:
            
            gravador.writerow([tarefa['Tarefa'],tarefa['Lista'],tarefa['Data'],tarefa['Status']])

def ler_csv():
     with open('arquivo_agenda.csv', mode="r") as vararquivo:
        leitor = csv.DictReader(vararquivo)
        print("|  Tarefa  |  Lista  |  Data  | Status |")
        for linha in leitor:
            print(f"|  {linha['Tarefa']} |   {linha['Lista']}    |   {linha['Data']}    |   {linha['Status']}    |")            

#GitHug-o
def imprimir_atrasadas(agenda):
    for tarefa in agenda:
        if tarefa['Data'] < datetime.now() and tarefa['Status'] == "pendente":
            print(f"|  {tarefa['Tarefa']} |   {tarefa['Lista']}    |   {tarefa['Data']}    |   {tarefa['Status']}    |")
        else:
            print("Não há atividades atrasadas!")
    criar_arquivo()

def deletar_tarefa(agenda):
    pesquisa = input("Digite o nome que deseja excluir: ")
    for tarefa in agenda:
        if tarefa['Tarefa'] == pesquisa:
            agenda.remove(tarefa)
        else:
            print("Não há atividades atrasadas!")
    criar_arquivo()
   
#BernardoGuerino
def cadastrar_tarefa(agenda):
    nometarefa = input("Digite a tarefa que teve ser realizada : ")
    lista = input("Lista : ")
    dia = int(input("Digite o dia de expiração: "))
    mes = int(input("Digite o mês de expiração: "))
    ano = int(input("Digite o ano de expiração: "))
    data = datetime(ano,mes,dia)

    tarefa= {
        'Tarefa' : nometarefa,
        'Lista' : lista,
        'Data' : data,
        'Status' : "pendente"
    }
    agenda.append(tarefa)
    criar_arquivo()
    print("")
    print("Tarefa adicionada")
    print("")
    
agenda = []

while True:
    print("Bem-vindo!")
    print("Escolha uma ação:")
    print("1 - Nova tarefa!!!!!")
    print("2 - Atualizar tarefa")
    print("3 - Imprimir atrasadas")
    print("4 - Excluir tarefa")
    print("5 - Sair")

    opc = int(input(""))
    print("")
    
    if opc == 1:
        cadastrar_tarefa(agenda)
    elif opc == 2:
        editar_tarefa(agenda)
    elif opc == 3:
        imprimir_atrasadas(agenda)
    elif opc == 4:
        deletar_tarefa(agenda)
    elif opc == 5:
        break
