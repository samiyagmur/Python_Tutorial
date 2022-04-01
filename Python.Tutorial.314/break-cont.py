# name='sami yagmur'

# for letter in name:
#     if latter== 'a':
#         break#break döngüyü kapatır.continiu ise belirli şartı iptal eder.

# x=0

# # while x<5:
# #     if x==4:
# #         break
# #     print(x)
# #     x += 1#4 ü görünce döngü bitti
# while x<5:
#     if x==4:
#         continue
#     print(x)
#     x += 1#4 ü görünce döngü 4 ü iptal etti


x=0
result=0

while x<=100:
    x += 1
    if x%2==1:
        continue            
    
    result += x

    
print(result)