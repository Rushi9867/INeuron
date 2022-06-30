def print_hi(name):
    print(f"hi {name}")

def genfib(n):
    a = 1
    b = 1
    l = []
    for i in range(n):
        l.append(a)
        a,b = b,a+b
    return l

print_hi("Kuldeep")

print(genfib(10))
