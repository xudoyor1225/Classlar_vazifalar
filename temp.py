# import math
#x=int(input())
# a,b,c= map(float, input().split(" "))
# print("%.2f" % x)

# x=int(input()) 
# s=x%2
# if s==0:
#     print("second")
# else:
#     print("firdt")
# a,b,c= map(float, input().split(" "))
# if a>0:
#     print(a)
# else:    
#     print(a*a)
# if b>0:
#     print(b)
# else:
#     print(b*b)
# if c>0:
#     print(c)
# else:
#     print(c*c)    
# from math import atanh,exp, cos
# x,y= map(float, input().split(" "))
# s1=x+(2/x*x)+(3/x*x*x)
# s2=exp(x*x+3*x)
# s3=  atanh(x+y)+(5+x)**2
# s4=cos(y**2+x**2/2)*cos(y**2+x**2/2)
# c=((1/s1+s2)/s3)-s4
# print ("%.2f" % c)
# from math import cos, fabs, sqrt, e, log 
# x,y= map(float, input().split(" "))
# s1=(x+y)*(x+y)
# s2=sqrt(fabs(y)+2)
# s3=x-(x*y/((x*x/2)-5))
# s4=cos(x+y)*cos(x+y)
# s5=pow((x+y),1/3)
# c=log((fabs(s1+s2-s3)),e)+s4/s5
# print("%.2f" % c)
# 23)
# from math import fabs,cos
# a,b,c,d, x= map(float, input().split(" "))
# Q=a*pow(x,2)+b*x+c
# W=x*pow(a,3)+pow(a,2)+pow(a,b-c)
# E=a*x+b
# R=c*x+d+pow(2,c)
# T=Q*1./W+cos(fabs(E*1/R))
# print("%.2f" % T)
#33) x,y,z= map(float, input().split(" "))



#35) from math import fabs    
# x,y,z= map(int, input().split(" "))
# if z<=y<=x:
#     print(2*x, 2*y, 2*z)
# elif x>0:
#     print(fabs(x), fabs(y), fabs(z))        
# x,y,z= map(float, input().split(" "))
# if x<y<z<1:
#     print((y+z)/2, y, z)

# if x<z<y<1:
#     print((y+z)/2, y, z)
    
# if y<z<x<1:
#     print(x, (x+z)/2, z)
    
# if y<x<z<1:
#     print(x, (x+z)/2, z)

# if z<x<y<1:
#     print(x, y, (y+x)/2)
    
# if z<y<x<1:
#     print(x, y, (y+x)/2)
 #42
# a,b,c,d= map(float, input().split(" "))
# x=min(a,b,c,d)  
# if a<=b<=c<=d:
#     print(d, d, d, d)
# else:
#     print(x, x, x, x)

# a,b,c= map(int, input().split(" "))
# from math import*
# a=float(input())
# if a<1:
#     print("%.2f" % fabs(a))
# if 1<=a<2:
#     print("%.2f" % 1)
# if 2<=a:
#     print("%.2f" % (-2*a+5))
#from math import fabs

# a=float(input())
# if a<-1:
#     print("%.2f" % (-1/(a*a)))
# if -1<=a<2:
#     print("%.2f" % (a*a))
# if 2<=a:
#     print("%.2f" % a)
# from math import fabs
# a=float(input())
# if a<=1:
#     print("%.2f" % (fabs(a)))
# if 1<=a<=2:
#     print("%.2f" % 1)   
# i

# b,c,d= map(int, input().split(" "))
# s1=round((b+0.2)/2)
# s2=round((c+0.2)/2)
# s3=round((d+0.2)/2)
# print(s1+s2+s3)
# i =11
# s=0
# while i<=99:
#     s+=i
#     i+=2
# print(s)
#========================for bilan ishlash
# s=0 
# for i in range(10,99,2): 
#     s=s+i
# print(s)  
# from math import sin
# n=int(input())
# s=0
# for i in range(1,n+1,1):
#     s+=sin(i)/pow(2,i)
# print("%.2f" % s)
# from math import sin
# n=int(input())      
# i =1
# s=0
# while i<=n:
#     s=s+sin(n)/pow(2,n)
#     i+=1
# print("%.2f" % s )    
#62) from math import sin
# n=int(input())
# s=0
# for i in range(1,n+1,1):
#     s+=(pow(-1,(i-1)))*sin(i**i)/pow(2,i)
# print("%.2f" % s) 
# =========from math import *
# n=int(input())
# s=0
# for i in range(1,n+1,1):
#     x=1
#     for j in range(1,10):
#         x*=(2*j-1)
#     s+=(pow(-1,(i-1)))*1/x
# print("%.2f" % s)   
#64) from math import *
# n,x= map(int, input().split(" "))
# s=0
# for i in range(1,n+1):
#     s+=pow(-1,i-1)*1/pow(x,2*i)
# print("%.3f" % s)
# from math import*
# a,b,c= map(int, input().split(" "))
# # a=int(input())

# # for x in range(1,11,3):
# x=-pi
# s=0   
# while x<=pi :  
#     s+=(log(a**(2*sin(x)))+exp(2*x))/(atan(x)+b)+c
#     x+=pi/10
# print("%.2f" % s)

    
    

# from math import *
# a,b,c,d = map(int, input().split(" "))

# S = 0
# for m in range(1,a+1):
#     S +=(3*m**3+4*m+5)/(m**3+log(m))

# P = 1
# for k in range(1,b+1):
#     P *= k/(k**3+7*k+5)

# SP = 1

# for i in range(1,c+1):
#     T = 1 
#     for m in range(1,d+1):
#         T *=(log(i)+m**i)/(m**i)
#     SP *= T

