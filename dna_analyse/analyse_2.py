# -*- coding: utf-8 -*-
"""
Created on Sun May 13 11:57:05 2018

@author: leon-
"""

from math import *

#-------------
#lists and dictionaries
#-------------
options = [
        'DNA-Analysis', 'Aminoacid-Analysis'
        ]

options_dna = [
        'translate to amino acid sequence', 'Comparison of two sequences'
        ]

options_aa = [
        'translate to another coding', 'translate to mRNA-sequence', 'calculate percentage shares'
        ]

AS_3 = [
    'Ala', 'Arg', 'Asn', 'Asp', 'Cys', 'Gln', 'Glu', 'Gly', 'His',
    'Ile', 'Leu', 'Lys', 'Met', 'Phe', 'Pro', 'Ser', 'Thr', 'Trp',
    'Tyr', 'Val', 'Sec', 'Pyl'
    ]

AS_1 = [
    'A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K',
    'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V', 'U', 'O'
    ]

DNA = [
       'A', 'T', 'C', 'G'
       ]

dict_AS_3 = dict(zip(AS_3, AS_1))

dict_AS_1 = dict(zip(AS_1, AS_3))

dict_code = {
        'GGG': 'G', 'GGA': 'G', 'GGC': 'G', 'GGU': 'G',
        'GAG': 'E', 'GAA': 'E',
        'GAC': 'D', 'GAU': 'D',
        'GCG': 'A', 'GCA': 'A', 'GCC': 'A', 'GCU': 'A',
        'GUG': 'V', 'GUA': 'V', 'GUC': 'V', 'GUU': 'V',
        'AGG': 'R', 'AGA': 'R', 'AGC': 'S', 'AGU': 'S',
        'AAG': 'K', 'AAA': 'K',
        'AAC': 'N', 'AAU': 'N',
        'ACG': 'T', 'ACA': 'T', 'ACC': 'T', 'ACU': 'T',
        'AUG': 'M',
        'AUA': 'I', 'AUC': 'I', 'AUU': 'I',
        'CGG': 'R', 'CGA': 'R', 'CGC': 'R', 'CGU': 'R',
        'CAG': 'Q', 'CAA': 'Q',
        'CAC': 'H', 'CAU': 'H',
        'CCG': 'P', 'CCA': 'P', 'CCC': 'P', 'CCU': 'P',
        'CUG': 'L', 'CUA': 'L', 'CUC': 'L', 'CUU': 'L',
        'UGG': 'W',
        'UGC': 'C', 'UGU': 'C',
        'UAC': 'Y', 'UAU': 'Y',
        'UCG': 'S', 'UCA': 'S', 'UCC': 'S', 'UCU': 'S',
        'UUG': 'L', 'UUA': 'L',
        'UUC': 'F', 'UUU': 'F',
        'UAG': 'STOP', 'UGA': 'STOP', 'UAA': 'STOP'
        }

dictionaries = [
        dict_AS_1, dict_AS_3, dict_code
        ]

choice = [
        options, options_dna, options_aa
        ]


#-------------
#functions
#-------------
def which_coding():
    """
    this function should return the encoding in which the entry was made
    (1-letter or 3-letters).
    """
    pass

def validation(seq, signs, match_case=False):           #works
    if match_case == False:
        seq = seq.upper()
        signs = ''.join(signs).upper()
    for c in seq:
        if c not in signs:
            return False
    return True

def users_input(dna_aa, allowed_signs):                 #works
    while True:
        if dna_aa == 'dna':
            sequence = input('Please enter a DNA-sequence: ')

            if validation(sequence, DNA):
                return sequence.upper()

            print()
            print('no valid enry!')
            print()
            print()
        if dna_aa == 'aa':
            sequence = input('Please enter an amino acid-sequence: ')

            if validation(sequence, AS_1):
                return sequence

            print()
            print('no valid entry!')
            print()
            print()
            
                
def translate_to_another_coding(direction, input_seq):       #works
    inp = input_seq
    #users_input('aa', AS_1)
    inp = list(inp.upper())
    trans = []
    for i in inp:
        trans.append(direction[i])
    
    return trans

    
def translate_to_mrna_sequence():
    """
    this function should translate the entered sequence into
    a nucleotide sequence. All triplets that qualify for an amino
    acid should be written in parenthesis after the first choice of triplet.
    
    e.g.:
    entered aa-seq.:    ['Ala', 'Arg', 'Asn']
    output:             'GCG(GCA, GCC, GCU)-AGG(AGA)-AAC(AAU)'
    """
    pass


def calculate_percentage_shares():
    """
    this function should query which amino acids should be used to
    calculate their percentage shares.
    
    e.g.:
    entered aa-seq.:        ['Ala', 'Arg', 'Asn']
    which amino acids...?   'Ala'
    output:                 percentage share of Ala in amino acid sequence: 33.3%
    """
    pass


def comparison_of_two_sequences():
    """
    this function compares two DNA-sequences
    """
    pass


def find_start(codon):                              #works
    """
    this function looks for the firs start codon in the entered sequence.
    """
    a = 0
    for i in range(len(codon)):
        b = codon[i]
        if b == 'AUG':
            return a
            pass
        a = a+1
    print('no startcodon found')
    pass


def build_triplets(input_seq):                      #works
    """
    this function builds triplets from users input
    """
    input_seq = input_seq.replace('T', 'U')
    triplets_list = []
    for i in range(len(input_seq)-2):
        triplets = input_seq[i]+input_seq[i+1]+input_seq[i+2]
        triplets_list.append(triplets)
        
    return triplets_list


def translate_to_amino_acid_sequence():             #works
    """
    this function translates triplets to an amino acid sequence.
    """
    codons = build_triplets(users_input('dna', DNA))
    start = find_start(codons)
    del codons[0:start]

    DNA_seq = []
    b = 0
    for i in range(ceil(len(codons)/3)):
        DNA_seq.append(codons[b])
        b = b + 3
        
    trans = []
    for i in DNA_seq:
        trans.append(dict_code[i])
    return trans
    
    

def option(choice):                                 #works
    print()
    for i, item in enumerate(choice, 1):
        print(i, '-', item)

    while True:
        try:
            b = input('select an option-number: ')
            print()
            print()
            print()
            b = int(b)
            if b <= len(choice) and b > 0:
                return b
                pass
            else:
                pass
        except ValueError:
            print('bitte gültige Auswahl treffen.')


#--------------
#main
#--------------
if __name__ == '__main__':
#not completed at this version
    
    #option_1
    option_choice_num = option(choice[0])
    option_choice = options[option_choice_num-1]
    print('your choice:', option_choice)
    #option_2
    further_1_num = option(choice[option_choice_num])
    further_1 = choice[option_choice_num]
    further_1 = further_1[further_1_num-1]
    print('your choice:', further_1)
    further_1 = further_1.replace('-', '_').replace(' ', '_').lower()
    print(further_1)
    
    if further_1 == translate_to_another_coding:
        further_2 = eval(further_1 + '(dict_AS_1)')         #not correct at this version
    else:
        further_2 = eval(further_1 + '()')