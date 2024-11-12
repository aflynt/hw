# %%
from libgd import *


# %%
def p1001():

    g = Gas_mgr().AIR_EE

    M1 = 2.95
    T1 = 500 #R

    M2 = 1.60

    # a) compute T2, Tt2

    TTR1 = ray_ratio_Tt(M1)
    TTR2 = ray_ratio_Tt(M2)
    TR1  = ray_ratio_T(M1)
    TR2  = ray_ratio_T(M2)
    ITR1 = isen_ratio_t(M1)
    ITR2 = isen_ratio_t(M2)

    TS = T1/TR1
    T2 = TR2*TS

    TT1 = ITR1*T1
    TT2 = ITR2*T2

    print(f"INFO: T*   = {TS:12.3f} R")
    print(f"INFO: Tt1  = {TT1:12.3f} R")

    print(f"ANS -> T2  = {T2:12.0f} R")
    print(f"ANS -> Tt2 = {TT2:12.0f} R")

    q = g.cp*(TT2 - TT1)
    print(f"q [Btu/lbm-R]: {q:10.1f}")


    # b) find amount and direction of heat transfer

#p1001()

def p1003():
    g = Gas_mgr().AIR_EE
    mdot = 39
    M1 = 0.3
    P1 = 50
    T1 = 650
    A = 0.5
    q = 290
    
    rPR1  = ray_ratio_P(M1)
    rTTR1 = ray_ratio_Tt(M1)
    rTR1  = ray_ratio_T(M1)
    iTR1  = isen_ratio_t(M1)
    print_var("rPR1 ",rPR1 )
    print_var("rTTR1",rTTR1)
    print_var("rTR1 ",rTR1 )
    print_var("iTR1 ",iTR1 )
    
    Tt1 = iTR1*T1
    print_var("Tt1 ",Tt1 )
    a1 = gas_sos(T1,g)
    V1 = M1*a1
    
    rho1 = P1*144/(g.R*T1)
    print_var("rho1", rho1)
    
    Tt2 = Tt1 + q/g.cp
    print_var("Tt2", Tt2)
    
    TT2oTT1 = Tt2/Tt1
    print_var("TT2oTT1", TT2oTT1)
    
    TS = T1/rTR1
    TtS = Tt1/rTTR1
    print_var("T*", TS)
    print_var("Tt*", TtS)
    
    TT2oTTS = Tt2/TtS
    print_var("Tt2/Tt*", TT2oTTS)
    
    fzero = lambda M: ray_ratio_Tt(M) - TT2oTTS
    
    M2 = bisector(fzero, M1, 1)
    print_var("M2", M2)
    
    rPR2  = ray_ratio_P(M2)
    rTTR2 = ray_ratio_Tt(M2)
    rTR2  = ray_ratio_T(M2)
    iTR2  = isen_ratio_t(M2)
    iPR2  = isen_ratio_p(M2)
    print_var("rPR2 ",rPR2 )
    print_var("rTTR2",rTTR2)
    print_var("rTR2 ",rTR2 )
    print_var("iTR2 ",iTR2 )
    print_var("iPR2 ",iPR2 )
    
    T2 = rTR2*TS
    print_var("T2", T2)
    
    PS = P1*(1/rPR1)
    print_var("PS", PS)
    
    P2 = rPR2*PS
    print_var("P2", P2)
    T2 = TS*rTR2
    print_var("T2", T2)
    
    rho2 = P2*144/(g.R*T2)
    print_var("rho2", rho2)
    
    rho_rat = rho2/rho1
    print_var("rho2/rho1", rho_rat)