# print("%.2f" % S,"%.2f" % P,"%.2f" % (SP +1))

# import math
# x, y, c, d = map(int, input().split())
# s = 0
# for i in range(1, x+1):
#     s += (pow(i, 4) + i*i + 3) / math.sqrt(i + math.exp(i))
# p = 0
# for k in range(1, y+1):
#     p += (k+1) / (pow(k, 3) + 5*k)
# sp = 0
# for m in range(1, c+1):
#     p1 = 1
#     for n in range(1, d+1):
#         p1 *= math.sqrt(abs(pow(m, n) - pow(n, m)) / (pow(m, n) + pow(n, m)))
#     sp += p1
# print('{:.2f} {:.2f} {:.2f}'.format(s, p, sp))    





# def sezr_shifrlash(matn, son):

#   shifrlangan_matn = ""
#   for harf in matn:
#     if harf.isalpha():
#       yangi_kod = ord(harf) + son
#       if yangi_kod > ord("Z"):
#         yangi_kod -= 26
#       shifrlangan_matn += chr(yangi_kod)
#     else:
#       shifrlangan_matn += harf
#   return shifrlangan_matn
# x=str(input())
# k=int(input())
# #X= kiritiladigan so'z k=kalit shifrlash uchun
# print(sezr_shifrlash(x, k))


# def gammalash(soz, kalit):
#   kalit = kalit.upper()
#   natija = ""
#   index = 0
#   for harf in soz:
    
#     if harf.isalpha():
#       harf = harf.upper()

#       almashtirilgan = chr((ord(harf) - 65 + ord(kalit[index])-65) % 25 + 65)
      
#       natija += almashtirilgan
      
#       index += 1
      
#       if index >= len(kalit):
#         index = 0
#     else:
#       natija += harf
#   return natija
# soz = str(input())
# kalit = str(input())
# print("Javob: ")
# print(gammalash(soz, kalit))
# from math import*
# x,y,c,d=map(int, input().split(" "))
# s=0
# for a in range(1,x+1):
#     s+=(a*a+2*a)/(a**3+a*cos(a)**2+1)
# p=1
# for i in range(1,y+1):
#     p*=(i*i+1)/(pow(i,3/i)+2)
# sp=0
# for j in range(1,c+1):
#     p1=0
#     for k in range(1, d+1):
#         p1*=log((pow(k,j)+pow(k,1/j))/(pow(k,3)+pow(j,1/k)))
#     sp+=p1
# print("%.2f" % s, "%.2f" % p, "%.2f" % sp)    
        
    
    
    
    #Bugungi darsda #mavzu_5

# #1.massiv qiymatlarini consoldan o'qish
# m = list(map(int, input().split()))

# #2.oxiriga element qo'shish
# m.append(15) 

# #3.biror indeksiga element qo'shish, 2 chi indeksiga 50 qiymatini kiritadi
# m.insert(2, 50)

# #4.indeksi bo'yicha o'chirish
# m.pop(2) 

# #5.indeksi bo'yicha o'chirish
# del m[3] 

# #6.massivni qiymati bo'yicha birinchi topgan elementni o'chiradi
# m.remove(23)

# #7.berilgan qiymatli elementni indeksini topadi
# b = m.index(21) 

# #8.kichikdan kattaga qarab tartiblaydi
# m.sort() 

# #9.eng kattasini aniqlash
# maxx = max(m) 

# #10.eng kichigini aniqlash
# minn = min(m) 

# #11.massiv yig'indisini aniqlash
# yigindi = sum(m)

# #12. massiv uzunligini aniqlash
# uzunligi = len(m) 

# #13.massivni 2-indeksidan 6-indeksigacha bo'lgan qiymatlarni olish
# b = m[2:6]

# #14.massivni 3-indeksidan oxirigacha qiymatlarni olish
# b = m[3:]

# #15.massivni boshidan 6-indeksigacha bo'lgan qiymatlarni olish
# b = m[:6]

# #16.massivni 3-indeksidan oxirgi qiymatigacha olish
# b = m[3:-1]
    
    
#1 n = int(input())
# a = list(map(int, input().split()))
# z,x=map(int, input().split())
# minn=min(a)

# for i in range(0,n):
#     if a[i]==0:
#         print(a[i])
#     elif a[i]/minn==1:
#         print(float(minn), end=" ")
    
#     else:    
        
#         s= a[i]/minn

#         print(f"{s+0.01:.1f}", end=" ")   
# 105) n=int(input())
# a = list(map(int, input().split()))
# k,l=map(int, input().split())
# x=sum(a)
# s=0

# for i in range(k-1,l):
#     s+=a[i]
# print("%.2f" % ((x-s)/(n-l-k+1)))

 

     
    

#124) from math import log    
# n=int(input())
# a = list(map(int, input().split()))
# k=int(input())
# m=max(a)
# z=a.index(m)
# for i in range(0,n) :
#     a[z]=a[k-1]
# for j in range(0,n):
#     a[k-1]=m  
# print(*a)
    

#116) n=int(input())
# a = list(map(int, input().split()))

# s=0
# m=max(a)
# for i in range(0,n) :
#     if a[i]==0:
#         print("%.2f" % a[i], end=" ")
#     else:
#         s=a[i]/m
       
#         print("%.2f" % s, end=" ")



# n=int(input())
# a = list(map(int, input().split()))
# x=0
# s=0
# for i in range(0,n):
#     if a[i]%2==1:
#         s+=a[i]
#         x+=1
# print("%.2f" % (s/x+0.0001))   
  
# n=int(input())
# a = list(map(int, input().split()))

