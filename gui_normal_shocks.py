from tkinter import *
from tkinter import ttk
import libgd as gd
import math as m
import traceback
from gui_isentropics import Isen
from typing import List, Dict, Callable
import numpy as np

def ray_get_mach(x, intype):

  M = x
  try:
    match intype:
      #'U/U*',
      #'(S*-S)/R_sub',
      #'(S*-S)/R_sup',
      case 'M':
        M = x
      case 'Tt/Tt*_sub':
        fzero = lambda mm: gd.ray_ratio_Tt(mm) - x
        M = gd.bisector(fzero, 0, 1)
      case 'Tt/Tt*_sup':
        fzero = lambda mm: gd.ray_ratio_Tt(mm) - x
        M = gd.bisector(fzero, 1, 10)
      case 'T/T*_sub':
        fzero = lambda mm: gd.ray_ratio_T(mm) - x
        M = gd.bisector(fzero, 0, 1)
      case 'T/T*_sup':
        fzero = lambda mm: gd.ray_ratio_T(mm) - x
        M = gd.bisector(fzero, 1, 10)
      case 'P/P*':
        fzero = lambda mm: gd.ray_ratio_P(mm) - x
        M = gd.bisector(fzero, 1e-4, 20)
      case 'Pt/Pt*_sub':
        fzero = lambda MM: gd.ray_ratio_Pt(MM) - x
        M = gd.bisector(fzero, 0.001, 1)
      case 'Pt/Pt*_sup':
        fzero = lambda MM: gd.ray_ratio_Pt(MM) - x
        M = gd.bisector(fzero, 1, 20)
      case 'U/U*':
        fzero = lambda MM: gd.ray_ratio_v(MM) - x
        M = gd.bisector(fzero, 0.01, 20)
      case '(S*-S)/R_sub':
        dsor = x
        fzero = lambda m: gd.ray_dsor(m) - dsor
        M = gd.bisector(fzero, 0.001, 1)
      case '(S*-S)/R_sup':
        dsor = x
        fzero = lambda m: gd.ray_dsor(m) - dsor
        M = gd.bisector(fzero, 1, 20)
      case '_':
        pass

  except Exception as e:
     print(f"error e: {str(e)}")
     traceback.print_exc()

  return M

def ray_calc(x: float, intype: str, rdict: dict):
  try:
    M = ray_get_mach(x, intype)
    TTR = gd.ray_ratio_Tt(M)
    TR  = gd.ray_ratio_T(M)
    PR  = gd.ray_ratio_P(M)
    PTR = gd.ray_ratio_Pt(M)
    VR  = gd.ray_ratio_v(M)
    dsor = gd.ray_dsor(M)

    rdict['M'].resstr.set(   f"{M:14.6f}") 
    rdict['T/T*'].resstr.set(  f"{TR:14.6f}")
    rdict['P/P*'].resstr.set(  f"{PR:14.6f}")
    rdict['Pt/Pt*'].resstr.set(  f"{PTR:14.6f}")
    rdict['U/U*'].resstr.set(  f"{VR:14.6f}")
    rdict['Tt/Tt*'].resstr.set(  f"{TTR:14.6f}")
    rdict['(S*-S)/R'].resstr.set(  f"{dsor:14.6f}")

  except Exception as e:
    print(f"error e: {str(e)}")
    traceback.print_exc()

