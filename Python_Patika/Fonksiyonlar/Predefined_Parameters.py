def hello(end, start = "Hello"):
   
  print(start + " " + end)


hello("Denis")
hello("Denis", start = "Hey")
hello("Aa")
hello("askin","aa")

def power(x, y=1):
    
    return x ** y


power(3)
power(4, 2)

# Aksini belirtmezsek predefined değerleri kullanacak fonksiyon
# predefined olarak vereceğimiz değerleri en sona yazmalıyız yoksa hata alırız
## hata:  def hello(start = "Hello", end): 
 ##   print(start + end)
print("***")

def g(x, y=1, z=2):
    print("ha?")
    print(x+y+z)
    return x+y+z

g(2)
g(2,5)
g(2,5,6)

print("22222")