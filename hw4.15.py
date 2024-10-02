from libgd import *

# Gas:
g = gases_si["CARBON_DIOXIDE"]
USING_SI = True

g_c = 1 if USING_SI else 32.174

# Given at station 1
T_1 = 600 # K
P_1 = 7*101325 # Pa

# Given at station 2
M_2 = 0.9
T_2 = 550 # K
P_2 = 4*101325 # Pa


# Can get station 2 ratios
TR_2 = isen_ratio_t(g.k, M_2)
PR_2 = isen_ratio_p(g.k, M_2)

Tt_2 = TR_2*T_2
print(f"TR_2 = {TR_2:10.3f}")
print(f"Tt_2 = {Tt_2:10.3f}")

# Tt doesnt change
Tt_1 = Tt_2

TR_1 = Tt_1 / T_1
print(f"TR_1 = {TR_1:10.3f}")

M = sp.Symbol("M")

# Find station 1 Mach number
res = sp.solveset(sp.Eq(TR_1,1 + (g.k-1)/2*M**2), M, domain=sp.Reals)
M_1 = float(list(res)[1])


a_1 = speed_of_sound(g.k, g.R, T_1, is_si=True)
V_1 = M_1* a_1
print(f"M1 = {M_1}")
print(f"a1 = {a_1} m/s")
print(f"V1 = {V_1} m/s")

AreaRatio21 = P_1/P_2*M_1/M_2*m.sqrt(T_2/T_1)
print(f"Area Ratio A2/A1 = {AreaRatio21:10.3f}")



# ok, we can get sos and velocity
#a_1 = speed_of_sound(g.k,g.R,T_1, is_si=True) # ft/s
#V_1 = M_1 * a_1

#print(f"a_1 = {a_1:10.3f} ft/s")
#print(f"u_1 = {V_1:10.3f} ft/s")

## with M we get TR, PR
#TR_1 = isen_ratio_t(g.k,M_1)
#PR_1 = isen_ratio_p(g.k,M_1)
#
#Tt_1 = T_1*TR_1
#Pt_1 = P_1*PR_1

# energy balance with no heat transfer or work -> Tt = constant
#Tt_2 = Tt_1


#print(f"{a_2 = }")
#
#
## mass conservation in const-area duct requires:
#
#P_2 = P_1 * (V_1/V_2) * (T_2/T_1)
#
#Pt_2 = PR_2*P_2
#
#
## total pressure ratio
#PTR = Pt_2/Pt_1
#
#WoH = 778.2 # Btu / ft-lbf work to heat ratio
#
#ds = -g.R*m.log(PTR) / WoH
#
#print(f"ds = {ds:10.4f} Btu/lbm-R")
#
#D_duct = 1 #ft
#A_duct = m.pi/4*D_duct**2
#
#mdot_1 = P_1*144*A_duct*V_1/(g.R*T_1)
#
#print(f"mdot = {mdot_1:12.3f} lbm/s")
#
#Ff = mdot_1/g_c*(V_2-V_1) + (P_2-P_1)*A_duct*144
#print(f"Ff = {Ff:12.3f} lbf")