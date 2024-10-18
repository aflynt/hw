from libgd import *

#Gas: Carbon monoxide 
#adiabatic system. 
#(a)	Are there losses in this system? If so, compute s.
#(b)	Determine the ratio of A2/A1

g = Gas_mgr().CARBON_MONOXIDE_EE

M1 = 4.0
Pt1 = 45 # psia 


M2 = 1.8 
P2 = 7.0 # psia

PR2 = isen_ratio_p(M2,g.k)
Pt2 = PR2*P2

inv_pr = 1/PR2

ds = ds_given_dpt(Pt1, Pt2, g.R)

TR1 = isen_ratio_t(M1,g.k)
TR2 = isen_ratio_t(M2,g.k)

A2oA1 = A2oA1_given_MR_ds(M1, M2, ds, g)

ds_btu = ds/778.2
# GIVEN
# Adiabatic -> q = 0
# no work  -> Tt = constant



print()

