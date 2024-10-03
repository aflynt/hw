from libgd import *

def ex701():
    #given
    g = Gas_mgr().AIR_EE

    T1 = 520  # R
    P1 = 14.7 # psia
    Vs = 1800 # ft/s
    V1 = 0 #ft/s
    
    # add shock velocity to get prime values (statics dont change)
    T1p = T1
    P1p = P1
    V1p = V1 + Vs
    a1p = gas_sos(T1p, g)
    M1p = V1p/a1p

    # Now can use normal shock tables at M1'
    pr = norm_shock_pr(M1p, g.k)
    tr = norm_shock_tr(M1p, g.k)
    M2p = norm_shock_m2(M1p, g.k)

    # get actual values at 2'
    P2p = pr*P1p
    T2p = tr*T1p
    a2p = gas_sos(T2p, g)
    V2p = M2p*a2p

    V2 = Vs - V2p

    M2 = V2/a2p

    pt1 = P1
    pt2p = isen_ratio_p(g.k, M2)*P2p

    print_var("a1'", a1p)
    print_var("V1'", V1p)
    print_var("M1'", M1p)
    print_var("M2'", M2p)
    print_var("M2", M2)
    print_var("PR", pr)
    print_var("TR", tr)
    print_var("P2'", P2p)
    print_var("T2'", T2p)
    print_var("a2'", a2p)
    print_var("V2'", V2p)
    print_var("V2", V2)
    print_var("pt1'", pt1)
    print_var("pt2p'", pt2p)

ex701()