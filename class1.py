
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#=====================================            
class ishchi:
    def __init__(self,ism, f_raqam, staji ):
        self.ism=ism
        self.f_raqam=f_raqam
        self.staji=staji
    def get_info(self):
        return f"Foydalanuvchi:{self.ism} ishlash joyi: {self.f_raqam} staji: {self.staji}"
    def update_staji(self,x):
        self.staji=x
        


#===============================================

class jurnal:
    def __init__(self,nomi, davr, korinishi, nashr):
        self.nomi=nomi
        self.davr=davr
        self.korinishi=korinishi
        self.nashr=nashr
    def get_info(self):
        return f"Jurnal nomi: {self.nomi} chiqish vaqti: {self.davr} muqovasi: {self.korinishi} Tashkilot: {self.nashr}"
    def set_staji(self,x):
        self.nomi=x
    
 

#=================================================



class MAXSULOT:
    def __init__(self,ism, narxi, country):
        self.ism=ism
        self.soni=0
        self.narxi=narxi
        self.country=country
    def get_info(self):
        return f"Maxsulot nomi: {self.ism} Maxsulot soni: {self.soni} Maxsulot narxi: {self.narxi} Ishlab chiqarilgan yeri: {self.country}"
    def set_staji(self,x):
        self.narxi=x
    def update_f(self,x):
        self.narxi=self.narxi+self.narxi*x/100
    
#==========================================================================================

    
class KVITANSIYA:
    def __init__(self,raqami, sana, pulM, manzili):
        self.raqami=raqami
        self.sana=sana
        self.pulM=pulM
        self.manzili=manzili
    def get_info(self):
        return f"Narxi: {self.raqami} SANA: {self.sana} Pul: {self.pulM} manzili: {self.manzili}"
    def set_manzili(self,x):
        self.manzili=x



#============================================================


class TIKUVCHILIKSEXI:
    def __init__(self,ismi, boshliq, ishchi_s, zavod):
        self.ismi=ismi
        self.boshliq=boshliq
        self.ishchi_s=ishchi_s
        self.zavod=zavod
    def get_info(self):
        return f"Ismi: {self.ismi} BOSHLIQ: {self.boshliq} I_soni: {self.ishchi_s} ZAVOD: {self.zavod}"
    def set_ishchi_soni(self,x):
        self.ishchi_s=x
        

#=============================================================



class SHAXS:
    def __init__(self,ismi, yoshi, jinsi, millati):
        self.ismi=ismi
        self.yoshi=yoshi
        self.jinsi=jinsi
        self.millati=millati
    def get_info(self):
        return f"Ismi: {self.ismi} YOSH: {self.yoshi} JINSI: {self.jinsi} millati: {self.millati}"
    def set_millati(self,x):
        self.millati=x
        
        

#==============================================================

class KORABL:
    def __init__(self,ismi, suvsiljishi, turi, yoshi):
        self.ismi=ismi
        self.suvsiljishi=suvsiljishi
        self.turi=turi
        self.yoshi=yoshi
    def get_info(self):
        return f"Ismi: {self.ismi} Siljish: {self.suvsiljishi} Turi: {self.turi} Yoshi: {self.yoshi}"
    def set_turi(self,x):
        self.turi=x    

#===============================================================

class SHAXAR:
    def __init__(self,nomi, respublikasi, tumani, xuquqiy_x):
        self.nomi=nomi
        self.respublikasi=respublikasi
        self.tumani=tumani
        self.xuquqiy_x=xuquqiy_x
    def get_info(self):
        return f"Nomi: {self.nomi} Respublikasi: {self.respublikasi} Tumani: {self.tumani} Xuquqqiy_x: {self.xuquqiy_x}"
    def set_nomi(self,x):
        self.nomi=x  
       

#===============================================================



class TASVIR:
    def __init__(self,nomi, tasvirchi, yili, galeriya):
        self.nomi=nomi
        self.tasvirchi=tasvirchi
        self.yili=yili
        self.galeriya=galeriya
    def get_info(self):
        return f"Nomi: {self.nomi} Tasvirchi: {self.tasvirchi} Yili: {self.yili} Galeriya: {self.galeriya}"
    def set_yili(self,x):
        self.yili=x  


#==========================================================



class IJARACHI:
    def __init__(self,ismi, mamlakati, yoshi , sayoxat_m):
        self.ismi=ismi
        self.mamlakati=mamlakati
        self.yoshi=yoshi
        self.sayoxat_m=sayoxat_m
    def get_info(self):
        return f"Ismi: {self.ismi} Mamlakati: {self.mamlakati} Yoshi: {self.yoshi } Sayohat_m: {self.sayoxat_m}"
    def set_yoshi(self,x):
        self.yoshi=x 
        

#=====================================================




class TELEFON:
    def __init__(self,ismi, raqami, manzili, turi):
        self.ismi=ismi
        self.raqami=raqami
        self.manzili=manzili
        self.turi=turi
    def get_info(self):
        return f"Ismi: {self.ismi} raqami: {self.raqami} manzili: {self.manzili } Turi: {self.turi}"
    def set_raqami(self,x):
        self.raqami=x  
        
        

#======================================================


class FUTBOLCHI:
    def __init__(self,ismi, yoshi, kim_b,gollar_s ):
        self.ismi=ismi
        self.yoshi=yoshi
        self.kim_b=kim_b
        self.gollar_s=gollar_s
    def get_info(self):
        return f"Ismi: {self.ismi} yoshi: {self.yoshi} KIm bo'lib o`ynaydi: {self.kim_b } SONI: {self.gollar_s}"
    def set_gollar_s(self,x):
        self.gollar_s=x  
 

#========================================================

class DISK:
    def __init__(self,nomi, xajmi, narxi,mamlakati ):
        self.nomi=nomi
        self.xajmi=xajmi
        self.narxi=narxi
        self.mamlakati=mamlakati
    def get_info(self):
        return f"Nomi: {self.nomi} XAJMI: {self.xajmi} Narxi: {self.narxi } MAMLAKATI: {self.mamlakati}"
    def set_narxi(self,x):
        self.narxi=self.narxi+(self.narxi*x)/100
 
        

#===========================================================

class USTOZ:
    def __init__(self,ismi, yoshi, maktab, sinf):
        self.ismi=ismi
        self.yoshi=yoshi
        self.maktab=maktab
        self.sinf=sinf
    def get_info(self):
        return f"Ismi: {self.ismi} yoshi: {self.yoshi} MAKTAB: {self.maktab } SINF: {self.sinf}"
    def set_sinf(self,x):
        self.sinf=x  
        
        

#==========================================================


class FAN:
    def __init__(self,nomi, soati, kursi,turi ):
        self.nomi=nomi
        self.soati=soati
        self.kursi=kursi
        self.turi=turi
    def get_info(self):
        return f"Nomi: {self.nomi} SOAT XAJMI: {self.soati} KURSI: {self.kursi } Turi: {self.turi}"
    def set_kursi(self,x):
        self.kursi=x
        

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    