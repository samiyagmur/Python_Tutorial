website = "http://www.sadikturan.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"


# 1-  ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.

r = ' Hello World '.strip() #Başındaki ve sonundaki boşlukları siler
r = ' Hello World '.lstrip() #Soldaki boşluk karakterilerini siler
r = ' Hello World '.rstrip() #Sağdaki boşluk karakterlerini siler

r=website.lstrip('/:pth') #soldan '/:pth' tüm karakterlerini siler
# 2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.

r='www.sadikturan.com'.strip('w.moc') #'www.sadikturan.com' ifadesindeki w.moc olan tüm karakterleri siler

# 3-  'course' karakter dizisinin tüm karakterlerini küçük harf yapın.

r = course.lower() #course içindeki tüm harkleri küçültür
r = course.upper() #course içindeki tüm harkleri büyültür
r = course.title() #course içindeki tüm baş hargleri büyültür.

# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))

r=website.count('a') #website içinde kaç tane a olduğunu bulur
r=website.count('www')  #website içinde kaç tane sırayla 'www'dizisi olduğunu bulur
r=website.count('www',0,10) #0 ve 10 karakter arasında 'www' varmı diye arar.

# 5- 'website' "www" ile başlayıp com ile bitiyor mu?

r = website.startswith('www') #website ifademiz 'www' ile başlıyomu.Başlıyosa true.Başalmıyosa false cevabını verir.
r = website.endswith('com')#website ifademiz 'com' ile bitiyomu

# 6-  'website' içinde '.com' ifadesi var mı?

r = website.find('com') #'com' ifadesi website içirisinde varmı.varsa indeks numarasını söyler.
r = website.find('com',0,10) #'com' ifadesi 0 ve 10 indeks arasında varmı ?
r = course.find('Python')
r = course.rfind('Python')#sağdan sola 'Python' ifadesini arar

r = website.index('com')#kaçıncı indekste com ifadesinin olduğunu söyler
r = website.rindex('com')# sağdan sola taradığında kaçıncı indekste com ifadesi olduğunu söyler
#eğer indekste o harf yoksa hata verir.

# 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)

r = course.isalpha()
r = 'hello'.isalpha()#hello içindeki harflar alfabetikmi
r = course.isdigit() #course ifadsi rakam yada decimal mi
r = '123'.isdigit()#'123' numerikmi

# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.

r='contests'.center(50,'*')
r='contests'.ljust(50,'*')
r='contests'.rjust(50,'*')

# 9-  'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.

r = course.replace(' ','-',)# boşluklar yerine - koyar
r = course.replace(' ','-',5)#5 karakteri değiştirri
r = course.replace(' ','')#tüm boşlukları siler

# 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin

r = 'Hello World'.replace('World','There')

# 11-  'course' karakter dizisini boşluk karakterlerinden ayırın.

r = course.split(' ')

print(r)