def fanno_get_mach(x, intype):

  M = x
  try:
    match intype:
      case 'M':
        M = x
      case 'T/T*':
        TR = max(min(x, 0.2), 0) # must be bewteen 0 and 1.2
        fzero = lambda MM: gd.fanno_ratio_T(MM) - TR
        M = gd.bisector(fzero, 0.01, 20)
      case 'P/P*':
        M = gd.fanno_M_from_PR(x, 0.05, 10)
      case 'Pt/Pt*_sub':
        PTR = max(x,0)
        fzero = lambda MM: gd.fanno_ratio_Pt(MM) - PTR
        M = gd.bisector(fzero, 0.001, 1)
      case 'Pt/Pt*_sup':
        PTR = max(x,0)
        fzero = lambda MM: gd.fanno_ratio_Pt(MM) - PTR
        M = gd.bisector(fzero, 1, 20)
      case 'U/U*':
        VR = x
        fzero = lambda MM: gd.fanno_ratio_v(MM) - VR
        M = gd.bisector(fzero, 0.001, 20)
      case 'fL*/D_sub':
        fld = x
        fzero = lambda MM: gd.fanno_flod_max(MM) - fld
        M = gd.bisector(fzero, 0.001, 1)
      case 'fL*/D_sup':
        fld = min(x, -1.8214)
        fzero = lambda MM: gd.fanno_flod_max(MM) - fld
        M = gd.bisector(fzero, 1, 20)
      case '(S*-S)/R_sub':
        dsor = x
        fzero = lambda m: gd.fanno_SmaxoR(m) - dsor
        M = gd.bisector(fzero, 0.001, 1)
      case '(S*-S)/R_sup':
        dsor = x
        fzero = lambda m: gd.fanno_SmaxoR(m) - dsor
        M = gd.bisector(fzero, 1, 20)
      case '_':
        pass

  except Exception as e:
     print(f"error e: {str(e)}")
     traceback.print_exc()

  return M

def fanno_calc(x: float, intype: str, rdict: dict):
  try:
    M = fanno_get_mach(x, intype)
    TR   = gd.fanno_ratio_T(M)
    PR   = gd.fanno_ratio_P(M)
    PTR  = gd.fanno_ratio_Pt(M)
    VR   = gd.fanno_ratio_v(M)
    fld  = gd.fanno_flod_max(M)
    dsor = gd.fanno_SmaxoR(M)

    rdict['M'].resstr.set(   f"{M:14.6f}") 
    rdict['T/T*'].resstr.set(   f"{TR:14.6f}") 
    rdict['P/P*'].resstr.set(   f"{PR:14.6f}") 
    rdict['Pt/Pt*'].resstr.set(   f"{PTR:14.6f}") 
    rdict['U/U*'].resstr.set(   f"{VR:14.6f}") 
    rdict['fL*/D'].resstr.set(   f"{fld:14.6f}") 
    rdict['(S*-S)/R'].resstr.set(   f"{dsor:14.6f}") 

  except Exception as e:
    print(f"error e: {str(e)}")
    traceback.print_exc()


def isen_get_M(x, intype):

    match intype:
        case 'M':
          M = x
          return M
        case 'T/Tt':
          M = gd.get_mach_given_tr(1/x, gd.Gas_mgr().AIR_SI)
          return M
        case 'P/Pt':
          M = gd.get_mach_given_pr(1/x, gd.Gas_mgr().AIR_SI)
          return M
        case 'A/A*-':
          Msub,_ = gd.get_mach_given_aoastar(x, 1.4)
          M = Msub
          return M
        case 'A/A*+':
          _,Msup = gd.get_mach_given_aoastar(x, 1.4)
          M = Msup
          return M
        case 'PM-angle (deg)':
          M = gd.isen_pm_M(x)
          return M
        case '_':
          return M

def isen_calc(x, intype, rdict):
    try:
        M = isen_get_M(x, intype)

        #print(f"now M = {M}")

        pr = gd.isen_ratio_p(M)
        tr = gd.isen_ratio_t(M)
        pm_nu = gd.isen_pm_nu(M) if M >= 1 else 0
        mach_angle = m.asin(1/M) * 180/m.pi if M >= 1 else 0
        prs = gd.isen_ratio_p(1)
        pops = prs/pr
        trs = gd.isen_ratio_t(1)
        tots = trs/tr
        aoas = gd.aoastar(1.4, M)

        rdict['M'].resstr.set(           f"{M:15.6f}")
        rdict['Pt/p'].resstr.set(        f"{pr:15.6f}")
        rdict['p/Pt'].resstr.set(        f"{1/pr:15.6f}")
        rdict['Tt/T'].resstr.set(        f"{tr:15.6f}")
        rdict['T/Tt'].resstr.set(        f"{1/tr:15.6f}")
        rdict['PM-angle'].resstr.set(    f"{pm_nu:15.6f}")
        rdict['Mach angle'].resstr.set(  f"{mach_angle:15.6f}")
        rdict['P/P*'].resstr.set(        f"{pops:15.6f}")
        rdict['T/T*'].resstr.set(        f"{tots:15.6f}")
        rdict['A/A*'].resstr.set(        f"{aoas:15.6f}")

    except ValueError:
        pass

