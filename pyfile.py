import name

name = input("Your Name: ")
name.greet(name)

def square(x):
    return x*x

for i in range(5):
    print(i, "square: ", square(i))
