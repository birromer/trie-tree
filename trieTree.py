import csv

class nodo(object):
    def __init__(self, valor = 0):
        self.filhos = [None]*26
        self.valor = valor

class trie(object):
    def __init__(self):
        self.raiz = nodo()
        
    def buscaPalavra(self, palavra, incrementa=0):
        raiz = self.raiz
        for i in range(len(palavra)):
            if raiz.filhos[ord(palavra[i])-ord('a')] == None:
                return False
            else:
                if i == len(palavra)-1:
                    if incrementa == 1:
                        raiz.valor += 1
                    return True
                else:
                    raiz = raiz.filhos[ord(palavra[i])-ord('a')]
        
    def inserePalavra(self, palavra):
        raiz= self.raiz
        
        if self.buscaPalavra(palavra):
            buscaPalavra(palavra, incrementa=1)
            print("Palavra ja existe, incrementando valor do nodo final")
            return True
            
        for i in range(len(palavra)):
            if raiz.filhos[ord(palavra[i])-ord('a')] == None:
                if i == len(palavra)-1:
                    print("Chegou no fim da palavra e inseriu nodo")
                    print(palavra[i])
                    raiz.filhos[ord(palavra[i])-ord('a')] = nodo(1)
                else:
                    print("Inseriu novo nodo")
                    print(palavra[i])
                    raiz.filhos[ord(palavra[i]) - ord('a')] = nodo()
            else:
                print("Passando para proximo nodo pois valor atual ja existe")
                raiz = raiz.filhos[ord(palavra[i]) - ord('a')]
            
    def vaiFundo(self, nod, pal):
        for i in range(26):
            if nod.filhos[i] != None:
                if nod.valor != 0:
                    return pal.append(str(i + ord('a')))
                    print(str(i+ord('a')))
                else:
                    self.vaiFundo(nod.filhos[i], pal)
    
    
    def buscaPalavras(self):
        raiz = self.raiz
        palavras = []
        
        for i in range(26):
            palavras.append(' ')
            pal = []
            pal = self.vaiFundo(raiz, pal)
            palavras.append(pal)
        
        return palavras
        
            
# =============================================================================
#     def salvaPalavras(self):
#         with open("saida.csv", 'w') as saida:
# =============================================================================
            

if __name__ == "__main__":
#    st = input("Digite a string: ")
    st = "querida quero quero"
    palavras = st.split()
    print(palavras)
    arvore = trie()
    for palavra in palavras:
        arvore.inserePalavra(palavra)
    pals = arvore.buscaPalavras()
    print(pals)
    
    