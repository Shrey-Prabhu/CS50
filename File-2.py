
def main(): 
    names = ["Sarika", "Shrey", "Kusum", "Gurudatta"]

    for name in names:
        greet(name.strip())


def greet(name):
    print(f"Hello, {name}")


main()