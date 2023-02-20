# 16.01.2023
# Muallif : Nurullo Obloqulov

"""
Robocontest Round #74
"""

# a=str(input())
# s=0
# for i in range(len(a)):
#     if a[i]=='1':
#         s+=1

# if s%2==1:
#     print("YES")
# else:
#     print("NO")

# s=str(input())
# t=int(input())
# for i in range(t):
#     l,r = map(int,input().split(" ")) ; n=0 ; m=0
#     for w in range(l-1,r):
#         if s[w].isupper():
#             n+=1
#         else:
#             m+=1
#     if n>m:
#         print("Katta harflar")
#     elif n==m:
#         print('Teng')
#     else:
#         print("Kichik harflar")

# print(map(int,input().split()))


"""
Masalalar
"""

# Floyd uchburchagi

# n=int(input())
# s=0
# for i in range(1,n+1):
#     for l in range(i):
#         print(s+1,end=' ')
#         s+=1
#     print()

# Floyid uchberchagi 2

# n=int(input())
# m=list(map(int,input().split(' ')))

# for i in range(n):
#     t=m[i]
#     d=1+8*t ;x = (-1+(d)**(1/2))/2
#     if (x*10)%10==0:
#         print(1,end='')
#     else:
#         print(0,end='')

# Retoran

# a,i = map(int,input().split(" "))
# l = list(map(int,input().split(" ")))
# p=int(input())
# print(p-(sum(l)-l[i])//2)

# Teskari kodlash

# t=int(input())
# l = [10 , 20 , 5 , 0 , 1 , 2]
# l1 = [ 55 , 210 , 15 , 0 , 1 , 3 ]

# for i in range(t):
#     s=0
#     n,m = map(int,input().split(" "))
#     for d in range(6):
#         if l[d]==n and l1[d]==m:
#             s=1
#             break
#     if s!=1:
#         print(0,end='')
#     else:
#         print(s,end='')

# Daraxtlarni yig'ish

# t=int(input())
# for i in range(t):
#   n=int(input())
#   if n==1:
#       print(1)
#   else:
#       l=0
#       while (2**l)<=n :
#           if (2**l)==n:
#               print(l)
#               break
#           elif (2**(l+1))>n:
#               print(l)
#               break
#           l+=1

# Sonlar soni
# l,r,s = map(int,input().split(" "))
# res = 0
# for i in range(l,r+1):
#     c=0
#     while i>=1:
#         c+=i%10
#         i//=10
#     if c==s:
#         res+=1
# print(res)

# sort

# a=[]
# n=int(input())

# for i in range(n):
#     a.append(int(input()))
#     mn = a[i]

# a.sort()

# print('\n'.join(map(str, a)))

# o'zing top shartini

# a=input()
# if a=='A089957':
# 	print(1)
# else:
#     print(0)

''''# O'nlikdagi satr (error)'''

# while a>1:
#   a=a/2
# if a==0:
#   print(1)
# else:
#   print(2)

# n = int(input())
# a = [1,1] ; l=1 ; r=1 

# Gnameoning dastur kodi 

# while r+l<=n+1:
#     d=r ; r=l+r ; l=d
#     a.append(r)
# for n in range(2,len(a)+1):
#     for i in range(2,int(n**(1/2))+1):
#         if n%i==0:
#             break
#     else:
#         print(a[n-1])

# To'rtburchak

# a,b=map(int,input().split(" "))
# if a*b>2*(a+b):
#   print(a*b)
# else:
#   print(2*(a+b))

# Isfandyor matem

# from math import*
# x=int(input())
# y=pow(x,5)+8*pow(x,4)-5*pow(x,3)+3*x*x+x-12
# print(int(y))


# n=int(input())

# if n%2==0:
#   print(n//2+1)
# else:
#   print(n//2+1)


# a=int(input())

# if a%100==0:
#     print(a//100)
# else :
#     print(a/100)

# Uzluksiz birlar

# a=int(input())
# a=str(a)

# for i in range(len(a)):
#     if a[i]=='0':
#         for l in range(i,len(a)):
#             if a[l]=='1':
#                 print("NO")
#                 break
#         else:
#             print("YES")
#             break
#         break
# else:
#     print("YES")

# Maosh 

# a,b,c= map(int,input().split(" "))

# mi = a ; ma = a
# if a>b and c>b:
#     mi = b
# if a>c and b>c:
#     mi=c
# if b>a and b>c:
#     ma=b
# if c>a and c>b:
#     ma=c
# print(ma-mi)

