from libgd import *
print("\n")
"""
The following information is known about the steady flow of air through an adiabatic system:
•	At section 1, T1 = 556°R, p1,= 28.0 psia
•	At section 2, T2 = 70°F, Tt2 = 109°F, p2,= 18 psia
(a)	Find M2, V2, and pt2.
(b)	Determine M1, V1, and pt1.
(c)	Compute the area ratio A2/A1.
(d)	Sketch a physical diagram of the system along with a T –s diagram
"""
# KNOWN
# no work ? -> yes
# q = 0? -> yes
# ->-> Tt = constant
# no losses? -> NO

g = gases_ee["AIR"]

#•	At section 1, 
T1 = 556  # R
p1 = 28.0 # psia

#•	At section 2, 
T2  =  70 + 459.67 # R
Tt2 = 109 + 459.67 # R
p2  = 18 # psia


a2 = gas_sos(T2, g)
TR2 = Tt2/T2
M2 = get_mach_given_tr(TR2, g) #__
PR2 = isen_ratio_p(g.k, M2)
V2 = M2*a2 #__
Pt2 = PR2*p2 #__

# at 1
Tt1 = Tt2

TR1 = Tt1/T1
M1 = get_mach_given_tr(TR1, g)
PR1 = isen_ratio_p(g.k, M1)
Pt1 = PR1*p1
a1 = gas_sos(T1, g)
V1 = M1*a1

A2oA1 = nohw_A2oA1(p1, p2, M1, M2, T1, T2)
ds = ds_given_dpt(Pt1, Pt2, g.R)
s0 = 0
s1 = ds

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.plot([s0, s1], [Tt1, Tt2], '-o', color='k')
ax.plot([s0, s0], [Tt1, T1], '--o', color='k')
ax.plot([s1, s1], [Tt2, T2], '--o', color='k')
ax.plot([s0, s1], [T1, T2], '-o', color='b')
ax.set_xlabel("s [ft-lbf/lbm-R]")
ax.set_ylabel("T [R]")
ax.grid()
plt.show()




def other():
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


