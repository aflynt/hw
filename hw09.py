
# %%e
from libgd import *

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

p801()
# %%
