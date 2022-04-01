#range
# print(list(range(4,12,3)))#l4 ten 12 kadar 2şer liste oluşrturur.
# for item in range(3,10,2):#3 ten 10 a kdar sayıları 2şer,saydırır.
#     print(item),

#enumerate

# index = 0
# greeting = 'Hello There'

# for letter in greeting:
#     print(f'index:{index} letter:{greeting[index]}')
#     index +=1


# greeting = 'Hello There'

# for index,letter in enumerate(greeting):#enumerate her harf için bulunduğu index numarasını söyler.
#     print(f'index:{index} letter:{letter}')


#zip
lst1 = [1,2,3,4,5]
lst2 = ['a','b','c','d','e']

# print(list(zip(lst1,lst2)))#zip komutu iki listeyi bir birne eşitler
# #sonuç
# [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]

for item in zip(lst1,lst2):#sonuçları ayrı listeler halinde alt alta yazdırdık
    print(item)

#sonuc
# (1, 'a')
# (2, 'b')
# (3, 'c')
# (4, 'd')
# (5, 'e')

# for a,b in zip(lst1,lst2):#sonuçları bu şekilde liste dışına atabiliririz.
#     print(a,b)
# # sonuç
# # 1 a
# # 2 b
# # 3 c
# # 4 d
# # 5 e