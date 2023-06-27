x = 2
print("x in değeri" + " " + str(x))
print(f"x in değeri {x}")
print(f"x in değerinin iki fazlası {x+2}")
print(f"verilen isim {isim}")
print(f"verilen isim {isim.capitalize()}")


def kare(x):
    return x**2


x = 10
print(f"{x} sayısının karesi {kare(x)}")