"""
Develop by: lucas costa
Date: 02/04/2019
github : https://github.com/lukkascost
"""
from Exercice_01.Models import AutomatonFD

automaton = AutomatonFD()
automaton.insert_alphabet("01")
automaton.insert_states("q0", "q1")
automaton.insert_transitions()
automaton.set_initial_state("q0")
automaton.set_final_states("q1")
print(automaton)

words = ["00000", "1111", "10101"]
for word in words:
    result = automaton.process(word)
    print("Palavra: ", word, result[0], "no estado", result[1].name)
