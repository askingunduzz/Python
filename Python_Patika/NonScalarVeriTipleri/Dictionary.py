
##bunlar listeler:

notlar=[80,72,95]
isim = ["Deniz", "Ege", "Gizem"]
isim[0]
notlar[0]
print(isim[0], "adlı öğrencinin notu", notlar[0])

no = [703, 408, 690]
isim[0]
no[0]


##DICTIONARIES:
#mutable
print("----------")
notlar = {"Deniz": 80, "Ege":72, "Gizem": 95}
print(notlar["Ege"])
notlar["Gizem"]

ogrenciler = {"Deniz": {"not":80, "ogrenci_no":703}, "Ege":{"not":72, "ogrenci_no":408}, "Gizem": {"not":95, "ogrenci_no":690}}
ogrenciler["Ege"]

{'not': 72, 'ogrenci_no': 408}

ogrenciler["Ege"]["not"]
##indexing yok.
anotlar = {"A":5,0:9}
print(anotlar[0])
print(anotlar[0]) #nope

len(notlar)
print(notlar)
notlar["Mert"]=58
print(notlar)
del notlar["Mert"]
print(notlar)

d = {1:2, 3:"b"}
d[1]
d2 = {(1,2):"a", (4,5): [1,2,3]}
#NO : d3 = {[1,2]:4}   list: mutable olduğu içn
#bunlar immutable!!
d = {}#empty dictionary

print("Mert" in notlar) #True/False
"Deniz" in notlar
##dictionary is mutable, they can be changed after there created.