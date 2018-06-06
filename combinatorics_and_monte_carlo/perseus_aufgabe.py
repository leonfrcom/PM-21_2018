# Perseus, Pegasus und Andromeda: eine Variante des Ziegenproblems
#
# siehe Seite 7 in:
# www.school-scout.de/vorschau/62770/mathematische-spiele-und-strategien-22012.pdf

import random


counter_andromeda_in_original_cave = 0
counter_andromeda_in_third_cave = 0

def monster_func():
    kein_monster = random.choice(caves)
    monster_liste = caves[:]
    monster_liste.remove(kein_monster)
    return monster_liste

def perseus_wahl():
    wahl = random.choice(caves)
    return wahl

def tipp_func(wahl, monster):
    if wahl in monster:
        monster.remove(wahl)
        return monster[0]
    else:
        n = random.randint(0, 1)
        return monster[n]

def perseus_wahl_2(tipp, wahl_1):
    caves.remove(tipp)
    wahl = random.choice(caves)
    if wahl == wahl_1:
        return wahl, '0'
    else:
        return wahl, '1'


trials = 10000
for trial in range(trials):
    caves = [1,2,3]
    auswahl = perseus_wahl()
    monster = monster_func()
    tipp = tipp_func(auswahl, monster)
    wahl_2, wert = perseus_wahl_2(tipp, auswahl)

    if wert == '1':
        if wahl_2 not in monster:
            counter_andromeda_in_third_cave += 1
            
            
            

# report results of simulation
print(
    'Reconsidering his original choice would have been good for Perseus in '
    '{0} out of {1} cases.'
    .format(counter_andromeda_in_third_cave, trials)
    )
