a = 2
def f(x):
    x = 4
    print(x)
    return x
f(a)
print(a)

def f(l): 
    l[0] = "a"
    return l


f(l)
['a', 2, 3]

def f(x):
    
    x[0] = 2
    
    return x
def f(penguin): 
    penguin[0] = 2
    
    return penguin
f(l)


def f(x):
    
    l2= x.copy()   ##copyde degismez, l2=l diyince degisir wow!!
    l2[0] = 2
    
    return l2
f(l)
print(l)

#listte l2 degisince l de degisiyo vayyy