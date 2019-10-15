
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


#########################################################################
#########################################################################
#########################################################################
#OBLICZENIA I ALGORYTMY




#Rownanie kwadratowe
#Napisz skrypt obliczający pierwiastki równania kwadratowego
#w postaci : y = ax2+bx+c. Wejściem skryptu są wartości: a, b, c

def square_roots(a, b, c):
    '''Calculation roots of quadratic equation

    The arguments are coefficients of quadratic equation
    in form like ax^2 + bx + c = 0:
    a -- next to x^2
    b -- next to x
    c -- free term
 
    Return one, two square roots or None
    '''
    
    delta = b**2 - 4*a*c
    
    if delta > 0:
        return (-b - 4**(1/2))/(2 * a), (-b + 4**(1/2))/(2 * a)
    elif delta == 0:
        return (-b)/(2 * a)
    else:
        return None


#Sortowanie
#Napisz skrypt sortujący liczby malejąco. Wygeneruj losowo 50
#liczb - wykorzystąj standardową funkcje do losowania. Z wbudowanej
#funkcji sortującej korzystaj tylko w celu weryfikacjiwyników
import random, time

def my_sort(ls):
    """Function to sort in decreasing order

    as input enter a list with unsorted numbers
    
    function return None, but its working on reference to
    a list, so te original will change
    """
    
    tmp = None
    cond = True
    
    while cond == True:             '''sorting until proper order (if condition
                                    always False after looking whole list)'''
        
        cond = False
        
        for index in range(1, len(ls)):            
            if ls[index] > ls[index - 1]:
                tmp = ls[index - 1]
                ls[index - 1] = ls[index]
                ls[index] = tmp
                
                cond = True
'''
to_sort = [int(random.random() * 100) for x in range(50)] #list to sort
to_my_sort = to_sort[:]  #copy for another algorithm

start = time.time()     #time check
my_sort(to_my_sort)
my_alg = time.time()
to_sort.sort(reverse = True)
python_alg = time.time()

print('is result the same? ', to_sort == to_my_sort)
print('my_time: ' + str(my_alg - start) + ', python alg time: ' + str(python_alg - my_alg))
'''

#Iloczyn skalarny
#Napisz skrypt obliczający wartość iloczynu dwóch wektorów:
#a = [1, 2, 12, 4], b = [2, 4, 2, 8], tzw. iloczyn skalarny wektorów



    
        
    













    
