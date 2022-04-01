face = {'orange','apple','banana'}

#print(face[0]) #bu şekilde 0 indeksteki orange olduğpunu seçemeyiz.onun yetine;

for x in face:

    print(x)

face.add('cherry')  #bu şekilde listeye eleman ekleyebilriz.  
face.update(['mango','grape']) #bu şekilde ise birden fazla eleman ekleyebiliz

face.remove('mango') #remove metodu ile mago listeden silinir.
face.discard('apple') #discard metodu ile apple listeden silinir.

face.pop()#herhangi bir eleman silinebilir.

face.clear()# tüm elemanların siinmeisne neden olur.

mylist = [1,2,5,8,9,4]

print(set(mylist))