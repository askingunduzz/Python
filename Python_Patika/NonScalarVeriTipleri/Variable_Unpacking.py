x, y = (4, 7)
print(x)
print(y)

x, y, z = (4, 7, 11)
print(x,y,z)

x, _ = (4, 7)

#no : x, y, z = (4, 7, 11, 4, 21)
#Bunu gidermek için * yapısını kullanacağız. Aşağıdaki kod şu demek oluyor: İlk iki elemanı x ve y'ye eşitle, sonuna kadar kalan diğer tüm elemanları z'ye eşitle. Bunun sonunda z 11,2,21'den oluşacak, tipi list olacak.
x, y, *z = (4, 7, 11, 4, 21)
print(x,y)
print(z)
print(type(z))
x, y, *_ = (4, 7, 11, 12, 13)
x, y, *z, t = (4, 7, 11, 4, 21)
print(x,y,t)
print(z)
# It will give an error
#x, *y, *t = (4, 7, 11, 4)
#Ama aşağıdaki kod error verir, çünkü y ve t için kaç tane alacağını bilmiyor.
## *z ile belirtilen * olan her şeyi list olarak döndürür!
