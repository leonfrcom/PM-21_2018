# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 17:58:41 2018

@author: leon-
"""

gueltige_nukleotide = ['A', 'T', 'G', 'C', 'a', 't', 'g', 'c', ' ']

# Molekulargewichte in mg/mol
# Nukleotidmonophosphate ohne 3'-OH-Gruppe
mw_a = 313210
mw_t = 304200
mw_g = 329210
mw_c = 289180
# freie OH-Gruppe am 3'-Ende eines DNA-Fragments
mw_oh = 17010


def hole_dna_sequenz():
    """Liefere eine vom Nutzer erfragte und validierte DNA-Sequenz.
    Um gültig zu sein, darf die Sequenz nur aus den Buchstaben
    A, G, T, C, a, g, t, c bestehen.
    """

    while True:
        sequence = input('Gib eine DNA-Sequenz ein: ')
        seq2 = list(sequence)
        erfolgreiche_validierung = 0
        a = 0
        while a+1 <= len(seq2):
            if seq2[a] in gueltige_nukleotide:
                a = a+1
                erfolgreiche_validierung = 1
            else:
                erfolgreiche_validierung = 0
                break
        
        # Hier fehlt natürlich noch die Validierung.
        # Dafür brauchst Du noch eine Schleife, in der jeder Buchstabe
        # der Eingabe auf Gültigkeit geprüft werden muss.
        # Für einen Anfänger ist das schon eine ordentlich harte Nuss,
        # die aber mit etwas Anstrengung zu knacken sein sollte.

        if erfolgreiche_validierung == 1:
            break
        else:
            # Dieser Teil wird ausgeführt wenn die Bedingung hinter if
            # nicht erfüllt war.
            print()
            print(
                'Bei der Eingabe handelt es sich nicht um eine gültige '
                'DNA-Sequenz!'
                )
            print()
            print()
        
    return sequence


seq = hole_dna_sequenz()
print("Eingelesene Sequenz:\n", seq)
print("Länge: ", len(seq))

seq = str(seq)

g = seq.count('g')+seq.count('G')
a = seq.count('a')+seq.count('A')
t = seq.count('t')+seq.count('T')
c = seq.count('c')+seq.count('C')

gc = ((g+c)/(g+a+t+c))*100
m = g*mw_g + a*mw_a + t*mw_t + c*mw_c

print("Base\tHäuigkeit\nG\t", g,"\nA\t", a, "\nT\t", t, "\nC\t", c)
print()
print("GC-Gehalt: ", gc, "%")
print()
print("Molekulargewicht: ", m, "g/mol")