# if a==sorted(a):
#     print("YES")
# else:
#     print("NO")
# x,y = map(int, input().split())
# a = list(map(int, input().split()))
# s=0
# for i in range(0,y):
#     if s+=a[i]:
    

  
# n=int(input())
# a = list(map(int, input().split()))
# k=int(input())
# m=max(a)
# z=a.index(m)
# for i in range(0,n) :
#     a[z]=a[k-1]
# for j in range(0,n):
#     a[k-1]=m  
# print(*a)  
    
 #---------------------------------------   
# from random import randint

# ball = 0
# a = randint(1, 10)
# while True:
    
    
#     print(" men o'ylagan son=",end=" ")
#     n = int(input())
    
#     if n != a:
#         ball +=1
#         print("yoq bu son emas")
#         continue
#     else:
#         ball+=1
#         print("siz yuttingiz")
#         break

# print(f"siz {ball} ta urinishda men o'ylagan sonni topdingiz")
#---------------------------------------    
# from math import *   
# x,n= map(int, input().split())
# #x=int(input())
# s=0
# for i in range(1,n+1):
#     s+=pow(x+1,1/i)

# print("%.2f" % s)
   
 
    
 
# alifbo = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","/","@","!","#","$","%","^","*","&"]
# z = list(map(str,input('Harflarni kriting: ').split()))
# e=int(input("e ni kirit= "))
# n=int(input("n ni kirit="))
# a = list(map(int, input().split()))
# for i in range(len(a)):
#     s1=(a[i]**e)%n
#     print(f"shifr raqam: {s1},alibo harfi: {alifbo[s1-1]}")

# for i in z:  
#     b=alifbo.index(i.upper()) 
#     print(b)   
#======== max va minni o'rnini almawtiruvchi dastur======== 
# from math import *
# #n=int(input())
# a=list (map(float, input().split()))
# maxx=max(a)
# minn=min(a)
# b=a.index(maxx)
# z=a.index(minn)
# for i in range(len(a)):
#     a[b]=minn
#     a[z]=maxx
        
# print(*a)
 
# from math import *

# r,h= map(int, input().split())

# v=pi*r*r*h
# print("%.2f" % v)




# from math import *
# x,y,c,d = map(int, input().split(" "))

# S = 0
# for i in range(1,x+1):
#     S +=sqrt(c*i+d)

# P = 1
# for k in range(1,y+1):
#     P *= (sin(c+d)+3*c)/(cos(c*k)+2.78*d)

# SP = 0

# for z in range(1,c+1):
#     T = 1 
#     for j in range(1,d+1):
#         T *=(c*x**j+z*j)/(d*z+c*j)
#     SP += T

# print("%.2f" % S,"%.2f" % P,"%.2f" % (SP))



# a=list(map(str, input().split()))

        
# print(z)
#---------------------------------------------        

# son,son2 = map(str, input().split())

# d1 = {
#             'A':'1',
#             'B':'2',
#             'C':'3',
#             'D':'4',
#             'E':'5',
#             'F':'6',
#             'G':'7',
#             'H':'8',
#             'I':'9',
#             'J':'10',
#             'K':'11',
#             'L':'12',
#             'M':'13',
#             'N':'14',
#             'O':'15',
#             'P':'16',
#             'Q':'17',
#             'R':'18',
#             'S':'19',
#             'T':'20',
#             'U':'21',
#             'V':'22',
#             'W':'23',
#             'X':'24',
#             'Y':'25',
#             'Z':'26',
# }



# a2 = d1.get(son2, "")
# a1 = d1.get(son, "")
# s=int(a1)+int(a2)

# print(s)





#==================SATRLAR==========================


#06.12.2023 Bugungi darsda

# # satrli o`zgaruvchilarga qiymat berish
# a = 'bittalik qo`shtirnoq'
# a2 = "ikkitalik qo`shtirnoq"
# a3 = """3 ta ikkitalik 
# qo`shtirnoq, bunda qiymatni
# ko`p qatorli qilib 
# kiritish ham mumkin"""

# # consoldan o`qish
# b1 = input()
# b2 = str(input())

# # satrni har bir so'zini list qilib o'qish
# c1 = list(input().split())

# # satrni har bir abzastini list qilib o'qish
# c2 = list(a.split("\n"))

# # a satr uzunligini aniqlash
# l = len(a) 

# # a satrni katta harflarga o'tkazish
# b1 = a.upper()

# # a satrni kichik harflarga o'tkazish
# b2 = a.lower()

# # har bir so'zni bosh harfini kattaga o'tkazish
# b3 = a.title()

# # a satrdan bitta belgini olish
# b1 = a[3] 

# # a satrdan [1,4) oraliq indeksidagi belgilarini qirqib olish
# b2 = a[1:4]

# # a satrdan [0,8) oraliq indeksidagi belgilarini qirqib olish
# b3 = a[:8]

# # a satrdan 3-indeksdan oxirigacha qirqib olish
# b4 = a[3:]

# # a satrdan [0,-3) oraliq ya'ni oxiridan 3 oldingi belgisigacha qirqib olish
# b5 = a[:-3]

# # a satrni teskari tartibda ifodalash
# b6 = a[::-1]

# # a satrdan 5 marta takroran yozish
# b7 = a*5

# # a satrdagi tan yozuvi qatnashganlarni tojikiston yozuviga almashtirish
# b8 = a.replace("tan","tojikiston")

# # ASCII kodlash jadvalidan belgining kodini olish
# c1 = ord("A")    # javobi 65

# # ASCII kodlash jadvalidan kodning belgisini olish
# c2 = chr(65)     # javobi A

# #algo 148-masala
# a = list(input().split())

# #1-usul
# for i in a:
#     if i[0] == "A":
#         print(i)