# a=list(map(int,input().split(" ")))
# s=int(input())

# if (s-sum(a))<=0:
#     print(0)
# else:
#     print(s-sum(a))

# Baho

# a=int(input())

# if a<38:
#     print(a)
# else:
#     if a==100 :
#         print(100)
#     elif a%10<5:
#         if (a//10*10+5)-a<3:
#             print(a//10*10+5)
#         else :
#             print(a)
#     elif a%10>5:
#         if (a//10*10+10)-a<3:
#             print(a//10*10+10)
#         else :
#             print(a)
#     else:
#         print(a)

# Zoo

# a=input()
# if a.count('z')*2==a.count('o'):
#     print("Yes")
# else:
#     print("No")

# Raqamlari yig'indisi .

# a=int(input())
# s=0
# while a>=1:
#   s+=a%10
#   a//=10
# print(s)


# Ajoyib topshiriq 

# a=int(input())
# i=0 ; s='1' ; l=2
# while a>=i:
#     if a==i :
#         print(s[i-1])
#         break
#     else:
#         i+=1
#         s+=str(l)
#         l+=1



# n = int(input())
# a = [1,1] ; l=1 ; r=1 

# while r+l<=n+1:
#     d=r ; r=l+r ; l=d
#     a.append(r)
# for n in range(2,len(a)+1):
#     for i in range(2,int(n**(1/2))+1):
#         if n%i==0:
#             break
#     else:
#         print(a[n-1],end=' ')

# Kingru

# x1,v1,x2,v2 = map(int,input().split(" "))

# x = abs(x1-x2)
# v = abs(v1-v2)

# if x%v==0:
#     print("YES")
# else:
#     print("NO")

# n,s = map(int,input().split(" "))
# li = list(map(int,input().split(" ")))
# li.sort()

# a,b = map(int,input().split(" "))
# if a==b:
#   print(0)
# else:
#   if (b-a)%10==0:
#     print((b-a)//10)
#   else:
#     print((b-a)//10+1)

# m,n = map(int,input().split(" "))
# li = list(map(int,input().split(" ")))
# if sum(li)<m:
#     print(-1)
# else:
#     li.sort(reverse = True) ; s=0 ; c=0
#     for i in range(len(li)):
#         if s>=m:
#             print(c)
#             break
#         else:
#             c+=1 ; s+=li[i]

# Juftlik

# a,b = map(int,input().split(" "))
# if a==b:
#   print(0)
# else:
#   if abs(a-b)%10==0:
#     print(abs(a-b)//10)
#   else:
#     print(abs(a-b)//10+1)

# m,n = map(int,input().split(" "))
# li = list(map(int,input().split(" ")))

# li.sort(reverse = True)
# b = 0 ; s=0
# for i in li :
#     s+=i ; b+=1
#     if s>=m:
#         break
# print(b)

# Formula

# from math import*
# x,y = map(float,input().split(" "))

# f=(1/(x+2/(x*x)+3/(x*x*x))+pow(e,(x*x+3*x)))/(atan(x+y)+pow((5+x),2))-pow(cos(y*y+(x*x)/2),2)
# print("%.2f"%f)

# a=input()
# s=''
# for i in range(len(a)):
#     if a[i]=='P' or a[i]=='Q' or a[i]=='7':
#         s='yes'

# if not(s):
#     print('no')
# else:
#     print(s)

# a = input()
# if a[0]=='-' and len(a)>2:
#   print((-1)*int(a[1])+int(a[2:]))
# else:
#   print(a)

# m,n = map(int,input().split(" "))
# li = list(map(int,input().split(" ")))

# li.sort()
# s = 0 ; co = 0
# for i in range (n-1,-1,-1):
#     s+=li[i] ; co+=1
#     if s>=m:
#         print(co)
#         break

# n=int(input())

# for i in range(n):
#   x1,y1,x2,y2 = map(int,input().split(" "))
#   if x1>x2 :
#     x=x2-abs(x1-x2)
#   else:
#     x=x2+abs(x1-x2)
#   if y2>y1 :
#     y=y2+abs(y1-y2)
#   else:
#     y = y2-abs(y1-y2)
#   print(x,y)

# a=int(input())
# s = 0 

 
# for i in range(1,int(abs(a)**(1/2))+1):
#     if a%i == 0 :
#         s+=1
#         if -1*i*i!=a:
#             s+=1
# if a==0:
#     print(-1)
# elif abs(a)==1:
#     print(1)
# else:
#     print(s)

# from math import*

