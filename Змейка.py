import math
# n = input('number =' )
n = 4

a = [[0]*(int(math.sqrt(n)))]*(int(math.sqrt(n)))


# def result_list(a):
#     for elem in a:
#         print (elem)
# result_list(a)

i = 0
j = -1
iDir = 0
jDir = 1
s = math.sqrt(n)
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
print(a)
