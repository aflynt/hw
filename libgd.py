import math as m
from typing import Tuple
import numpy as np

def my_cot(x):
    return 1/m.tan(x)

def my_sign(x):
    '''
    The sign function returns -1 if 1 < 0, 0 if x == 0, 1 if x > 0
    '''
    if   x <  0: return -1
    elif x == 0: return  0
    else:        return  1

def rad2deg(theta_rad):
    return theta_rad*180/m.pi

def deg2rad(theta_deg):
    return theta_deg*m.pi/180

class Gas:
    def __init__(self, name="AIR", M=28.97, k=1.4, R=287, cp=1000, cv=716, isSI=True):
        self.name = name
        self.M = M
        self.k = k
        self.R = R
        self.cp = cp
        self.cv = cv
        self.isSI= isSI
        self.g_c = 1 if isSI else 32.174

    def __str__(self):
        return f"{self.name:15s} k {self.k:4.2f} R {self.R:4.0f} cp {self.cp:5.0f}"

    def __repr__(self):
        return f'Gas("{self.name:15s}", {self.M:5.2f}, {self.k:4.2f}, {self.R:4.0f}, {self.cp:5.0f}, {self.cv:5.0f}, {self.isSI})'

    def print_props(self):
        print(f"{self.name}:", end='')
        print(f"   k: {self.k :.2f}", end='')
        print(f"   R: {self.R :.3f}", end='')
        print(f"   cp: {self.cp:.3f}")

