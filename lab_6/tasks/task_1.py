"""
Jesteś informatykiem w firmie Noe's Animals Redistribution Center.
Firma ta zajmuje się międzykontynentalnym przewozem zwierząt.
---------
Celem zadania jest przygotowanie funkcji pozwalającej na przetworzenie
pliku wejściowego zawierającego listę zwierząt do trasnportu.
Funkcja ma na celu wybranie par (samiec i samica) z każdego gatunku,
tak by łączny ładunek był jak najlżeszy (najmniejsza masa osobnika
rozpatrywana jest względem gatunku i płci).
---------
Na 1 pkt.
Funkcja ma tworzyć plik wyjściowy zwierający listę wybranych zwierząt
w formacie wejścia (takim samym jak w pliku wejściowym).
Wyjście ma być posortowane alfabetycznie względem gatunku,
a następnie względem nazwy zwierzęcia.
---------
Na +1 pkt.
Funkcja ma opcję zmiany formatu wejścia na:
"<id>_<gender>_<mass>"
(paramter "compressed") gdzie:
- "id" jest kodem zwierzęcia (uuid),
- "gender" to jedna litera (F/M)
- "mass" zapisana jest w kilogramach w notacji wykładniczej
z dokładnością do trzech miejsc po przecinku np. osobnik ważący 456 gramów
ma mieć masę zapisaną w postaci "4.560e-01"
---------
Na +1 pkt.
* Ilość pamięci zajmowanej przez program musi być stałą względem
liczby zwierząt.
* Ilość pamięci może rosnąć liniowo z ilością gatunków.
---------
UWAGA: Możliwe jest wykonanie tylko jednej opcji +1 pkt.
Otrzymuje się wtedy 2 pkt.
UWAGA 2: Wszystkie jednoski masy występują w przykładzie.
"""
from pathlib import Path
import csv
from collections import OrderedDict

def przelicz_mase(masa):
    liczba, slowo = masa.split()
    if slowo=="mg":
        return float(liczba)*1e-6
    if slowo=="g":
        return float(liczba)*1e-3
    if slowo=="kg":
        return float(liczba)
    if slowo=="Mg":
        return float(liczba)*1e3
        
def select_animals(input_path, output_path, compressed=False):
    zwierzaki={}
    with open(input_path) as _file:
        reader=csv.DictReader(_file,delimiter=",")
        for row in reader:
            if row['genus'] in zwierzaki.keys():
                if row['gender'] in zwierzaki[row['genus']].keys():
                    if przelicz_mase(row['mass']) < przelicz_mase(zwierzaki[row['genus']][row['gender']]['mass']):
                        zwierzaki[row['genus']][row['gender']]=row
                else:
                    zwierzaki[row['genus']][row['gender']]=row
            else:
                zwierzaki[row['genus']]={row['gender']:row}
    zwierzaki=OrderedDict(sorted((zwierzaki.items())))
    zwierzaki_sort=[]
    for i in zwierzaki.values():
        sortowanie_po_nazwie=[j for j in i.values()]
        sortowanie_po_nazwie.sort(key=lambda k:k['name'])
        zwierzaki_sort.extend(sortowanie_po_nazwie)
    with open(output_path,'w', newline='') as _file:
        if compressed:
            _file.write('uu')
            for i in zwierzaki_sort:
                i['mass']=f"{przelicz_mase(i['mass']):.3e}"
                if i['gender']=='female':
                    i['gender']='F'
                if i['gender']=='male':
                    i['gender']='M'
                zapis = csv.DictWriter(_file,['id','gender','mass'], extrasaction='ignore',delimiter='_')
        else:
            zapis = csv.DictWriter(_file, zwierzaki_sort[0].keys())
        zapis.writeheader()
        zapis.writerows(zwierzaki_sort)
        
if __name__ == '__main__':
    input_path = Path('s_animals.txt')
    output_path = Path('s_animals_s.txt')
    select_animals(input_path, output_path)
    with open(output_path) as generated:
        with open('s_animals_se.txt') as expected:
            assert generated.read() == expected.read()

    output_path = Path('s_animals_sc.txt')
    select_animals(input_path, output_path, True)
    with open(output_path) as generated:
        with open('s_animals_sce.txt') as expected:
            assert generated.read() == expected.read()
