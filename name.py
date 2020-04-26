def greet(name):
    print("Hello", name,"!")

def square(x):
    return x*x

def main():
    for i in range(5):
        print(i, "square: ", square(i))

if __name__ == "__main__":
    main()
