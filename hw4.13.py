from libgd import *

g = Gas_mgr().METHANE_SI
R  = g.R
k  = g.k

P1 = 14e5
T1 = 500
V1 = 125

# can get a from T1
a1 = speed_of_sound(k,R,T1)

# can get M1
M1 = V1/a1

# with M we get TR, PR
TR1 = isen_ratio_t(M1,k)
PR1 = isen_ratio_p(M1,k)

# now get Pt Tt
Tt1 = T1*TR1
Pt1 = P1*PR1

print(f"Tt1 = {Tt1:10.3f} K")
print(f"Pt1 = {Pt1:10.3e} Pa")

# Energy balance shows no losses
Tt2 = Tt1
Pt2 = Pt1

# we know mach 2
M2 = 0.8
TR2 = isen_ratio_t(M2,k)
PR2 = isen_ratio_p(M2,k)

# now get static values
T2 = Tt2/TR2
P2 = Pt2/PR2
print(f"found T2 = {T2:12.3f} K")
print(f"found p2 = {P2:12.3f} Pa")

# now get a2
a2 = speed_of_sound(k,R,T2)
V2 = M2*a2
print(f"found v2 = {V2:12.3f} m/s")

AR = P1/P2 * T2/T1 * V1/V2
print(f"AR = {AR:10.3f}")
