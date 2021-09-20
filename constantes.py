
# Unidades base
m_ = 1.0
s_ = 1.0
kg_ = 1.0

#Unidades derivadas
cm_ = 1e-2 * m_
mm_ = 1e-3 * m_

N_ = 1.0 * kg_ * m_ / s_
KN_ = 1e3 * N_
MN_ = 1e6 * N_
GN_ = 1e9 * N_

Pa_ = N_ / m_**2
KPa_ = KN_ / m_**2
MPa_ = MN_ / m_**2
GPa_ = GN_ / m_**2

#Constantes
g_ = 9.81 * m_ / s_**2

#Chilenismos
kgf_ = 1*kg_*g_
tonf_ = 1000*kg_*g_

#Propiedades acero
ρ_acero = 7600*kg_/m_**3
σy_acero = 420*MPa_
E_acero = 200*GPa_
