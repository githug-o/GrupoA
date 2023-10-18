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
            dia = input("Digite o dia de expiração: ")
            mes = input("Digite o mês de expiração: ")
            ano = input("Digite o ano de expiração: ")
            tarefa ['Data'] = datetime(ano,mes,dia)
            tarefa ['Status'] = input("Digite o status da atividade: ")
        else: 
            print("Tarefa não encontrada!")
    def criar_arquivo():
        



#Vitotoso
def criar_arquivo():
    gravador = csv.writer(open('arquivo_produtos.csv', mode="w", newline='')) 
    gravador.writerow(["Tarefa","Lista","Data","Status"])
    
    for tarefa in agenda:
            
            gravador.writerow([tarefa['Tarefa'],tarefa['Lista'],tarefa['Data'],tarefa['Status']])


def ler_csv():
     with open('arquivo_produtos.csv', mode="r") as vararquivo:
        leitor = csv.DictReader(vararquivo)
        print("|  Tarefa  |  Lista  |  Data  | Status |")
        for linha in leitor:
            print(f"|  {linha['Tarefa']} |   {linha['Lista']}    |   {linha['Data']}    |   {linha['Status']}    |")            

#GitHug-o
def imprimir_atrasadas(agenda):
    for tarefa in agenda:
        if agenda['Data'] > datetime.now() and agenda['Status'] == "Concluido":
            print(tarefa)
        else:
            print("Não há atividades atrasadas!")
    criar_arquivo()

def deletar_tarefa(agenda):
    pesquisa = input("Digite o nome que deseja excluir: ")
    for tarefa in agenda:
        if agenda['Data'] > datetime.now() and agenda['Status'] == "Concluido":
            print(tarefa)
        else:
            print("Não há atividades atrasadas!")
    criar_arquivo()

    

#BernardoGuerino
def cadastrar_tarefa(agenda)
    tarefa= {
        'Tarefa' : input("Digite a tarefa que teve ser realizada "),
        'Lista' : input("Lista : "),
        'Data' : input("Digite a data "),
        'Status' : "Pendente"
    }
    agenda.append(tarefa)
    criar_csv()
    print("")
    print("Tarefa adicionada")
    print("")
    


