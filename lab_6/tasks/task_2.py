"""
Na (1 pkt.):
Napisz program do sprawdzenia poprawności skompresowanego wyjścia poprzedniej
funkcji.
Funkcja MUSI w swej implementacji korzystać z wyrażeń regularnych.

Funkcja na wejściu przyjmuje nazwę pliku do sprawdzenia, na wyjściu zwraca
dwuelementową tuplę zawierającą liczbę poprawnych wierszy:
- na indeksie 0 płeć F
- na indeksie 1 płeć M
"""
import re
from pathlib import Path


def check_animal_list(file_path):
    F=0
    M=0
    chars='[\da-fA-F]'
    id=f'{chars}{{4}}-'
    id_chars=f'{chars}{{8}}-{id*3}{chars}{{12}}'
    gender_chars='[FM]'
    mass_chars=r'\d\.\d{3}e[-\+]\d{2}\n'
    full_word=f'{id_chars}_{gender_chars}_{mass_chars}'
    with open(Path(file_path)) as _file:
        _file.readline()
        rows=_file.readlines()
    for i in rows:
        if re.fullmatch(full_word,i):
            if re.search('_F_',i):
                F+=1
            else:
                M+=1
    return F,M

if __name__ == '__main__':
    assert check_animal_list('s_animals_sce.txt') == (2, 2)
    assert check_animal_list('animals_sc_corrupted.txt') == (5, 1)
