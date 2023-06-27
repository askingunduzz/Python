### ee hem and var hem &
## & de and in yaptığını yapıyomuş ama short circuit davranışı göstermezmiş

print((6<3) and "hey") ##false 
##buna short circuit denmektedir
print("bak şimdi")
print((6<3) & "hey")  ##eror

## or == |  fakat no short circuit
print((2==2) & "hey")  ##error
print("deneme")
print((2==2) & print("hey"))  ##hey ve EROR