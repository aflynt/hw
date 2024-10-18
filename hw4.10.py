from libgd import *

g_air = Gas_mgr().AIR_SI

print(f" given air:")
cp = g_air.cp
R = g_air.R
k = g_air.k

print(f" - cp = {cp:10.3f}")
print(f" -  R = {R:10.3f}")
print(f" -  k = {k:10.3f}")

print(f" Given:")
pt = 3.8e5 # Pa
M = 1.35
ht = 4.5e5 # J/kg

TR = (1 + (k-1)/2*M**2)
PR = (TR)**(k/(k-1))

print(f"TR = {TR:10.4f}")
print(f"PR = {PR:10.4f}")

Tt = ht / cp
Ts = Tt / TR

print(f"Tt = {Tt:10.3f}")
print(f"Ts = {Ts:10.3f}")

Ps = pt / PR
print(f"Ps = {Ps/1000:10.3f} kPa")

a_s = m.sqrt(k*R*Ts)
u = M * a_s

print(f"a_s = {a_s:10.3f} m/s")
print(f"u   = {u:10.3f} m/s")

