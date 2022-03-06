i=1
student={}
while i<3 :

    no=input('okul numarası: ')

    isim=input('ad: ')

    soyisim=input('soyad: ')

    telefon=input('tel: ')

    student[no] = {

    'ad :' : isim,
    'soyad :' : soyisim,
    'tel :' : telefon


    }

    print(i,'.öğrenci:')
    print(student)

    i=i+1
