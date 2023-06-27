squares = []

for i in range(1,11):
    squares.append(i*i)
print(squares)

squares = [i * i for i in range(1,11)]
#same

# list comprehension ve fonksiyon mantığını birleştirme

def cube(x):
    return x * x * x # x ** 3
cubes = [cube(x) for x in range(1,11)]
print(cubes)

print("**********")
squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
odd_squares=[]
for e in squares:
    if e%2 == 1:
        odd_squares.append(e)
print(odd_squares)        
print("**********")


print(squares)
odd_squares = []

for e in squares:
    
    if e % 2 == 1:
        odd_squares.append(e)
print(odd_squares)

# squares listindeki tek elemanlardan yeni bir liste yaratmak

odd_squares = [e for e in squares if e % 2 == 1]

# bu test mantığını fonksiyonla da sağlayabilirdik

def is_odd(x): 
    
    if x % 2 == 0:
        return False
    
    if x % 2 == 1:
        return True
odd_squares = [e for e in squares if is_odd(e)]

def empty(x): 
    
    if x % 2 == 0:
        return False
    
    if x % 2 == 1:
        return False
empty_squares = [e for e in squares if empty(e)]
print(empty_squares)

def is_even(x):
    
    if x % 2 == 0:
        return True
    
    if x % 2 == 1:
        return False
even_squares = [e for e in squares if is_even(e)]

print("000000000")
weird_squares = [2*e if e % 2 == 0 else -1 for e in squares]
print(weird_squares)
print("000000000")
print("ultraweird:")
ultra_weird_squares = [e if e % 2 == 0 else -1 for e in squares if is_odd(e)]
print(ultra_weird_squares)
#set comprehension
numbers = [1,2,3,4,5,6,7,1,2]
set_numbers = {s for s in numbers if s in [1,2,3,4,6,1,2]}
print(set_numbers)
##SETLER SADECE UNIQUE DEGERLERİ ALIR!
#dictionary comprehension
square_dict = {e:e * e for e in range(1,11)}
print(square_dict)
#nested list comprehension
m = [[j for j in range(7)] for i in range(5)]
m = [[j for j in range(7)] for _ in range(5)]
print(m)

m = [[10, 11, 12], [13, 14], [15, 16, 17, 18]] 
for l in m:
    print(l)

new_m = []
for l in m:
    print(l)
    for e in l:
        new_m.append(e)
        print(e)

print(new_m)
# matrixi list comprehension ile flat etmek
print("--*-*-*-*-*-*-*-*-*-*-*")
flatten_m = [e for l in m for e in l]
print(flatten_m)
# Sadece çift değerleri kabul edecek

flatten_m = [e for l in m for e in l if e % 2 == 0]
print(flatten_m)
print("////////////////")
m=[[[ 25, 36, 62],[ 28, 38, 64],[ 30, 40, 67]],[[ 1, 27, 56],[ 1, 25, 55],[ 2, 21, 51]]]
#flat_m=[e for l in m for e in l]
flat_m= [i for l in m for e in l for i in e]
print(flat_m)
