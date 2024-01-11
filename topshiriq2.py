class ISHCHI:
    def __init__(self, ismi, g_raqami, staji):
        self.ismi = ismi
        self.g_raqami = g_raqami
        self.staji = staji

    def get_info(self):
        full = f"ISMI: {self.ismi} "
        full += f"RAQAMI: {self.g_raqami} "
        full += f"STAJI: {self.staji}"
        
        return full

    def __repr__(self):
        full = f"ISMI: {self.ismi} "
        full += f"RAQAMI: {self.g_raqami} "
        full += f"STAJI: {self.staji}"
 
        return full


class KORXONA:
    def __init__(self, nomi, firma_r, manzili):
        self.nomi = nomi
        self.firma_r=firma_r
        self.manzili = manzili
        self.ishchilar = [] 
    def add_w(self, c):
        self.ishchilar.append(c)
    
    def get_w(self):
        return self.ishchilar
            
         

#===========================================================

class MAXSULOT:
    def __init__(self, nomi, narxi, mamlakati):
        self.nomi = nomi
        self.soni= 0
        self.narxi= narxi
        self.mamlakati= mamlakati
        

    def get_info(self):
        full = f"ISMI: {self.nomi} "
        full += f"NARXI: {self.narxi} "
        full += f"MAMLAKATI: {self.mamlakati}"
        
        return full

    def __repr__(self):
        full = f"ISMI: {self.nomi} "
        full += f"NARXI: {self.narxi} "
        full += f"MAMLAKATI: {self.mamlakati}"


        return full


class DUKON:
    def __init__(self, nomi, manzili, turi):
        self.nomi = nomi
        self.manzili = manzili
        self.turi=turi
        self.maxsulot = [] 
    def add_M(self, c):
        self.maxsulot.append(c)
    
    def get_M(self):
        return self.maxsulot
            
         

#==============================================================


class TIKUVCHI:
    def __init__(self, ismi, fam, lavozim,staji):
        self.ismi = ismi
        self.fam= fam
        self.lavozim= lavozim
        self.staji=staji
        

    def get_info(self):
        full = f"ISMI: {self.ismi} "
        full += f"LAVOZIMI: {self.lavozim} "
        full += f"familiyasi: {self.fam}"
        full += f"staji: {self.staji}"
        return full

    def __repr__(self):
        full = f"ISMI: {self.ismi} "
        full += f"LAVOZIMI: {self.lavozim} "
        full += f"familiyasi: {self.fam}"
        full += f"staji: {self.staji}"
       
        return full


class TIKUVCHILIKSEXI:
    def __init__(self, nomi, boshliq, i_soni):
        self.nomi = nomi
        self.boshliq = boshliq
        self.i_soni=i_soni
        self.tikuvchilar = [] 
    def add_T(self, c):
        self.tikuvchilar.append(c)
    
    def get_T(self):
        return self.tikuvchilar
            
         

#=================================================================


class SHAHAR: 
    def __init__(self, sh_nomi, xuquqiy_x):
        self.sh_nomi = sh_nomi
        self.xuquqiy_x=xuquqiy_x
       
        

    def get_info(self):
        full = f"SHAHAR NOMI: {self.sh_nomi} "
        full += f"XUQUQIY XOLATI: {self.xuquqiy_x} "
       
        return full

    def __repr__(self):
        full = f"SHAHAR NOMI: {self.sh_nomi} "
        full += f"XUQUQIY XOLATI: {self.xuquqiy_x} "
       
        return full


class VILOYAT:
    def __init__(self, nomi, yermaydoni_a, respublikasi):
        self.nomi = nomi
        self.yermaydoni_a = yermaydoni_a
        self.respublikasi=respublikasi
        self.shaharlari = [] 
    def add_SH(self, c):
        self.shaharlari.append(c)
    
    def get_SH(self):
        return self.shaharlari
            
         

#=====================================================================



class FUTBOLCHI: 
    def __init__(self, ismi, yoshi, position , gollar):
    
        self.ismi = ismi
        self.yoshi=yoshi
        self.position=position
        self.gollar=gollar
       
        

    def get_info(self):
        full = f"ISMI: {self.ismi} "
        full += f"YOSHI: {self.yoshi} "
        full+= f"POSITION: {self.position}"
        full+= f"GOLLAR SONI: {self.gollar}"
        return full

    def __repr__(self):
        full = f"ISMI: {self.ismi} "
        full += f"YOSHI: {self.yoshi} "
        full+= f"POSITION: {self.position}"
        full+= f"GOLLAR SONI: {self.gollar}"
        return full


class JAMOA:
    def __init__(self, nomi, g_soni, m_soni):
        self.nomi = nomi
        self.g_soni = g_soni
        self.m_soni=m_soni
        self.futbolchilar = [] 
    def add_f(self, c):
        self.futbolchilar.append(c)
    
    def get_f(self):
        return self.futbolchilar
            
         


#========================================================


class USTOZ: 
    def __init__(self, ismi, yoshi, maktab , sinf):
    
        self.ismi = ismi
        self.yoshi=yoshi
        self.maktab=maktab
        self.sinf=sinf
       
        

    def get_info(self):
        full = f"ISMI: {self.ismi} "
        full += f"YOSHI: {self.yoshi} "
        full+= f"MAKTAB: {self.maktab}"
        full+= f"SINF: {self.sinf}"
        return full

    def __repr__(self):
        full = f"ISMI: {self.ismi} "
        full += f"YOSHI: {self.yoshi} "
        full+= f"MAKTAB: {self.maktab}"
        full+= f"SINF: {self.sinf}"
        return full



class MAKTAB:
    def __init__(self, nomi, raqami, manzili, urini):
        self.nomi = nomi
        self.raqami = raqami
        self.manzili=manzili
        self.urini=urini
        self.ustozlar = [] 
    def add_m(self, c):
        self.ustozlar.append(c)
    
    def get_m(self):
        return self.ustozlar
            
         


