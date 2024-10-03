from libgd import *

def ex701():
    #given
    g = Gas_mgr().AIR_EE

    T1 = 520  # R
    P1 = 14.7 # psia
    Vs = 1800 # ft/s
    V1 = 0 #ft/s
    
    T1p = T1
    P1p = P1
    V1p = V1 + Vs
    a1p = gas_sos(T1p, g)
    M1p = V1p/a1p

    prp = norm_shock_pr(M1p, g.k)
    trp = norm_shock_tr(M1p, g.k)
    M2p = norm_shock_m2(M1p, g.k)

    P2p = prp*P1p # actual static pres after shock
    T2p = trp*T1p # actual static temp after shock

    a2p = gas_sos(T2p, g) # actual sos after shock
    V2p = M2p*a2p
    V2 = Vs - V2p # actual velocity after shock
    M2 = V2/a2p

    pr2  = isen_ratio_p(g.k, M2)

    pt1 = P1
    pt2 = pr2*P2p # total pressure post-shock
    ds = ds_given_dpt(pt2, pt1, g.R, False)
    print_var("ds", ds)

    pr1p = isen_ratio_p(g.k, M1p)
    pr2p = isen_ratio_p(g.k, M2p)
    pt1p = pr1p*P1
    pt2p = pr2p*P2p

    dsp = ds_given_dpt(pt1p, pt2p, g.R, False)
    print_var("ds", dsp)

    print_var("a1'", a1p)
    print_var("V1'", V1p)
    print_var("M1'", M1p)
    print_var("M2'", M2p)
    #print_var("pr'", prp)
    #print_var("tr'", trp)
    print_var("P2'", P2p)
    print_var("T2'", T2p)
    print_var("a2'", a2p)
    print_var("V2'", V2p)
    print_var("M2", M2)
    print_var("V2", V2)
    print_var("pt1", pt1)
    print_var("pt2", pt2)
    #print_var("pt1_'", pt1p)
    #print_var("pt2_'", pt2p)

def ex_known_shock_speed():
    # given
    # normal shock moves at Vs = 520 m/s into still air
    g = Gas_mgr().AIR_SI
    T1 = 300 #K
    P1 = 101325 # pa
    Vs = 520 # m/s
    V1 = 0   # m/s

    T1p = T1
    P1p = P1
    V1p = V1 + Vs
    a1p = gas_sos(T1p, g)
    M1p = V1p/a1p

    prp = norm_shock_pr(M1p, g.k)
    trp = norm_shock_tr(M1p, g.k)
    M2p = norm_shock_m2(M1p, g.k)

    P2p = prp*P1p # actual static pres after shock
    T2p = trp*T1p # actual static temp after shock

    a2p = gas_sos(T2p, g) # actual sos after shock
    V2p = M2p*a2p
    V2 = Vs - V2p # actual velocity after shock
    M2 = V2/a2p

    TR2   = isen_ratio_t(g.k, M2)
    Tt2 = TR2*T2p # total pressure post-shock

    TR2p  = isen_ratio_t(g.k, M2p)
    Tt2p  = TR2p*T2p

    TR1p  = isen_ratio_t(g.k, M1p)
    Tt1p  = TR1p*T1p

    rho1 = P1/(g.R*T1)
    rho1p = P1p/(g.R*T1p)
    print_var("rho_1", rho1)
    print_var("rho_1'", rho1p)

    Tt1 = T1
    #print_var("a1'", a1p)
    #print_var("V1'", V1p)
    #print_var("M1'", M1p)
    #print_var("M2'", M2p)
    #print_var("pr'", prp)
    #print_var("tr'", trp)
    #print_var("P2'", P2p)
    #print_var("T2'", T2p)
    #print_var("a2'", a2p)
    #print_var("V2'", V2p)
    #print_var("M2", M2)
    #print_var("V2", V2)
    print_var("Tt1", Tt1)
    print_var("Tt1'", Tt1p)
    print_var("Tt2", Tt2)
    print_var("Tt2'", Tt2p)

