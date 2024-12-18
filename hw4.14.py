from libgd import *

# Gas: AIR EE
g = Gas_mgr().AIR_EE
USING_SI = False

g_c = 1 if USING_SI else 32.174

# Given at station 1
T_1 = 520 # K
P_1 = 50  # Pa
M_1 = 0.45 

# Given at station 2
M_2 = 1

# ok, we can get sos and velocity
a_1 = speed_of_sound(g.k,g.R,T_1, is_si=False) # ft/s
V_1 = M_1 * a_1

print(f"a_1 = {a_1:10.3f} ft/s")
print(f"u_1 = {V_1:10.3f} ft/s")

# with M we get TR, PR
TR_1 = isen_ratio_t(M_1,g.k)
PR_1 = isen_ratio_p(M_1,g.k)

Tt_1 = T_1*TR_1
Pt_1 = P_1*PR_1

# energy balance with no heat transfer or work -> Tt = constant
Tt_2 = Tt_1

TR_2 = isen_ratio_t(M_2, g.k)
PR_2 = isen_ratio_p(M_2,g.k)

T_2 = Tt_2 / TR_2


a_2 = speed_of_sound(g.k, g.R, T_2, is_si=False)
V_2 = M_2* a_2

print(f"{a_2 = }")


# mass conservation in const-area duct requires:

P_2 = P_1 * (V_1/V_2) * (T_2/T_1)

Pt_2 = PR_2*P_2


# total pressure ratio
PTR = Pt_2/Pt_1

WoH = 778.2 # Btu / ft-lbf work to heat ratio

ds = -g.R*m.log(PTR) / WoH

print(f"ds = {ds:10.4f} Btu/lbm-R")

D_duct = 1 #ft
A_duct = m.pi/4*D_duct**2

mdot_1 = P_1*144*A_duct*V_1/(g.R*T_1)

print(f"mdot = {mdot_1:12.3f} lbm/s")

Ff = mdot_1/g_c*(V_2-V_1) + (P_2-P_1)*A_duct*144
print(f"Ff = {Ff:12.3f} lbf")