# r = list(map(float,input().split()))
# l = list(map(float,input().split()))
# w = list(map(float,input().split()))
# s = list(map(float,input().split()))


# r = sum(r)/(len(r))
# l = sum(l)/(len(l))
# w = sum(w)/(len(w))
# s = sum(s)/(len(s))

# s = (r+l+w+s)

# if s%4/4 >= 0 and s%4/4<0.25:
#     print(int(s/4))
# elif s%4/4 >= 0.25 and s%4/4<0.75 :
#     print(s//4+0.5)
# else:
#     print(int(s/4+1))


# li=list(input())
# print(len(li))
# for a in li :
#     a=str(bin(ord(a)))
#     print(a[2::])

# n=int(input()) ; print((n*(n-1)*(n-2))%(10**9+7) if (n!=1 and (n!=2)) else 1 if n==1 else 2)

# Sezir accepted

# a=list("abcdefghijklmnopqrstuvwxyz")
# k=int(input())
# b=list(input())


# for i in b :
#     for l in a :
#         if i=='_':
#             print("_",end='')
#             break
#         elif i==l:
#             print(a[(a.index(l)+k)%26],end='')
#             break
#         elif i==l.title():
#             print(a[(a.index(l)+k)%26].title(),end='')
#             break

# n = int(input())

# li = list(map(int,input().split(" ")))
# ma= 0

# for i in li :
#     if ma < li.count(i):
#         ma = li.count(i)
# print(n-ma)

# a=list(input())

# if (int(a[0])+int(a[1])+int(a[2]) == int(a[3])+int(a[4])+int(a[5])):
#     print("YES")
# else:
#     print("NO")




# a=int(input())

# for i in range(0,63):
    

# a=int(input())

# print((-1+int((1+8*a)**(1/2)))//2)

# a,b,c,d = map(int,input().split())
# if abs(a-c)>abs(b-d):
#   print(abs(a-c)//2 if abs(a-c)%2==0 else abs(a-c)/2+1)
# else:
#   print(abs(b-d)//2 if abs(b-d)%2==0 else abs(b-d)/2+1)

# n,k = map(int,input().split())
# li = list(map(int,input().split()))

# mi = li[k-1] ; li.sort() ; s=0 ; c=0

# for i in li :
#     if i==0:
#         c+=1
#     if i>=mi :
#         s+=1
# print(s if s!=c else 0)

# y,x = map(int,input().split())
# print("%.2f"%(x*100)/y)



'''# m,n = map(int,input().split(" "))
# li = list(map(int,input().split(" ")))

# li.sort(reverse = True)
# s=0 ; re = 0
# if sum(li)<m :
#     print(-1)
# else:
#     for i in range(n) :
#       s+=li[i] ; re+=1
#       if s>=m :
#         print(re)
#         break'''

# n,t,k = map(int,input().split())
# li = []
# for i in range(n):
#     li.append(t)

# ne=0 ; s=0
# while k>s:
#     ne -= 1 ; s+=1
#     if ne==-1 :
#         ne = n-1
#     li[ne]=li[ne]-1

# for i in range (len(li)):
#     if li[i]<=0:
#         print(1)
#         break
# else:
#     print(-1)

# t=int(input())

# for i in range(t):
#   print("NO")

# a,b = map(str,input().split(" "))


# al = list(map(str,"abcdefghijklmnopqrstuvwxyz"))


# for i in al:
#     if i.title()==a:
#         a=al.index(i)+1
#     if i.title()==b:
#         b=al.index(i)+1
# print(a+b)

# a=b=int(input()) ; s=0
# while a>=1 :
#     s+=a%10
#     a//=10
# print("yes" if b//10**8 != 0 and s%2==1 else "no")





''' Quruvchi Xumoy
while True :
    x = input()
    if not(x) :
        break
    else:
        x,y = map(int,x.split())
        if x==y:
            print(4)
        else:
            a=x ; b=y
            while x!=0 and y!=0:
                if x>y:
                    x%=y
                else:
                    y%=x
            x=x+y
            print(2*(a//x)+2*(b//x))'''


# A,k = map(int,input().split())

# li = list(map(int,input().split()))

# print(li.count(k)*k)

# for i in range(A):
#     if li[i]==k:
#         print(i+1,end = ' ')



''''# O'nlikdagi satr '''

# a=int(input())
# s=63 ; n=0
# while a>=0:
#     if 2**s <=  



# a = str(input().split())

# al = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

# for i in al :
#   print(f"{i} {a.count(str(i))}",end='\n')


