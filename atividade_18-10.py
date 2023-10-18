import csv


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



#GitHug-o



#BernardoGuerino


