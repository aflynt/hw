from tkinter import *
from tkinter import ttk
import libgd as gd
import math as m

class results_pair:

    def __init__(self, parent, rownum=0, infotext="", result_str=""):
        self.row = rownum
        self.txtstr = infotext
        self.resstr = StringVar(value=result_str)
        self.tlabel = ttk.Label(parent, text=f"{self.txtstr}:")
        self.rlabel = ttk.Label(parent, textvariable=self.resstr)

        self.tlabel.grid(row=self.row, column=1, sticky=E)
        self.rlabel.grid(row=self.row, column=2, sticky=E)


class Isen:

    def __init__(self, root):

        #root.title("Isentropic Flow Relations")

        self.mainframe = ttk.Frame(root, padding="3 3 12 12", )
        self.mainframe.grid(column=0, row=0, sticky=(N, S, E, W) )
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.mainframe.columnconfigure(1, weight=1)
        self.mainframe.columnconfigure(2, weight=2)
        self.mainframe.columnconfigure(3, weight=1)
        self.mainframe.rowconfigure(1, weight=1)
        self.mainframe.rowconfigure(2, weight=5)
        self.mainframe.rowconfigure(3, weight=5)
        self.mainframe.rowconfigure(4, weight=5)
        self.mainframe.rowconfigure(5, weight=5)
        self.mainframe.rowconfigure(6, weight=5)
        self.mainframe.rowconfigure(7, weight=5)
        self.mainframe.rowconfigure(8, weight=5)
        self.mainframe.rowconfigure(9, weight=5)
        self.mainframe.rowconfigure(10, weight=5)
        self.mainframe.rowconfigure(11, weight=5)
        self.mainframe.rowconfigure(12, weight=5)


        self.x = StringVar(value="2")

        # results dict
        self.rdict = {
                'M'          : results_pair(self.mainframe,  2, 'M' ),
                'Pt/p'       : results_pair(self.mainframe,  3, 'Pt/p' ),
                'p/Pt'       : results_pair(self.mainframe,  4, 'p/Pt' ),
                'Tt/T'       : results_pair(self.mainframe,  5, 'Tt/T' ),
                'T/Tt'       : results_pair(self.mainframe,  6, 'T/Tt' ),
                'PM-angle'   : results_pair(self.mainframe,  7, 'PM-angle' ),
                'Mach angle' : results_pair(self.mainframe,  8, 'Mach angle' ),
                'P/P*'       : results_pair(self.mainframe,  9, 'P/P*' ),
                'T/T*'       : results_pair(self.mainframe, 10, 'T/T*' ),
                'A/A*'       : results_pair(self.mainframe, 11, 'A/A*' ),
                'type'       : results_pair(self.mainframe, 12, 'type' ),
        }

        # Combobox
        self.incb = ttk.Combobox(self.mainframe, textvariable=self.rdict['type'].resstr)
        self.incb.grid(row=1, column=1, stick=(W,E))
        self.incb.bind('<<ComboboxSelected>>', self.update_type)
        self.incb['values'] = ('M', 'T/Tt', 'P/Pt', 'A/A*-','A/A*+', 'PM-angle (deg)')
        self.incb.set('M')
        self.incb.state(['readonly'])


        # Input Entry
        entry_x = ttk.Entry(self.mainframe, width=7, textvariable=self.x)
        entry_x.grid(row=1, column=2, sticky=(W,E))

        # Go Button
        ttk.Button(self.mainframe, text="Calculate", command=self.calculate).grid(row=1, column=3, sticky=(W,E))

        for child in self.mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        entry_x.focus()
        root.bind("<Return>", self.calculate)

    def update_type(self, *args):
        astr = self.incb.get()

        self.rdict['type'].resstr.set(astr)
        print(f" got: {astr}")

    def get_M(self, *args):
        x = float(self.x.get())
        intype = self.incb.get()

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

        
    def calculate(self, *args):
        try:
            M = self.get_M()

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

            self.rdict['M'].resstr.set(           f"{M:15.6f}")
            self.rdict['Pt/p'].resstr.set(        f"{pr:15.6f}")
            self.rdict['p/Pt'].resstr.set(        f"{1/pr:15.6f}")
            self.rdict['Tt/T'].resstr.set(        f"{tr:15.6f}")
            self.rdict['T/Tt'].resstr.set(        f"{1/tr:15.6f}")
            self.rdict['PM-angle'].resstr.set(    f"{pm_nu:15.6f}")
            self.rdict['Mach angle'].resstr.set(  f"{mach_angle:15.6f}")
            self.rdict['P/P*'].resstr.set(        f"{pops:15.6f}")
            self.rdict['T/T*'].resstr.set(        f"{tots:15.6f}")
            self.rdict['A/A*'].resstr.set(        f"{aoas:15.6f}")

        except ValueError:
            pass

if __name__ == "__main__":
    root = Tk()
    Isen(root)
    root.mainloop()