# a,b = map(int(),input().split())

# print(24-a+b)

# m,n = map(int,input().split(" "))
# li = list(map(int,input().split(" ")))

# li.sort(reverse = True)
# s=0 ; re = 0
# if sum(li)<m :
#     print(-1)
# else:
#     for i in range(n) :
#       s+=li[i] ; re+=1
#       if s>=m :
#         print(re)
#         break

# n,k = map(int,input().split())
# li = list(map(int,input().split()))

# mi = li[k-1];
# while(mi==li[k-1] and (k!=1 or li[k-1]>0) and k<len(li)):
#   k+=(1 if mi!=0 else -1)
# print(k-1 if li[k-1]==mi else k)


# a,b = map(int,input().split())
# if a>b:
#     a=b
# s=1
# for i in range(2,a+1):
#     s*=i
# print(s)

# print(s)

# a = int(input())
# li = list(map(int,"0123456789"))
# li_n = list(map(int,"6255456376"))
# s=0

# while a>=1:
#     for i in range(10):
#         if li[i]==a%10 :
#             s+=li_n[i]
#     a//=10
# print(s if s!=0 else 6)

# from math import *

# l,r = map(int,input().split())

# for i in range(l,r+1):
#     if i!=1:
#         for l in range(2,i):
#             if i%l==0:
#                 break
#         else:
#             print(i,end=' ')

# a=int(input())

# mo = a%47
# st = ['_','_','_']
# if mo<=25:
#     st[0]='O'
# if 22<=mo and 31>=mo:
#     st[1]='O'
# if 32<=mo:
#     st[2]='O'

# print(''.join(st))



# a=[]
# n=int(input())

# for i in range(n):
#     a.append(int(input()))

# for i in range(len(a)):
#     for l in range(i+1,len(a)):
#         if a[i]>a[l]:
#             c=a[i] ; a[i]=a[l] ; a[l]=c

# for i in range(n):
#     print(a[i])


# b=int(input())
# a = list(map(int,input().split(" ")))

# for i in range(len(a)):
#     for l in range (i+1,len(a)):
#         if a[i]>a[l]:
#             s=a[i] ; a[i]=a[l] ; a[l]=s
# print(' '.join(map(str,a)))

''' Uch o'quvchi '''
# n=int(input())
# if n>=6 and n%3==0 :
#   s=1
#   for i in range(2,n+1):
#       s*=i
#   print(s)
# else:
#   print(0)


# a=int(input())

# l = 1 ; r = 1000
# s=0
# while l<r:
#     s+=1
#     mid = (l+r)//2
#     print(mid)
#     if mid==a:
#         print(mid , s)
#         break
#     elif mid >a :
#         r=mid-1
#     else:
#         l=mid+1

# a=int(input())+1
# if a<=0:
#   print('___')
# else:
#   mo = a%50
#   st = ['_','_','_']
#   if mo<30 and mo!=0:
#       st[0]='O'
#   if 25 < mo and 36 > mo:
#       st[1]='O'
#   if 35 < mo or mo==0:
#       st[2]='O'
#   print(''.join(st))

# m,n = map(int,input().split(" "))
# li = list(map(int,input().split(" ")))

# li.sort(reverse = True)
# s=0 ; re = 0
# if sum(li)<m :
#     print(-1)
# else:
#     for i in range(len(li)):
#         s+=li[i] ; re +=1
#         if m<=s:
#             print(re)
#             break


# m,n = map(int, input().split())
# q = input().split()  
# for i in range (0, len(q)):
#     q[i]=int(q[i])
# q.sort()
# s=0
# n=0
# while s<=m:
#    s+=q[len(q)-n-1]
#    n+=1
#    if n==len(q):
#        break
# print(n if n!=len(q) else -1)

# a=int(input()) ; li = []
# for i in range(a):
#     li.append(int(input()))
# zero = li.count(0) ; one = li.count(1) 
# print(len(li)-max(zero,one))

# a=int(input())
# li = list(map(int,input().split()))
# print(min(li),max(li))

# a=list(input().split("1"))
# print(len(max(a)))

# b,a = map(int,input().split())
# d = int((b*b-4*a)**(1/2))
# print((b-d)//2,(b+d)//2)

# s=0 ; a=int(input())
# if a>0 :
#     for i in range(1,a+1):
#         s+=i
# else:
#     for i in range(a,2):
#         s+=i
# print(s)

# n = int(input())
# l = list(map(int,input().split()))
# for i in range(n-1,-1,-1):
#     print(l[i],end=' ')

