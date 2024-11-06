
# %%e
from libgd import *

def plot_wedge():
    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle, Circle, FancyArrow, FancyArrowPatch, Polygon
    import numpy as np
    
    fig,ax = plt.subplots()
    L = 6
    a = 12/2
    dy = L*0.5*m.sin(a*m.pi/180)
    dx = L*0.5*m.cos(a*m.pi/180)
    
    alpha = 3
    #alpha = 10
    
    point_list = [
        (0, 0),
        (dx,dy),
        (L, 0),
        (dx, -dy),
        (0,0)
    ]
    
    xs = [x[0] for x in point_list]
    ys = [x[1] for x in point_list]
    
    
    rpl = rotate_points(point_list, -alpha)
    
    xps = [x[0] for x in rpl]
    yps = [x[1] for x in rpl]
    
    #ax.plot(xs,ys, '-', color="k")
    ax.plot(xps,yps, '-', color="r")
    
    ax.set_xlim(-1, L+1)
    ax.set_ylim(-(L/2+1), L/2+1)
    ax.grid(True)
    plt.show()

# %%
def p801():
    M1 = 2
    T1 = 520
    P1 = 14.7
    dnu = 15
    
    nu1 = isen_pm_nu(M1)
    tr1 = isen_ratio_t(M1)
    pr1 = isen_ratio_p(M1)
    
    Pt1 = pr1*P1
    Tt1 = tr1*T1
    
    nu2 = nu1 + dnu
    
    M2 = isen_pm_M(nu2)
    pr2 = isen_ratio_p(M2)
    tr2 = isen_ratio_t(M2)
    
    P2 = Pt1 / pr2
    T2 = Tt1 / tr2
    print_var("M2", M2)
    print_var("P2", P2)
    print_var("T2", T2)

#p801()

# %% p 803
def p803():
    P1 = 1e5 # pa
    T1 = 350 # K
    
    dnu = 35 # degrees
    M2 = 3.5
    
    nu2 = isen_pm_nu(M2)
    pr2 = isen_ratio_p(M2)
    tr2 = isen_ratio_t(M2)
    mu2 = m.asin(1/M2)*180/m.pi
    th2 = mu2
    print_var("mach wave angle at 2", mu2)
    
    nu1 = nu2 - dnu
    M1  = isen_pm_M(nu1)
    pr1 = isen_ratio_p(M1)
    tr1 = isen_ratio_t(M1)
    mu1 = m.asin(1/M1)*180/m.pi
    print_var("mach wave angle at 1", mu1)
    
    print_var("nu2", nu2)
    T2 = 1/tr2*1*tr1*T1
    P2 = 1/pr2*1*pr1*P1
    print_var("T2", T2)
    print_var("P2", P2)
    
    th1 = 180 - mu1
    print_var("theta_1", th1)
    th3 = 180 + dnu - th1 - th2
    print_var("th3", th3)

# %%

