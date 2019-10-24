#ad.2
#Napisz skrypt, który pyta o imię, nazwisko i rok urodzenia
#(powinny być podane w jednej linii)


dane = input("Podaj: Imie, Nazwisko, Date urodzenia").split(' ')

print(dane)


#ad.3
#Napisz skrypt realizujący funkcję zamka szyfrowego. Prosi
#o podanie kodu i następnie sprawdza czy jest on zgodny z
#wcześniej wprowadzonym kodem


password = 'asd123'

write_password = input("Write your password")

if password == write_password:
    print('access granted')
else:
    print('access deny')
    
#ad.4
#Napisz skrypt zliczający ilość plików w katalogu /dev, skorzystaj
#ze standardowej biblioteki - os

import os

path = 'D:\Pobrane\ALDEC ACTIV HDL'
file_list = os.listdir(path)

print('\n'.join(file_list))

print('Amounth of files in directory: ', len(file_list))


#ad.4
#Napisz rekurencyjne przejście drzewa katalogów i wypisanie
#plików, które znajdują się w eksplorowanej strukturze

import os

path = 'D:\Pobrane\ALDEC ACTIV HDL'
stop_path= 'D:\ '

while path != stop_path[:-1]:
    print(path)
    print('\n'.join(os.listdir(path)))
    path = os.path.dirname(path)
print(path)
print('\n'.join(os.listdir(path)))

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
    
    while cond == True:                         #sorting until proper order (if condition
                                                #always False after looking whole list)
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

'''
import array

v1=[1,2,12,4]
v2=[2,4,2,8]

#v1 = input('write elements of first vector').split()
#v2 = input('write elements of second vector').split()

def Cross_Product(x,y):
    cProd=0
    for i in range(0, len(v1)):
        cProd = int(v1[i])*int(v2[i]) + cProd
    return cProd

suma = Cross_Product(v1,v2)

print(suma)
'''
######################
#OTHER WAY
######################

def dot_product(a, b):
    """Counting dot product of two 1D lists of the same size

    Input:
    a, b - lists with int values, len(a) == len(b)!!!
    Output:
    None, if lists aren't the same size or counted dot product
    """
    
    if len(a) != len(b):
        print("lists aren't the same size")
        return None
    else:
        return sum([a[index] * b[index] for index in range(len(a))])
'''
a = [1, 2, 12, 4]
b = [2, 4, 2, 8]
dot_product(a, b)
'''    
        
#Suma macierzy
#Napisz skrypt sumujący dwie macierze o rozmiarach 128x128.
#Wykorzystaj generator liczb losowych do wygenerowania
#macierzy.

def matrix_adder(matrix1, matrix2):
    """Funcktion which add two matrix

    Input:
    matrix1, matrix2 - to matrixes of the same size with numeric variables inside
    Output:
    Sum of two matrixes
    """
    
    try:
        
        x = []
        for row in range(len(matrix1)):
            x.append([matrix1[row][index] + matrix2[row][index]
                      for index in range(len(matrix1[row]))])
        return x
    
    except:
        print("Matrixes are differ in size or values aren't numeric")
        

a = [[1,2],[3,4]]
b = [[-1,-2],[-3,-4]]
matrix_adder(a,b)


#Mnożenie macierzy
#Napisz skrypt realizujący mnożenie dwóch macierzy o rozmiarach 8x8
import numpy as np

size = 8
array1 = np.random.randint(1,10,(size, size))
array2 = np.random.randint(1,10,(size, size))

array_multiplcation_score=np.multiply(array1, array2)

print(array_multiplcation_score)

#Napisz skrypt wyliczający wyznacznik macierzy wygenerowanej losowo


import numpy as np

def determinant(size = 8)
    array = np.random.randint(1,10,(size, size))
    return np.linalg.det(array)

#########################################################################
#########################################################################
#########################################################################







    


















    
