#class
class person:
    

    #class attributes
     
    address = 'no informetion'
    #constructor(yapıcı method)

    def __init__(self,name,year):

    #object attributes
        self.name = name
        self.year = year
    



    #methods
    

#object, instance

p1= person( 'ali', 1999) #p1 bir objedir
#kaç kere gönderirsek o kdar class çalışır.
p2= person('yağmur',1995) 

#update yenileme

p1.name = 'ahmet'

print(f'name:{p1.name} year:{p1.year} address {p1.address}')#name:ali year:1999
                                       #<class '__main__.person'>
print(f'name:{p2.name} year:{p2.year}')

print(type(p1))#<class '__main__.person'>
