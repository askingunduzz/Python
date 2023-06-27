x= int(input("Bir sayı giriniz: "))

if x%2 == 0:
    print("x çift")
else:
    print("x tek")

y=int(input("Bir sayi daha giriniz: "))        

if y%2 == 0:
    print("y çift")
elif y%5 == 0:
    print("y 5in katı")
elif y%7 == 0:
    print("y 7nin katı")
else:
    print("aferim") 
print("BYE")   

##nested olunca da böyle 
x = int(input("Bir sayı girin: "))

if x % 3 == 0:
    if x % 2 == 0:
        print("Sayı hem 2'ye hem de 3'e bölünüyor")
    else:
        print("Sayı 3'e bölünüyor ama 2'ye bölünmüyor")

else:
    
    print("3'e bölünmüyor")
    
print("Programınız sona ulaştı")


##nays
x = int(input("Bir sayı girin: "))

if (x % 3 == 0) and (x % 2) == 0:
    print("Sayı hem 2'ye hem de 3'e bölünüyor")
    
print("Programınız sona ulaştı")

# or 
x = int(input("Bir sayı girin: "))

if (x % 3 == 0) or (x % 2 == 0):
    print("Sayı 2 veya 3'den en az birine bölünüyor")
    
print("Programınız sona ulaştı")