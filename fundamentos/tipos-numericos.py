from decimal import Decimal, getcontext
a = -3
print(type(a))
print(5.0.is_integer())

print(abs(a))
print(a.__abs__())

print(1.1 + 2.2)
getcontext().prec = 2
print(Decimal(1.1) + Decimal(2.2))
print(Decimal.max(Decimal(10), Decimal(50)))
