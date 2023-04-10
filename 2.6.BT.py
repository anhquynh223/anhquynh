hoten=input("Ho ten: ")
a=int(input("So ngay cong: "))
b=float(input("Don gia ngay cong: "))
c=float(input("He so phu cap: "))
d=float(input("Tam ung: "))
f=c*a*b
e=b*a*c-d
print("Nhan vien",hoten,", co tien Luong="+str(round(f,1))+", Tam ung="+str(d)+" va Thuc linh="+round(e,1),sep="")