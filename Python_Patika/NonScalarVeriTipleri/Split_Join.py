s = "merhaba nasılsın ?"
s.split(" ")
print(s)
print(s.split(" "))
print(s.split())

print("----")
l = ['limon', 'portakal', 'elma']
print("----")
print(l)
",".join(l)
print(l)
s = "*".join(l)
d=" ".join(l)
print(d)
print(s)
print("******")

mailler={"kisi1":"ad1.soyad1@gmail.com",
         "kisi2":"ad2.soyad2@gmail.com",
         "kisi3":"ad3.soyad3@gmail.com"} 
l=[]

for v in mailler.values():
    l.append(v)
s="-".join(l)
print(s)    