def p808a():
    # given
    M1 = 1.8
    p1 = 8.5 # psia
    #alpha1 = 3
    alpha1 = 10
    theta_LE = 6
    L = 6*12 # in
    
    L_face = L/2/m.cos(theta_LE*m.pi/180)
    print_var("L_face", L_face)
    th_lo = theta_LE-alpha1
    th_hi = theta_LE+alpha1
    
    th_lo_rad = th_lo*m.pi/180
    th_hi_rad = th_hi*m.pi/180
    
    
    # station 2 top
    M2t = oblique_m2(M1, th_lo_rad)
    PR2t = oblique_ratio_p(M1, th_lo_rad)
    p2t = PR2t*p1
    
    # station 2 bottom
    M2b = oblique_m2(M1, th_hi_rad)
    PR2b = oblique_ratio_p(M1, th_hi_rad)
    p2b = PR2b*p1
    
    print_var("M2b", M2b)
    print_var("PR2b", PR2b)
    print_var("p2t [psia]", p2t)
    print_var("p2b [psia]", p2b)
    
    # PM expansion to station 3 top
    
    dnu = 2*theta_LE
    nu2t = isen_pm_nu(M2t)
    nu3t = nu2t + dnu
    M3t  = isen_pm_M(nu3t)
    print_var("nu2t", nu2t)
    print_var("nu3t", nu3t)
    print_var("M3t", M3t)
    
    
    pt2op2 = isen_ratio_p(M2t)
    pt3op3 = isen_ratio_p(M3t)
    print_var("Pt/p_2", pt2op2)
    print_var("Pt/p_3", pt3op3)
    
    p3t = 1/pt3op3*1*pt2op2*p2t
    print_var("P_3t", p3t)
    
    
    # PM expansion to station 3 bot
    print("-- PM expansion to station 3 bot")
    
    dnu = 2*theta_LE
    nu2b = isen_pm_nu(M2b)
    nu3b = nu2b + dnu
    M3b  = isen_pm_M(nu3b)
    print_var("nu2b", nu2b)
    print_var("nu3b", nu3b)
    print_var("M3b", M3b)
    
    
    pt2op2 = isen_ratio_p(M2b)
    pt3op3 = isen_ratio_p(M3b)
    print_var("Pt/p_2", pt2op2)
    print_var("Pt/p_3", pt3op3)
    
    p3b = 1/pt3op3*1*pt2op2*p2b
    print_var("P_3b", p3b)
    
    ## "SOLUTION PRESSURES"
    
    F2t = L_face*p2t*12
    F2b = L_face*p2b*12
    
    F3t = L_face*p3t*12
    F3b = L_face*p3b*12
    
    print_var("F2t", F2t)
    print_var("F2b", F2b)
    print_var("F3t", F3t)
    print_var("F3b", F3b)
    
    F2tx =  F2t*m.sin(th_lo_rad)
    F2ty = -F2t*m.cos(th_lo_rad)
    
    F3tx = -F3t*m.sin(th_hi_rad)
    F3ty = -F3t*m.cos(th_hi_rad)
    
    F2bx =  F2b*m.sin(th_hi_rad)
    F2by =  F2b*m.cos(th_hi_rad)
    
    F3bx = -F3b*m.sin(th_lo_rad)
    F3by =  F3b*m.cos(th_lo_rad)
    
    DRAG = sum([F2tx,F3tx,F2bx,F3bx,])
    LIFT = sum([F2ty,F3ty,F2by,F3by,])
    
    
    print_var("DRAG", DRAG)
    print_var("LIFT", LIFT)

# %%
def p808b():
    # given
    M1 = 1.8
    p1 = 8.5 # psia
    alpha = 10
    theta_LE = 6
    L = 6*12 # in
    L_face = L/2/m.cos(theta_LE*m.pi/180)

    th_lo = theta_LE - alpha
    th_hi = theta_LE + alpha
    
    th_lo_rad = th_lo*m.pi/180
    th_hi_rad = th_hi*m.pi/180

    # get state 1 values
    nu1 = isen_pm_nu(M1)
    PR1 = isen_ratio_p(M1)
    print_var("PR1", PR1)
    
    # station 2 top
    # 1 -> 2t is now a PM expansion

    dnu2 = -th_lo
    nu2t = nu1 + dnu2
    M2t = isen_pm_M(nu2t)
    PR2t = isen_ratio_p(M2t)

    P2t = 1/PR2t*1*PR1*p1


    print_var("nu1",   nu1)
    print_var("dnu2", dnu2)
    print_var("nu2t", nu2t)
    print_var("M2t", M2t)
    print_var("PR2t", PR2t)
    print_var("P2t", P2t)

    # 2t -> 3t is a PM expansion

    nu3t = nu2t + theta_LE*2
    M3t = isen_pm_M(nu3t)
    PR3t = isen_ratio_p(M3t)
    print_var("nu3t", nu3t)
    print_var("M3t", M3t)
    print_var("PR3t", PR3t)

    P3t = 1/PR3t*1*PR1*p1
    print_var("P3t", P3t)

    # station 2 bottom
    M2b = oblique_m2(M1, th_hi_rad)
    PR2b = oblique_ratio_p(M1, th_hi_rad)
    p2b = PR2b*p1
    
    print_var("M2b", M2b)
    print_var("PR2b", PR2b)
    print_var("p2b [psia]", p2b)
    
    
    # PM expansion to station 3 bot
    print("-- PM expansion to station 3 bot")
    
    dnu = 2*theta_LE
    nu2b = isen_pm_nu(M2b)
    nu3b = nu2b + dnu
    M3b  = isen_pm_M(nu3b)
    print_var("nu2b", nu2b)
    print_var("nu3b", nu3b)
    print_var("M3b", M3b)
    
    pt2op2 = isen_ratio_p(M2b)
    pt3op3 = isen_ratio_p(M3b)
    print_var("Pt/p_2", pt2op2)
    print_var("Pt/p_3", pt3op3)
    
    p3b = 1/pt3op3*1*pt2op2*p2b
    print_var("P_3b", p3b)
    
    ### "SOLUTION PRESSURES"

    p2t = 6.85
    p3t = 3.35
    p2b = 19.1
    p3b = 10.5
    
    F2t = L_face*p2t*12
    F2b = L_face*p2b*12
    
    F3t = L_face*p3t*12
    F3b = L_face*p3b*12
    
    print_var("F2t", F2t)
    print_var("F2b", F2b)
    print_var("F3t", F3t)
    print_var("F3b", F3b)
    
    F2tx =  F2t*m.sin(th_lo_rad)
    F2ty = -F2t*m.cos(th_lo_rad)
    
    F3tx = -F3t*m.sin(th_hi_rad)
    F3ty = -F3t*m.cos(th_hi_rad)
    
    F2bx =  F2b*m.sin(th_hi_rad)
    F2by =  F2b*m.cos(th_hi_rad)
    
    F3bx = -F3b*m.sin(th_lo_rad)
    F3by =  F3b*m.cos(th_lo_rad)
    
    DRAG = sum([F2tx,F3tx,F2bx,F3bx,])
    LIFT = sum([F2ty,F3ty,F2by,F3by,])
    
    
    print_var("DRAG", DRAG)
    print_var("LIFT", LIFT)

