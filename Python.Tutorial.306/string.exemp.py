#!/usr/bin/env python3
# Define a string value
from colored import fg,bg,attr

wepside = "http://www.samiyagmur.com"
course = "Python Kursu:Baştan Sona Python Programa Rehberiniz(40 saat)"
color=fg('blue')
color1=fg('red')
color2=fg('green')

legth = len(course)

reset=attr('reset')

# print(color+"course karakter dizisinde kaç karakter bulunmaktadır?----->>>"+reset,legth)

# print(color+"'wepsite'kelimesi içinden www alın------>>>>"+reset,wepside[7:10])

# print(color1+"'wepsite'kelimesi içinden com alın------>>>>"+reset,wepside[-3:])

# print(color2+"'course'kelimesi içinden ilk 15 ve son 15 karakterleri alın------>>>>"+reset,course[:15],course[-15:])

# print(color+"'course'kelimesi içinden  karakterleri tersten yazdırın------>>>>"+reset,course[::-1])

# name,surname,age,job = 'sami','yagmur',28,'mühendis'

# print(color1+"Benim adım",name,surname,"yaşım",str(age),"ve mesleğim",job+reset)
# print(color2+'Benim adım {} {} yaşım {} ve mesleğim {}'.format(name,surname,age,job)+reset)
# print(color+f'Benim adım {name} {surname} yaşım {age} ve mesleğim {job}'+reset)

# s ='Hello world'

# s="".join([s[0:6],s[6].upper(),s[7:]])

# print(s)

# d="abc "*3
# print(d)