# #2-usul
# for i in range(len(a)):
#     if a[i][0] == "A":
#         print(a[i])
#====================================================================


# a = list(input().split())

# z=[]
# for i in a:
#     if i[:4]=="info" or i[:4]=="Info":
        
#         z.append(i)

# print(*z)
      



# 132)
# z = int(input())
# a = list(map(int, input().split()))
# n, m = map(int, input().split())

# for i in range(0, n * m - z):
#     a.append(0)

# # Reshaping the list into a matrix
# v = []
# index = 0
# for i in range(n):
#     r = []
#     for j in range(m):
#         r.append(a[index])
#         index += 1
#     v.append(r)
# for j in v:
#     print(*j)
#-----------------------
#137)
# for i in range(n):
#     a.append(list(map(int,input().split())))
# s=0
# l=0
# z=int(input())
# for i in range(len(a)):
#     for j in range(0,n):
#         if a[i][j]%z==0:
#             l+=a[i][j]
#             s+=1
# print("%.2f" % (l/s))




# algo 130-masala:
# algo 130-masala:
# n, m = map(int, input().split())
# a,b=[],[]
# for i in range(n):
#     a.append(list(map(int,input().split())))
#     b.append(i[0])
# c=list(map(int,input().split()))
# b.append(c[0])

# print(b)


# a,b=[],[]
# n=int(input())
# for i in range(n):
#     a.append(list(map(int,input().split())))
# m=int(input())
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         if a[i][j]%m==0:
#            b.append(a[i][j])
# print(f"{(sum(b)/len(b)):.2f}")

#153) a = list(input().split())
# b=[]
# for i in a:
#     print(i,len(i))

#154) a =input()
# b=0
# for i in a:
#     b+=int(i)
# print(b)
        
#155) a =list(input().split())
# b=0
# for i in a:
#     if ord(i[0])<=90:
#         b+=1
# print(b)     

#156) a =list(input().split())
# n,m=map(int, input().split())
# x=a[m-1]

# for i in range(len(a)):
#     a[m-1]=a[n-1]
# a[n-1]=x    
# print(*a)   
     
#159) a =list(input().split())

# z=0
# for i in a:
#     if i[(len(i)-1)]=="b" and i[1]=="a":
#         z+=1
# print(z)

#160) a =input()

# z=0
# for i in a:
    
#     if ord(i)>=65 and ord(i)<90:
#         i=chr(ord(i)+32)
#     elif ord(i)>=97 and ord(i)<=122:    
#         i=chr(ord(i)-32)   
#     print(i, end="")
    
#161) n=int(input())
# a =input().split()

# z=0
# s=0
# b=0
# w=0
# r=0
# for i in a:
#     if ord(i)==65:
#         z+=1
#     elif ord(i)==83:    
#         s+=1
#     elif ord(i)==76:
#         b+=1
#     elif ord(i)==79:
#         w+=1
#     elif ord(i)==77:
#         r+=1
        
# if z>=2 and s>=2 and b>=1 and w>=1 and r>=1:
#     print("YES")
# else:
#     print("NO")
  
#162) n=int(input())
# a =input()
# a=a.replace("$","")

# print(a)
    

#163) a =input().split()
# b=[]
# for i in a:
#     b.append(len(i))
# m=max(b)
# z=b.index(m)
# print(a[z])
#//////////////////////////////////
# a =input()
# l,r=map(int, input().split())
# if l>r:
#     print(a[l::-r])
# else:
#     print(a[(l-1):r])
#////////////////////////////




#algo 130-masala
# n, m = map(int, input().split())
# b = []

# v = []
# max_v = []
# min_v = []

# for i in range(0,n):  
#     a = list(map(int, input().split()))
    
#     max_v.append(max(a))
#     min_v.append(min(a))
#     b.append(a)
    
# l=max(max_v)
# k=min(min_v)
# print(l+k)

# 346 matritsa
# 347 matritsa




# 353)a,b,c=map(int, input().split())
# if a*a+b*b>c*c and a*a+c*c>b*b and b*b+c*c>a*a:
#     print("2",end=" ")
# elif a*a+b*b==c*c and a*a+c*c==b*b and b*b+c*c==a*a:
#     print("1", end=" ")
# else:
#     print("3", end=" ")
# if a!=b!=c:
#     print("three")
# elif a==b==c:
#     print("one")
# else:
#     print("two")






#421) a="algo"
# s=input().lower()

# if a in s:
#     print("Yes") 
# else:
#     print("No")
        
# print(sum(map(int, input().strip())))

# 1) a=input()
# n=int(input())
# v=[]
# s=""
# for i in a:
#     v.append(i)
# del v[n-1]
# for i in v:
#     s+=i
# print(s)
    

# a=input()
# i=0
# while i<=len(a)/2:

#     if a[i]==a[len(a)-1-i]:
#         print("p")
#         break
#     else:
#         print("pm")
#         break




# from math import *
# n,m=map (int, input().split())
# for i in range(n,m+1):
#     z=factorial(i)

# x=str(z)[::-1]
# s=0
# for i in x:
#     if i=="0":
#         s+=1
#     elif i!="0":
#         break
# print(s)







# a=input()
# m=len(a)
# v=[]
# r=""
# for i in a:
#     v.append(i)
# z=v[0]
# v[0]=v[m-1]
# v[m-1]=z
# for i in v:
#     r+=i
# print(r)
    


# a=input()
# b=input()
# r=""
# m=a[:2]
# n=b[:2]
# m1=a[2:]
# n1=b[2:]
# print((n+m1), (m+n1))


#165) from math import fabs, sin
# t, s = map(float, input().split())

# def f(a,b,c):
#     natija = (2*a-b-sin(c))/(5+fabs(c))
#     return natija