#p808b()

# %%

def p812():
    aoas = 3.5
    _,M2 = get_mach_given_aoastar(aoas, 1.4)
    
    nu2 = isen_pm_nu(M2)
    PR2 = isen_ratio_p(M2)
    wa2 = m.asin(1/M2)
    
    print_var("M2", M2)
    print_var("nu2", nu2)
    print_var("PR2", PR2)
    print_var("wave_angle 2", wa2*180/m.pi)
    
    dwedge = 20*m.pi/180
    
    M3 = oblique_m2(M2, dwedge)
    PRB = oblique_ratio_p(M2, dwedge)
    th3 = oblique_beta_zero(M2, dwedge)
    nu3 = isen_pm_nu(M3)
    PR3 = isen_ratio_p(M3)
    
    PRC = PRB*PR3
    
    print_var("PRB", PRB)
    print_var("PR3", PR3)
    print_var("PRC", PRC)
    print_var("th3", th3*180/m.pi)
    print_var("nu3", nu3)
    
    M4 = get_mach_given_pr(PRC, Gas_mgr().AIR_SI)
    print_var("M4", M4)
    
    nu4 = isen_pm_nu(M4)
    print_var("nu4", nu4)
    
    dnu34 = nu4 - nu3
    print(f"dnu34 = {dnu34:10.3f}")


# %%

# p814

M1 = 2.0
g = Gas_mgr().AIR_SI
P1 = 0.7 # bar
P2 = 1.0 # bar

PRA = P2/P1
print_var("PRA", PRA)

# PR - PR* as function of deflection angle
f = lambda thb: oblique_ratio_p(M1, thb) - PRA
#
#xs = np.linspace(0.1*m.pi/180, m.pi/2-0.05, 100)
#
#fx = [abs(f(x)) for x in xs]
#
#import matplotlib.pyplot as plt
#
#plt.plot(xs*180/m.pi,fx)
#plt.show()

# find strong shock with large angle
thA = bisector(f, 0.1*m.pi/180, m.pi/2-0.05, 0.0005)
print(f"theta -> {thA:10.3f} -> {thA*180/m.pi:10.2f} deg")

d2 = oblique_beta_zero(M1, thA)
print_var("d2", d2*180/m.pi)

M2 = oblique_m2(M1, thA)
print_var("M2", M2)

# %%
