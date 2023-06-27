S={1,2,3,4,5}
print(S)
S2={1,2,2,2,3,4,2,2,5,6,3,4,5}
print(S2)

a={} #dictionary
s=set() #set
l = [1,2,3,4]
s = set(l)
print(s) #listin elemanlarıyla set oluşturma
#set içi her zaman UNİQUE!
t = (1,2,3,4,1) #tuple
s = set(t)
print(s)

message = "Merhaba, orda mısın?"
# Strinleri kullanarak da set oluşturabiliriz.
s = set(message)
print(s) #vay

len(s)
#setler indexlenemes s[0] yok
s.add(6) #mümkün
print(s)
s.remove('r')

# Eğer silmek istediğimiz eleman yoksa hata almak istemiyorsak, discard()'ı kullanabiliriz.
s.discard(10)
s.add(10)
print(s)
s.discard(10)
print(s)

s1 = set([1,5,10])
s2 = set([2,5,3])
# s1 in hangi elemanları s2 den farkıdır.
s1.difference(s2)  #farklı olanları basıyo s1deki
#{1, 10}
# '-' operatörü setlerde kullanıldığında bize farkı verir.
s1 - s2
#{1, 10}

# s2 nin hangi elemanları s1 den farklıdır
s2.difference(s1) #farklı olanları basıyo s1deki
#{2, 3}

##kesişim ve işte diğeri de bulunuyor
s1


{1, 5, 10}


s2


{2, 3, 5}


# (s1 \ s2) U (s2 \ s1)  - > A U B - (A n B)
s1.symmetric_difference(s2)


{1, 2, 3, 10}


# (s2 \ s1) U (s1 \ s2) same as (s1 \ s2) U (s2 \ s1)
s2.symmetric_difference(s1)


{1, 2, 3, 10}

#Intersection (kesişim)
{2, 3, 5}
s1.intersection(s2)
# `&` operatörü setlere uygulanınca kesişim olur
s1 & s2
# Bu işlem kesişim ile aynı sonucu verecek
s1 - (s1-s2)
s1
{1, 5, 10}
# kesişim yapıp s1 in değerini buna günceller
s1.intersection_update(s2) # s1 = s1.intersection(s2)
s1

s1 = set([1, 5, 10])
s1
{1, 5, 10}
s2
{2, 3, 5}
s1.union(s2)
{1, 2, 3, 5, 10}
s1
{1, 5, 10}
s1.union(s1)
{1, 5, 10}
#Disjoint Sets
#s1 ∩ s2 = Ø olup olmadığını kontrol eder
s1
{1, 5, 10}
s2
{2, 3, 5}
s3 = set([12,11])
s3
{11, 12}
# s1 ∩ s2 ≠ Ø(boş küme) değil, o yüzden False döner
s1.isdisjoint(s2) 
False
s2.isdisjoint(s1) 
False
s1.isdisjoint(s3) 
True
len(s1.intersection(s2)) == 0
False
#Subset (Alt küme)
#s1.issubset(s2), s1'in s2'nin alt kümesi olup olmadığını kontrol eder
s1.issubset(s2)
False
s3 = set([2,5])
s3
{2, 5}
s3.issubset(s2)
True
#Superset (üst küme)
#s2.issuperset(s3) s2'nin s3'ün üst kümesi olup olmadığını sorgular
s1
{1, 5, 10}
s2
{2, 3, 5}
s3
{2, 5}
s2.issuperset(s3)