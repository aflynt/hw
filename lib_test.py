
import unittest
import libgd as gd
import math as m

class TestLib(unittest.TestCase):

    def test_sos(self):
        ca = gd.speed_of_sound(1.4,287,295.15, 1)
        #ca = gd.speed_of_sound(1.4,287,250, 1)
        self.assertAlmostEqual(ca, 344.3708, 4)

    def test_aoas_mach_hi(self):

        _,Ma = gd.get_mach_given_aoastar(2,1.4)
        self.assertAlmostEqual(Ma, 2.197197, 4)

    def test_aoas_mach_lo(self):

        Ma,_ = gd.get_mach_given_aoastar(2,1.4)
        self.assertAlmostEqual(Ma, 0.305904, 4)

    def test_get_mach_given_tr(self):
        TR = 1.6
        x = gd.get_mach_given_tr(TR, gd.Gas_mgr().AIR_SI)
        self.assertAlmostEqual(x, 1.732051, 4)

    def test_get_mach_given_pr(self):
        PR = 1.6
        x = gd.get_mach_given_pr(PR, gd.Gas_mgr().AIR_SI)
        ans = 0.847705
        self.assertAlmostEqual(x, ans, 4)

    def test_nohw_area_ratio(self):
        x = gd.nohw_A2oA1(101325,81060, 1.3,1.5,300, 250)
        ans = 0.989
        self.assertAlmostEqual(x, ans, 3)

    def test_aoas(self):
        x = gd.aoastar(1.4, 2)
        ans = 1.6875
        self.assertAlmostEqual(x, ans, 4)

    def test_choked_mdot(self):
        x = gd.choked_mdot(101325, 400, 0.1, gd.Gas_mgr().AIR_SI)
        ans = 20.47698
        self.assertAlmostEqual(x, ans, 4)

    def test_nohw_trat(self):
        x = gd.nohw_T2oT1(1.3, 1.5, 1.4)
        ans = 0.922759
        self.assertAlmostEqual(x, ans, 4)

    def test_nohw_PTR_Ms(self):
        x = gd.nohw_Pt2oPt1_given_Ms(0.6, 1, 1.4, 1.1, 2)
        y = 2.198768
        self.assertAlmostEqual(x, y, 4)

    def test_ds_given_dpt(self):
        x = gd.ds_given_dpt(101325, 0.8*101325, 287)
        y = 64.0422
        self.assertAlmostEqual(x,y, 4)

    def test_norm_shock_m2(self):
        x = gd.norm_shock_m2(2, 1.4)
        y = 0.57735
        self.assertAlmostEqual(x,y,4)

    def test_norm_shock_pr(self):
        x = gd.norm_shock_pr(2, 1.4)
        y = 4.5
        self.assertAlmostEqual(x,y,4)

    def test_norm_shock_tr(self):
        x = gd.norm_shock_tr(2, 1.4)
        y = 1.6875
        self.assertAlmostEqual(x,y,4)

    def test_norm_shock_rr(self):
        x = gd.norm_shock_rr(2, 1.4)
        y = 2.667
        self.assertAlmostEqual(x,y,3)

    def test_norm_shock_ptr(self):
        x = gd.norm_shock_ptr(1.8, 1.4)
        y = 0.81268
        self.assertAlmostEqual(x,y,4)

    def test_norm_shock_dvoa(self):
        x = gd.norm_shock_dvoa(2.0, 1.4)
        y = 1.25
        #y = 1.00
        self.assertAlmostEqual(x,y,4)

class TestObliques(unittest.TestCase):

    def test_beta(self):
        x = gd.oblique_beta_zero(4, 20*m.pi/180)
        y = 0.5666
        self.assertAlmostEqual(x,y,4)

    def test_m2(self):
        x = gd.oblique_m2(4, 30*m.pi/180, 1.4)
        y = 1.8485
        self.assertAlmostEqual(x,y,3)

    def test_ob2(self):
        x = gd.oblique_beta_zero(2.2, 14*m.pi/180, 1.4)
        #x = gd.oblique_m2(2.2, 14*m.pi/180, 1.4)
        #y = 1.674
        y = 40*m.pi/180
        self.assertAlmostEqual(x,y,2)

    def test_ob3(self):
        M = 1.605
        beta = 14*m.pi/180
        M2 = gd.oblique_m2(M, beta, 1.4)
        x = M2

        y = 1.034
        self.assertAlmostEqual(x,y,3)

    def test_ob_rho(self):
        M1 = 4
        theta = 30
        rr = gd.oblique_ratio_rho(M1, theta*m.pi/180)
        self.assertAlmostEqual(rr, 3.703, 3)

    def test_ob_ratio_p(self):
        M1 = 4
        theta = 30
        pr = gd.oblique_ratio_p(M1, theta*m.pi/180)
        self.assertAlmostEqual(pr, 9.240, 3)

    def test_ob_ratio_t(self):
        M1 = 4
        theta = 30
        tr = gd.oblique_ratio_t(M1, theta*m.pi/180)
        self.assertAlmostEqual(tr, 2.495, 3)

class Test_isentropics(unittest.TestCase):
    def test_isen_ratio_t(self):
        tr = gd.isen_ratio_t( 1.0, 1.4)
        self.assertAlmostEqual(tr, 1.2, 4)

    def test_isen_ratio_p(self):
        pr = gd.isen_ratio_p( 1.0, 1.4)
        self.assertAlmostEqual(pr, 1.2**(1.4/(1.4-1)), 4)

    def test_isen_ratio_rho(self):
        pr = gd.isen_ratio_rho( 1.0, 1.4)
        self.assertAlmostEqual(pr, 1.2**(1/(1.4-1)), 4)

class Test_PM(unittest.TestCase):
    def test_pm_angle1(self):
        M = 2.00
        nu_table = 26.37976 # degrees
        nu_func = gd.isen_pm_nu(M)
        self.assertAlmostEqual(nu_func, nu_table, 5)

    def test_pm_angle2(self):
        M = 2.10
        nu_table = 29.09708 # degrees
        nu_func = gd.isen_pm_nu(M)
        self.assertAlmostEqual(nu_func, nu_table, 5)

    def test_pm_mach_1(self):
        nu_angle = 28.01973 # deg
        M_table = 2.06 
        M_func  = gd.isen_pm_M(nu_angle)
        self.assertAlmostEqual(M_table, M_func, 5)

    def test_pm_mach_2(self):
        nu_angle = 20.0 + 20.05026 # deg
        M_table = 2.54 
        M_func  = gd.isen_pm_M(nu_angle)
        self.assertAlmostEqual(M_table, M_func, 4)
    
    def test_pm_compression(self):
        M1 = 2.4
        nu_1 = gd.isen_pm_nu(M1)
        dnu = -20
        nu_2 = nu_1 + dnu
        M2 = gd.isen_pm_M(nu_2)
        M2_true = 1.6638565212488174
        self.assertAlmostEqual(M2_true, M2, 3)


if __name__ == '__main__':
    unittest.main()