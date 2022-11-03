def singleNumber(arr ):
    x=arr[0]
    n=len(arr)
    res1=0
    res2=0
    Sn=0
    for i in range(1,n):
        x=x ^ arr[i]
        print(x)
    Sn=x & ~(x-1)
    for i in range(0,n):
        if Sn & arr[i] >0:
            res1=res1 ^ arr[i]
        else:
            res2=res2 ^ arr[i]
    for i in range(0,n):
        if res1 == arr[i]:
            return res1, res2
        elif res2 == arr[i]:
            return res2,res1

arr=[2,1,3,2]
print(singleNumber(arr))