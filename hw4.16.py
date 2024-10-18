from libgd import *


g = Gas_mgr().OXYGEN_EE
# known
M_1 = 0.2    
Tt_1 = 1000  # R
Pt_1 = 100   # psia
A_1 = 1   # ft^2
P_2 = 14.7   # psia

TR_1 = isen_ratio_t(M_1,g.k)
PR_1 = isen_ratio_p(M_1,g.k)
T_1 = Tt_1 / TR_1
P_1 = Pt_1 / PR_1

rho_1 = P_1*144/ (g.R * T_1)
a_1 = gas_sos( T_1, g)
V_1 = M_1 * a_1
mdot_1 = rho_1*A_1*V_1

Pt_2 = Pt_1

PR_2 = Pt_2/P_2

import sympy as sp
M = sp.Symbol("M")

M_2 = get_mach_given_pr( PR_2, g)

TR_2 = isen_ratio_t(M_2,g.k)

Tt_2 = Tt_1
T_2 = Tt_2/ TR_2

a_2 = gas_sos(T_2, g)
V_2 = M_2*a_2

rho_2 = P_2*144/ (g.R * T_2)

A_2 = mdot_1/(rho_2*V_2)

Ff = mdot_1/g.g_c*(V_2 - V_1) + P_2*A_2 - P_1*A_1

AR_a = nohw_A2oA1(P_1, P_2, M_1, M_2, T_1, T_2)


# ------------ RESULTS --------------------
print(f"OK working with gas: {g.name}")
print(f"k  = {g.k}")
print(f"R  = {g.R}")
print(f"cp = {g.cp}")
print(f"is_SI = {g.isSI}")
print(f"{PR_1 = }")
print(f"{P_1 = }")
print(f"rho_1 = {rho_1 = }")
print(f"a_1 = {a_1:10.3f}")
print(f"V_1 = {V_1:10.3f}")
print(f"mdot_1 = {mdot_1:10.3f}")
print(f"PR_2 = {PR_2:10.3f}")
print(f"M_2  = {M_2:10.5f}")
print(f"TR_2 = {TR_2:10.5f}")
print(f"T_2 = {T_2:10.5f}")
print(f"a_2 = {a_2:10.3f}")
print(f"V_2 = {V_2:10.3f}")
print(f"{rho_2 = }")
print(f"{A_2 = }")
print(f"Ff = {Ff:12.4f} lbf")