def p703():
    '''
    given Air_EE

                Vs--- moving shock
    ------------------------
    flow ->   <__|  v=0     valve_closed
    ------------------------
    ------------------------
    flow --->    |  v=vs    valve_closed
    ------------------------

    valve closes on moving flow -> flow stagnates after a moving shock moves left up pipe
    P2 = 30 psia
    T2 = 600 R
    V2 = 0         air is brought to rest on RHS
    Vs = 1010 ft/s shock speed to left
    '''
    g = Gas_mgr().AIR_EE
    P2 = 30
    T2 = 600
    V2 = 0
    Vs = 1010

    V2p = Vs
    P2p = P2
    T2p = T2

    a2p = gas_sos(T2p, g)
    print_var("a_2'", a2p)

    M2p = V2p/a2p
    print_var("M_2'", M2p)

    # NORMAL SHOCK TABLES -> M1p
    M1p = norm_shock_m1(M2p, g.k)
    print_var("M_1'", M1p)

    dvoa = norm_shock_dvoa(M1p, g.k)
    print_var("dV/a'", dvoa)

    T2poT1p = norm_shock_tr(M1p, g.k)
    P2poP1p = norm_shock_pr(M1p, g.k)
    T1p = T2p/T2poT1p
    P1p = P2p/P2poP1p

    a1p = gas_sos(T1p, g)
    dvp = dvoa * a1p
    print_var("dv'", dvp)

def p704():
    '''
    given oxygen_ee

                Vs--- moving shock
    ------------------------
    flow ->   <__|  v=0     valve_closed
    ------------------------
    ------------------------
    flow --->    |  v=vs    valve_closed
    ------------------------

    valve closes on moving flow -> flow stagnates after a moving shock moves left up pipe
    P1 =   20 psia
    T1 =  560 R
    V1 =  450 ft/s
    V2 =    0 air is brought to rest on RHS
    Vs = ?? IDK
    '''
    g = Gas_mgr().OXYGEN_EE
    P1 = 20
    T1 = 560
    V1 = 450

    P1p = P1
    T1p = T1

    a1p = gas_sos(T1p, g)

    dvoa = V1 / a1p

    fzero = lambda m: norm_shock_dvoa(m, g.k) - dvoa

    M1p  = bisector(fzero, 1, 5)
    M2p  = norm_shock_m2(M1p, g.k)
    TRns = norm_shock_tr(M1p, g.k)
    PRns = norm_shock_pr(M1p, g.k)
    T2p = TRns * T1p
    P2p = PRns * P1p
    a2p = gas_sos(T2p, g)
    V2p = M2p*a2p


def p705():

    g = Gas_mgr().NITROGEN_SI

    P1p = 1e4
    T1p = 293.15
    Vs  = 380
    V1p = 0 + Vs
    a1p = gas_sos(T1p, g)
    M1p = V1p/a1p

    M2p  = norm_shock_m2(M1p, g.k)
    PRns = norm_shock_pr(M1p, g.k)
    TRns = norm_shock_tr(M1p, g.k)
    P2p = PRns * P1p
    T2p = TRns * T1p
    a2p = gas_sos(T2p, g)
    V2p = M2p*a2p
    V2  = Vs - V2p

    print_var("M2p " , M2p )
    print_var("PRns" , PRns)
    print_var("TRns" , TRns)
    print_var("P2p " , P2p , 12, 0)
    print_var("T2p " , T2p )
    print_var("a2p " , a2p )
    print_var("V2p " , V2p )
    print_var("V2  " ,V2 )

def p705b():
    g = Gas_mgr().NITROGEN_SI
    T2p = 310
    P2p = 12201
    V2  = 50.3

    a2p = gas_sos(T2p, g)
    print(f"a2p = {a2p}")
    dvoa = V2/a2p
    print(f"dv/a = {dvoa}")

    fzero = lambda x: norm_shock_dvoa(x, g.k) - dvoa

    M2p  = bisector(fzero, 1, 5)
    M3p  = norm_shock_m2(M2p, g.k)
    PRns = norm_shock_pr(M2p, g.k)
    TRns = norm_shock_tr(M2p, g.k)
    T3p  = TRns * T2p
    P3p  = PRns * P2p
    a3p = gas_sos(T3p, g)
    V3p = M3p*a3p

    print(f"M2p  = bisector(fzero, 1, 5) = {M2p}")
    print(f"M3p  = norm_shock_m2(M2p, g.k) = {M3p}")
    print(f"PRns = norm_shock_pr(M2p, g.k) = {PRns}")
    print(f"TRns = norm_shock_tr(M2p, g.k) = {TRns}")
    print(f"T3p  = TRns * T2p = {T3p}")
    print(f"P3p  = PRns * P2p = {P3p}")
    print(f"a3p = gas_sos(T3p, g) = {a3p}")
    print(f"V3p = M3p*a3p = {V3p}")



#ex701()
#ex_known_shock_speed()
print()
p705b()