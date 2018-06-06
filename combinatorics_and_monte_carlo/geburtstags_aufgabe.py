# Geburtstagsparadoxon
#
# siehe auch:
# https://de.wikipedia.org/wiki/Geburtstagsparadoxon

import random

def choices(seq, k):
    result = []
    for n in range(k):
        result.append(random.choice(seq))
    return result

def calculate_likelihood_for_2_out_of_n(n):
    count_trials_with_people_with_same_birthday = 0
    trials = 10000
    for trial in range(trials):
        birthdays = set(choices(range(365), k=n))
        if len(birthdays) < n:
            count_trials_with_people_with_same_birthday += 1
    return count_trials_with_people_with_same_birthday / trials


def users_input():
    while True:
        eingabe = input('Anzahl personen:' )
        try:
            eingabe = int(eingabe)
            return eingabe
        except ValueError:
            print("Zahl eingaben")

eingabe = users_input()
loesung = calculate_likelihood_for_2_out_of_n(eingabe)
print(loesung)
loesung_prozent = loesung * 100
loesung_prozent = round(loesung_prozent, 2)
print(loesung_prozent, '%')
