#1 cevap
# # fage=18
# # feducation='university'

# # name = input('Name= ')
# # surname = input('Surname= ')
# # age = input('Age= ')
# # education=input('Education= ')

# # if (fage < int(age)) and (education == feducation):

# #     print(f" {name} {surname}.You are{age} years old and you graduated from {education}.You can get driver's license")
        
# # else :
# #     print(f" {name} {surname}.You are{age} years old and you graduated from {education}.You can't get driver's license")
# #     if (fage > int(age)):
# #         print("Your age not yet for driver's licance")
# #     else:
# #         print("Your education level not yet for driver's licance")


# # #2.
# # totalexam=int(input('sınav sayısını giriniz = '))
# # i=0
# # grades = []
# # avarage=0
# # while (0 < totalexam):
    
    
# #     exam=input('Enter your '+str(totalexam)+'.exam grade = ')

# #     if (int(exam)>=0) and (int(exam)<=100):
        
# #         grades.append(exam)

# #         avarage=int(grades[i])+avarage
            
# #     else:
# #         print('Yalnış sınav notu girdiniz notunuz 0 ile 100 arasında olmalıdır.')
# #         totalexam += 1
# #         i -= 1

        
    
# #     totalexam -=1
# #     i += 1

# # print(grades)
# # print(avarage)
# # puan=avarage/len(grades)

# # print(puan)


# # if (0<puan) and (puan<25):
   
# #     print(f"Dönem ortalamanız={puan}.Notunuz 0'dır")

# # elif (25 <= puan) and (puan < 45):
# #     print(f"Dönem ortalamanız={puan}.Notunuz 1'dır")

# # elif (45 <= puan) and (puan < 55):
# #     print(f"Dönem ortalamanız={puan}.Notunuz 2'dır")

# # elif (55 <= puan) and (puan < 70):
# #     print(f"Dönem ortalamanız={puan}.Notunuz 3'dır")

# # elif (70 <= puan) and (puan < 84):
# #     print(f"Dönem ortalamanız={puan}.Notunuz 4'dır")

# # else:
# #     print(f"Dönem ortalamanız={puan}.Notunuz 5'dır")

#3


import datetime

trh=input("Aracın son servis zamanını girniz (gg.aa.yy)=")
trh=trh.split('.')
trh[0]=int(trh[0])
trh[1]=int(trh[1])
trh[2]=int(trh[2])

while True:

    if (0<trh[0]) and ((trh[0])<=30):

        if (0<trh[1]) and ((trh[1])<=12):       
           
            btrh=datetime.datetime.now()
            btrh=str(btrh).split()[0].split('-')[::-1]
            btrh[0]=int(btrh[0])
            btrh[1]=int(btrh[1])
            btrh[2]=int(btrh[2])
            

            while True:
                if (0<btrh[0]) and ((btrh[0])<=30):
                    if (0<btrh[1]) and ((btrh[1])<=12):
                        print(f'aracın son servis tarihi:{trh}.Bu günün tarhi:{btrh}')
                        servy=int(btrh[2]-trh[2])   	
                        serva=int(btrh[1]-trh[1])       
                        servg=int(btrh[0]-trh[0])  
                        
                        while True:                                                           
                                                        
                            if 0 <= servg:
                                
                                if  0 <= serva:
                                    
                                    if  0 <= servy:

                                        servzmn=[servg,serva,servy]

                                        
                                        if servy>10:
                                            print(f"Servis tarihiniz:{trh[0]}.{trh[1]}.{trh[2]+10}")
                                            print(f"Servis zamanınızın  { servy-10:} yıl,{serva} ay,{servg} gün geçmiştir.")
                                            quit();
                                        elif servy==10:
                                            print(f"Servis tarihiniz:{trh[0]}.{trh[1]}.{trh[2]+10}")
                                            print(f"Servis zamanınızın {serva} ay,{servg} gün geçmiştir.")
                                            quit();
                                        elif servy==9:
                                            print(f"Servis tarihiniz:{trh[0]}.{trh[1]}.{trh[2]+10}")
                                            print(f"Servis zamanınız gelmesine {12-serva} ay,{30-servg} gün kalmıştır.")
                                            quit();
                                        else:
                                            print(f"Servis tarihiniz:{trh[0]}.{trh[1]}.{trh[2]+10}")
                                            print(f"Servis zamanınız gelmesine {9-servy} yıl,{12-serva} ay,{30-servg} gün kalmıştır.")
                                            quit();
                                    else:        
                                        print('hatalı tarih girişi girişi!!!.Lütfen son servis zamanını tekrar giriniz')
                                        
                                        trh[0]=int(input('Aracın en son bakım tarihininin gününü giriniz:'))
                                        trh[1]=int(input('Aracın en son bakım tarihininin ayını giriniz:'))
                                        trh[2]=int(input('Aracın en son bakım tarihininin yılını giriniz:'))
                                        servy=btrh[2]-trh[2]
                                        
                                            
                                else:
                                    servy -= 1
                                    serva += 12
                                    
                            else:
                                serva -= 1
                                servg += 30    
                   
                    else:
                        print('Bu gün için Yalnış ay bilgisi giriniz lütfen tekrar deneyiniz.')
                        btrh[1]=int(input('bu ayı tekrar giriniz:'))
                            
                else:
                    print('Bu gün için yalnış gün bilgisi giriniz lütfen tekrar deneyiniz.')
                    btrh[0]=int(input('bu günü tekrar giriniz:'))
        
        else:
            print('Yalnış ay bilgisi giriniz lütfen tekrar deneyiniz.')
            trh[1]=int(input('ayı tekrar giriniz:'))
   
    else:
        print('Yalnış gün bilgisi giriniz lütfen tekrar deneyiniz.')
        trh[0]=int(input('günü tekrar  giriniz:'))    
        

