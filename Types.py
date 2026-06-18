A=type("A",(),{"x":100})
obj=A()
print(obj.x)

B=type("B",(),{"k":200,"show":lambda self:self.k})
o=B()
print(type(o))
print(o.show())