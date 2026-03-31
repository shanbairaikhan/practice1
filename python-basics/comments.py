#1
x=10
y=3
#сначала делим а потом прибавляем
result=x/y+2
print(result)
#2
#Важно:int() просто отбрасывает дробную часть
number=int(7.9)
print(number)
#3
password="Qwerty123"
#проверим, что длина пароля больше 8
is_strong=len(password)>8
print(is_strong)
#4
#True ы Python=1,False=0
print(True*5+False)
#5
x="10"
#print(x+5) give TypeError
print(int(x)+5)