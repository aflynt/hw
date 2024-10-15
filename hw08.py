# %%
from libgd import *
import matplotlib.pyplot as plt

# %%
def p706():
    g = Gas_mgr().AIR_EE

    # oblique shock forms in air at theta = 30 deg
    th = 30*m.pi/180
    M1 = 2.6

    P1 = 10 # psia
    T1 = 60+460 # 520 R
    a1 = gas_sos(T1, g)
    v1 = M1*a1
    v1n = v1*m.sin(th)
    v1t = v1*m.cos(th)
    M1n = M1*m.sin(th)
    M2n = norm_shock_m2(M1n,g.k)
    PR  = norm_shock_pr(M1n, g.k)
    TR  = norm_shock_tr(M1n, g.k)
    P2  = PR*P1
    T2  = TR*T1
    a2  = gas_sos(T2, g)
    v2n = M2n*a2
    v2t = v1t
    v2  = m.sqrt(v2n**2 + v2t**2)
    beta = m.atan(v2t/v2n)
    delta = th - m.pi/2+beta

    print_var("P1  = 10 # psia",                       P1)
    print_var("T1  = 60+460 # 520 R",                       T1)
    print_var("a1  = gas_sos(T1, g)",                       a1)
    print_var("v1  = M1*a1",                       v1)
    print_var("v1n = v1*m.sin(th)",                       v1n)
    print_var("v1t = v1*m.cos(th)",                       v1t)
    print_var("M1n = M1*m.sin(th)",                       M1n)
    print_var("M2n = norm_shock_m2(M1n,g.k)",                       M2n)
    print_var("PR  = norm_shock_pr(M1n, g.k)",                       PR )
    print_var("TR  = norm_shock_tr(M1n, g.k)",                       TR )
    print_var("P2  = PR*P1",                       P2 )
    print_var("T2  = TR*T1",                       T2 )
    print_var("a2  = gas_sos(T2, g)",                       a2 )
    print_var("v2n = M2n*a2",                       v2n)
    print_var("v2t = v1t",                       v2t)
    print_var("v2  = m.sqrt(v2n**2 + v2t**2)",                       v2 )
    print_var("beta= m.atan(v2t/v2n)",                       beta)
    print_var("delta = th - m.pi/2+beta",                       delta)
    print_var("beta  [deg]",                       beta *180/m.pi)
    print_var("delta [deg]",                       delta*180/m.pi)


def p707():
    g = Gas_mgr().AIR_SI

    # oblique shock forms in air at theta = 30 deg
    T1 = 40+273.15
    P1 = 1.2e5 # psia
    M1 = 3.0
    th = 45*m.pi/180

    a1 = gas_sos(T1, g)
    v1 = M1*a1
    v1n = v1*m.sin(th)
    v1t = v1*m.cos(th)
    M1n = M1*m.sin(th)
    M2n = norm_shock_m2(M1n,g.k)
    PR  = norm_shock_pr(M1n, g.k)
    TR  = norm_shock_tr(M1n, g.k)
    P2  = PR*P1
    T2  = TR*T1
    a2  = gas_sos(T2, g)
    v2n = M2n*a2
    v2t = v1t
    v2  = m.sqrt(v2n**2 + v2t**2)
    beta = m.atan(v2t/v2n)
    delta = th - m.pi/2+beta
    M2 = v2 / a2

    M22 = oblique_m2(M1, delta)
    print(f"M22 = {M22}")

    print_var("P1  : [kpa]",                       P1/1000)
    print_var("T1  : [K]",                       T1)
    print_var("a1  : gas_sos(T1)",                       a1)
    print_var("v1  : M1*a1",                       v1)
    print_var("v1n : v1*sin(th)",                       v1n)
    print_var("v1t : v1*cos(th)",                       v1t)
    print_var("M1n : M1*sin(th)",                       M1n)
    print_var("M2n : ns_m2(M1n",                       M2n)
    print_var("M2  :          ",                       M2)
    print_var("PR  : ns_pr(M1n",                       PR )
    print_var("TR  : ns_tr(M1n",                       TR )
    print_var("P2  : PR*P1 [kPa]",                       P2/1000 )
    print_var("T2  : TR*T1 [K]",                       T2 )
    print_var("a2  : gas_sos(T2)",                       a2 )
    print_var("v2n : M2n*a2",                       v2n)
    print_var("v2t : v1t",                       v2t)
    print_var("v2  : sqrt(v2n**2 + v2t**2)",                       v2 )
    print_var("beta: atan(v2t/v2n)",                       beta)
    print_var("delta : th - m.pi/2+beta",                       delta)
    print_var("beta  [deg]",                       beta *180/m.pi)
    print_var("delta [deg]",                       delta*180/m.pi)

