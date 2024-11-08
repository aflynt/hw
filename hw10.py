# %% FIRST
from libgd import *


def p901():
    M1 = 3.0
    M2 = 1.5
    P1 = 8e4

    PR1 = fanno_ratio_P(M1)
    PR2 = fanno_ratio_P(M2)

    P2 = PR2/PR1*P1

    print_var("P2 [kPa]", P2/1000)

    flodmax1 = fanno_flod_max(M1)
    flodmax2 = fanno_flod_max(M2)

    fdxod = flodmax1 - flodmax2

    print_var("f dx/D", fdxod)

#p901()

def eval_ratio(val1, val2, str1, str2):
    print_var(f"{str1}", val1)
    print_var(f"{str2}", val2)
    ratio = val2/val1
    print_var("ratio", ratio)
    print(f"dx/x_1 [%]: {(ratio-1)*100:6.1f} %")


def p903a():

    M1 = 3
    M2 = 2

    flodmax1 = fanno_flod_max(M1)
    flodmax2 = fanno_flod_max(M2)

    fdxod = flodmax1 - flodmax2

    print_var("flodmax1", flodmax1)
    print_var("flodmax2", flodmax2)
    print_var("f dx/D", fdxod)

    TR1 = fanno_ratio_T(M1)
    TR2 = fanno_ratio_T(M2)
    eval_ratio(TR1, TR2, "TR1", "TR2")

    TR1 = fanno_ratio_P(M1)
    TR2 = fanno_ratio_P(M2)
    eval_ratio(TR1, TR2, "PR1", "PR2")

    TR1 = fanno_ratio_rho(M1)
    TR2 = fanno_ratio_rho(M2)
    eval_ratio(TR1, TR2, "rho_R1", "rho_R2")

    # c -> entropy increase
    g = Gas_mgr().AIR_EE

    PTR1 = fanno_ratio_Pt(M1)
    PTR2 = fanno_ratio_Pt(M2)
    PTR = PTR2/PTR1
    eval_ratio(PTR1, PTR2, "PTR1", "PTR2")

    print(f"R = {g.R}")

    ds = ds_given_dpt(1, PTR, g.R, g.isSI)

    ds2 = -53.3*m.log(0.399)/778.2

    print(f"ds = {ds}")
    print(f"ds = {ds2}")



def p903d():
    # part d) now M1 = 0.5 with same length of duct
    #M1 = 0.5

    #flodmax1 = fanno_flod_max(M1)
    #pr
    M1 = 0.5
    #M2 = 2

    flodmax1 = fanno_flod_max(M1)
    #eflodmax2 = fanno_flod_max(M2)

    fdxod = 0.21716

    flodmax2 = flodmax1 - fdxod  

    fzero = lambda M: fanno_flod_max(M) - flodmax2

    M2 = bisector(fzero, M1, 1)
    M2 = 0.53

    print_var("M2", M2)

    print_var("flodmax1", flodmax1)
    print_var("flodmax2", flodmax2)
    print_var("f dx/D", fdxod)

    TR1 = fanno_ratio_T(M1)
    TR2 = fanno_ratio_T(M2)
    eval_ratio(TR1, TR2, "TR1", "TR2")

    TR1 = fanno_ratio_P(M1)
    TR2 = fanno_ratio_P(M2)
    eval_ratio(TR1, TR2, "PR1", "PR2")

    TR1 = fanno_ratio_rho(M1)
    TR2 = fanno_ratio_rho(M2)
    eval_ratio(TR1, TR2, "rho_R1", "rho_R2")

    # c -> entropy increase
    g = Gas_mgr().AIR_EE

    PTR1 = fanno_ratio_Pt(M1)
    PTR2 = fanno_ratio_Pt(M2)
    PTR = PTR2/PTR1
    eval_ratio(PTR1, PTR2, "PTR1", "PTR2")

    print(f"R = {g.R}")

    ds = ds_given_dpt(1, PTR, g.R, g.isSI)

    print(f"ds = {ds}")


def p906():

    M1  =  0.8
    Pt1 = 66.8 # psia
    P2  = 60.0 # psia
    T2  = 120+460 # R

    TR1 = fanno_ratio_T(M1)
    PR1 = fanno_ratio_P(M1)
    PTR1 = fanno_ratio_Pt(M1)
    IPR1 = isen_ratio_p(M1)
    FLD1 = fanno_flod_max(M1)


    P1 = Pt1/IPR1

    PS = P1/PR1

    PR2 = P2/PS


    fzero = lambda M: fanno_ratio_P(M) - PR2
    M2 = bisector(fzero, 0.1, 0.8)

    TR2 = fanno_ratio_T(M2)
    PR2 = fanno_ratio_P(M2)
    PTR2 = fanno_ratio_Pt(M2)
    IPR2 = isen_ratio_p(M2)
    FLD2 = fanno_flod_max(M2)

    T1 = TR1/TR2*T2

    FDX = FLD2 - FLD1

    #print_var("IPR2 " , IPR2  )
    #print_var("TR2 " , TR2  )
    #print_var("PR2 " , PR2  )
    #print_var("PTR2" , PTR2 )
    #print_var("T1" , T1 )
    print_var("FLD1" , FLD1 )
    print_var("FLD2" , FLD2 )
    print_var("FDX" , FDX )



