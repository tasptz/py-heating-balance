import pint

ur = pint.UnitRegistry()
m2 = ur.m * ur.m
m3 = ur.m * m2
u = ur.W / (ur.K * m2)
W = ur.W
C = ur.celsius
K = ur.K
hour = ur.hour
kg = ur.kg
J = ur.J

def with_unit(v, unit=''):
    return ur.Quantity(v, unit)