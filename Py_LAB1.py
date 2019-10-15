
#Konwersja rozszerzenia
#Napisz skrypt konwersji rozszerzeń plików *.jpg na
#*.png (uprzednio stwórz zestaw 4 plików z rozszerzeniem *.jpg)
'''
from PIL import Image

im = Image.open("aaa.jpg")
rgb_im = im.convert('RGB')
rgb_im.save('bbb.png')
'''


#########################################################################
#########################################################################
#########################################################################
#TEKST




#Usuwanie słów
#Napisz skrypt usuwający z wejściowego ciągu tekstowego
#(wybierz kilka plików z repozytorium: Tekstowego) następujące
#słowa : się, i, oraz, nigdy, dlaczego
'''
file_to_change = input('enter path to text file which you want to change')

to_remove = [' się ', ' i ', ' oraz ', ' nigdy ', ' dlaczego ']
with open(file_to_change, 'r+') as file:
    txt = file.read()
    file.truncate(0)
    for string in to_remove:
        txt = txt.replace(string,' ')
    file.write(txt)
'''


#Podmienianie słów
#Napisz skrypt zmieniający w podanym ciągu wejściowym
#(wybierz kilka plików z repozytorium: Tekstowego) następujące
#słowa : i, oraz, nigdy, dlaczego na następujący zestaw słów : oraz,
#i, prawie nigdy, czemu. Zalecaną strukturą jest słownik.
'''
to_remove = {'i' : 'oraz', 'oraz' : 'i', 'nigdy' : 'prawie nigdy', 'dlaczego' : 'czemu'}

file_to_change = input('enter path to text file which you want to change')

with open(file_to_change, 'r+') as file:
    txt = file.read()
    file.truncate(0)
    for k in to_remove:
        txt = txt.replace(k, to_remove[k])
    file.write(txt)
'''




    