#p707()
# %%
def p710():

    # a wedge with total angle
    d = 28/2*m.pi/180
    th = 50*m.pi/180

    #L = lambda M1: m.tan(d) - (2/m.tan(th))*(M1**2*m.sin(th)**2-1)/( M1**2*(1.4+m.cos(2*th))   + 2)

    #M = bisector(L, 1, 10)
    M = oblique_m1(d,th)
    print(f"M -> {M}")

    print(f"per Fig. AD.3 shocks would detach for M1 < 1.6")
    print(f" -> useful for M1 >= 1.6")

#p710()

# %%
def p713():
    g = Gas_mgr().AIR_EE
    P0 = 243 # psfa
    T0 = 392 # R
    M0 = 2.5
    d  = 15 * m.pi/180 # wedge angle

    # a) conditions of air (temp, pressure, entropy change) just after
    #    it passes through the normal shock

    # go thru oblique shock to get to 1
    _, M1, PR1, TR1, PTR1, _, _ = oblique_shock_relations(M0, d)

    ## go thru normal shock to get to 2
    M2, PR2, TR2, PTR2 = norm_shock_relations(M1, g.k)

    T1 = TR1 * T0
    T2 = TR2 * T1

    P1 = PR1 * P0
    P2 = PR2 * P1

    ds1 = ds_given_dpt(1, PTR1, g.R, g.isSI)
    ds2 = ds_given_dpt(1, PTR2, g.R, g.isSI)
    dstot = ds1+ds2

    # report results
    print(f"after oblique shock -> ")
    print_var("M1", M1)
    print_var("PR1", PR1)
    print_var("TR1", TR1)
    print_var("T1", T1)
    print_var("P1", P1)
    print_var("PTR1", PTR1)
    print_var("ds1 [Btu/lbm-R]", ds1)
    print(f"after normal shock -> ")
    print_var("M2", M2)
    print_var("PR2", PR2)
    print_var("TR2", TR2)
    print_var("T2", T2)
    print_var("P2", P2)
    print_var("PTR2", PTR2)
    print_var("ds2 [Btu/lbm-R]", ds2)
    print_var("dst [Btu/lbm-R]", dstot)

    Tt0 = isen_ratio_t(g.k, M0)*T0
    s0 = 0

    PTRa = PTR2*PTR1
    print(f"PTRA = {PTRa:10.4f}")

    ## state before shock
    ss0 = [s0 , s0]
    ts0 = [Tt0, T0]
    plt.plot(ss0, ts0, "--k")

    ## ok now show after oblique shock
    ss1 = [ds1 , ds1]
    ts1 = [Tt0, T1]
    plt.plot(ss1, ts1, "--k")

    # ok now show after normal shock
    ss2 = [dstot , dstot]
    ts2 = [Tt0, T2]
    plt.plot(ss2, ts2, "--k")
    plt.plot([0, ds1], [T0, T1], "-b")
    plt.plot([ds1, dstot], [T1, T2], "-r")


    '''
    # part_c, single 15 degree wedge replaced by double wedge of
    * 7 deg
    * 8 deg
    '''
    # given
    cM1 = 2.5
    cP1 = P0
    cT1 = T0
    cd1 = deg2rad(7)
    cd2 = deg2rad(8)

    _, cM2, cPR2, cTR2, cPTR2, _, _ = oblique_shock_relations(cM1, cd1)
    _, cM3, cPR3, cTR3, cPTR3, _, _ = oblique_shock_relations(cM2, cd2)
    cM4, cPR4, cTR4, cPTR4 = norm_shock_relations(cM3, g.k)

    cT2 = cTR2*cT1
    cT3 = cTR3*cT2
    cT4 = cTR4*cT3

    cP2 = cPR2*cP1
    cP3 = cPR3*cP2
    cP4 = cPR4*cP3

    cds2  = ds_given_dpt(1,cPTR2, g.R, g.isSI)
    cds3  = ds_given_dpt(1,cPTR3, g.R, g.isSI)
    cds4  = ds_given_dpt(1,cPTR4, g.R, g.isSI)

    print(f"part c, after 1st shock")
    print_var("cM2   ", cM2   )
    print_var("cPR2  ", cPR2  )
    print_var("cTR2  ", cTR2  )
    print_var("cPTR2 ", cPTR2 )
    print_var("cT2   ", cT2   )
    print_var("cP2   ", cP2   )
    print_var("cds2  ", cds2  )
    print(f"part c, after 2nd shock")
    print_var("cM3   ", cM3   )
    print_var("cPR3  ", cPR3  )
    print_var("cTR3  ", cTR3  )
    print_var("cPTR3 ", cPTR3 )
    print_var("cT3   ", cT3   )
    print_var("cP3   ", cP3   )
    print_var("cds3  ", cds3  )
    print(f"part c, normal shock")
    print_var("cM4   ", cM4)
    print_var("cTR4  ", cTR4)
    print_var("cPR4  ", cPR4)
    print_var("cPTR4 ", cPTR4)
    print_var("cT4   ", cT4)
    print_var("cP4   ", cP4)
    print_var("cds4  ", cds4)

    PTRc = cPTR2*cPTR3*cPTR4
    print(f"PTRc = {PTRc:10.4f}")

    cs1 = 0
    cs2 = cs1 + cds2
    cs3 = cs2 + cds3
    cs4 = cs3 + cds4
    print(f"ds4 = {cs4:10.4f} [Btu/lbm-R]")

    css = [cs1, cs2, cs3, cs4]
    cts = [cT1, cT2, cT3, cT4]
    plt.plot(css,cts, "--b", marker="*")
    plt.grid(True)

    plt.show()

