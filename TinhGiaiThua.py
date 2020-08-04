#Viết một chương trình có thể tính giai thừa của một số cho trước.
print("--Tinh Giai Thua-- ")
p=int(input("Nhập p:"))
def fact(p):
    if p == 0:
      return 1
    return p * fact(p - 1)
print (fact(p))
#Ham Range()
print("--Ham Range--")
i=[]
for p in range(2000, 3201):
    if (p%7==0) and (p%5!=0):
       i.append(str(p))
print (','.join(i))
#Dictionary
print("--Dictionary--")
n=int(input("Nhập vào một số:"))
P=dict()
for i in range(1,n+1):
    P[i]=i*i
print (P)
#convert
print("--Convert--")
values=input("Nhập vào các giá trị:")
x=values.split(",")
y=tuple(x)
print (x)
print (y)
#Toan Tu
print("--Toan Tu--")
x=int(input("Nhập số cần tính bình phương : "))
def square(p):
  return p ** 2
print("Ket qua la: ",square(x))
#__init__
print("--__init__")
class InputString(object):
   def __init__(self):
       self.s = " "
   def getString(self):
       self.s = input("Nhập s:")
   def printString(self):
       print(self.s.upper())
strObj = InputString()
strObj.getString()
strObj.printString()
#__doc__
print("abs")
print(abs.__doc__)
print("int")
print(int.__doc__)
print("input")
print(input.__doc__)
#instance
print("--instance--")
class Employee:
 name = "Employee"
 def __init__(self, name = None):self.name = name
Phuoc = Employee("Phuoc")
print("%s ten la %s" % (Employee.name, Phuoc.name))
Le = Employee()
Le.name = "Le"
print("%s ten la %s" % (Employee.name, Le.name))
#Q = √([(2 * C * D)/H])
print("--Q = √([(2 * C * D)/H])--")
import math
c=50
h=30
D = []
items=[x for x in input("Nhập giá trị của D: ").split(',')]
for d in items: D.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
print (','.join(D))
#Array
print("--Array__")
inputS = input("Nhập X, Y: ")
P=[int(x) for x in inputS.split(',')]
h=P[0]
c=P[1]
kq = [[0 for col in range(c)] for row in range(h)]
for i in range(h):
    for j in range(c):kq[i][j]= i*j
print (kq)
#ChuHoa
print("--ChuHoa--")
L = []
while True:
   s = input()
   if s: L.append(s.upper())
   else: break;
for sentence in L: print (sentence)
#Set()
print("--Set()--")
s = input("Nhập s: ")
P = [P for P in s.split(" ")]
print (" ".join(sorted(list(set(P)))))
#Đếm Chuỗi
print("--Dem chuoi--")
s = input("Nhập s ")
d={"so":0, "chu":0}
for c in s:
 if c.isdigit(): d["so"]+=1
 elif c.isalpha(): d["chu"]+=1
 else: pass
print("Số chữ = ", d["chu"])
print("Số = ", d["so"])
#DemChuHoa
print("--DemChuHoa--")
s = input("Nhập s: ")
p={"hoa":0, "thuong":0}
for i in s:
    if i.isupper(): p["hoa"]+=1
    elif i.islower(): p["thuong"]+=1
    else: pass
print ("Chữ hoa = ", p["hoa"])
print ("Chữ thường = ", p["thuong"])
