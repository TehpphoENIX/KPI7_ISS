import sys

OPERATIONS = {
    "+":lambda a,b: a+b,
    "-":lambda a,b: a-b,
    "*":lambda a,b: a*b,
    "/":lambda a,b: a/b,
    "%":lambda a,b: a%b,
    "^":lambda a,b: a**b,
}

if len(sys.argv) != 4:
    sys.stderr.write("Incorrect ammount of arguments supplied!\n")
    sys.exit(1)

A = int(sys.argv[1])
OP = str(sys.argv[2])
B = int(sys.argv[3])
    
if not(OP in OPERATIONS.keys()):
    sys.stderr.write("Operation {} is not supported!\n".format(OP))
    sys.exit(2)

print(OPERATIONS[OP](A,B))