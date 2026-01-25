#1
x = ["apple", "banana", "cherry"]
print(x)
#2
y = {"name" : "John", "age" : 36}
print(y)
#3
z=("apple","banana","cherry")
print(type(z))
#4
a=str("Hello world")
print(a)
print(type(a))
#5
b=float(20.5)
print(b)
print(type(b))
#6
x=range(3,10)
print(x)
print(list(x))
#7
x=set(("apple","banana","orange"))
print(x)
print(type(x))
#8bool
a=10
b=5
result=a>b
print(result)
#9bytes
text=b"Hello"
print(text[0])
#10h yo j
data=bytearray(b"Hello")
view=memoryview(data)
view[0]=74
print(data)
