t=(1,2,3,4,5)
print(t)
print(("the first element"),t[0])
print(("the last element"),t[-1])
for item in t:
    print(("each item in tupple"),item)
print(("lenght of the tupple"),len(t))

# conversion of list to tupple
a=[1,2,3,4,5]
a=tuple(a)
print(a)
# conversion of tupple to list
b=(1,2,3,4,5)
b=list(b)
print(b)

# c to l 
t=("fawad ali khan","jawad ali khan","aimal khan")
l=list(t)
l.append("rehan khan")
t=tuple(l)
print(t)

# add
t=(1,2,3)
s=(4,5,6)
k=t+s
print(k)


# multply
t=("rehan khan","jawad ali khan","aimal khan","fawad ali khan")
k=t*2
print(k)

# slicing
t=("rehan khan","jawad ali khan","aimal khan","fawad ali khan")
k=t[1:3]
print(k)

# check
t=("rehan khan","jawad ali khan","aimal khan","fawad ali khan")
k=("rehan khan" in t)
y=("hamza khan" in t)
print(t)
print(k)
print(y)

# find
t=("rehan khan","jawad ali khan","aimal khan","fawad ali khan")
print(t.count("rehan khan"))
print(t.index("aimal khan"))