# for i in range(7):
#     li = list(map(int,input().split()))
#     for j in li :
#         if j==1 :
#             print(abs(li.index(j)+1-4)+abs(i+1-4))
#             break

# st = ''
# for i in range(3):
#     l = list(map(str,input().split()))
#     for i in l :
#         st+=i
# print("O" if st.count("O")==st.count("X") else  "X")

# a=int(input())

# li = list(map(int,input().split()))
# li_1 = list(map(int,input().split()))

# for i in range(a):
#     print((li[i]+li_1[i])%2,end = ' ')

# a,b = map(int,input().split()) ; s=''
# for i in range(2,int(a**(1/2))+1):
#     for j in range(2,int(b**(1/2))+1):
#         if a%i == 0 or b%j == 0:
#             s = ("No")
# if not(s):
#     print("Yes" if  abs(b-a)==2 else "No")
# else:
#     print(s)
# li=[]
# for i in range(2):
#     a=input()
#     if a.count(" ")==0:
#         li.append(int(a))
#     else:
#         a,b = map(int,a.split()) ; print(a+b)
#         break
# if li:
#     print(li[1]*li[0])

# n , q = map(int,input().split())

# a = list(map(int,input().split()))
# b = list(map(int,input().split()))

# for i in range(q):
#     l,r = map(int,input().split()) ; s=0
#     for i in range(l-1,r):
#         s+=max(sum(a[l-1:i+1]),sum(b[l-1:i+1]))
#     print(s)

# k = int(input()) ; li = list(input().split())
# res = [i[::-1]  for i in li  if len(i)>k]

# print(' '.join(res))
'''
a,b = map(int,input().split())

if (b-a)<2 and b>=a and ((b*a) != 0 or (a==0 and b==1)) :
  if a==0 and b==1 :
      print(a,b)
  else:
      print ( f"{a*10} {b*10+1}" if (b-a)==0 else f"{a*10+9} {b*10} ")
else:
  print(-1)'''

# k = int(input()) ; li = list(input().split())
# for i in li :
#     if len(i)>k :
#         print(i[::-1],end = " ")
#     else:
#       print(i,end = " ")

# a = int(input())

# print((5**a)%1000000007 if int(a)!=0 else 0)


# vazn , boy = map(int,input().split())
# TVI=(10000*vazn)/boy**2

# if TVI<16 :  print("Yuqori vazn yetishmasligi")
# elif 16<=TVI<18.5 : print("Vazn yetishmasligi")
# elif 18.5<=TVI<=25: print("Ideal vazn")
# elif 25<TVI<=30 : print("Ortiqcha vazn")
# elif 30<TVI<=35 : print("Semizlikning I darajasi")
# elif 35<TVI<=40: print("Semizlikning II darajasi")
# else: print("Semizlikning III darajasi")

# c = a = int(input())
# dig = 0 ; mod = 1 ; res = 0
# while mod!=0:
#     mod = a//10 ; a//=10 ; 
#     dig += 1

# for i in range(dig-1):
#     res+=(i+1)*10**i*9
# print(res+(c-int((dig-1)*"9" if (dig-1)*"9" != "" else 0))*dig)


# a = list("йцукенгшщзхъфывапролджэячсмитьбю.")

# b = list("qwertyuiop[]asdfghjkl;'zxcvbnm,./")

# c = input()
# s = ''
# for i in c :
#     for j in range(len(a)):
#         if i==a[j] :
#             s+=b[j]
#         elif i.title() ==a[j].title():
#             s+=b[j].title()
#         elif i==" ":
#             s+=" " ; break
# print(s)



# h,m = map(int,input().split(":"))

# a1 = h-1 if (h-1)>9 else f"0{h-1}" if (h-1)!=-1 else 23

# a2 = h+1 if (h+1)>9 and (h+1)!=24 else f"0{h+1}" if (h+1)!=24 else "00"

# def ekub(a,b):
#     while a!=0 and b!=0 :
#         if b>a:
#             b%=a
#         else:
#             a%=b
#     return (a+b)
# a,b,c,d = map(int,input().split())

# print(ekub(a**b-c,d))


n,k = map(int,input().split())
# s=input() ; res=0
s=list(map(int,input().split())) ; res = 0

def kop(i,j):
    global s
    ko=1
    for k in range(i,j):
        ko*=s[k]
        # print(ko)
    return ko

for i in range (n):
    for j in range(i,n):
        if kop(i,j+1)<=k:
            print(kop(i,j+1))
# print(res)