def norm_shock_get_M1(x, intype):

    M1 = x
    
    try:
      match intype:
          case 'M1':
            M1 = x if x >= 1 else 1
          case 'M2':
            M1 = gd.norm_shock_m1(x, 1.4, 1, 100) if x <= 1 else 1
          case 'P2/P1':
            M1 = gd.norm_get_M1_given_pr(x)
          case 'rho2/rho1':
            M1 = gd.norm_get_M1_given_rr(x)
          case 'T2/T1':
            M1 = gd.norm_get_M1_given_tr(x)
          case 'Pt2/Pt1':
            M1 = gd.norm_get_M1_given_ptr(x) if x <= 1 else 1
          case 'p1/pt2':
            M1 = gd.norm_get_M1_given_p1opt2(x) if x <= 0.52828178 else 1
          case '_':
            M1 = x if x >= 1 else 1
    except Exception as e:
      print(f"error: x:{x} -> intype: {intype}")
      traceback.print_exc()

    return M1

def norm_shock_calc(x: float, intype:str , rdict: dict):

    try:
        M1 = norm_shock_get_M1(x, intype)
        M2 = gd.norm_shock_m2(M1)
        PTR = gd.norm_shock_ptr(M1)
        PR = gd.norm_shock_pr(M1)
        TR = gd.norm_shock_tr(M1)
        RR = gd.norm_shock_rr(M1)
        p1opt2 = gd.norm_shock_p1opt2(M1)

        rdict['M1'].resstr.set(           f"{M1:15.6f}")
        rdict['M2'].resstr.set(           f"{M2:15.6f}")
        rdict['Pt2/Pt1'].resstr.set(        f"{PTR:15.6f}")
        rdict['P2/P1'].resstr.set(        f"{PR:15.6f}")
        rdict['T2/T1'].resstr.set(        f"{TR:15.6f}")
        rdict['r2/r1'].resstr.set(        f"{RR:15.6f}")
        rdict['p1/pt2'].resstr.set(        f"{p1opt2:15.6f}")

    except Exception as e:
        print(f"error: M1: {M1} e: {str(e)}")
        traceback.print_exc()
      
def oblique_get_theta(x, intype, M1):

  theta = x*m.pi/180  # rad
  try:
    match intype:
       case 'turn angle weak':
          theta = x*m.pi/180  # rad
       case 'turn angle strong':
          theta = x*m.pi/180  # rad
       case 'wave angle':
          wave_angle = x*m.pi/180
          theta = gd.oblique_delta(M1, wave_angle)
       case 'M1n':
          wave_angle = m.asin(x/M1)
          theta = gd.oblique_delta(M1, wave_angle)
          print(f"ok here theta = {theta*180/m.pi}")
       case '_':
          pass

  except Exception as e:
     print(f"error e: {str(e)}")
     traceback.print_exc()

  return theta

def oblique_shock_calc(x: float, intype: str, rdict: dict):
  try:
    M1 = float(mach_spinner.get()) # always known
    theta = oblique_get_theta(x, intype, M1)
    M2 = gd.oblique_m2(M1, theta)
    wave_angle = gd.oblique_beta_zero(M1, theta)
    PR = gd.oblique_ratio_p(M1, theta)
    RR = gd.oblique_ratio_rho(M1, theta)
    TR = gd.oblique_ratio_t(M1, theta)
    PTR = gd.oblique_ratio_pt(M1, theta)
    M1n = M1*m.sin(wave_angle)
    M2n = gd.norm_shock_m2(M1n)

    rdict['M2'].resstr.set(   f"{float(M2):15.6f}") 
    rdict['Turn Angle'].resstr.set(f"{theta*180/m.pi:15.6f}")
    rdict['Wave Angle'].resstr.set(f"{wave_angle*180/m.pi:15.6f}")
    rdict['P2/P1'].resstr.set(f"{PR:15.6f}")
    rdict['rho2/rho1'].resstr.set(f"{RR:15.6f}")
    rdict['T2/T1'].resstr.set(f"{TR:15.6f}")
    rdict['Pt2/Pt1'].resstr.set(f"{PTR:15.6f}")
    rdict['M1n'].resstr.set(f"{M1n:15.6f}")
    rdict['M2n'].resstr.set(f"{M2n:15.6f}")

  except Exception as e:
    print(f"error e: {str(e)}")
    traceback.print_exc()