p713()

# %% p714
def p714():

    g = Gas_mgr().NITROGEN_SI

    M1 = 2.5
    T1 = 150   # K
    P1 = 0.7e5 # Pa
    Prec = 1.0e5 # Pa

    # oblique shock at A
    PRA = Prec/P1
    th = oblique_theta(M1, PRA)
    dA = oblique_delta(M1, th)

    PRA = oblique_ratio_p(M1, dA)
    TRA = oblique_ratio_t(M1, dA )
    M2  = oblique_m2(M1, dA)
    T2 = TRA*T1
    P2 = Prec

    print_var("PRA", PRA)
    print_var("TRA", TRA)

    print_var("P2", P2)
    print_var("T2", T2)

    # now go across oblique shock at B
    dB = dA

    thB = oblique_beta_zero(M2, dB)
    PRB = oblique_ratio_p(M2, dB)
    TRB = oblique_ratio_t(M2, dB )
    M3  = oblique_m2(M2, dB)
    T3 = TRB*T2
    P3 = PRB*P2

    print(f"theta_B = {rad2deg(thB):10.4f} deg")
    print(f"delta_B = {rad2deg(dB):10.4f} deg")
    print_var("thB [deg]", rad2deg(thB)) 
    print_var("PRB", PRB) 
    print_var("TRB", TRB) 
    print_var("M3 ", M3 ) 
    print_var("T3 [K]", T3) 
    print_var("P3 [bar]", P3/1e5) 

#p714()

# %% problem 7.15
from libgd import *

M1 = 1.8
P1 = 15  # psia
T1 = 600 # R
d1 = 10*m.pi/180

# a)
# oblique shock from 1->2

th1 = oblique_beta_zero(M1, d1)
M2 = oblique_m2(M1, d1)
pr12 = oblique_ratio_p(M1,d1)
tr12 = oblique_ratio_t(M1,d1)
T2 = tr12*T1
P2 = pr12*P1

# c)
# now oblique shock from 2->3
d2 = d1
th2 = oblique_beta_zero(M2, d2)
M3 = oblique_m2(M2, d2)
pr23 = oblique_ratio_p(M2,d2)
tr23 = oblique_ratio_t(M2,d2)
T3 = tr23*T2
P3 = pr23*P2

# d)
# T2, P2, M2 if pt2 = 71 psia
pt2 = 71
ptop1 = isen_ratio_p(1.4, M1)
pt1 = ptop1*P1
print(f"pt1 = {pt1:10.2f}")
ptr = pt2/pt1

f = lambda th1d: oblique_ratio_pt_theta(M1, th1d) - ptr

# find strong shock with large angle
th1d = bisector(f, m.pi/10, m.pi/2-0.05)
print(f"theta -> {th1d:10.3f} -> {th1d*180/m.pi:10.2f} deg")


k = 1.4
pr12d = 1 + 2*k/(k+1)*(M1**2*m.sin(th1d)**2 - 1)
tr12d = 1 + 2*(k-1)/(k+1)**2*(k*M1**2*m.sin(th1d)**2 + 1)/(M1**2*m.sin(th1d)**2)*(M1**2*m.sin(th1d)**2-1)
p2d = P1*pr12d
t2d = T1*tr12d
print_var("pr12d",pr12d)
print_var("tr12d",tr12d)
print_var("p2d",p2d)
print_var("t2d",t2d)

sin_val = m.sin(th1d-d2)**2
M2d     = m.sqrt((1 + (k-1)/2*M1**2*m.sin(th1d)**2) / ((k*M1**2*m.sin(th1d)**2 - (k-1)/2) * sin_val))
print_var("M2d",M2d)


# %%
