a = "Hello world"
b = a
print("a =", a, ", id(a) =", id(a))
print("b =", b, ", id(b) =", id(b))
print("Один объект?", id(a) == id(b))

c = a[:]
print("a =", a, ", id(a) =", id(a))
print("c =", c, ", id(c) =", id(c))
print("Один объект?", id(a) == id(c))
