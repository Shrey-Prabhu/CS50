import sys

if len(sys.argv) < 2:   #sys.argv are the characters entered while running a program eg: python File-6.py Shrey
    sys.exit("Too few arguments")   #sys.exit ends the execution of the code after printing the arguement
elif len(sys.argv) > 2:
    sys.exit("Too many args")

print(f"Hello, {sys.argv[1]}")