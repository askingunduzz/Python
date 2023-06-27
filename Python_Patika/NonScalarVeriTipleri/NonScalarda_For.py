notlar = [90,72,81,77]
print("------------")
##TUPLES ARE IMMUTABLE YANİ DEGERLERİNİ DEGİSTİREMEZSİN!!
for e in notlar:
    print(e)


t = 0

for e in notlar:
    t += e
    
ortalama = t / len(notlar)

print(ortalama)

t = 0

for penguen in notlar:
    t += penguen
    
ortalama = t / len(notlar)

print("Ortalama:",ortalama)

for i in range(4):
    print("Iteration: ", i)

t = 0

for i in range(len(notlar)):
    t += notlar[i]
    
ortalama = t / len(notlar)

print("Ortalama:",ortalama)

notlar

[90, 72, 81, 77]
for e in notlar:
    print(e)

for e in notlar:
    print(e)
    e = e + 10
    print(e)
    print(notlar)
    print("--------------")

print(notlar)

for i in range(len(notlar)): notlar[i] += 5
print(notlar)

notlar = [90,72,81,77]
for i in range(len(notlar)):
    
    if i == 1:
        continue
        
    notlar[i] += 5

print(notlar)

x = int(input("Hangi sayıyı kontrol edeyim?:"))

l = [2,3,40,100,10,1]

for e in l:
    print(e) # iterasyon break ile çıkmış mı görelim mi diye
    if e == x:
        print("Buldum!!")
        break

t = (1,2,3,4)
for e in t:
    print(e)

toplam = 0

for e in t:
    toplam += e
    
print(toplam)

for i in range(len(t)):
    print(t[i])

for i in range(len(t)):
    t[i] += 2

d = {"student_1": [90,89], "student_2": [80,83], "student_3": [72,71]}
for k in d:
    print(k)

for k in d:
    v = d[k]
    print(v)

d = {"student_1": 90, "student_2": 80, "student_3": 72}
for v in d.values():
    print(v)

d = {"student_1": [90,89], "student_2": [80,83], "student_3": [72,71]}

for v in d.values():
    print(v)

d = {"student_1": 90, "student_2": 80, "student_3": 72}

for k in d:
    value = d[k]
    
    if value > 85:
        print(k)
for k,v in d.items():
    print("key değeri:", k, "value değeri:", v)

print("AAAAAAAAAAAAAA")
for i in range(2,5,3):
    print(i)

    ##for(i=2;i<5;i+=3)