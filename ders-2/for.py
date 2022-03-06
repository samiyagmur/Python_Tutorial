# numbers = [1,2,3,4,5]

# for num in  numbers:
#     print(num)

# numbers = [1,2,3,4,5]

# for num in  numbers:
#     print('hello') #listenin eleman sayısı kadar hello yazdırır.

# names= ['sami','yagmur','ömer']

# for name in names:
#     print(f'my name is {name}')#name içindeki isimleri tek tek bu satırdaki namein yerine koyarak yazdıracak

# name ='sami yagmur'

# for n in name:
#     print(n)
###cevap
# s
# a
# m
# i

# y
# a
# g
# m
# u
# r


# tuple = (1,2,3,4,5)

# for a in tuple:
#     print(a)
# #cevap
# 1
# 2
# 3
# 4
# 5
# tuple = ((1,2),(1,3),(3,5),(5,7))

# for a,b in tuple:
#     print(a)
#cevap
# 1
# 1
# 3
# 5
# tuple = ((1,2),(1,3),(3,5),(5,7))

# for a,b in tuple:
#     print(a,b)

# #cevap
# 1 2
# 1 3
# 3 5
# 5 7

# d= {'k1':1,'k2':2,'k3':3}

# for item in d:

#     print(item)

# #cevap
# k1
# k2
# k3
# d= {'k1':1,'k2':2,'k3':3}

# for item in d.items():

#     print(item)

# #cevap
# ('k1', 1)
# ('k2', 2)
# ('k3', 3)

d= {'k1':1,'k2':2,'k3':3}

for key,value in d.items():

    print(key,value)#Eğer sadece key bilgisini siresek key yazmamız yeterli 
    #Eğer value istersek value yazmamız yeterli
    #eğer her ikisini yazmak istersek bu şekilde kullanmamız gerekli