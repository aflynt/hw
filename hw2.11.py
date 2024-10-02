
from sympy import *

x,t,z,nu = symbols('x t z nu')

init_printing(use_unicode=True)
print('\n')

#res = diff(sin(x)*exp(x), x)
#res = integrate(sin(x)*exp(x)+exp(x)*cos(x), (x, -oo, oo))
#res = integrate(sin(x**2), (x, -oo, oo))
#print()
#print(res)
#print()
#pprint(res)
#
##ans = solve(x**2 - 4*x + 4, x)
#ans = roots(x**2 - 4*x + 4, x)
#print()
#pprint(ans)

#y = Function('y')
#yofx = y(x)
#yp = diff(y(x),x)
#ypp = diff(yp,x)
#
#a1 = dsolve(Eq(ypp - yofx , exp(x)), y(x))
#pprint(a1)
#
#M = Matrix([[1,2], [2,2]])
#
#es = M.eigenvals()
#
#pprint(es)

h1,u1,q,h2,u2 = symbols('h1 u1 q h2 u2')

energy_eqn = Eq(h1 + u1**2/2 + q , h2 + u2**2/2)
pprint(energy_eqn)

ss = solveset(energy_eqn, u2, S.Reals)
pprint(ss)

cp = 850

reps = {
    h1: cp*300,
    h2: cp*280,
    q: -1.4*104,
    u1: 10,
}

r = max(ss.subs(reps))
pprint(r)

rho1 = 12.3457
rho2 = 6.17284
u1 = 10
u2 = 183.872

A1_o_A2 = rho2/rho1 * u2/u1
print(f'A1/A2 = {A1_o_A2: 12.3f}')



rho1, AR, u1, rho2, u2 = symbols('rho1  AR  u1  rho2  u2' )
ss2 = solveset(Eq(rho1 * AR * u1 , rho2 * u2), AR)
pprint(ss2)

subs = {
    rho2: 6.17284,
    rho1: 12.3457,
    u1: 10,
    u2: 183.872
}

rr2 = ss2.subs(subs)
pprint(rr2)
