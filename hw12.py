
# %%
from libgd import *
import matplotlib.pyplot as plt


# %%

def p1211():
    g = Gas_mgr().AIR_EE
    T0 = 411 # R
    P0 = 628 # psfa
    M0 = 4
    
    D2 = 18 # in
    P2 = 850 # psfa
    T2 = 1800 # R
    V2 = 5000 # ft/s
    
    A2 = m.pi/4*(D2/12)**2 # ft^2
    rho2 = P2/(g.R*T2) # lbm/ft^3
    mdot = rho2*V2*A2
    c0 = gas_sos(T0, g)
    V0 = M0*c0
    
    Fnet = mdot/g.g_c*(V2-V0) + A2*(P2-P0)
    Pt = Fnet*V0/550 # hp

    print(f"Fnet         = {Fnet:12.1f} lbf")
    print(f"Thrust power = {Pt:12.1f} hp")

#p1211()

# %%
def ex_1203():
    # example 12.3 turbofan
    
    g = Gas_mgr().AIR_EE
    M0 = 0.9
    T0 = 400 # R
    P0 = 546 # psfa
    beta = 3.0 # bypass ratio
    mdotp = 50 # lbm/s primary
    eta_c = 0.88
    eta_f = 0.90
    eta_b = 0.96
    eta_t = 0.94
    eta_n = 0.95
    eta_r = 0.98
    PRc = 15
    PRf = 2.5
    T4 = 2500 # R
    Pt4oPt3 = (1-0.03)
    HV = 18900 # Btu/lbm
    
    
    # State at [0] free stream
    a0 = gas_sos(T0, g)
    V0 = M0*a0
    iPR0 = isen_ratio_p(M0)
    iTR0 = isen_ratio_t(M0)
    Pt0 = iPR0*P0
    Tt0 = iTR0*T0
    s0 = 0
    
    # State at [2] end of diffuser
    Tt2 = round(Tt0,0)
    Pt2 = eta_r*Pt0
    s2 = ds_given_dpt(Pt0, Pt2, g.R, g.isSI)
    
    
    # State at [3] end of compressor
    Pt3 = PRc*Pt2
    isen_TR23 = (Pt3/Pt2)**((g.k-1)/g.k)
    isen_TR23 = round(isen_TR23, 2)
    Tt3s = isen_TR23*Tt2
    dTt23 = (Tt3s-Tt2)/eta_c
    Tt3 = Tt2 + dTt23
    ds23 = ds_given_dpt(1, Pt2/Pt3, g.R, g.isSI)
    s3 = s2 + ds23
    
    
    # State at [3'] end of fan
    Pt3p = PRf*Pt2
    
    TR23sp = (PRf)**((g.k-1)/g.k)
    TR23sp = round(TR23sp, 2)
    Tt3sp = TR23sp*Tt2
    dT23p = (round(Tt3sp,0) - Tt2)/eta_f
    
    Tt3p = Tt2 + dT23p
    Tt3p = round(Tt3p,0)
    Tt3p
    ds23p = ds_given_dpt(1, Pt2/Pt3p, g.R, g.isSI)
    s3p = s2 + ds23p
    
    
    # State at [4] end of burner/combustion chamber
    Pt4 = round(Pt4oPt3*Pt3 + 1,0)
    Tt4 = T4
    s4 = s3 + ds_given_dpt(1, Pt4/Pt3, g.R, g.isSI)
    
    # state at [5] end of turbine
    
    dT45 = (Tt3-Tt2) + beta*(Tt3p-Tt2)
    Tt5 = Tt4 - dT45
    dT45s = dT45/eta_t
    
    Tt5s = Tt4 - dT45s
    
    Pt4oPt5 = (Tt4/Tt5s)**(g.k/(g.k-1))
    Pt5 = Pt4/Pt4oPt5
    
    s5 = s4 + ds_given_dpt(1, Pt5/Pt4, g.R, g.isSI)
    
    
    # State at [6] end of nozzle
    npr = P0/Pt5
    if (npr < 0.528):
        print(f"nozzle pressure ratio: [{P0/Pt5}] < 0.528 -> IS  choked")
    else:
        print(f"nozzle pressure ratio: [{P0/Pt5}] > 0.528 -> NOT choked")
    
    Tt6 = Tt5
    M6 = 1
    iTR6 = isen_ratio_t(M6, g.k)
    T6 = Tt6/iTR6
    a6 = gas_sos(T6, g)
    V6 = M6*a6
    dT56s = (Tt5 - T6)/eta_n
    
    T6s = Tt5 - dT56s
    
    PR56s = (Tt5/T6s)**(g.k/(g.k-1))
    P6 = Pt5/PR56s
    
    
    print_var("T6s", T6s)
    
    
    # plotting ....
    plt.plot([s0,s2], [T0, Tt2], "-k")
    plt.plot([s2,s2], [Tt2, Tt3s], "--k")
    plt.plot([s2,s3], [Tt2, Tt3], "-k")
    plt.plot([s2,s3p], [Tt2, Tt3p], "-b")
    plt.plot([s3, s4], [Tt3, Tt4], "-k")
    plt.plot([s4, s5], [Tt4, Tt5], "-k")
    plt.plot([s4, s4], [Tt4, Tt5s], "--k")
    plt.plot([s5, s5], [Tt5, T6s], "--r")
    plt.grid(True)
    #plt.show()


