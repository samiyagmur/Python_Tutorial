#1.soru
# def kelime(kelime='lütfen bir kelime giriniz'):
#     return kelime

# kelam=input('Göndermek istediğiniz kelimeyi giriniz: ')
# adet=int(input('Kelimenin kaç kez yazılacağını giriniz: '))

# for i in range(adet):
    
#     print(kelime(kelam))
#2.soru
# lste=[]
# def lst (parametr='parametre girmedniz: '):
#     return lste.append(parametr)

# while True:
#     lst(input('listenin parametrelerini giriniz: '))
#     if lste[-1] == 'son':
#         lste.pop(-1)
#         break

# print(lste)

#3.soru
def asal(sayi1,sayi2):

  
    for i in range(sayi1,sayi2):
        lst=[]
        for t in range(2,i):
            
            lst.append(t)
            print(lst)    
            if lstasal.count(i)==1 or lstnotasal.count(i)==1 :
                continue
                 
            if i%t==0:
                lstnotasal.append(i)
                
            else:
                lstasal.append(i)

lstasal=[]
lstnotasal=[]

sayi1=input('1.sayiyi giriniz: ')
sayi2=input('2.sayiyi giriniz: ')

asal(int(sayi1),int(sayi2))

print(lstasal)
print(lstnotasal)
                    
# def asal(sayi1,sayi2):                
#     a=0
#     lst=[sayi1:sayi2]
#     print(lst)
    
#     while a<len(lst):

#         if lst[a]%2==0:
            
#             lstnotasal.append(lst[a])
        
#         else:
#             lstasal.append(lst[a]) 
#     a += 1
   
# lst=[]               
# lstasal=[]
# lstnotasal=[]

# sayi1=input('1.sayiyi giriniz: ')
# sayi2=input('2.sayiyi giriniz: ')

# asal(int(sayi1),int(sayi2))

# print(lstasal)
# print(lstnotasal)

            

