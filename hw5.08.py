from libgd import *
"""
5.8 Two venturi meters are installed in a 30-cm-diameter duct that is insulated
(Figure P5.8). The conditions are such that sonic flow exists at each throat
(i.e., M1 = M4 = 1.0). Although each venturi is isentropic, the connecting duct
has friction and hence losses exist between sections 2 and 3. p1 = 3 bar abs.
and p4 = 2.5 bar abs. If the diameter at section 1 is 15 cm and the fluid is air:
(a)	Compute ds for the connecting duct.
(b)	Find the diameter at section 4.

Gas: AIR
adiabatic system  -> q=0
no work -> Tt = constant
"""
# ----------------------------------------------
g = gases_si["AIR"]
# ----------------------------------------------
# Given station data
D1 = 0.150 # m
M1 = 1.0
P1 = 3.0 # bar abs

M4 = 1.0
P4 = 2.5 # bar abs
# ----------------------------------------------
# get area ratio from 1 to 2

PTrat = nohw_Pt2oPt1_given_Ms(P4, P1, g.k, M1, M4)
ds    = ds_given_dpt(1, PTrat, g.R)
A4oA1 = A2oA1_given_MR_ds(M1, M4, ds, g)
D4    = m.sqrt(A4oA1)*D1

print(f"ds = {ds:12.6f} J/kg-K")
print(f"D4 = {D4*1000:6.0f} mm")