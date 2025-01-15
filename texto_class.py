texto_class

class TextAnalyzer(object):
    def __init__(self, text):
        # remove punctuation and make text lowercase
        texto_formatado = text.replace("!", ".").replace("?", ".").replace(",", ".")
        texto_formatado = texto_formatado.lower()
        self.text = texto_formatado

    def freqAll(self):
        # split text into words
        palavras = self.text.split()  # Corrigido: usando self.text em vez de self.texttrans
        
        # Create dictionary using dictionary comprehension
        freqmap = {palavra: palavras.count(palavra) for palavra in set(palavras)}
        return freqmap  # Adicionado: retorno do dicionário
    
    def freqOf(self, word):
        # get frequency map
        frq = self.freqAll()
        if word in frq:
            return frq[word]
        else:
            return 0











