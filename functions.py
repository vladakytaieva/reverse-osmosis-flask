def membr(Gv, Cv, Xz, Xp):
    Gp = Xp * Gv
    Gk = Gv - Gp
    Cp = Cv * (1 - Xz)
    Ck = (Gv * Cv - Gp * Cp) / Gk
    return Gp, Cp, Gk, Ck

def rozd(Gk, Xr):
    Gr = Xr * Gk
    Gs = Gk - Gr
    return Gr, Gs

def zmish(Gr, Ck, Ci, Gv):
    Gi = Gv - Gr
    Cv = (Gi * Ci + Gr * Ck) / Gv
    return Gi, Cv

def zmish2(Gr1, Ck1, Gr2, Ck2):
    Gr = Gr1 + Gr2
    Ck = (Gr1 * Ck1 + Gr2 * Ck2) / Gr
    return Gr, Ck

def calc1(Ci, Gv, Xz, Xp, Xr):
    Cv = 1.2 * Ci
    i = 0
    while i < 100:
        Gp, Cp, Gk, Ck = membr(Gv, Cv, Xz, Xp)
        Gr, Gs = rozd(Gk, Xr)
        Gi, Cv = zmish(Gr, Ck, Ci, Gv)
        i += 1
    LP = Gi * Ci
    RP = Gp * Cp + Gs * Ck
    return (Gi, Gv, Gp, Cp, Gk, Ck, Gr, Gs, LP, RP)

def calc2(Ci, Gv, Xz, Xp, Xr, Xr2):
    Cv1 = 1.2 * Ci
    i = 0
    while i < 100:
        Gp1, Cp1, Gk1, Ck1 = membr(Gv, Cv1, Xz, Xp)
        Gr1, Gs1 = rozd(Gk1, Xr)
        Gp2, Cp2, Gk2, Ck2 = membr(Gp1, Cp1, Xz, Xp)
        Gr2, Gs2 = rozd(Gk2, Xr2)
        Gi2, Cv2 = zmish2(Gr1, Ck1, Gr2, Ck2)
        Gi1, Cv1 = zmish(Gi2, Cv2, Ci, Gv)
        i += 1
    LP = Gi1 * Ci
    RP = Gs1 * Ck1 + Gs2 * Ck2
    return (Gi1, Cv1, Gp1, Cp1, Gk1, Ck1, Gr1, Gs1, Gi2, Cv2, Gp2, Cp2, Gk2, Ck2, Gr2, Gs2, LP, RP)