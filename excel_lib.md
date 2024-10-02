
//get_mach_given_pr( PR, k):
//# isentropic Pt/P = f(k,M) -> M
= LAMBDA(PR, k
   LET(
    M , sqrt(  2/(k-1)*(PR^((k-1)/k) - 1)  ),
    M
   ))



// nohw_A2oA1(p1,p2, M1, M2, T1, T2):
    # steady 1D flow of perfect gas
    # conservation of mass, q = 0, w = 0, dz = 0
= LAMBDA(p1,p2, M1, M2, T1, T2,
  LET(
    PR , p1/p2,
    MR , M1/M2,
    TR , T2/T1,
    AR , PR*MR*sqrt(TR),
    AR
  ))


  =LAMBDA(A,pt,Tt,  
    LET(   
       R, 287,   
       y, 1.4,   
       mdot, A*pt/SQRT(Tt)*SQRT(y/R)*((y+1)/2)^(-(y+1)/(2*(y-1))),   
       mdot  
       )
    )