# javob = f(t,-2*s,1.17)+f(2.2,t,s-t)
# print(f"{javob:.2f}")



#169) a,b=map(float, input().split())
# v=[]
# def f(a,b):
#     u=min(a,b)
#     v=min(a*b,max(a,b))
#     s=min(u+v,3.14)
#     return u,v,s


# javob = f(a,b)
# print(*javob)



# 369) def sanoq_sistemasiga_otkazish(n, m):
#     result = ''
#     if n == 0:
#         result = '0'
#     while n > 0:
#         bit = str(n % m)
#         result = bit + result
#         n = n // m
#     return result

# n, m = map(int, input().split())
# result = sanoq_sistemasiga_otkazish(n, m)

# # print(result)
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if n==(2*i+j-1)*j/2:
           
#             print(i ,j)




# 1 chi masala ========================
# a=input()
# z=a[3:5]
# print(f"{z}-oy")


#2-masala ============================

# a=input()
# z=a[4:6]
# print(f"{z}")

#3-masala ============================


# a=input()
# z=a[-2:]
# if z=="va":
#     print("ayol")
# else:
    
#     print("erkak")

#4-masala ============================

# s=input()
# z=s.lower()

# d1 = {
        
#       'yanvar':31,
#       'fevral':"28 yoki 29",
#       'mart':31,
#       'aprel':30,
#       'may':31,
#       'iyun':30,
#       'iyul':31,
#       'avgust':31,
#       'sentabr':30,
#       'oktabr':31,
#       'noyabr':30,
#       'dekabr':31
#      }
       
# print(f"{d1[z]} kun bor" )



#5-masala ============================



# a=input()

# z=a[:4]
# v=a[4:]
# if z=="+998" and len(v)==9:
#     print("yaroqli")
# else:
#     print("yaroqsiz")






#406) a=list(input().lower().split())
# z=input()
# s=0
# for i in a:
#     if i[0]==z:
#         print(i, end=" ")
        

       
#407) a=list(input().split()) 
# r=""
# for i in a:
#     if len(i)%2==1:
#         v=len(i)//2+1
       
#         for j in range(len(i)):
#             if j!=v-1:
#                 r+=i[j]
#         print(r, end=" ")
#     else:
#         print(i, end=" ")

# n=int(input())
# a=list(map(int, input().split()))
# z=sum(a)
# s=0
# l=n/2
# i=0
# while i<n/2:
#     s+=a[i]
#     i+=1
# if n%2==1:
#     v=2*s-z-a[int(l)]
    
#     print(v)
# else:
#     print(2*s-z)
     
#413) n=int(input())
# a=list(map(int, input().split()))

# x=sorted(a)


# print(*sorted(a))
 
# print(*x[::-1])   

#423) n=int(input())
# a=list(map(int, input().split()))

# for i in a:
#     if i<0:
#         i*-1
# a.sort()
# print(a[n-1]*a[n-2]*a[n-3])



#433) a=list(map(str, input().split()))

# d1 = {
#             'cin':'kiritish operatori',
#             'cout':'chiqarish operatori',
#             'for':'sikl operatori',
#             'if':'shart operatori',
#             '{':'boshlash',
#             '}':'tugash',
#             'int':'butun tip',
#             'double':'haqiqiy tip',
        
# }

# print(a)

# 439) a=input()
# s=0
# for i in range(0,len(a),2):
#     if ord(a[i])>=48 and ord(a[i])<=57:
#         s+=2
        
# if s-1==len(a) :
#     print("Yes")
# else:
#     print("No")    


















# class user:
#     def __init__(self,ism, ismf,email):
#         self.ism=ism
#         self.ismf=ismf
#         self.email=email
#     def get_info(self):
#         return f"Foydalanuvchi:{self.ismf} ismi: {self.ism} email: {self.email}"
#     def set_email(self, x):
#         self.email=x
        
# user1=user("shohruh", "shoh", "sho553@gmail.com")
# print(user1.get_info())
# user1.set_email("shohjadbadov")
# print(user1.get_info())

# a=[]
# i=0
# while True:
#     a.append (list(map(str, input().split())))
#     if len(a)==0:
#         break
        
    
# print(a)


# #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# #=====================================            
# class ishchi:
#     def __init__(self,ism, f_raqam, staji ):
#         self.ism=ism
#         self.f_raqam=f_raqam
#         self.staji=staji
#     def get_info(self):
#         return f"Foydalanuvchi:{self.ism} ishlash joyi: {self.f_raqam} staji: {self.staji}"
#     def update_staji(self,x):
#         self.staji=x
        
# ishchi1=ishchi("shohruh", 112, "2 yil")
# print(ishchi1.get_info())
# ishchi1.update_staji("4 yi 5 oy")
# print(ishchi1.get_info())
 

# #===============================================

# class jurnal:
#     def __init__(self,nomi, davr, korinishi, nashr):
#         self.nomi=nomi
#         self.davr=davr
#         self.korinishi=korinishi
#         self.nashr=nashr
#     def get_info(self):
#         return f"Jurnal nomi: {self.nomi} chiqish vaqti: {self.davr} muqovasi: {self.korinishi} Tashkilot: {self.nashr}"
#     def set_staji(self,x):
#         self.nomi=x
        
# J1=jurnal("shifo info", "har hafta", "rangli", "fotima MCHJ")
# print(J1.get_info())
# J1.set_staji("4 yi 5 oy")
# print(J1.get_info())
 

# #=================================================