def p911():
    L = 10 # ft
    D1 = 12/12 # ft
    g = Gas_mgr().OXYGEN_EE

    g.print_props()

    P1 = 30
    T1 = 800
    P2 = 23

    mdot = 80 # lbm/s

    rho1 = P1/(g.R*T1)*144
    A = m.pi/4*D1**2
    V1 = mdot/(rho1*A)
    a1 = gas_sos(T1, g)
    M1 = V1/a1

    TR1 = fanno_ratio_T(M1)
    PR1 = fanno_ratio_P(M1)
    PTR1 = fanno_ratio_Pt(M1)
    IPR1 = isen_ratio_p(M1)
    FLD1 = fanno_flod_max(M1)

    PS = P1/PR1
    TS = T1/TR1

    PR2 = P2/PS

    M2 = fanno_M_from_PR(PR2)

    TR2 = fanno_ratio_T(M2)
    PR2 = fanno_ratio_P(M2)
    PTR2 = fanno_ratio_Pt(M2)
    IPR2 = isen_ratio_p(M2)
    ITR2 = isen_ratio_t(M2)
    FLD2 = fanno_flod_max(M2)

    T2 = TS*TR2
    rho2 = P2/(g.R*T2)*144
    V2 = mdot/(rho2*A)

    Tt2 = ITR2*T2

    Pt2 = IPR2*P2

    FDX = FLD1 - FLD2

    print(f"FDX = {FDX:10.3f}")


    print(f"ITR2 = {ITR2:10.3f}")
    print(f"Tt2  = {Tt2:10.3f}")
    print(f"Pt2  = {Pt2:10.3f}")

    mu = 4.2e-7

    Re = rho1 * V1 * D1/(mu*g.g_c)
    print(f"Re = {Re:10.3e}")



    
# %% # CELL?

g = Gas_mgr().AIR_EE

M1  = 2.5
Pt1 = 67
Tt1 = 700

IPR = isen_ratio_p(M1)
ITR = isen_ratio_t(M1)
print_var("IPR", IPR)
print_var("ITR", ITR)

P1 = Pt1/IPR
T1 = Tt1/ITR
print_var("P1", P1)
print_var("T1", T1)

M2    = norm_shock_m2(M1)
PR12  = norm_shock_pr(M1)
PTR12 = norm_shock_ptr(M1)
TR12  = norm_shock_tr(M1)

ds = ds_given_dpt(1, PTR12, g.R, g.isSI)

T2 = T1*TR12
P2 = P1*PR12

# fanno flow at 2

PR2 = fanno_ratio_P(M2)
TR2 = fanno_ratio_T(M2)
PTR2 = fanno_ratio_Pt(M2)
FLD2 = fanno_flod_max(M2)

PS = P2/PR2
TS = T2/TR2

M4 = 1.0
P4 = 14.7
IPR4 = isen_ratio_p(M4)
ITR4 = isen_ratio_t(M4)

PT4 = IPR4*P4
TT4 = ITR4*1*TS

PT2 = PTR12*Pt1

PTS = PT2/PTR2

PTR3 = PT4/PTS

fzero = lambda M: fanno_ratio_Pt(M) - PTR3

#Ms = np.arange(0.2,1,0.05)
#for M in Ms:
#    print(f"M: {M:10.3f} -> ptr: {fanno_ratio_Pt(M):10.3f}")

M3 = bisector(fzero, M2, 1)
print(f"M3 = {M3:10.3f}")

ds23 = ds_given_dpt(1, PT4/PT2, g.R, g.isSI)
print(f"ds23 = {ds23:10.3f}")
print(f"ds13 = {ds+ds23:10.3f}")

ds1s = ds_given_dpt(Pt1, PTS, g.R, g.isSI)
print(f"ds1s = {ds1s:10.3f}")

FLD3 = fanno_flod_max(M3)
TR3  = fanno_ratio_T(M3)

T3 = TR3*TS


import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

line_1  = {"x" : [0, 0], "y" : [T1, Tt1], }
line_2  = {"x" : [0, ds], "y" : [T1, T2], }
line_3  = {"x" : np.array([ds, ds+ds23, ds1s]), "y" : np.array([T2, T3, TS]), }

cubic_interp = interp1d(line_3["x"], line_3["y"], kind="quadratic")

l3x = np.linspace(line_3["x"].min(), line_3["x"].max(), 100)
l3y = cubic_interp(l3x)

fig,ax = plt.subplots()

ax.plot(line_1["x"], line_1["y"], "--k")
ax.plot(line_2["x"], line_2["y"], "-b")
ax.plot(line_3["x"], line_3["y"], "*r")
ax.plot(l3x, l3y, "-.r")

ax.set_xlabel(r"$\Delta s \;\; [Btu/lbm-R]$")
ax.set_ylabel(r"$T \;\; [^\circ R]$")
plt.grid(True)

plt.show()




# %%
