#1
x=5
x="amina"
print(x)
#2
x=6
y="Sally"
print(type(x))
print(type(y))
#3
x=y=z='Orange'
print(x)
print(y)
print(z)
#4
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
#5
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
#6
x=7
y='Serik'
print(x,y)
#7
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
#8
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
#9
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#10
x=5
y=10
print(x+y)
