from libgd import *
print("\n")

#g = gases_ee["NITROGEN"]
g = gases_ee["OXYGEN"]


# KNOWN
# Tt = constant
# no work
# q = 0
# no losses?
A_1 = 6 #ft^2
A_2 = 5 #ft^2
T_1 = 750 # R
P_1 = 30 # psia
V_1 = 639 # ft/s


a_1 = gas_sos(T_1, g)
M_1 = V_1 / a_1

TR_1 = isen_ratio_t(g.k, M_1)
PR_1 = isen_ratio_p(g.k, M_1)

Tt_1 = T_1 * TR_1
Pt_1 = P_1 * PR_1

#print(f"a = {a_1:10.3f}")
#print(f"M = {M_1:10.3f}")
#print(f"Tt_1 = {Tt_1:10.3f}")
#print(f"Pt_1 = {Pt_1:10.3f}")

# c) no losses, no ht xfer no work -> Tt=const Pt=const
aoas_1 = aoastar(g.k, M_1)
as1oas2 = 1
aoas_2 = (A_2/A_1)*aoas_1*as1oas2

M_2,_ = get_mach_given_aoastar(aoas_2, g.k)
ptop = isen_ratio_p(g.k, M_2)
ttop = isen_ratio_t(g.k, M_2)

PR = 1/ptop
TR = 1/ttop

P_2 = PR * Pt_1
T_2 = TR * Tt_1

print(f"------ RESULTS ---------")
print(f" at station 2")
print(f"A/A* = {aoas_2:10.6f}")
print(f"M    = {M_2:10.6f}")
print(f"T = {T_1:10.6f}")
print(f"P = {P_2:10.6f}")


