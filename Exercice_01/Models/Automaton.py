from Exercice_01.Models.Alphabet import Alphabet
from Exercice_01.Models.State import State
from Exercice_01.Models.Transition import Transition
import numpy as np


class AutomatonFD(object):
    def __init__(self):
        self.Q = []
        self.E = Alphabet()
        self.delta = []
        self.start = None
        self.end = []

    def insert_alphabet(self, symbols):
        for x in symbols:
            self.E.insert_symbol(x)

    def insert_states(self, *key):
        for i in key:
            self.Q.append(State(i))
        self.Q = np.array(self.Q)

    def insert_transitions(self):
        for i in self.Q:
            for j in self.E.symbols:
                while (True):
                    to = input("{} recebe {} vai para?: ".format(i, j))
                    if to in self.Q:
                        self.delta.append(Transition(i, self.Q[self.Q == to][0], j))
                        break
                    else:
                        print("ERROR: Estado nao encontrado digite novamente.")
        self.delta = np.array(self.delta)

    def set_initial_state(self, state):
        if state in self.Q:
            self.start = self.Q[self.Q == state][0]
        else:
            print("Estado nao encontrado!")

    def set_final_states(self, *key):
        for i in key:
            if i in self.Q:
                self.end.append(State(i))
            else:
                print("Estado '{}'nao encontrado!".format(i))

    def process(self, param):
        actual = self.start
        for i in param:
            ac = self.delta[self.delta == "S({},{})".format(actual.name, i)]
            actual = ac[0].end
        if actual in self.end:
            return "ACEITA", actual
        else:
            return "REJEITA", actual

    def __str__(self):
        result = ""
        result += "States: \n"
        for i in self.Q:
            result += str(i) + "\n"
        result += "Alphabet: \n" + str(self.E) + "\n"
        result += "Transitions: \n"
        for i in self.delta:
            result += str(i) + "\n"
        result += "Initial state: \n"
        if not (self.start is None):
            result += str(self.start) + "\n"
        result += "End states: \n"
        for i in self.end:
            result += str(i) + "\n"
        return result