class Gas_mgr:
    def __init__(self, isSI=True):
        self.isSI = isSI
        self.gases_si = {
            "AIR":            Gas("AIR",             28.97 , 1.40,  287,  1000,  716),
            "AMMONIA":        Gas("AMMONIA",         17.03 , 1.32,  488,  2175, 1648),
            "ARGON":          Gas("ARGON",           39.94 , 1.67,  208,   519,  310),
            "CARBON_DIOXIDE": Gas("CARBON_DIOXIDE",  44.01 , 1.29,  189,   850,  657),
            "CARBON_MONOXIDE":Gas("CARBON_MONOXIDE", 28.01 , 1.40,  297,  1040,  741),
            "HELIUM":         Gas("HELIUM",           4.00 , 1.67, 2080,  5230, 3140),
            "HYDROGEN":       Gas("HYDROGEN",         2.02 , 1.41, 4120, 14300,10200),
            "METHANE":        Gas("METHANE",         16.04 , 1.32,  519,  2230, 1690),
            "NITROGEN":       Gas("NITROGEN",        28.02 , 1.40,  296,  1040,  741),
            "OXYGEN":         Gas("OXYGEN",          32.00 , 1.40,  260,   913,  653),
            "WATER":          Gas("WATER",           18.02 , 1.33,  461,  1860, 1400),
        }
        self.gases_ee = {
            "AIR":            Gas("AIR",             28.97 , 1.40, 53.3, 0.240,0.171, isSI=False),
            "ARGON":          Gas("ARGON",           39.94 , 1.67, 38.7, 0.124,0.074, isSI=False),
            "CARBON_DIOXIDE": Gas("CARBON_DIOXIDE",  44.01 , 1.29, 35.1, 0.203,0.157, isSI=False),
            "CARBON_MONOXIDE":Gas("CARBON_MONOXIDE", 28.01 , 1.40, 55.2, 0.248,0.177, isSI=False),
            "HELIUM":         Gas("HELIUM",           4.00 , 1.67,  386, 1.250,0.750, isSI=False),
            "HYDROGEN":       Gas("HYDROGEN",         2.02 , 1.41,  766, 3.420,2.430, isSI=False),
            "METHANE":        Gas("METHANE",         16.04 , 1.32, 96.4, 0.532,0.403, isSI=False),
            "NITROGEN":       Gas("NITROGEN",        28.02 , 1.40, 55.1, 0.248,0.177, isSI=False),
            "OXYGEN":         Gas("OXYGEN",          32.00 , 1.40, 48.3, 0.218,0.156, isSI=False),
            "WATER":          Gas("WATER",           18.02 , 1.33, 85.7, 0.445,0.335, isSI=False),
        }
        self.AIR_SI =            Gas("AIR",             28.97 , 1.40,  287,  1000,  716)  
        self.AMMONIA_SI =        Gas("AMMONIA",         17.03 , 1.32,  488,  2175, 1648)  
        self.ARGON_SI =          Gas("ARGON",           39.94 , 1.67,  208,   519,  310)  
        self.CARBON_DIOXIDE_SI = Gas("CARBON_DIOXIDE",  44.01 , 1.29,  189,   850,  657)  
        self.CARBON_MONOXIDE_SI= Gas("CARBON_MONOXIDE", 28.01 , 1.40,  297,  1040,  741)  
        self.HELIUM_SI =         Gas("HELIUM",           4.00 , 1.67, 2080,  5230, 3140)  
        self.HYDROGEN_SI =       Gas("HYDROGEN",         2.02 , 1.41, 4120, 14300,10200)  
        self.METHANE_SI =        Gas("METHANE",         16.04 , 1.32,  519,  2230, 1690)  
        self.NITROGEN_SI =       Gas("NITROGEN",        28.02 , 1.40,  296,  1040,  741)  
        self.OXYGEN_SI =         Gas("OXYGEN",          32.00 , 1.40,  260,   913,  653)  
        self.WATER_SI =          Gas("WATER",           18.02 , 1.33,  461,  1860, 1400)  

        self.AIR_EE              = Gas("AIR",             28.97 , 1.40, 53.3, 0.240,0.171, isSI=False)  
        self.ARGON_EE            = Gas("ARGON",           39.94 , 1.67, 38.7, 0.124,0.074, isSI=False)  
        self.CARBON_DIOXIDE_EE   = Gas("CARBON_DIOXIDE",  44.01 , 1.29, 35.1, 0.203,0.157, isSI=False)  
        self.CARBON_MONOXIDE_EE  = Gas("CARBON_MONOXIDE", 28.01 , 1.40, 55.2, 0.248,0.177, isSI=False)  
        self.HELIUM_EE           = Gas("HELIUM",           4.00 , 1.67,  386, 1.250,0.750, isSI=False)  
        self.HYDROGEN_EE         = Gas("HYDROGEN",         2.02 , 1.41,  766, 3.420,2.430, isSI=False)  
        self.METHANE_EE          = Gas("METHANE",         16.04 , 1.32, 96.4, 0.532,0.403, isSI=False)  
        self.NITROGEN_EE         = Gas("NITROGEN",        28.02 , 1.40, 55.1, 0.248,0.177, isSI=False)  
        self.OXYGEN_EE           = Gas("OXYGEN",          32.00 , 1.40, 48.3, 0.218,0.156, isSI=False)  
        self.WATER_EE            = Gas("WATER",           18.02 , 1.33, 85.7, 0.445,0.335, isSI=False)  
        if self.isSI:
            self.gases = self.gases_si.copy()
        else:
            self.gases = self.gases_ee.copy()

    def get_gas_AIR(self):            return self.gases["AIR"]
    def get_gas_AMMONIA(self):        return self.gases["AMMONIA"]
    def get_gas_ARGON(self):          return self.gases["ARGON"]
    def get_gas_CARBON_DIOXIDE(self): return self.gases["CARBON_DIOXIDE"]
    def get_gas_CARBON_MONOXIDE(self):return self.gases["CARBON_MONOXIDE"]
    def get_gas_HELIUM(self):         return self.gases["HELIUM"]
    def get_gas_HYDROGEN(self):       return self.gases["HYDROGEN"]
    def get_gas_METHANE(self):        return self.gases["METHANE"]
    def get_gas_NITROGEN(self):       return self.gases["NITROGEN"]
    def get_gas_OXYGEN(self):         return self.gases["OXYGEN"]
    def get_gas_WATER(self):          return self.gases["WATER"]

