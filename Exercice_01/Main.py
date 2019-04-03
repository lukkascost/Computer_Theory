"""
Develop by: lucas costa
Date: 02/04/2019
github : https://github.com/lukkascost
"""
from Exercice_01.Models import AutomatonFD

""" 
Para executar é criado o objeto do tipo automato.
"""
automaton = AutomatonFD()

""" 
Posteriormente é inserido o alfabeto contendo os simbolos em uma unica string ou lista:
    Ex1: automaton.insert_alphabet("01")
    Ex2: automaton.insert_alphabet(["0","1"])
"""
automaton.insert_alphabet("01")

"""
Nesta etapa é necessario informar os estados possiveis em sequencia  como no exemplo abaixo:
    Ex: automaton.insert_states("q0", "q1")
"""
automaton.insert_states("q0", "q1")
automaton.set_initial_state("q0") ## Setando estado inicial

"""
Nesta etapa é necessario informar os estados finais em sequencia como no exemplo abaixo:
    Ex: automaton.set_final_states("q0", "q1")
"""
automaton.set_final_states("q1")


automaton.insert_transitions() ## Nesta etapa será necessario informar todas as transiçoes do automato.


print(automaton) ## Visualizaçao do automato

while(True):
    word = input("digite uma sequencia com simbolos validos a ser testada: ")
    result = automaton.process(word)
    print("Palavra: ", word, result[0], "no estado", result[1].name)
    print()
