#bir fonksiyonu başka bir değere atayabilriz
def kare(x):
    return x**2
a=kare
kare(5)
a(5)

#bir fonksiyou başkba bir fonksiyonu argüman olarak atayabilriz
def f2(x, f):
    return f(x) + 4

f2(3,kare)

def f3(x):
    return x**5
f2(2, f3)