#gases_si = {
#    "AIR":            Gas("AIR",             28.97 , 1.40,  287,  1000,  716),
#    "AMMONIA":        Gas("AMMONIA",         17.03 , 1.32,  488,  2175, 1648),
#    "ARGON":          Gas("ARGON",           39.94 , 1.67,  208,   519,  310),
#    "CARBON_DIOXIDE": Gas("CARBON_DIOXIDE",  44.01 , 1.29,  189,   850,  657),
#    "CARBON_MONOXIDE":Gas("CARBON_MONOXIDE", 28.01 , 1.40,  297,  1040,  741),
#    "HELIUM":         Gas("HELIUM",           4.00 , 1.67, 2080,  5230, 3140),
#    "HYDROGEN":       Gas("HYDROGEN",         2.02 , 1.41, 4120, 14300,10200),
#    "METHANE":        Gas("METHANE",         16.04 , 1.32,  519,  2230, 1690),
#    "NITROGEN":       Gas("NITROGEN",        28.02 , 1.40,  296,  1040,  741),
#    "OXYGEN":         Gas("OXYGEN",          32.00 , 1.40,  260,   913,  653),
#    "WATER":          Gas("WATER",           18.02 , 1.33,  461,  1860, 1400),
#}
#
#gases_ee = {
#    "AIR":            Gas("AIR",             28.97 , 1.40, 53.3, 0.240,0.171, isSI=False),
#    "AMMONIA":        Gas("AMMONIA",         28.97 , 1.40, 53.3, 0.240,0.171, isSI=False),
#    "ARGON":          Gas("ARGON",           39.94 , 1.67, 38.7, 0.124,0.074, isSI=False),
#    "CARBON_DIOXIDE": Gas("CARBON_DIOXIDE",  44.01 , 1.29, 35.1, 0.203,0.157, isSI=False),
#    "CARBON_MONOXIDE":Gas("CARBON_MONOXIDE", 28.01 , 1.40, 55.2, 0.248,0.177, isSI=False),
#    "HELIUM":         Gas("HELIUM",           4.00 , 1.67,  386, 1.250,0.750, isSI=False),
#    "HYDROGEN":       Gas("HYDROGEN",         2.02 , 1.41,  766, 3.420,2.430, isSI=False),
#    "METHANE":        Gas("METHANE",         16.04 , 1.32, 96.4, 0.532,0.403, isSI=False),
#    "NITROGEN":       Gas("NITROGEN",        28.02 , 1.40, 55.1, 0.248,0.177, isSI=False),
#    "OXYGEN":         Gas("OXYGEN",          32.00 , 1.40, 48.3, 0.218,0.156, isSI=False),
#    "WATER":          Gas("WATER",           18.02 , 1.33, 85.7, 0.445,0.335, isSI=False),
#}

def isen_ratio_t(M:float, k=1.4):
   '''
   Isentropic temp ratio of total/static
   '''
   TR = (1 + (k-1)/2*M**2)
   return TR

def isen_ratio_p(M: float, k=1.4):
   TR = isen_ratio_t(M, k)
   PR = TR**(k/(k-1))
   return PR

def isen_ratio_rho(M: float, k=1.4):
    TR = isen_ratio_t(M, k)
    RR = TR**(1/(k-1))
    return RR

def speed_of_sound(k: float, R: float,T: float , g_c: float = 1.0):
   a = m.sqrt(k*g_c*R*T)
   return a

def gas_sos( T: float, g: Gas):
    return speed_of_sound(g.k, g.R, T, g.g_c)

def get_mach_given_pr( PR: float, g: Gas):
    # isentropic Pt/P = f(k,M) -> M
    M = m.sqrt(  2/(g.k-1)*(PR**((g.k-1)/g.k) - 1)  )
    return M

def get_mach_given_tr( TR: float, g: Gas):
    # isentropic Tt/T = f(k,M) -> M
    M = m.sqrt(  2/(g.k-1)*(TR - 1)  )
    return M

def nohw_A2oA1(p1,p2, M1, M2, T1, T2):
    # steady 1D flow of perfect gas
    # conservation of mass, q = 0, w = 0, dz = 0
    PR = p1/p2
    MR = M1/M2
    TR = T2/T1
    AR = PR*MR*m.sqrt(TR)
    return AR

def nohw_T2oT1(M1, M2, k):
    # steady 1D flow of perfect gas
    # conservation of mass, q = 0, w = 0, dz = 0
    # Tt1 = Tt2 = constant
    TR1 = isen_ratio_t(M1, k)
    TR2 = isen_ratio_t(M2, k)

    T2oT1 = TR1/TR2
    return T2oT1