class results_pair:

    def __init__(self, parent, rownum=0, infotext="", result_str=""):
        self.row = rownum
        self.txtstr = infotext
        self.resstr = StringVar(value=result_str)
        self.tlabel = ttk.Label(parent, text=f"{self.txtstr}:")
        self.rlabel = ttk.Label(parent, textvariable=self.resstr)

        self.tlabel.grid(row=self.row, column=1, sticky=E)
        self.rlabel.grid(row=self.row, column=2, sticky=E, columnspan=2)

class GenPack:
   def __init__(self, frame:ttk.Frame, labeltext:str, result_list:List[str], combo_list:List[str], result_callback: Callable[[float, str, Dict], None], ioffset=3):
    self.frame = frame

    self.frame.grid(column=0, row=0, sticky=(N, S, E, W))
    self.frame.columnconfigure(1, weight=1)
    self.frame.columnconfigure(2, weight=2)
    self.frame.columnconfigure(3, weight=1)
    self.frame.rowconfigure(1, weight=1)
    self.frame.rowconfigure(2, weight=1)

    for i in range(len(result_list)):
      self.frame.rowconfigure(i+ioffset, weight=5)

    self.itl = ttk.Label(self.frame, text=labeltext, style="BW.TLabel", font=("Kozuka Mincho Pro M", 12, "bold"))
    self.itl.grid(row=1, column=1, sticky=(E,W))

    self.irdict = {}
    for i,resname in enumerate(result_list):
       self.irdict[resname] = results_pair(self.frame, i+ioffset, resname)

    # Combobox
    self.incb = ttk.Combobox(self.frame, style="TCombobox")
    self.incb.grid(row=2, column=1, stick=(W,E))
    self.incb['values'] = combo_list
    self.incb.set(combo_list[0])
    self.incb.state(['readonly'])

    # Input Entry
    self.i_entry_x = ttk.Spinbox(self.frame, width=7, from_=0.0, to=45, increment=0.1)
    self.i_entry_x.set("1.1")
    self.i_entry_x.grid(row=2, column=2, sticky=(W,E))
    
    self.ifcmd = lambda :  result_callback(float(self.i_entry_x.get()), self.incb.get(), self.irdict)
    self.ret_wrapper = lambda e: self.ifcmd()
    
    self.i_entry_x.bind('<Return>', self.ret_wrapper)
    self.i_entry_x.bind("<<Increment>>", self.ret_wrapper)
    self.i_entry_x.bind("<<Decrement>>", self.ret_wrapper)
    
    # Go Button
    ttk.Button(self.frame, text="Calculate", command=self.ifcmd).grid(row=2, column=ioffset, sticky=(W,E))
    
    for child in self.frame.winfo_children(): 
      child.grid_configure(padx=5, pady=5)

# ROOT ------------------------------------------------------------------------
root = Tk()
#root.geometry("700x400")
root.title("Gas Dynamics")
root.configure(background='black')

style = ttk.Style(root)
style.configure('TFrame', background='#080808')
#style.configure('TLabel', background='#00005F', foreground="#AFAF00", font=("Fixedsys", 12))
style.configure('TLabel', background='#080808', foreground="#AFAF00", font=("Kozuka Mincho Pro M", 11))
style.configure('TPanedWindow', background='#080808')
#style.configure('TButton', background='#808080', foreground="#AFAF00")
#style.configure('TCombobox', foreground="blue", background="yellow", fieldbackground="yellow", selectbackground="yellow")
#                #foreground="black",
#                #background="blue",
#                fieldbackground='#800080',
#                selectbackground='#lightgray',
#)
#style.configure('TSpinbox', selectbackground='#800080',fieldbackground='#800080', foreground="#AFAF00")


# make paned windows
#mp = ttk.PanedWindow(root, orient=VERTICAL)
mp = ttk.PanedWindow(root, orient=HORIZONTAL)
mp.pack(fill=BOTH, expand=1)





