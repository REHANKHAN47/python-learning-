fav=["appel","banana","orange","grape","watermelon"]
print(fav[2])
fav.append("kiwi")
print(fav)
for item in fav:
    print(item)
for item in fav:
    print(len(item))
# *****************************************************************************
f=["rehan khan","jawad ali khan","fawad ali khan","aimal khan"]
print(f[0])
print(f[-1])
f.append("hamza khan")
f[1]="ali khan"
print(f)
for item in f:
    print(item.upper())
# ******************************************************************************
n=[1,2,3,4,5]
print(n[0])
print(n[-1])
n.append(6)
print(n)
n.remove(6)
print(n)
for item in n:
    print(item*item)

total=0
for n in n:
    total+=n
    print(total)
# *****************************************************************************
a=[1,2,3,4,5,]
maxnum=a[0]
for item in a:
    if item>maxnum:
        maxnum=item
print(maxnum)
# ***************n**************************************************************
b=list(map(int,input("enter numbers with space: ").split()))
maxnum=b[0]
minnum=b[0]
for n in b:
    if n>maxnum:
        maxnum=n
    if n<minnum:
        minnum=n
print("maxnum is",maxnum)
print("minnum is",minnum)
# ******************************************************************************
num=list(map(int,input(f"enter 5 numbers of list with space: ").split()))   
print(num)
total=0
for n in num:
    total+=n
print(total)
avg=total/len(num)
print(avg)
maxnum=num[0]
for b in num:
    if b>maxnum:
        maxnum=b
print("maxnum is",maxnum)
# *******************************************************************************
num=list(map(int,input(f"enter 5 numbers of list with space: ").split())) 
num.sort()
print(num)
num.sort(reverse=True)
print(num)
num.sort()
print(f"the minimum nuber is:  ",num[0])
print(f"the maximum nuber is:  ",num[-1])
# *******************************************************************************
name=list((input(f"enter names of list with space: ").split())) 
print(name)
name.sort()
print(name)
print(name[0])
name.sort(reverse=True)
print(name)
print(name[-1])
for item in name:
    print(item)
    print(len(item))
for item in name:
    if len(item)>4:
        print(item)