def nohw_Pt2oPt1_given_Ms(p2, p1, k, M1, M2):
    # ok if: Tt1 == Tt2
    PR = p2/p1
    TR2 = isen_ratio_t(M2, k)
    TR1 = isen_ratio_t(M1, k)
    sup = k / (k-1)
    Pt2oPt1 = PR * (TR2/TR1)**sup
    return Pt2oPt1

def nohw_Pt2oPt1_given_ds( ds, R):
    # ok if: Tt1 == Tt2
    Pt2oPt1 = m.exp(-ds/R)
    return Pt2oPt1

def nohw_A1SoA2S_given_ds( ds, R):
    # A1* / A2* 
    # ok if: Tt1 == Tt2
    Pt2oPt1 = m.exp(-ds/R)
    return Pt2oPt1

def ds_given_dpt(Pt1, Pt2, R, isSI=True):
    ds = -R*m.log(Pt2/Pt1)
    if not isSI:
        ds /= 778.2
    return ds

def aoastar(k, M):
    '''
    - isentropic A/A*
    - returns one unique area ratio A/A*
    '''
    TR  = isen_ratio_t(M,k)
    sup = (k+1)/(2*(k-1))
    C   = (k+1)/2
    aoas = 1/M*(TR/C)**sup
    return aoas

def get_mach_given_aoastar(AoAS: float, k:float) -> Tuple[float, float]:

    f = lambda M: AoAS - aoastar(k, M)

    M_2_sub = bisector(f, 0.01,  1.00)
    M_2_sup = bisector(f, 1.00, 10.00)

    return M_2_sub,M_2_sup

def bisector(f, a, b, tol=1e-6):
    if my_sign(f(a)) == my_sign(f(b)):
        raise Exception("The scalars a and b dont bound a root")
    
    m = (a+b)/2

    

    if abs(f(m)) < tol:
        return m
    elif my_sign(f(a)) == my_sign(f(m)):
        return bisector(f, m, b, tol)
    else:
        return bisector(f, a, m, tol)


def A2oA1_given_MR_ds(M1:float, M2:float, ds:float, g:Gas):

    TR1 = isen_ratio_t(M1, g.k)
    TR2 = isen_ratio_t(M2, g.k)
    
    A2oA1 = M1/M2*(TR2/TR1)**((g.k+1)/(2*(g.k-1)))*m.exp(ds/g.R)

    return A2oA1

def choked_mdot(Pt:float, Tt:float, Astar, g:Gas):
    k = g.k
    C = m.sqrt(g.k/g.R) * ((k+1)/2)**(-(k+1)/(2*(k-1)))
    moa = Astar*Pt/m.sqrt(Tt) * C
    return moa 

def norm_shock_m2(M1, k=1.4):
    numer = M1**2 + 2/(k-1)
    denom = 2*k/(k-1)*M1**2 - 1
    M2 = m.sqrt(numer/denom)
    return M2

def norm_shock_m1(M2, k=1.4, lo=1, hi=5):

    M2 = bisector(lambda x: norm_shock_m2(x,k) - M2, lo, hi)
    return M2

def norm_shock_pr(M1, k=1.4):
    PR = 2*k/(k+1)*M1**2 - (k-1)/(k+1)
    return PR

def norm_shock_tr(M1, k=1.4):
    M2 = norm_shock_m2(M1, k)
    ttot1 = isen_ratio_t(M1, k)
    ttot2 = isen_ratio_t(M2, k)
    TR = ttot1/ttot2
    return TR

def norm_shock_rr(M1, k=1.4):
    numer = (k+1)*M1**2
    denom = (k-1)*M1**2 + 2
    rho2orho1 = numer/denom
    return rho2orho1

def norm_shock_ptr(M1, k=1.4):
    '''
    total pressure ratio across normal shock
    * ptr = Pt2 / Pt1
    '''
    C1 = k/(k-1)
    C2 = 1/(1-k)
    A  = (k+1)/2*M1**2 / isen_ratio_t(M1,k)
    B  = 2*k/(k+1)*M1**2 - (k-1)/(k+1)
    ptr = A**C1 * B**C2
    return ptr

