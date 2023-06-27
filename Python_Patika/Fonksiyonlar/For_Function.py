l = [1,2,3,4]


def apply(l, f):
    """ l bir liste, f listenin tüm elemanlarına uygulanacak fonksiyon sonunda listenin orijinali elemanlarına fonksiyonun uygulanmış haliyle güncellenir """
    
    n = len(l)
    
    for i in range(n):
        l[i] = f(l[i])

def kare(x):
    return x**2
apply(l, kare)

print(l)
l = [1,2,3,4]

def kup(x):
    return x**3
apply(l, kup)
print(l)

def apply_funcs(f_list, x): 
    l = []
    for f in f_list:
        l.append(f(x))
        
    return l


apply_funcs([kare, kup], 5)

#not: underscore placeholders
##kod için 10_000_000_000 ile 10000000 ün hiçbi farkı yok ama bana okuması çok daha kolay.