# %%

P0   =  546 # psfa
Tt5  = 1420 # R
Pt5  = 1528 # psfa
V5   =  400 # ft/s
mdot =   50 # lbm/s
g = Gas_mgr().AIR_EE

T5 = Tt5 - V5**2/(2*g.g_c*g.cp*778.2)
a5 = gas_sos(T5, g)
M5 = V5/a5
iTR5 = isen_ratio_t(M5, g.k)
iPR5 = isen_ratio_p(M5, g.k)

P5 = Pt5/iPR5
rho5 = P5/(g.R*T5)
A5 = mdot/(rho5*V5)

rTTR5 = ray_ratio_Tt(M5)
rPR5 = ray_ratio_P(M5)
print_var("rPR5", rPR5)
Tts = Tt5/rTTR5

Tt5p = 3500 # R

rTTR5p = Tt5p / Tts

print_var("rTTR5p", rTTR5p)
#print_var("Tts", Tts)
#print_var("rho5", rho5)
#print_var("P5", P5)
#print_var("A5", A5)
#print_var("a5", a5)
#print_var("M5", M5)
#print_var("iTR5", iTR5)
#print_var("iPR5", iPR5)

fzero = lambda M: ray_ratio_Tt(M) - rTTR5p

M5p = bisector(fzero, 0.1, 0.8, 1e-4)
print_var("M5p", M5p)

iTR5p = isen_ratio_t(M5p)
iPR5p = isen_ratio_p(M5p)
print_var("iTR5p", iTR5p)
print_var("iPR5p", iPR5p)

T5p = Tt5p/iTR5p
print_var("T5p", T5p)

rPR5p = ray_ratio_P(M5p)
print_var("rPR5p", rPR5p)

P5p = P5*rPR5p/rPR5
print_var("P5p", P5p)

Pt5p = iPR5p*P5p
print_var("Pt5p", Pt5p)

PRNOZZLE = P0/Pt5p
print_var("PRNOZZLE", PRNOZZLE)

#fz = lambda Astar: choked_mdot(Pt5p, Tt5p, Astar, g) - mdot
#
#astar = bisector(fz, 1, 10)
#eta_n = 0.95
#astar = astar/eta_n
#print_var("astar", astar)

#astar = 3
#while astar < 7:
#    x = fz(astar)
#    print(f"A*: {astar:10.3f} -> f(x): {x:10.3f}")
#    astar += 0.25

#aoas = aoastar(g.k, M5p)
#print_var("aoas", aoas)
#
#A6 = A5/aoas
#print_var("A6", A6)

mdotoa = Pt5p/m.sqrt(Tt5p) *m.sqrt(g.k*g.g_c/g.R) *((g.k+1)/2)**(-(g.k+1)/(2*(g.k-1)))

f = 1/(((0.96*18900)/(0.24*(Tt5p-Tt5))) - 1)
print_var("f", f)

mdot = mdot* (1+f)
print(f"mdot = {mdot:10.3f}")

Astar = mdot/mdotoa*0 + 3.96
print(f"Astar = {Astar:10.3f} ft^2")
M6 = 1
iTR6 = isen_ratio_t(M6)
iPR6 = isen_ratio_p(M6)
print_var("iTR6", iTR6)
print_var("iPR6", iPR6)

T6 = Tt5p / iTR6*0 + 2920
eta_n = 0.95
print_var("T6", T6)

dT56s = (Tt5p - T6)/eta_n
print_var("dT56s", dT56s)
    
T6s = Tt5 - dT56s
print_var("T6s", T6s)
    
PR56s = (Tt5p/T6s)**(g.k/(g.k-1))
print_var("PR56s", PR56s)
P6 = Pt5p/PR56s*0 + 742
print_var("P6", P6)

a6 = m.sqrt(g.k*g.g_c*g.R*T6)
print_var("a6", a6)

Fnet = mdot*a6/g.g_c - 50*882/g.g_c + Astar*(P6 - P0)

print_var("Fnet", Fnet)

# %%