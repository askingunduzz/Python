ogrenci_1 = 78
ogrenci_2 = 80
ogrenci_3 = 43
ogrenci_4 = 65
ogrenci_5 = 90

##notlar = [78, 80, 43, 65, 90]
# bunun aynısını şu şekilde de tutabilirdik:

notlar = [ogrenci_1, ogrenci_2, ogrenci_3, ogrenci_4, ogrenci_5]
print(notlar[0])
print(notlar[-1])   ##son eleman
print(notlar[1:]) #1. den başlar
print(notlar[1:3])  # 1.den 3.ye kadar
print(notlar[:200]) ##0dan 200ye kadar!
print(notlar[:5])
print(notlar[:6])
print(notlar[:4])

## LİSTLER MUTABLE!
##elemanları değiştirebiliyorsun:
notlar[1]=50
print(notlar)

print(len(notlar))
notlar.append(201)
notlar.append([200,23])
print(notlar)

notlar.extend([1,2,3])
print(notlar)

notlar[3]=5
print(notlar)
notlar.insert(3,6)  
 ##5'i silmedi. Kaydırdı sağa!
print(notlar)

notlar.remove(201)
print(notlar)
##ilk gördüğü değeri siler remove
## 1,2,3,4,2 var ise:
##remove(2) -> 1,3,4,2 .
notlar.pop(1)
##hem siler hem de o sildiği değeri döndürür
notlar.count(2)
##2 sayısının notlar listinde kaç kere olduğunu sayar

print("--------------------------------------")
print()
### ALİASİNG
list1=[1,2,3]
list2=list1
list1[0]=5
print(list2)
##list2 also gets effected!
##doesnt happen with a=2 or sth.
##bunu nasıl çözeriz:
list3=list1.copy()
##böyle olunca, list1 değişse de list3 değişmez!
print("*************")
##Concatenation
print(list1+list2+list3)
##Belirtli bir elemanın indexini bulmak
list1.index(3)  #ilk görülen 3'ün indexi
## '3' nerde. 
##listi tersine çevirmek
list1.reverse()
## inplace: listenin güncellenmesi
list2= list2[::-1]  ##same
##list2= kısmı olmasaydı güncellenmezdi
l=[a,c,b]
sorted(l) ##l güncellenmedi
l.sort()   ##güncellendi
