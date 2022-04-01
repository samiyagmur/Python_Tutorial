# global scope
x = 'global x'

def function(): 
    # local scope
    # x = 'local x'
    print(x)

function()
print(x)
#burada fonksiyonun çağırıldığı terde local değişken fonksiyon dışındaki yazdırılmada global değişken sonuç verecektyir.
####################

# global
name = 'Çınar'

def changeName(new_name):
    # local 
    global name #global komutu fonksiyon içerisinde değiken üzerinde yapılan değişikliği sanki fonksiyon dışındaymış gibi davranmasına neden olur.
    name = new_name
    print(name)

changeName('Ada')
print(name)

####################

name = 'global string'

def greeting():
    # name = 'Çınar'

    def hello():
        # name = 'Ada'
        print('hello '+ name)

    hello()

greeting()
#burada her fonksiyonun içinde local olarak verilen değişkenler(name) eğer verilmeseydi
#bir önceki fonksiyondaki(name) değişkenine veya ana fonksiyondaki değişkeni baz alarak çalışır 
####################

x = 50
def test(): 
    global x#fonksiyon dışında tanımlı fakat içinde tanımsız olna değişkenler için global key word kullanılabilir
    print(f'x : {x}')

    x = 100
    print(f'changed x to {x}')

test()
print(x)