# class MAXSULOT:
#     def __init__(self,ism, narxi, country):
#         self.ism=ism
#         self.soni=0
#         self.narxi=narxi
#         self.country=country
#     def get_info(self):
#         return f"Maxsulot nomi: {self.ism} Maxsulot soni: {self.soni} Maxsulot narxi: {self.narxi} Ishlab chiqarilgan yeri: {self.country}"
#     def set_staji(self,x):
#         self.narxi=x
#     def update_f(self,x):
#         self.narxi=self.narxi+self.narxi*x/100
    
        
# M1=MAXSULOT("hp", 7500000, "USA")
# print(M1.get_info())
# M1.set_staji(6500000)
# print(M1.get_info())
# M1.update_f(20)
# print(M1.get_info())
# #==========================================================================================

    
# class KVITANSIYA:
#     def __init__(self,raqami, sana, pulM, manzili):
#         self.raqami=raqami
#         self.sana=sana
#         self.pulM=pulM
#         self.manzili=manzili
#     def get_info(self):
#         return f"Narxi: {self.raqami} SANA: {self.sana} Pul: {self.pulM} manzili: {self.manzili}"
#     def set_manzili(self,x):
#         self.manzili=x



# #============================================================


# class TIKUVCHILIKSEXI:
#     def __init__(self,ismi, boshliq, ishchi_s, zavod):
#         self.ismi=ismi
#         self.boshliq=boshliq
#         self.ishchi_s=ishchi_s
#         self.zavod=zavod
#     def get_info(self):
#         return f"Ismi: {self.ismi} BOSHLIQ: {self.boshliq} I_soni: {self.ishchi_s} ZAVOD: {self.zavod}"
#     def set_ishchi_soni(self,x):
#         self.ishchi_s=x
        
# #=============================================================



# class SHAXS:
#     def __init__(self,ismi, yoshi, jinsi, millati):
#         self.ismi=ismi
#         self.yoshi=yoshi
#         self.jinsi=jinsi
#         self.millati=millati
#     def get_info(self):
#         return f"Ismi: {self.ismi} YOSH: {self.yoshi} JINSI: {self.jinsi} millati: {self.millati}"
#     def set_millati(self,x):
#         self.millati=x
        
# #==============================================================

# class KORABL:
#     def __init__(self,ismi, suvsiljishi, turi, yoshi):
#         self.ismi=ismi
#         self.suvsiljishi=suvsiljishi
#         self.turi=turi
#         self.yoshi=yoshi
#     def get_info(self):
#         return f"Ismi: {self.ismi} Siljish: {self.suvsiljishi} Turi: {self.turi} Yoshi: {self.yoshi}"
#     def set_turi(self,x):
#         self.turi=x    

# #===============================================================

# class SHAXAR:
#     def __init__(self,nomi, respublikasi, tumani, xuquqiy_x):
#         self.nomi=nomi
#         self.respublikasi=respublikasi
#         self.tumani=tumani
#         self.xuquqiy_x=xuquqiy_x
#     def get_info(self):
#         return f"Nomi: {self.nomi} Respublikasi: {self.respublikasi} Tumani: {self.tumani} Xuquqqiy_x: {self.xuquqiy_x}"
#     def set_nomi(self,x):
#         self.nomi=x  
        
# #===============================================================



# class TASVIR:
#     def __init__(self,nomi, tasvirchi, yili, galeriya):
#         self.nomi=nomi
#         self.tasvirchi=tasvirchi
#         self.yili=yili
#         self.galeriya=galeriya
#     def get_info(self):
#         return f"Nomi: {self.nomi} Tasvirchi: {self.tasvirchi} Yili: {self.yili} Galeriya: {self.galeriya}"
#     def set_yili(self,x):
#         self.yili=x  


# #==========================================================



# class IJARACHI:
#     def __init__(self,ismi, mamlakati, yoshi , sayoxat_m):
#         self.ismi=ismi
#         self.mamlakati=mamlakati
#         self.yoshi=yoshi
#         self.sayohat_m=sayoxat_m
#     def get_info(self):
#         return f"Ismi: {self.ismi} Mamlakati: {self.mamlakati} Yoshi: {self.yoshi } Sayohat_m: {self.sayoxat_m}"
#     def set_yoshi(self,x):
#         self.yoshi=x  
# #=====================================================




# class TELEFON:
#     def __init__(self,ismi, raqami, manzili, turi):
#         self.ismi=ismi
#         self.raqami=raqami
#         self.manzili=manzili
#         self.turi=turi
#     def get_info(self):
#         return f"Ismi: {self.ismi} raqami: {self.raqami} manzili: {self.manzili } Turi: {self.turi}"
#     def set_raqami(self,x):
#         self.raqami=x  
        
        
# #======================================================


# class FUTBOLCHI:
#     def __init__(self,ismi, yoshi, kim_b,gollar_s ):
#         self.ismi=ismi
#         self.yoshi=yoshi
#         self.kim_b=kim_b
#         self.gollar_s=gollar_s
#     def get_info(self):
#         return f"Ismi: {self.ismi} yoshi: {self.yoshi} KIm bo'lib o`ynaydi: {self.kim_b } SONI: {self.gollar_s}"
#     def set_gollar_s(self,x):
#         self.gollar_s=x  
        
# #========================================================

# class DISK:
#     def __init__(self,nomi, xajmi, narxi,mamlakati ):
#         self.nomi=nomi
#         self.xajmi=xajmi
#         self.narxi=narxi
#         self.mamalakati=mamlakati
#     def get_info(self):
#         return f"Nomi: {self.nomi} XAJMI: {self.xajmi} Narxi: {self.narxi } MAMLAKATI: {self.mamlakati}"
#     def set_narxi(self,x):
#         self.narxi=self.narxi+(self.narxi*x)/100
        
# #===========================================================

