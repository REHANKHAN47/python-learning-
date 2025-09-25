
def iseven(num):
    if num%2==0:
        return True
    else:
        return False
print(iseven(5))
# **************************************************************************
def maxnum(numbers):
    maxnum=numbers[0]
    for i in numbers:
        if i>maxnum:
            maxnum=i
    return maxnum
print(maxnum([1,2,3,4,5,6,7,8,9]))
# *****************************************************************************
def vowels(sentance):
    count=0
    vowels=set("aeiou")
    found={ch for ch in sentance.lower() if ch in vowels}
    if found:
        print("vowels found:", " ".join(sorted(found)))
    for ch in sentance.lower():
        if ch in vowels:
            count+=1
    return count
    
print(vowels("rehan khan is a good boy" ))
# ***********************************************************************************
def square(num):
    return num*num
print(square(5))
# ***********************************************************************************
def reverse(sting):
    return sting[::-1]
print(reverse("rehan khan"))
# ***********************************************************************************
def sum_num(numbers):
    return sum(numbers)
print(sum_num([1,2,3,4,5,6,7,8,9]))

def sumnumbers(numbers):
    total=0
    for n in numbers:
        total+=n
    return total
print(sumnumbers([1,2,3,4,5,6,7,8,9]))
# ***********************************************************************************
def factoraial(num):
    f=1
    for i in range (1,num+1):
        f=f*i
    return f
x=5
result=factoraial(x)
print(result)
# *******************************************************************************************
def palindrome(number):
        number=str(number)
        if number==(number)[::-1]:
            return number+" is palindrome"
        else:
            return number+" is not palindrome"
print(palindrome(231))
# *******************************************************************************************
def febecconi(n):
    a=0
    b=1
    if n<=0:
        return "invalid" 
    elif n==1:
        return a
    elif n==2:
        return b
    else:
        for i in range(2,n):
            c=a+b
            a=b
            b=c
        return c
print(febecconi(10))
