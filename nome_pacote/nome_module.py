class NomeClasse:
    # __init__ é o construtor
    # self é a instância da classe
    # .caminho é um atributo da instância da classe 
    def __init__(self, caminho): 
        self.caminho = caminho

    def nome_funcao(self):
        try:
            with open(self.caminho, 'r') as arquivo:
                return arquivo.read()
        except FileNotFoundError:
            return "404"
        except Exception as e:
            print(f"Erro ao ler o arquivo: {e}")