# class USTOZ:
#     def __init__(self,ismi, yoshi, maktab, sinf):
#         self.ismi=ismi
#         self.yoshi=yoshi
#         self.maktab=maktab
#         self.sinf=sinf
#     def get_info(self):
#         return f"Ismi: {self.ismi} yoshi: {self.yoshi} MAKTAB: {self.maktab } SINF: {self.sinf}"
#     def set_sinf(self,x):
#         self.sinf=x  
        
# #==========================================================


# class FAN:
#     def __init__(self,nomi, soati, kursi,turi ):
#         self.nomi=nomi
#         self.soati=soati
#         self.kursi=kursi
#         self.turi=turi
#     def get_info(self):
#         return f"Nomi: {self.nomi} SOAT XAJMI: {self.soati} KURSI: {self.kursi } Turi: {self.turi}"
#     def set_kursi(self,x):
#         self.kursi=x
        

# #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    




# class AVTO:
#     def __init__(self, madel, rangi, karobka, narxi):
#         self.madel = madel
#         self.rangi = rangi
#         self.karobka = karobka
#         self.narxi = narxi
#         self.km = 0
    
#     def get_info(self):
#         full = f"nomi: {self.madel} "
#         full += f"rangi: {self.rangi} "
#         full += f"karobka: {self.karobka}"
#         full += f"narxi: {self.narxi} "
                
#         return full
    
#     def update_km(self, qiymat):
#         self.km = self.km + qiymat
    
#     def __repr__(self):
#         full = f"nomi: {self.madel } "
#         full += f"rangi: {self.rangi } "
#         full += f"karobka: {self.karobka }"
#         full += f"narxi: {self.narxi } "
#         full += f"KM: {self.km } "
#         return full


# class AVTOSALON:
#     def __init__(self, salonnomi, manzili):
#         self.salonnomi = salonnomi
#         self.manzili = manzili
#         self.cars = [] 
#     def add_cars(self, c):
#         self.cars.append(c)
    
#     def get_cars(self):
#         return self.cars
            
         
# car1 = AVTO("Nexia 3", "qora", "avtamat", "13000$")
# car2 = AVTO("Malibu", "oq", "avtamat", "33000$")


# obj1 = AVTOSALON("KIA", "Toshkent")
# obj1.add_cars(car1)
# obj1.add_cars(car2)
# print(obj1.get_cars())


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# class ISHCHI:
#     def __init__(self, ismi, g_raqami, staji):
#         self.ismi = ismi
#         self.g_raqami = g_raqami
#         self.staji = staji

#     def get_info(self):
#         full = f"ISMI: {self.ismi} "
#         full += f"RAQAMI: {self.g_raqami} "
#         full += f"STAJI: {self.staji}"
        
#         return full

#     def __repr__(self):
#         full = f"ISMI: {self.ismi} "
#         full += f"RAQAMI: {self.g_raqami} "
#         full += f"STAJI: {self.staji}"
 
#         return full


# class KORXONA:
#     def __init__(self, nomi, firma_r, manzili):
#         self.nomi = nomi
#         self.firma_r=firma_r
#         self.manzili = manzili
#         self.ishchilar = [] 
#     def add_w(self, c):
#         self.ishchilar.append(c)
    
#     def get_w(self):
#         return self.ishchilar
            
         
# obj1 = ISHCHI("nodir", 15, "5-yil")

# K1 = KORXONA("COCE", 225, "toshkent")
# K1.add_w(obj1)
# print(K1.get_w())

# #===========================================================

# class MAXSULOT:
#     def __init__(self, nomi, narxi, mamlakati):
#         self.nomi = nomi
#         self.soni= 0
#         self.narxi= narxi
#         self.mamlakati= mamlakati
        

#     def get_info(self):
#         full = f"ISMI: {self.nomi} "
#         full += f"NARXI: {self.narxi} "
#         full += f"MAMLAKATI: {self.mamlakati}"
        
#         return full

#     def __repr__(self):
#         full = f"ISMI: {self.nomi} "
#         full += f"NARXI: {self.narxi} "
#         full += f"MAMLAKATI: {self.mamlakati}"


#         return full


# class DUKON:
#     def __init__(self, nomi, manzili, turi):
#         self.nomi = nomi
#         self.manzili = manzili
#         self.turi=turi
#         self.maxsulot = [] 
#     def add_M(self, c):
#         self.maxsulot.append(c)
    
#     def get_M(self):
#         return self.maxsulot
            
         
# max1 = MAXSULOT("cola", 13000, "amerika")

# D1 = DUKON("baraka", "xiva", "mini market")
# D1.add_M(max1)
# print(D1.get_M())

# #==============================================================


# class TIKUVCHI:
#     def __init__(self, ismi, fam, lavozim,staji):
#         self.ismi = ismi
#         self.fam= fam
#         self.lavozim= lavozim
#         self.staji=staji
        

#     def get_info(self):
#         full = f"ISMI: {self.ismi} "
#         full += f"LAVOZIMI: {self.lavozim} "
#         full += f"familiyasi: {self.fam}"
#         full += f"staji: {self.staji}"
#         return full

#     def __repr__(self):
#         full = f"ISMI: {self.ismi} "
#         full += f"LAVOZIMI: {self.lavozim} "
#         full += f"familiyasi: {self.fam}"
#         full += f"staji: {self.staji}"
       
#         return full


# class TIKUVCHILIKSEXI:
#     def __init__(self, nomi, boshliq, i_soni):
#         self.nomi = nomi
#         self.boshliq = boshliq
#         self.i_soni=i_soni
#         self.tikuvchilar = [] 
#     def add_T(self, c):
#         self.tikuvchilar.append(c)
    
#     def get_T(self):
#         return self.tikuvchilar
            
         
# tiku1 = TIKUVCHI("asal", "otanazarova", "ish boshqaruvchi", "4-yil")

