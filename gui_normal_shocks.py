from tkinter import *
from tkinter import ttk
import libgd as gd
import math as m
import traceback
from gui_isentropics import Isen
from typing import List, Dict, Callable

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

class results_pair:

    def __init__(self, parent, rownum=0, infotext="", result_str=""):
        self.row = rownum
        self.txtstr = infotext
        self.resstr = StringVar(value=result_str)
        self.tlabel = ttk.Label(parent, text=f"{self.txtstr}:")
        self.rlabel = ttk.Label(parent, textvariable=self.resstr)

        self.tlabel.grid(row=self.row, column=1, sticky=E)
        self.rlabel.grid(row=self.row, column=2, sticky=E)

class GenPack:
   def __init__(self, frame:ttk.Frame, labeltext:str, result_list:List[str], combo_list:List[str], result_callback: Callable[[float, str, Dict], None]):
    self.frame = frame

    self.frame.grid(column=0, row=0, sticky=(N, S, E, W))
    self.frame.columnconfigure(1, weight=1)
    self.frame.columnconfigure(2, weight=2)
    self.frame.columnconfigure(3, weight=1)
    self.frame.rowconfigure(1, weight=1)
    self.frame.rowconfigure(2, weight=1)

    for i in range(len(result_list)):
      self.frame.rowconfigure(i+3, weight=5)

    self.itl = ttk.Label(self.frame, text=labeltext, style="BW.TLabel", font=("Kozuka Mincho Pro M", 12, "bold"))
    self.itl.grid(row=1, column=1, sticky=(E,W))

    self.irdict = {}
    for i,resname in enumerate(result_list):
       self.irdict[resname] = results_pair(self.frame, i+3, resname)

    # Combobox
    #self.incb = ttk.Combobox(self.frame, textvariable=self.irdict['type'].resstr)
    self.incb = ttk.Combobox(self.frame, style="TCombobox")
    self.incb.grid(row=2, column=1, stick=(W,E))
    self.incb['values'] = combo_list
    self.incb.set(combo_list[0])
    self.incb.state(['readonly'])

    # Input Entry
    self.i_entry_x = ttk.Spinbox(self.frame, width=7, from_=0.0, to=10, increment=0.1)
    self.i_entry_x.set("1.1")
    self.i_entry_x.grid(row=2, column=2, sticky=(W,E))
    
    self.ifcmd = lambda :  result_callback(float(self.i_entry_x.get()), self.incb.get(), self.irdict)
    self.ret_wrapper = lambda e: self.ifcmd()
    
    self.i_entry_x.bind('<Return>', self.ret_wrapper)
    self.i_entry_x.bind("<<Increment>>", self.ret_wrapper)
    self.i_entry_x.bind("<<Decrement>>", self.ret_wrapper)
    
    # Go Button
    ttk.Button(self.frame, text="Calculate", command=self.ifcmd).grid(row=2, column=3, sticky=(W,E))
    
    for child in self.frame.winfo_children(): 
      child.grid_configure(padx=5, pady=5)

# ROOT ------------------------------------------------------------------------
root = Tk()
#root.geometry("700x400")
root.title("Gas Dynamics")
root.configure(background='black')

style = ttk.Style(root)
style.configure('TFrame', background='#00005F')
#style.configure('TLabel', background='#00005F', foreground="#AFAF00", font=("Fixedsys", 12))
style.configure('TLabel', background='#00005F', foreground="#AFAF00", font=("Kozuka Mincho Pro M", 11))
style.configure('TPanedWindow', background='#00005F')
#style.configure('TButton', background='#808080', foreground="#AFAF00")
#style.configure('TCombobox', foreground="blue", background="yellow", fieldbackground="yellow", selectbackground="yellow")
#                #foreground="black",
#                #background="blue",
#                fieldbackground='#800080',
#                selectbackground='#lightgray',
#)
#style.configure('TSpinbox', selectbackground='#800080',fieldbackground='#800080', foreground="#AFAF00")

# make paned windows
mp = ttk.PanedWindow(root, orient=VERTICAL)
mp.pack(fill=BOTH, expand=1)

P1 = ttk.PanedWindow(mp, orient=VERTICAL)
P1.columnconfigure(0, weight=1)
P1.rowconfigure(0, weight=1)
mp.add(P1)

P2 = ttk.PanedWindow(mp, orient=VERTICAL)
P2.columnconfigure(0, weight=1)
P2.rowconfigure(0, weight=1)
mp.add(P2)


# ISENTROPICS -------------------------------------
fis = ttk.Frame(P1, padding="3 3 12 12")
P1.add(fis)
irlist = ['M','Pt/p','p/Pt','Tt/T','T/Tt','PM-angle','Mach angle','P/P*','T/T*','A/A*','type',]
iclist = ('M', 'T/Tt', 'P/Pt', 'A/A*-','A/A*+', 'PM-angle (deg)')
GenPack(fis, "Isentropic Flow", irlist, iclist, isen_calc)

# NORMAL SHOCKS -------------------------------------
fns = ttk.Frame(P2, padding="3 3 12 12")
P2.add(fns)
nrlist = ['M1','M2','Pt2/Pt1','P2/P1','T2/T1','r2/r1','p1/pt2',]
nclist = ('M1', 'M2', 'P2/P1', 'rho2/rho1','T2/T1', 'Pt2/Pt1', 'p1/pt2')
GenPack(fns, "Normal Shocks", nrlist, nclist, norm_shock_calc)

root.mainloop()