def p1005():

    # Oxygen
    g = Gas_mgr().OXYGEN_EE
    g.print_props()

    M1  = 3
    Tt1 = 800
    P1  = 35

    rPR1  = ray_ratio_P(M1)
    rTTR1 = ray_ratio_Tt(M1)
    rTR1  = ray_ratio_T(M1)
    iTR1  = isen_ratio_t(M1)

    print_var("rPR1 ",rPR1 )
    print_var("rTTR1",rTTR1)
    print_var("rTR1 ",rTR1 )
    print_var("iTR1 ",iTR1 )

    PS = 1/rPR1*P1
    TtS = 1/rTTR1*Tt1
    T1 = 1/iTR1*Tt1
    TS = 1/rTR1*T1
    print_var("PS", PS)
    print_var("TS", TS)
    print_var("TtS", TtS)
    print_var("T1", T1)

    M2 = 1.5
    rPR2  = ray_ratio_P(M2)
    rTTR2 = ray_ratio_Tt(M2)
    rTR2  = ray_ratio_T(M2)
    iTR2  = isen_ratio_t(M2)
    iPR2  = isen_ratio_p(M2)
    print_var("rPR2 ",rPR2 )
    print_var("rTTR2",rTTR2)
    print_var("rTR2 ",rTR2 )
    print_var("iTR2 ",iTR2 )
    print_var("iPR2 ",iPR2 )
    
    T2 = rTR2*TS
    print_var("T2", T2)
    
    PS = P1*(1/rPR1)
    print_var("PS", PS)
    
    P2 = rPR2*PS
    print_var("P2", P2)
    T2 = TS*rTR2
    print_var("T2", T2)
    Tt2 = rTTR2*TtS
    print_var("Tt2", Tt2)
    Pt2 = iPR2*P2
    print_var("Pt2", Pt2)

# %%
def p1009():

    f = 0.02
    dx = 10.86 # ft
    D = 1 # ft
    M1 = 3
    Tt1 = 600 # R
    Pt1 = 150 # psia
    
    fdxod = f*dx/D
    
    flmaxod1 = fanno_flod_max(M1)
    
    flmaxod2 = flmaxod1 - fdxod
    
    fzero = lambda M: fanno_flod_max(M) - flmaxod2
    
    M2 = bisector(fzero, M1, 1)
    
    #fPR = fanno_ratio_P(M1)
    #fTR = fanno_ratio_T(M1)
    fPTR1 = fanno_ratio_Pt(M1)
    
    
    PtS = 1/fPTR1*Pt1
    
    
    fPTR2 = fanno_ratio_Pt(M2)
    
    Pt2 = fPTR2 * PtS

#p1009()

# %%

g = Gas_mgr().NITROGEN_EE
g.print_props()
#M2 = 0.5
M2 = 0.3
Tt2 = 600
Pt2 = 100

iPR2 = isen_ratio_p(M2)
iTR2 = isen_ratio_t(M2)
rPR2 = ray_ratio_P(M2)
rTR2 = ray_ratio_T(M2)
rTTR2 = ray_ratio_Tt(M2)

print_var("iPR2 =Pt/P",iPR2 )
print_var("iTR2 =Tt/T",iTR2 )
print_var("rPR2 =P/P*",rPR2 )
print_var("rTR2 =T/T*",rTR2 )
print_var("rTTR2=Tt/Tt*",rTTR2)

P2 = 1/iPR2*Pt2
T2 = 1/iTR2*Tt2

PS = 1/rPR2*P2
TS = 1/rTR2*T2

TtS = 1/rTTR2*Tt2
#q = g.cp*(TtS - Tt2)

print_var("P2", P2)
print_var("T2", T2)
print_var("PS", PS)
print_var("TS", TS)
print_var("TtS", TtS)
#print_var("q", q)

rPR3 = 47.42/PS
print_var("P3/P*", rPR3)

fzero = lambda M: ray_ratio_P(M) - rPR3

M3 = bisector(fzero, 0.2, 1)
print_var("M3", M3)

rTTR3 = ray_ratio_Tt(M3)
print_var("Tt3/Tt*", rTTR3)

Tt3 = rTTR3*TtS
print_var("Tt3'", Tt3)

q = g.cp*(Tt3 - Tt2)
print_var("q", q)

# %%
