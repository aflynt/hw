
from libgd import *

def prob_601():
    # AIR
    # standing normal shock

    g = Gas_mgr().AIR_SI
    M1 = 1.8

    pr = norm_shock_pr(M1, g.k)
    tr = norm_shock_tr(M1, g.k)
    rr = norm_shock_rr(M1, g.k)

    print(f"PR = {pr:.3f}")
    print(f"TR = {tr:.3f}")
    print(f"RR = {rr:.3f}")

    dpt = norm_shock_ptr(M1, g.k)
    ds = -g.R*m.log(dpt)
    print(f"dpt = {dpt:.4f}")
    print(f"ds  = {ds :.4f}")

    dpt2 = norm_shock_ptr(2.8, g.k)
    dpt3 = norm_shock_ptr(3.8, g.k)
    ds2 = -g.R*m.log(dpt2)
    ds3 = -g.R*m.log(dpt3)
    print(f"dpt2.8 = {dpt2 :.4f}")
    print(f"dpt3.8 = {dpt3 :.4f}")
    print(f"ds2.8 = {ds2 :.4f}")
    print(f"ds3.8 = {ds3 :.4f}")

    
def prob_605():

    g = Gas_mgr().AIR_SI
    M3 = 0.52
    P2oP1 = 2
    Pt1oPt2 = 1

    M2 = norm_shock_m1(M3, g.k)
    pr2 = isen_ratio_p(M2,g.k)
    aoas2 = aoastar(g.k, M2)
    print(f" found M2 = {M2:.6f}")
    print(f"{pr2 =}")
    print(f"{aoas2 =}")

    # isentropic flow from 1 to 2 -> pt1 == pt2
    pr1 = Pt1oPt2*pr2*P2oP1
    M1 = get_mach_given_pr(pr1,g)
    aoas1 = aoastar(g.k, M1)
    #print(f"{pr1=}")
    #print(f"{M1=}")
    print_var("A/A*_1", aoas1)

    A1oA2 = aoas1 * 1 * (1/aoas2)
    print_var("A1 / A2", A1oA2)

def prob_606():

    # GIVEN
    g = Gas_mgr().NITROGEN_SI
    k = g.k
    M1 = 2.90
    A3 = 0.20
    A2 = 0.25

    M2 = norm_shock_m2(M1, k)
    T2oT1 = norm_shock_tr(M1, k)

    TR2 = isen_ratio_t(M2,k)
    aoas2 = aoastar(k, M2)

    aoas3 = A3/A2*aoas2*1

    M3,_ = get_mach_given_aoastar(aoas3, k)

    TR3 = isen_ratio_t(M3,k)

    T3oT1 = (1/TR3)*(1)*TR2*T2oT1

    print(f" --- problem 6.06 ---")
    print_var("M_2", M2)
    print_var("Tt_2/T_2", TR2)
    print_var("A_2/A*_2", aoas2)
    print_var("A_3/A*_3", aoas3)
    print_var("M_3", M3)
    print_var("Tt_3/T_3", TR3)
    print_var("T_3/T_2", T3oT1)

def prob_607():

    # given CD NOZZLE DESIGNED FOR M = 2.5
    Me = 2.5
    g = Gas_mgr().AIR_EE
    k = g.k

    # CRITICAL PT 3: supersonic exit
    pr3 = 1/isen_ratio_p(Me,k)
    aoas3 = aoastar(k, Me)

    # CRITICAL PT 1: subsonic exit
    M1,_ = get_mach_given_aoastar(aoas3, k)
    pr1   = 1/isen_ratio_p(M1,k)

    # CRITICAL PT 2: shock at exit
    prs = norm_shock_pr(Me, k)
    pr2 = prs*pr3*1

    print(f" ---- Design point ---- ")
    print_var("Nozzle A/A*", aoas3)
    print_var("CP 1: Pe/Pt", pr1)
    print_var("CP 2: Pe/Pt", pr2)
    print_var("CP 3: Pe/Pt", pr3)
    print_var("M_sub"  , M1)
    print_var("M_super", Me)
    print_var("NS P4/P3", prs)

    # b) given Pt = 150 psia -> get pe for each critical point operation
    pt = 150
    pe1 = pr1*pt
    pe2 = pr2*pt
    pe3 = pr3*pt
    print_var("pe1", pe1)
    print_var("pe2", pe2)
    print_var("pe3", pe3)

    # c) given pe = 15 psia -> get Pt
    pe = 15

    pt1 = pe/pr1
    pt2 = pe/pr2
    pt3 = pe/pr3
    print_var("pt1", pt1)
    print_var("pt2", pt2)
    print_var("pt3", pt3)

def prob_609():

    # given
    M1 = 3
    g = Gas_mgr().CARBON_MONOXIDE_EE
    k = g.k
    R = g.R

    p1opt1 = 1/isen_ratio_p(M1,k)
    aoastar1 = aoastar(k,M1)

def prob_615():

    # Given
    pt1   = 8.0 # bar
    prec  = 3.5 # bar
    AR_design = 3.0 # area ratio of exit to throat
    k = 1.4
    PR_op = prec/pt1

    M_sub, M_sup = get_mach_given_aoastar(AR_design, k)

    # PR for 1st and 3rd critical point
    popt1 = 1/isen_ratio_p(M_sub,k)
    popt3 = 1/isen_ratio_p(M_sup,k)

    # PR for 2nd critical point
    pr_shock = norm_shock_pr(M_sup, k)
    popt2 = pr_shock*popt3*1

    # b) Mach number at the outlet
    AR_PR = AR_design*PR_op
    M_outlet = mach_given_ar_pr(AR_design, PR_op, k)

    # c) shock location & Mshock
    popt5 = 1/isen_ratio_p(M_outlet,k)
    pt5opt1 = PR_op/popt5

    mshock = mach_given_ptr(pt5opt1, k)
    aoas = aoastar(k,mshock)

    print_var("oper. PR", PR_op)
    print_var("M_sub", M_sub)
    print_var("M_sup", M_sup)
    print_var("p/pt1", popt1)
    print_var("p/pt2", popt2)
    print_var("p/pt3", popt3)
    print_var("P4/P3 across shock", pr_shock)
    print_var("AR*PR", AR_PR)
    print_var("M at exit", M_outlet)
    print_var("p5/Pt5", popt5)
    print_var("Pt5/Pt1", pt5opt1)
    print_var("M shock", mshock)
    print_var("aoas", aoas)

def prob_619():
    g = Gas_mgr().AIR_EE
    cp = g.cp
    k = g.k
    R = g.R

    mdot = 18.39
    dH = 742

    dT = (dH * 550  )/(   mdot*cp*778.2  )
    T7 = 539.67
    T6 = T7 - dT

    T7oT6 = T7/T6
    PR = T7oT6**(k/(k-1))
    P7 = 14.7
    P6 = P7/PR
    print_var("delta T", dT)
    print_var("T6 ", T6)
    print_var("TR ", T7oT6)
    print_var("PR ", PR)
    print_var("P6 ", P6)





prob_619()