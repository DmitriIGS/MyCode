'''На вход квадратное число (4,9,16,25, ... n).   
Нужно вывести числа от 1 до n в виде змейки. 

Пример вывода с n = 4:
[1, 2]
[4, 3]

С n = 16:
[1, 2, 3, 4]
[12, 13, 14, 5]
[11, 16, 15, 6]
[10, 9, 8, 7]
'''
import math

# n = input('number = ')
n = 4

a = [[0]*(int(math.sqrt(n)))]*(int(math.sqrt(n)))


def result_list(a):
    for elem in a:
        print (elem)
result_list(a)

i = 0
j = -1
iDir = 0
jDir = 1
s = math.sqrt(n) #кол-во элементов в одном списке 
k = 1
offset = 0
Direction = 0

while k <= n:
    i += iDir
    j += jDir
    a[i][j] = k
    # print(a)
    k += 1 
    
    if j == (s - offset - 1) and (Direction % 4 == 0): #заполнение вниз
        iDir = 1
        jDir = 0
        Direction += 1
    
    if i == (s - offset - 1) and (Direction % 4 == 1): #заполнение справа-налево
        iDir = 0
        jDir = -1
        Direction += 1
        
    if j == offset and (Direction % 4 == 2): #заполнение вверх
        iDir = -1
        jDir = 0
        Direction += 1
        
    if i == offset and (Direction % 4 == 3): #заполнение слева-направо 
        iDir = 0
        jDir = 1
        Direction += 1
    
    offset = ((Direction + 1) // 4)
result_list(a)
