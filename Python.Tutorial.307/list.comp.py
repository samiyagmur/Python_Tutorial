# numbers = []

# for x in range(10):
#     numbers.append(x)
# print(numbers)
#ile
# numbers=[x for x in range(10)]

# print(numbers)

# aynıdır.

# numbers = [x for x in range(10) if x%3==0]
# #10 a kadar üçe tam bölünen sayıları lisete içine alır
# print(numbers)#[0, 3, 6, 9]

# myString='hello'
# myList=[]

# for letter in myString:
#     myList.append(letter)
# print(myList)#['h', 'e', 'l', 'l', 'o']
# #string içindeki harfleri tek tek for döngüsünde my list içine ekledi.
# #başka bir yönetemle

# myList=[letter for letter in myString]
# print(myList)
#bu yöntem daha kolay

# years = [1983,1999,2008,1956,1986]
# ages= [2020-year for year in years]

# print(ages)[37, 21, 12, 64, 34]

# results = [x if x%2==0 else 'TEK' for x in range(1,10)]
# print(results)#['TEK', 2, 'TEK', 4, 'TEK', 6, 'TEK', 8, 'TEK']
# #x ifadesini burda bir koşula bağlayabiliriz 
# # #liste içinde for döngüsünün önüne konulan x herhangi bir koşul
# #veya başka bir döngü kullanılmasına olanak sağlayabilir.
# #ayrıca saydırma yani 'in'den ssonrada saydırma koşulu sağlanabilir.

# result = []

# for x in range(3):
#     for y in range(3):
#         result.append((x,y))

# print(result)
#[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)] 

# numbers = [(x,y) for x in range(3) for y in range(3)]
# #yukarıdaki yöntemle aynı sonuç verir.dediğimiz gibi x mümkün kılıyor fazla döngüyü.
# print(numbers)
# #[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
