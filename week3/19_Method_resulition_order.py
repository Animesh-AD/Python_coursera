class A:
    num = 10
class B(A):
    num = 20
class C(B):
    pass
print(C.mro())  # it will show how inheritence work
print(help(C)) # it will show in structed format