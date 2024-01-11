from topshiriq1 import*
obj1 = ISHCHI("nodir", 15, "5-yil")

K1 = KORXONA("COCE", 225, "toshkent")
K1.add_w(obj1)
print(K1.get_w())

#-----
max1 = MAXSULOT("cola", 13000, "amerika")

D1 = DUKON("baraka", "xiva", "mini market")
D1.add_M(max1)
print(D1.get_M())

#-----

tiku1 = TIKUVCHI("asal", "otanazarova", "ish boshqaruvchi", "4-yil")

t1 = TIKUVCHILIKSEXI("ASL", "NIyozjon", 89)
t1.add_T(tiku1)
print(t1.get_T())

#------

SH1 = SHAHAR("xorazm", "yaxwi")

v1 = VILOYAT("xorazm", "2-mln", "O`zbekiston")
v1.add_SH(SH1)
print(v1.get_SH())

#-------

F1 =FUTBOLCHI("neymar", 32, "HUjumchi", 565)

fu1 = JAMOA("PSJ", 502, 102)
fu1.add_f(F1)
print(fu1.get_f())

#--------

U1 = USTOZ("Feruzbek", 21, "9-son", "11_b")

m1 = MAKTAB("agohiy", 9, "xiva tumani", 1)

m1.add_m(U1)
print(m1.get_m())


