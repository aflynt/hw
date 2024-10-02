
from libgd import *


def cq_09():
    A2 = 0.02
    A1 = 0.06
    
    aoas = A1/A2
    
    M1,_ = get_mach_given_aoastar(aoas, 1.4)
    
    print(f"M1 = {M1:12.6f}")

def cq_10():
    '''
    10.	Same nozzle as Example 4, air and Pt=500kPa, Tt= 300K.  	What is max.
    possible mass flowrate through the nozzle?  Assume isentropic flow, calorically
    thermally perfect gas, γ=1.4.
    '''
    A2 = 0.02
    #A1 = 0.06
    astar = A2
    
    #aoas = A1/A2
    #M1,_ = get_mach_given_aoastar(aoas, 1.4)

    Pt = 500e3 # Pa
    Tt = 300   # K
    g = gases_si["AIR"]

    #moa = max_mdot_o_astar(Pt, Tt, g)
    mdot_max = choked_mdot(Pt, Tt, astar, g)

    #mdot_max = moa*astar
    

    #print(f"moa = {moa:12.6f}")
    print(f"mdot_max = {mdot_max:12.6f}")

def prob_5_11():
    '''
    5.11. Nitrogen is stored in a large chamber under conditions of 450 K and
    1.5 x 105 N/m2. The gas leaves the chamber through a convergent-only nozzle
    whose outlet area is 30 cm2. The ambient room pressure is 1 x 105 N/m2 and
    there are no losses. 
    (a)	What is the velocity of the nitrogen at the nozzle exit?
    (b)	What is the mass flow rate?
    (c)	What is the maximum flow rate that could be obtained by lowering the ambient pressure?
    '''

    g = Gas_mgr().NITROGEN_SI
    g.print_props()
    
    #P2 = 1.0 * 105
    #Pt1 = 1.5 * 105
    P2  = 1.0e5
    Pt1 = 1.5e5
    Pt2 = Pt1
    T1 = 450 # K
    Tt1 = T1
    Tt2 = Tt1

    PR_2 = Pt2/P2
    M2 = get_mach_given_pr(PR_2, g)
    print(f"PR = {PR_2:12.6f}")
    print(f"M2 = {M2:12.6f}")

    TR_2 = isen_ratio_t(g.k, M2)
    inv_TR = 1/TR_2
    print(f"{inv_TR = }")
    T2 = Tt2 / TR_2
    print(f"{T2 = }")

    a2 = gas_sos(T2, g)
    V2 = M2*a2

    print(f"V2 = {V2:12.6f}")

    rho_2 = P2/(g.R*T2)
    print(f"rho_2 = {rho_2:12.6e}")

    rho_2 = P2/ (g.R*T2)
    A2 = 30/100**2
    mdot_2 = rho_2*V2*A2
    print(f"{T2 = }")
    print(f"{a2 = }")
    print(f"mdot = {mdot_2:12.6e}")

    #mdot_max = max_mdot_o_astar(Pt1, Tt1, g)*A2
    mdot_max = choked_mdot(Pt1, Tt1, A2, g)
    print(f"mdot_max = {mdot_max:12.6e}")

    x = 1


def prob_5_16():

    g = Gas_mgr().AIR_EE
    M1 = 0.3
    A1 = 1 #ft**2

    T1 = 800 #R
    P1 = 100 #psia
    P3 = 15 # psia

    # for sanity, switch to psf
    P1_psf = P1*144 # psf
    P3_psf = P3*144 # psf

    a1 = gas_sos(T1, g)

    V1 = M1*a1 # ft/s

    rho1 = P1_psf / (g.R*T1) # lbm/cuft

    mdot1 = rho1*V1*A1 # lbm/s
    print(f"mdot1 = {mdot1:12.3f}")

    PR_1 = isen_ratio_p(g.k, M1)
    TR_1 = isen_ratio_t(g.k, M1)

    aoas_1 = aoastar(g.k, M1)

    astar = A1/aoas_1

    print(f"Found Astar = {astar:12.5f} ft^2")

    Pt1 = P1_psf*PR_1

    print(f"Found Pt1 = {Pt1:12.5f} psf")

    # no losses, q=0, -> Pt = const
    PR_3 = Pt1/P3_psf
    M3 = get_mach_given_pr(PR_3, g)
    print(f"exit mach no: {M3:12.3f}")
    aoas_3 = aoastar(g.k, M3)
    print(f"exit A/A*: {aoas_3:5.4f}")
    Ae = aoas_3*astar
    print(f"Ae = {Ae:.3f} ft^2")

def prob_5_18():

    # Given:
    # adiabatic, ideal is no losses -> Pt2 = Pt1
    g = Gas_mgr().CARBON_MONOXIDE_EE
    Tt_2 = Tt_1 = 540+460 # R
    Pt_1 = Pt_2 = 100*144 # psf
    P_2         =  20*144 # psf

    # isentropic/ ideal M2
    PR_2 = Pt_2/P_2
    M_2s  = get_mach_given_pr(PR_2, g)
    TR_2s = isen_ratio_t(g.k, M_2s)
    T_2s = Tt_2 / TR_2s

    # actual M2
    M_2 = 1.6
    TR_2 = isen_ratio_t(g.k, M_2)
    T_2 = Tt_2/TR_2

    # efficiency and entropy
    eta = (Tt_1 - T_2)/(Tt_1 - T_2s)
    Pt_PR = Pt_1/P_2*(1 - eta*(1-(P_2/Pt_1)**((g.k-1)/g.k)))**(g.k/(g.k-1))
    ds = -g.R*m.log(1/Pt_PR)

    #import matplotlib.pyplot as plt
    #line0ss = [0, ds]
    #line1Ts = [Tt_1, T_2]
    #plt.plot(line0ss, line1Ts, "--o", color="b")
    #plt.plot([ 0,  0], [Tt_1, T_2s], "--o", color="k")
    #plt.plot([ds, ds], [Tt_1, T_2 ], "--o", color="k")
    #plt.plot([0 , ds], [Tt_1, Tt_1 ], "-", color="k")
    #plt.xlabel(r"$\Delta s$  [ft-lbf/lbm-R]")
    #plt.ylabel(r"T [$^\circ$ R]")
    #plt.grid(True)
    #plt.show()

    print(f"T_2 = {T_2:.4f}")
    print(f" -> efficiency = {eta:.4f}")
    print(f"ds = {ds:.4f} ft-lbf/lbm-R")
    print(f"ds = {ds/778.2:.4f} Btu/lbm-R")
    print(f"Pt_PR = {Pt_PR:.5f}")

    #print(f"{Pt2 = }")
    #print(f"{P_2 = }")
    #print(f"{PR_2 = }")
    #print(f"inv_PR_2: {inv_PR_2 :10.4f}")
    #print(f"1/TR_2s = {1/TR_2s:.3f}")
    print(f"{T_2s = }")

    #print(f"a) ideal exit mach number is -> M_2s = {M_2s:.3f}")
    


print()
prob_5_11()
#cq_10()