# t1 = TIKUVCHILIKSEXI("ASL", "NIyozjon", 25)
# t1.add_T(tiku1)
# print(t1.get_T())

# #=================================================================


# class SHAHAR:
#     def __init__(self, sh_nomi, xuquqiy_x):
#         self.sh_nomi = sh_nomi
#         self.xuquqiy_x=xuquqiy_x
       
        

#     def get_info(self):
#         full = f"SHAHAR NOMI: {self.sh_nomi} "
#         full += f"XUQUQIY XOLATI: {self.xuquqiy_x} "
       
#         return full

#     def __repr__(self):
#         full = f"SHAHAR NOMI: {self.sh_nomi} "
#         full += f"XUQUQIY XOLATI: {self.xuquqiy_x} "
       
#         return full


# class VILOYAT:
#     def __init__(self, nomi, yermaydoni_a, respublikasi):
#         self.nomi = nomi
#         self.yermaydoni_a = yermaydoni_a
#         self.respublikasi=respublikasi
#         self.shaharlari = [] 
#     def add_SH(self, c):
#         self.shaharlari.append(c)
    
#     def get_SH(self):
#         return self.shaharlari
            
         
# SH1 = SHAHAR("xorazm", "yaxwi")

# v1 = VILOYAT("xorazm", "2-mln", "O`zbekiston")
# v1.add_SH(SH1)
# print(v1.get_SH())

#=====================================================================










# class Talaba:
#     number = 0
#     myid=0
#     def __init__(self, ism, familiya, t_sanasi ):
        
#         self.ism = ism
#         self.familiya = familiya
#         self.t_sanasi = t_sanasi
        
#         Talaba.myid += 1
#         Talaba.number += 1
    
#     def get_info(self):
#         return f"{self.ism} {self.familiya} {self.t_sanasi} {self.myid}"
    
#     def set_t_sanasi(self,new_sana):
#         self.t_sanasi = new_sana
    
#     def __repr__(self):
#         return self.ism
    
        
        
        
    
    
# a = Talaba("Alisher", "Botirov", "2001-10-15")
# b = Talaba("Sanjar", "To'rayev", "2002-08-21")

# class Fan:
#     def __init__(self, nomi,soati):
#         self.nomi = nomi
#         self.soati=soati
#         self.fanlarim = []
    
#     def get_info(self):
#         return f"{self.nomi} {self.soati}"
    
#     def add_yozil(self,f):
#         self.fanlarim.append(f)
    
#     def remove_fan(self,obj):
#         if obj in self.fanlarim:
#             self.fanlarim.remove(obj)
#         else:
#             return f"siz bu fanga yozilmagansiz"
        
    
#     def show_myf(self):
#         return self.fanlarim

# f1 = Fan ("MTA", "180-soat")
# f1.add_yozil(a)
# f1.add_yozil(b)

# print(f1.show_myf())
















# class SHAXS:
#     def __init__(self,ismi, yoshi, jinsi, millati):
#         self.ismi=ismi
#         self.yoshi=yoshi
#         self.jinsi=jinsi
#         self.millati=millati
#     def get_info(self):
#         return f"Ismi: {self.ismi} YOSH: {self.yoshi} JINSI: {self.jinsi} millati: {self.millati}"
#     def set_millati(self,x):
#         self.millati=x
        

# class MIJOZ(SHAXS):
#     pass
# m1=MIJOZ("vali", 25, "erkek", "millati")


# class SOTUVCHI(SHAXS):
#     def __init__(self,ismi, yoshi, jinsi ,millati, staji):
#         super().__init__(ismi, yoshi, jinsi, millati )
#         self.staji=staji
        
#         def get_info(self):
#             full=super()>get_info()
#             full+=self.staji



#             return full
    

# s1= SOTUVCHI("navruz", 25, "erakak", "o'zbek", "4-yil")

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\%%%%

# class TALABA:
#     number=0
#     def __init__(self,ismi, fam, guruh, shartnoma, bosqich=1,):
#         self.ismi=ismi
#         self.fam=fam
#         self.guruh=guruh
#         self.shartnoma=shartnoma
#         TALABA.number += 1
#         self.__id=TALABA.number
        
#     def get_id(self):
#         return self.__id
#     def set_id(self,x):
#         self.__id=x
    
        
#     def show(self):
#         return f"Ismi: {self.ismi} FAMILIYASI: {self.fam} GURUH: {self.guruh} SHARTNOMA: {self.shartnoma}"
#     @classmethod
#     def obyektlar_soni(cls):
#         return cls.number
        





# class SHAXS:
#     def __init__(self,ismi, fam, ishjoyi, millati, jshshir, passport="AC3135942"):
#         self.ismi=ismi
#         self.fam=fam
#         self.ishjoyi=ishjoyi
#         self.millati=millati
#         self.__passport=passport
#         self.__jshshir=jshshir
        
        
#     def get_info(self):
        
#         return self.__passport, self.__jshshir
    
#     def get_stir(self, z, c):
#         self.__pasport=z
#         self.__jshshir=c
                    
        
#     def show_w(self):
#         return f"Ismi: {self.ismi} FAMILIYASI: {self.fam} ISH JOYI: {self.ishjoyi} MILLATI: {self.millati}"

        

# t1=TALABA("xudoyor", "shonazarov", "942-22", "grant")
# t2=TALABA("vali", "najimov", "942-11", "tolov kantirakti")
# sh1=SHAXS("ulugbek", "abdullayev", "turon bank", "o'zbek", 123456789123456)


# print(t1.get_id())
# print(t2.show())
# print(t1.obyektlar_soni())


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


























