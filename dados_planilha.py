import pandas as pd


class DadosPlanilha:
    def __init__(self):
        tabela = pd.read_excel("Arquivos/Planilhateste.xlsx")
        self.computadores = tabela["Name Computers"]
        self.nomes = tabela["Name"]
        self.email = tabela["Email"]
