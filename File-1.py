def main():
    name = input("Enter your name: ").strip().title()
    greet(name)


def greet(name):
    print("Hello,",name)

main()