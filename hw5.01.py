from libgd import *

g = gases_ee["NITROGEN"]


# known
# Tt = constant
# no work
# q = 0
# no losses
A1 = 1.5 # ft2
A2 = 4.5 # ft2


def do_part_a():
    M_1 = 0.7
    P_1 = 70 # psia
    as1oas2 = 1

    # know state 1
    aoas_1 = aoastar(g.k, M_1)
    PR_1 = isen_ratio_p(g.k, M_1)

    # get A/A* at 2
    aoas_2 = A2/A1 * aoas_1 * as1oas2

    # subsonic at 1, with expanding area -> subsonic at 2
    M_2, _ = get_mach_given_aoastar(aoas_2, g.k)
    PR_2 = isen_ratio_p(g.k, M_2)

    print(f"A/A*_1: {aoas_1:10.3f}")
    print(f"A/A*_2 = {aoas_2:10.3f}")
    print(f"M_2 = {M_2:10.5f}")
    print(f"{PR_2 = }")

    # P2 = P2   PT2  PT1 P1
    #      ------------------
    #      PT2  PT1  P1
    #
    P_2 = 1/PR_2 * 1 * PR_1 * P_1
    print(f"p_2 = {P_2:10.3f}")

def do_part_b():
    # given
    M_1 = 1.7
    T_1 = 95 + 459.67
    as1oas2 = 1
    
    # know state 1
    TR_1 = isen_ratio_t(g.k, M_1)
    aoas_1 = aoastar(g.k, M_1)

    # get A/A* at 2
    aoas_2 = A2/A1 * aoas_1 * as1oas2

    # ss at 1, with expanding area -> ss at 2
    _, M_2 = get_mach_given_aoastar(aoas_2, g.k)
    TR_2 = isen_ratio_t(g.k, M_2)

    T_2 = 1/TR_2*1*TR_1* T_1
    print(f"A/A*_1: {aoas_1:10.3f}")
    print(f"A/A*_2: {aoas_2:10.3f}")
    print(f"M_2   : {M_2:10.5f}")
    print(f"TR_2  : {TR_2:10.5f}")
    print(f"T_2   : {T_2:10.5f}")

#do_part_a()
print(f"----------------")
do_part_b()


#r1 = bisector(f, 0, 2, 0.1)
#r2 = bisector(f, 0, 2, 0.01)
#print(f"r2 = {r2}")
#print(f"f(r1) = {f(r1)}")
#print(f"f(r2) = {f(r2)}")
