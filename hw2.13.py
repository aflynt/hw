
from sympy import *
import math as m

x,t,z,nu = symbols('x t z nu')

init_printing(use_unicode=True)
print('\n')

#energy_eqn = Eq(h1 + u1**2/2 + q , h2 + u2**2/2)
#pprint(energy_eqn)
#
#ss = solveset(energy_eqn, u2, S.Reals)
#pprint(ss)
#
#
#reps = {
#    h1: cp*300,
#    h2: cp*280,
#    q: -1.4*104,
#    u1: 10,
#}
#
#r = max(ss.subs(reps))
#pprint(r)

## NITROGEN
class gas:
    def __init__(self, name="AIR", M=28.97, k=1.4, R=287, cp=1000, cv=716):
        self.name = name
        self.M = M
        self.k = k
        self.R = R
        self.cp = cp
        self.cv = cv

    def __str__(self):
        return f"{self.name:15s} k {self.k:4.2f} R {self.R:4.0f} cp {self.cp:5.0f}"

N2 = gas('nitrogen')
print(N2)

gases = {
    "AIR":            gas("AIR",             28.97 , 1.40,  287,  1000,  716),
    "AMMONIA":        gas("AMMONIA",         17.03 , 1.32,  488,  2175, 1648),
    "ARGON":          gas("ARGON",           39.94 , 1.67,  208,   519,  310),
    "CARBON_DIOXIDE": gas("CARBON_DIOXIDE",  44.01 , 1.29,  189,   850,  657),
    "CARBON_MONOXIDE":gas("CARBON_MONOXIDE", 28.01 , 1.40,  297,  1040,  741),
    "HELIUM":         gas("HELIUM",           4.00 , 1.67, 2080,  5230, 3140),
    "HYDROGEN":       gas("HYDROGEN",         2.02 , 1.41, 4120, 14300,10200),
    "METHANE":        gas("METHANE",         16.04 , 1.32,  519,  2230, 1690),
    "NITROGEN":       gas("NITROGEN",        28.02 , 1.40,  296,  1040,  741),
    "OXYGEN":         gas("OXYGEN",          32.00 , 1.40,  260,   913,  653),
    "WATER":          gas("WATER",           18.02 , 1.33,  461,  1860, 1400),
}

g = gases["NITROGEN"]

print(f"R = {g.R}, cp = {g.cp}")

p1,T1 = symbols("p1 T1")

rho = p1 / (g.R * T1)
rho = rho.subs({p1: 14e5, T1: 800})

pprint(rho)

u = m.sqrt(2*g.cp*(800-590) + 12**2)
print(f"u = {u}")
