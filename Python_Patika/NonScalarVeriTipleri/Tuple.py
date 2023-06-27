x=10
y=34
konum = (x,y)
##bir kere belirlendikten sonra güncellenemez
x=20
print(konum)  ## 10,34 basar!
## not mutable, immutable!
##listelerdeki gibi indexing slicing var
##konum[0]=100 ---not possible
t=(1,2,"a",3)  ##mümkün
##çinde liste olabilir içinde tuple olabilir..
a=3
b=4
##tuple değerini değiştirmek için
temp=a
a=b
b=temp  ##ya da 
z=0
y=9
(z,y)=(y,z)
print(y)
print(z)   #nice
a=1,2,3  ##böyle de tuple tanımlanır!
print(a)   