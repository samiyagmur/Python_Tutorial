# number=int(input('Bir sayı giriniz='))

# result=(0 <= number) and (number <= 100)


# if result == True:

#     result=('evet')
#     print(f"Giririlen sayı 0-100 arasındamı:{result}")
# else:
#     result=('hayır')
#     print(f"Giririlen sayı 0-100 arasındamı:{result}")

#################

# number=int(input('Bir sayı giriniz='))
# pozitif=(0<number)
# cift=(number%2==0)
# result = cift and pozitif

# if result == True:
    
#     result=('Evet')
#     print(f"Giririlen sayı hem pozitif hem çift bir sayımıdır:{result}")

# else:
#     result=('Hayır')
#     print(f"Giririlen sayı hem pozitif hem çift bir sayımıdır:{result}")
#     if pozitif== True:
#         print(f"Sayı pozitiftir fakat çift değildir.")
#     elif cift == True:
#         print(f"Sayı çifttir fakat pozitif değildir.")
#     else:
#         print(f"Sayı hem çift değildir hemde pozitif değildir.")
################################
# comparison=[]
# quantity=int(input('Karşılaştırılacak sayı miktarını giriniz : '))
# i=1
# while (0<quantity):
    
    
#     a=int(input(f'{i}.sayı giriniz='))
#     comparison.append(a)
#     i += 1
#     quantity -= 1

# comparison.sort()

# print(comparison)
# print(f"Girilen sayılardan en büyüğü : {comparison[-1]}")
####################################################


# vize1=int(input('1. vize notunu giriniz='))
# vize2=int(input('2. vize notunu giriniz='))
# final=int(input('Final notunu giriniz='))

# while True:
    
#     if (0 <= vize1 <=100) and (0 <= vize2 <=100) and (0 <= final <=100):
#         lst=[(vize1*0.3+vize2*0.3),(final*0.4)]
#         i=0
#         ort=0
#         while i < len(lst):    
#             ort=lst[i]+ort
#             i +=1
    
    
#         if ((50<=ort) and (50<=final)):

#             print(f"Tebrikler ortalama notunuz {ort}'dir.Dersten geçtiniz.")
#             quit();
#         elif (70<=final) and (ort<50):
#             print(f"Tebrikler ortalama notunuz {ort} olmasına rağmen final notunuzu {final} olduğu için.Dersten geçtiniz.")
#             quit();
#         else:
#             print(f"Üzgünüm ki ortalama notunuz {ort}'dir.Dersten kaldınız.")
#             quit();


#     elif (0 <= vize1 <=100) == False:
#         print("vize 1 notunu yalnış girdiniz.")
#         vize1=int(input('1. vize notunu giriniz='))
#     elif (0 <= vize2 <=100) == False:
#         print("vize 2 notunu yalnış girdiniz.")
#         vize2=int(input('2. vize notunu giriniz='))
#     elif (0 <= final <=100) == False:
#         print("final notunu yalnış girdiniz.")
#         final=int(input('Final notunu giriniz='))
#     else:print('son')
#########################################

ad=input('Adınız : ')
soyad=input('Soyadınız : ')
boy=int(input('Boyunuz :(.,.) '))
kg=int(input('Kilonuz : '))

index=(kg)/(boy**2)

if (0 <= index) and (index <= 18.4):
    print(f'{ad} {soyad} Zayıfsınız')
elif  (18.5 <= index) and (index <= 24.9):
    print(f'{ad} {soyad} Kilonuz normaldir')
elif  (25 <= index) and (index <= 29.9):
    print(f'{ad} {soyad} Fazla kilolusunuz')
elif  (30 <= index) and (index <= 34.9):
    print(f'{ad} {soyad} Obezsiniz')
else:
    print('yalnış giriş yaptınız')


