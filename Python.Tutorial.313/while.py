# #1-100 e kdar

# x = 0

# while x <= 100:
#     print(x)
#     x += 1
# x = 0

# while x <= 100:
#     if x % 2 ==0 :
#         print(x)
    
#     x += 1


name = ''

while not name.strip():#strip girilen boşluk karakterlerini siler yok sayar.Böylece fazladan boşluk karakteri girilirse yok sayar.
    name=input('isminiz: ')

print(f'merhaba {name}')