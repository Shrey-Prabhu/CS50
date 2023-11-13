import sys
if len(sys.argv) <2:
    sys.exit("too few args")

for arg in sys.argv[1:]:    #[initial: final] both inclusive
    print(f"Hello, {arg}")