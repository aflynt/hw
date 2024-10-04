
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


if __name__ == '__main__':
    unittest.main()