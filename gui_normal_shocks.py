from tkinter import *
from tkinter import ttk
import libgd as gd
import math as m
import traceback
from gui_isentropics import Isen

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
P2 = ttk.PanedWindow(mp, orient=VERTICAL)
mp.add(P1)
mp.add(P2)

## normal shocks ----------------------------------------------
x = StringVar(value="2")
fns = ttk.Frame(P1, padding="3 3 12 12")
P1.add(fns)
fns.grid(column=0, row=0, sticky=(N, S, E, W) )
P1.columnconfigure(0, weight=1)
P1.rowconfigure(0, weight=1)
fns.columnconfigure(1, weight=1)
fns.columnconfigure(2, weight=2)
fns.columnconfigure(3, weight=1)
fns.rowconfigure(1, weight=1)
fns.rowconfigure(2, weight=5)
fns.rowconfigure(3, weight=5)
fns.rowconfigure(4, weight=5)
fns.rowconfigure(5, weight=5)
fns.rowconfigure(6, weight=5)
fns.rowconfigure(7, weight=5)
fns.rowconfigure(8, weight=5)
fns.rowconfigure(9, weight=5)

tl = ttk.Label(fns, text="Normal Shocks", style="BW.TLabel", font=("Kozuka Mincho Pro M", 12, "bold"))
tl.grid(row=1, column=1, sticky=(E,W))


st = ttk.Style().configure("BW.TLabel", padding=6, relief="flat", background="#00005F", foreground="#AFAF00")
rdict = {
      'M1'          : results_pair(fns,  3, 'M1' ),
      'M2'          : results_pair(fns,  4, 'M2' ),
      'Pt2/Pt1'     : results_pair(fns,  5, 'Pt2/Pt1' ),
      'P2/P1'       : results_pair(fns,  6, 'P2/P1' ),
      'T2/T1'       : results_pair(fns,  7, 'T2/T1' ),
      'r2/r1'       : results_pair(fns,  8, 'r2/r1' ),
      'p1/pt2'      : results_pair(fns,  9, 'p1/pt2' ),
}

# Combobox
incb = ttk.Combobox(fns, style="TCombobox")
incb.grid(row=2, column=1, stick=(W,E))
incb['values'] = ('M1', 'M2', 'P2/P1', 'rho2/rho1','T2/T1', 'Pt2/Pt1', 'p1/pt2')
incb.set('M1')
incb.state(['readonly'])

# Input Entry
entry_x = ttk.Spinbox(fns, width=7, textvariable=x, from_=0.0, to=10, increment=0.1)

fcmd = lambda : norm_shock_calc(float(entry_x.get()), incb.get(), rdict)
fcmdx = lambda e: norm_shock_calc(float(entry_x.get()), incb.get(), rdict)
fwrapper = lambda e: fcmd()

entry_x.bind("<<Increment>>", fwrapper)
entry_x.bind("<<Decrement>>", fwrapper)
entry_x.grid(row=2, column=2, sticky=(W,E))

# Go Button
ttk.Button(fns, text="Calculate", command=fcmd).grid(row=2, column=3, sticky=(W,E))

for child in fns.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

entry_x.focus()
entry_x.bind("<Return>", fwrapper)



## isentropics ----------------------------------------------
#ix = StringVar(value="2")

class PackIsen:
   def __init__(self, parent):

    fis = ttk.Frame(parent, padding="3 3 12 12")
    parent.add(fis)
    fis.grid(column=0, row=0, sticky=(N, S, E, W))
    parent.columnconfigure(0, weight=1)
    parent.rowconfigure(0, weight=1)
    fis.columnconfigure(1, weight=1)
    fis.columnconfigure(2, weight=2)
    fis.columnconfigure(3, weight=1)
    fis.rowconfigure(1, weight=1)
    fis.rowconfigure(2, weight=5)
    fis.rowconfigure(3, weight=5)
    fis.rowconfigure(4, weight=5)
    fis.rowconfigure(5, weight=5)
    fis.rowconfigure(6, weight=5)
    fis.rowconfigure(7, weight=5)
    fis.rowconfigure(8, weight=5)
    fis.rowconfigure(9, weight=5)
    fis.rowconfigure(10, weight=5)
    fis.rowconfigure(11, weight=5)
    fis.rowconfigure(12, weight=5)
    fis.rowconfigure(13, weight=5)
    itl = ttk.Label(fis, text="Isentropic Flow", style="BW.TLabel", font=("Kozuka Mincho Pro M", 12, "bold"))
    itl.grid(row=1, column=1, sticky=(E,W))

    irdict = {
            'M'          : results_pair(fis,  3, 'M' ),
            'Pt/p'       : results_pair(fis,  4, 'Pt/p' ),
            'p/Pt'       : results_pair(fis,  5, 'p/Pt' ),
            'Tt/T'       : results_pair(fis,  6, 'Tt/T' ),
            'T/Tt'       : results_pair(fis,  7, 'T/Tt' ),
            'PM-angle'   : results_pair(fis,  8, 'PM-angle' ),
            'Mach angle' : results_pair(fis,  9, 'Mach angle' ),
            'P/P*'       : results_pair(fis, 10, 'P/P*' ),
            'T/T*'       : results_pair(fis, 11, 'T/T*' ),
            'A/A*'       : results_pair(fis, 12, 'A/A*' ),
            'type'       : results_pair(fis, 13, 'type' ),
    }

    # Combobox
    i_incb = ttk.Combobox(fis, textvariable=irdict['type'].resstr)
    i_incb.grid(row=2, column=1, stick=(W,E))
    i_incb['values'] = ('M', 'T/Tt', 'P/Pt', 'A/A*-','A/A*+', 'PM-angle (deg)')
    i_incb.set('M')
    i_incb.state(['readonly'])

    # Input Entry
    i_entry_x = ttk.Spinbox(fis, width=7, from_=0.0, to=10, increment=0.1)
    i_entry_x.set("4")
    i_entry_x.grid(row=2, column=2, sticky=(W,E))
    
    ifcmd = lambda : isen_calc(float(i_entry_x.get()), i_incb.get(), irdict)
    ret_wrapper = lambda e: ifcmd()
    
    i_entry_x.bind('<Return>', ret_wrapper)
    
    # Go Button
    ttk.Button(fis, text="Calculate", command=ifcmd).grid(row=2, column=3, sticky=(W,E))
    
    for child in fis.winfo_children(): 
      child.grid_configure(padx=5, pady=5)

PackIsen(P2)

root.mainloop()