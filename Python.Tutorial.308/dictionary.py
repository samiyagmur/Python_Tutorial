#key - value

# 41 => kocaeli 34 => istanbul

# sehirler = ['kocaeli','istanbul']
# plakalar = [41,34]

# r=plakalar[sehirler.index('kocaeli')] #insekx 0 plakalar indeksinde 41 e denk gelir.

# plakalar={'kocaeli':41,'istanbul':34}

# print(plakalar['kocaeli'])
#  # bu şekilde yapıldığında koceli bilgisinin verilen plaka bilgisine denk geldiği görülebilir.

# plakalar['ankara']=6 # ankara ve ankaraya karşılık gelen 6 bilgisi bu şekilde listeye eklenilebilir.
# plakalar['kocaeli']='new value'# bu şekilde kocaelinin karşılığı değişebilir.


# print(plakalar)


users = { 'samiyagmur':{
'age':27,
'roles':['admin','user'],
'email':'samiyagmur92@gmail.com',
'adress':'kışehir',
'phone':'5457548798'

},
          'nazmiyeöniz':{
'age':28,
'roles':['user'],
'email':'nazmiyeyagmur1@gmail.com',
'adress':'uşak',
'phone':'5456898798'

}


}
#print(users['nazmiyeöniz']) #nazmiye öniz bilgileri gelir.
# print(users['nazmiyeöniz']['age'])

print(users['samiyagmur']['roles'][0])# bu bize saminin rollerinden ilkini vercektir.