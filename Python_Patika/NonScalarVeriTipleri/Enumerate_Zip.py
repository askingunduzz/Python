l = [(1,2), (10,20)]
for e in l:
    print(e)
print(type(l[0]))
print("*******")
for e in l:
    a, b = e
    print(a)
    print(b)
    print("*********")

for a, b in l:
    print("tuple'ın ilk elemanı", a)
    print("tuple'ın ikinci elemanı", b)
    print("-----------------------------")

#enumerate() bize (index, element) olarak verecek.
adlar = ['Tyler', 'Blake', 'Cory', 'Cameron']
for e in adlar:
    print(e)

for i, e in enumerate(adlar):
    print(i, "indexindeki eleman:", e)

#enumerate() 0'dan başlamak zorunda değil, özellikle kaçtan başlayacağını belirtebiliriz.

for i, e in enumerate(adlar, start = 10):
    print(i, "lokasyonunda bulunan eleman:", e)

#zip()
ogrenciler = ["ogrenci_1", "ogrenci_2", "ogrenci_3"]
notlar = [90,80,72]
for s, g in zip(ogrenciler, notlar):
    print(s, g)
for e in zip(ogrenciler, notlar):
    print(e)
for i in range(len(ogrenciler)):
    print(ogrenciler[i], notlar[i])
print("000")

##enumerate: notlandırdı bildiğin. 0:a 1:e diye kendisi verdi 
#zip iki ayrı listi birleştirdi yani i[0]ile e[0] ı birleştirdi.

# Her ayki karı hesaplamak
satis = [3500.00, 76300.00, 67200.00]


maliyet = [56700.00, 21900.00, 12100.00]
##length leri aynı olmalı!

for i in range(len(maliyet)):
    s = satis[i]
    c = maliyet[i]
    
    kar = s - c
    print(f'Total profit: {kar}')


satis = [3500.00, 76300.00, 67200.00]
maliyet = [56700.00, 21900.00, 12100.00]
for s, c in zip(satis, maliyet):
    kar = s - c
    print(f'Total profit: {kar}')


#zip() ile dictionary yaratmak:
keys = ['isim', 'soyad', 'ulke', 'is']
values = ['Denis', 'Walker', 'Turkey', 'data scientist']
d={}

for k, v in zip(keys, values): 
    d[k] = v

print(d)
{'isim': 'Denis', 'soyad': 'Walker', 'ulke': 'Turkey', 'is': 'data scientist'}
##very nays.
print(d["isim"])

for i in range(len(keys)):
    k=keys[i]
    v=values[i]
    d[k]=v
print(d)  ##same but longer.
