# 1-  "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
arabalar = ['Bmw','Mercedes','Opel','Mazda']

# 2-  Liste Kaç elemanlıdır ?
 r=len(arabalar)
# 3-  Listenin ilk ve son elemanı nedir ?
 r=arabalar[0]
 r=arabalar[-1]
# 4-  Mazda değerini Toyota ile değiştirin.

r=arabalar[-1].replace('Mazda','Toyota')
 arabalar[-1]=r #yada
 arabalar[-1]='Toyota'

# 5-  Mercedes listenin bir elemanı mıdır ?

 r='Mercedes' in arabalar

# 6-  Listenin -2 indeksindeki değer nedir ?

 r=arabalar[-2]

# 7-  Listenin ilk 3 elemanını alın.

 r=arabalar[0:3]

# 8-  Listenin son 2 elemanı yerine "Totoya" ve "Renault" değerlerini ekleyin.

 arabalar[-2:] = ['Toyota','Renault']

# # 9-  Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.

 arabalar+['Audi','Nissan']

# # 10- Listenin son elemanını silin.

 del arabalar[-1]
 r=arabalar

# # 11- Liste elemanlarını tersten yazdırınız.

r=arabalar[::-1]

# 12- Aşağıdaki verileri bir liste içinde saklayınız.

      # studentA: Yiğit Bilgi 2010, (70,60,70)
      # studentB: Sena Turan  1999, (80,80,70)
      # studentC: Ahmet Turan 1998, (80,70,90)

studentA = ['Yiğit','Bilgi','2010',[70,60,70]]
studentB = ['Sena','Turan','1999',[80,80,70]]
studentC = ['Ahmet','Turan','1998',[80,70,90]]


# 13- Liste elemanlarını ekrana yazdırınız.

r=studentA[3][2]

r=f"{studentA[0]} {studentA[1]} {2020 - int(studentA[2])} yaşında  ve not ortalaması {(studentA[3][0]+studentA[3][1]+studentA[3][2])/len(studentA[3])} "

print(r)