def norm_shock_dvoa(M1: float, k:float =1.4) -> float:
    '''
    dvoa = (V1 - V2)/a1
    returns velocity delta relative to incoming speed of sound
    '''
    dvoa = (2/(k+1))*(M1*M1 - 1)/M1
    return dvoa


def print_var(name, value, w=12, d=7):
    print(f"{name:20s} = {value:{w}.{d}f} = {value:{w}.3f}")

def mach_given_ar_pr(ar:float, pr:float, k=1.4, M_lo=0.01, M_hi=1.0) -> float:
    '''
    * ar = A_exit/A_throat
    * pr = p_exit/pt_inlet
    '''

    AR_PR = ar*pr

    fzero = lambda M: aoastar(k, M)/isen_ratio_p(M,k) - AR_PR

    Mexit = bisector(fzero, M_lo, M_hi)

    return Mexit

def mach_given_ptr(ptr, k=1.4, M_lo=1.0, M_hi=5):
    '''
    Mach # us of shock
    * ptr = Pt_us / Pt_ds
    '''
    fzero = lambda m: norm_shock_ptr(m, k) - ptr

    mshock = bisector(fzero, M_lo, M_hi)

    return mshock

def lin_interp(x, x0, x1, y0, y1):
    y = y0 + (x-x0)*(y1-y0)/(x1-x0)
    return y

def zero_ob_beta(theta, beta, M1, k):

    numer = M1**2 * m.sin(beta)**2 - 1
    denom = 2 + M1**2*(k + m.cos(2*beta))

    y = m.tan(theta) - 2*my_cot(beta) *numer/denom
    return y

def oblique_beta_zero(M, theta, k=1.4):
    '''
    Get oblique shock angle "BETA"
    * M = incoming mach number
    * theta = deflection angle 
    '''

    betas = np.arange(0.0001,m.pi/3,0.0001)
    bs = [float(bi) for bi in betas]

    fs = [abs(zero_ob_beta(theta, b, M, k)) for b in bs]

    bmin = bs[0]
    fmin = fs[0]

    for b,f in zip(bs,fs):
        if f < fmin:
            fmin = f
            bmin = b

    return bmin

def oblique_m2(M1, theta, k=1.4):
    '''
    Get oblique shock Mach # behind shock
    * M1    = incoming mach number
    * theta = deflection angle 
    '''

    beta = oblique_beta_zero(M1,theta, k)

    sin_val = m.sin(beta-theta)**2
    numer   = 1 + (k-1)/2*M1**2*m.sin(beta)**2
    denom   = k*M1**2*m.sin(beta)**2 - (k-1)/2
    RHS     = numer / (denom * sin_val)
    ans     = m.sqrt(RHS)

    return ans

def oblique_ratio_rho(M1, theta, k=1.4):
    '''
    oblique shock density ratio rho2/rho1
    '''

    beta = oblique_beta_zero(M1,theta, k)
    #beta = wave angle

    numer = (k+1)*M1**2*m.sin(beta)**2
    denom = (k-1)*M1**2*m.sin(beta)**2 + 2
    rr = numer/denom
    return rr

def oblique_ratio_p(M1, theta, k=1.4):
    '''
    P2/P1 across oblique shock
    * M1    = incoming Mach number
    * theta = deflection angle
    '''

    beta = oblique_beta_zero(M1,theta, k)
    pr = 1 + 2*k/(k+1)*(M1**2*m.sin(beta)**2 - 1)
    return pr

def oblique_ratio_pt(M1, delta, k=1.4):
    '''
    Pt1/Pt0 total pressure ratio
    * M1    = incoming mach number
    * delta = deflection angle
    '''
    beta = oblique_beta_zero(M1,delta, k)

    MS = M1**2*m.sin(beta)**2

    E1 = k/(k-1)
    E2 = 1/(1-k)

    A = (k+1)/2*MS
    B = 1+(k-1)/2*MS
    C = 2*k/(k+1)*MS-(k-1)/(k+1)

    ptr = (A/B)**E1 * (C)**E2

    return ptr

