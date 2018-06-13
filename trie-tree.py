import csv

class nodo(object):
    def __init__(self, valor=0):
        self.filhos = [None]*26
        self.valor= valor
    
class trie(object):
    def __init__(self):
        self.raiz = nodo()
    
    def buscaPalavra(self, palavra, incrementa=0):
        raiz = self.raiz
        for i in range(len(palavra)):
            if raiz.filhos[ord(palavra[i]) - ord('a')] == None:
                return False
            else:
                if i == len(palavra)-1:
                    if incrementa == 1:
                        raiz.filhos[ord(palavra[i]) - ord('a')].valor+=1
#                        print(raiz.valor)
                    return True
                else:
                    raiz = raiz.filhos[ord(palavra[i]) - ord('a')]

    
    def inserePalavra(self, palavra):
        raiz = self.raiz
        if self.buscaPalavra(palavra):
            self.buscaPalavra(palavra, incrementa=1)
#            print("Palavra ja existem incrementando valor do nodo final")
#            print(palavra[-1])
            return True
    
        for i in range(len(palavra)):
            if raiz.filhos[ord(palavra[i]) - ord('a')] == None:
                if i == len(palavra)-1:
                    raiz.filhos[ord(palavra[i]) - ord('a')] = nodo()
                    raiz.filhos[ord(palavra[i]) - ord('a')].valor=1
#                    print("Chegou no fim da palavra e inseriu o nodo")
#                    print(raiz.valor)
#                    print(palavra[i])
                    return True
                else:
                    raiz.filhos[ord(palavra[i]) - ord('a')] = nodo()
                    raiz = raiz.filhos[ord(palavra[i]) - ord('a')]
#                    print("Inseriu nodo")
#                    print(palavra[i])
            else:
                raiz = raiz.filhos[ord(palavra[i]) - ord('a')]
#                print("Nodo ja existe, atualizando raiz")
#                print(palavra[i])
                
    def vaiFundo(self, nod, palavra, palavras, valores, charAtual):
        if nod != None:
            if nod.valor != 0:
                palavras.append(palavra)
                valores.append(nod.valor)
            for i in range(26):
                novaPal = palavra + chr(i + ord('a'))
                self.vaiFundo(nod.filhos[i], novaPal, palavras, valores, chr(i + ord('a')))
    
    def buscaPalavras(self):
        raiz = self.raiz
        palavras = []
        valores = []
        self.vaiFundo(raiz, "", palavras, valores, '')
        return [palavras, valores]
            
    def geraSaida(self, arquivo):
        palsM = self.buscaPalavras()
        with open(arquivo, 'w') as f:
            topo = ['palavra', 'ocorrencias']
            writer = csv.DictWriter(f, topo)
            writer.writeheader()
            for i in range(len(palsM[0])):
                writer.writerow({'palavra': palsM[0][i], 'ocorrencias': palsM[1][i]})
                
    
    
if __name__ == "__main__":
    entrada = input("Digite a string de entrada: ")
#    entrada = "querida queremos ate quero quero"
    
    palavras = entrada.split()
    arvore = trie()
    pals = []
    
    for palavra in palavras:
        arvore.inserePalavra(palavra)
#    palsM = arvore.buscaPalavras()
    arvore.geraSaida("saida.csv")
    
