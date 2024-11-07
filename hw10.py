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

p903d()