def oblique_ratio_pt_theta(M1, theta, k=1.4):
    '''
    Pt2/Pt1 oblique shock pressure ratio

    * M1: incoming mach number
    * theta: shock angle
    '''
    MS = M1**2*m.sin(theta)**2

    E1 = k/(k-1)
    E2 = 1/(1-k)

    A = (k+1)/2*MS
    B = 1+(k-1)/2*MS
    C = 2*k/(k+1)*MS-(k-1)/(k+1)

    ptr = (A/B)**E1 * (C)**E2

    return ptr



def oblique_ratio_t(M1, theta, k=1.4):
    '''
    T2/T1 across oblique shock
    * M1    = incoming Mach number
    * theta = deflection angle
    '''

    beta = oblique_beta_zero(M1, theta, k)
    tr = 1 + 2*(k-1)/(k+1)**2*(k*M1**2*m.sin(beta)**2 + 1)/(M1**2*m.sin(beta)**2)*(M1**2*m.sin(beta)**2-1)
    return tr


def oblique_m1(delta, theta):
    '''
    M1    = incoming Mach number
    delta = deflection angle
    theta = shock      angle
    '''

    d = delta
    th = theta

    L = lambda M1: m.tan(d) - (2/m.tan(th))*(M1**2*m.sin(th)**2-1)/( M1**2*(1.4+m.cos(2*th))   + 2)

    M = bisector(L, 1, 10)
    return M

def oblique_theta(M1, PR, k=1.4):
    '''
    get shock angle
    * M1 = incoming mach number
    * PR = pressure ratio across shock
    '''

    f = lambda beta: 1 + 2*k/(k+1)*(M1**2*m.sin(beta)**2 - 1) - PR

    b = bisector(f, 0, m.pi/2, 1e-4)
    return b

def oblique_delta(M1, theta):
    '''
    Find oblique shock turn angle
    * M1 incoming mach number
    * theta shock angle
    '''
    th = theta
    k = 1.4
    numer = M1**2*m.sin(th)**2 - 1
    denom = M1**2*(k+m.cos(2*th)) + 2
    RHS = 2/m.tan(th)*numer/denom

    f = lambda d: m.tan(d) - RHS

    delta = bisector(f, 0, m.pi/2, 1e-4)
        
    return delta

def oblique_shock_relations(M1:float, turn_angle:float, k=1.4) -> Tuple[float, float, float, float, float, float, float]:
    '''
    get: beta_deg, M2, PR, TR, PTR, M1n, M2n
    '''

    beta_rad = oblique_beta_zero(M1, turn_angle, k)
    beta_deg = rad2deg(beta_rad)
    M2 = oblique_m2(M1, turn_angle, k)
    PR = oblique_ratio_p(M1, turn_angle, k)
    TR = oblique_ratio_t(M1, turn_angle, k)
    PTR = oblique_ratio_pt(M1, turn_angle, k)
    M1n = M1*m.sin(beta_rad)
    M2n = norm_shock_m2(M1n, k)

    return beta_deg, M2, PR, TR, PTR, M1n, M2n

def norm_shock_relations(M1, k=1.4):

    M2   = norm_shock_m2(  M1, k)
    PR2  = norm_shock_pr(  M1, k)
    TR2  = norm_shock_tr(  M1, k)
    PTR2 = norm_shock_ptr( M1, k)

    return M2, PR2, TR2, PTR2

def isen_pm_nu(M,k=1.4):
    '''
    Prandtl-Meyer Flow angle
    * M = mach number
    * -> nu [deg]
    '''
    kp1 = k + 1
    km1 = k - 1
    MM = M**2-1
    A = m.sqrt(kp1/km1)
    B = m.atan(m.sqrt(km1/kp1*MM))
    C = m.atan(m.sqrt(MM))

    nu_rad = A*B - C
    nu_deg = rad2deg(nu_rad)

    return nu_deg

def isen_pm_M(nu, k=1.4):
    '''
    Prandtl-Meyer Mach # given angle
    * nu: angle [deg]
    * -> M
    '''

    L = lambda M: isen_pm_nu(M,k)-nu

    M = bisector(L, 1, 10)
    return M