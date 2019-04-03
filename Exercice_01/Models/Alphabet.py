class Alphabet(object):
    def __init__(self):
        self.symbols = []

    def insert_symbol(self, symbol):
        self.symbols.append(symbol)


    def __str__(self):
        return "\tSymbols of alphabet: {}".format(self.symbols)