# ISENTROPICS -------------------------------------
P1 = ttk.PanedWindow(mp, orient=VERTICAL)
P1.columnconfigure(0, weight=1)
P1.rowconfigure(0, weight=1)
mp.add(P1)
f1 = ttk.Frame(P1, padding="3 3 12 12")
P1.add(f1)
irlist = ['M','Pt/p','p/Pt','Tt/T','T/Tt','PM-angle','Mach angle','P/P*','T/T*','A/A*']
iclist = ('M', 'T/Tt', 'P/Pt', 'A/A*-','A/A*+', 'PM-angle (deg)')
GenPack(f1, "Isentropic Flow", irlist, iclist, isen_calc)

# NORMAL SHOCKS -------------------------------------
P2 = ttk.PanedWindow(mp, orient=VERTICAL)
P2.columnconfigure(0, weight=1)
P2.rowconfigure(0, weight=1)
mp.add(P2)
f2 = ttk.Frame(P2, padding="3 3 12 12")
P2.add(f2)
nrlist = ['M1','M2','Pt2/Pt1','P2/P1','T2/T1','r2/r1','p1/pt2',]
nclist = ('M1', 'M2', 'P2/P1', 'rho2/rho1','T2/T1', 'Pt2/Pt1', 'p1/pt2')
GenPack(f2, "Normal Shocks", nrlist, nclist, norm_shock_calc)

# OBLIQUE SHOCKS -----------------------------------
P3 = ttk.PanedWindow(mp, orient=VERTICAL)
P3.columnconfigure(0, weight=1)
P3.rowconfigure(0, weight=1)
mp.add(P3)

f3 = ttk.Frame(P3, padding="3 3 12 12")
P3.add(f3)
rlist3 = ['M2','Turn Angle','Wave Angle','P2/P1','rho2/rho1','T2/T1','Pt2/Pt1','M1n','M2n',]
clist3 = ('turn angle weak','turn angle strong','wave angle','M1n',)
gpo = GenPack(f3, "Oblique Shocks", rlist3, clist3, oblique_shock_calc, 4)


gpo.mach_label = ttk.Label(f3, text="M1:", style="BW.TLabel", font=("Kozuka Mincho Pro M", 11, "bold"))
gpo.mach_label.grid(row=3, column=1, sticky=E, padx=5, pady=5 )
gpo.mach_label.configure(background="#00005F", foreground="#7E5F7E")
gpo.i_entry_x.set("20")

mach_spinner = ttk.Spinbox(f3, width=7, from_=1.0, to=10, increment=0.25)
mach_spinner.set("5.0")
mach_spinner.grid(row=3, column=2, sticky=(W,E), padx=5, pady=5)

# FANNO FLOW -------------------------------------
P4 = ttk.PanedWindow(mp, orient=VERTICAL)
P4.columnconfigure(0, weight=1)
P4.rowconfigure(0, weight=1)
mp.add(P4)
f4 = ttk.Frame(P4, padding="3 3 12 12")
P4.add(f4)
rlist4 = ['M','T/T*','P/P*','Pt/Pt*','U/U*','fL*/D','(S*-S)/R']
clist4 = ('M','T/T*','P/P*','Pt/Pt*_sub','Pt/Pt*_sup','U/U*','fL*/D_sub','fL*/D_sup','(S*-S)/R_sub','(S*-S)/R_sup',)
GenPack(f4, "Fanno Flow", rlist4, clist4, fanno_calc)

# RAYLEIGH FLOW -------------------------------------
P5 = ttk.PanedWindow(mp, orient=VERTICAL)
P5.columnconfigure(0, weight=1)
P5.rowconfigure(0, weight=1)
mp.add(P5)
f5 = ttk.Frame(P5, padding="3 3 12 12")
P5.add(f5)
rlist5 = ['M','Tt/Tt*','T/T*','P/P*','Pt/Pt*','U/U*','(S*-S)/R']
clist5 = ('M','Tt/Tt*_sub','Tt/Tt*_sup','T/T*_sub','T/T*_sup','P/P*','Pt/Pt*_sub','Pt/Pt*_sup','U/U*','(S*-S)/R_sub','(S*-S)/R_sup',)
GenPack(f5, "Rayleigh Flow", rlist5, clist5, ray_calc)

root.mainloop()