import csv


#escrevam o cógido abaixo do comentário com seu nome
#variaveis: tarefa, descricao, data, tipodetarefa
#objeto = agenda
#funcoes = imprimir_atrasadas(), cadastrar_tarefa(), editar_tarefa(), criar_arquivo(), ler_csv()

#DaNasser



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



#BernardoGuerino



