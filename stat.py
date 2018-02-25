from math import sqrt

arr=list()
n=input("enter the number of elements")
print("enter the numbers")
#MEAN
for i in range(n):
    arr.append(int(input()))
sum=0

for i in range(n):
    sum=sum+arr[i]

mean=sum/(len(arr)*1.0)
print("MEAN :{0}".format(mean))

#MEDIAN
crr=arr
arr=sorted(arr)
if (len(arr)%2==0):
    median=(arr[(n-1)/2]+arr[n/2])/2.0
else:
    median=arr[n/2]

print("MEDIAN:{0}".format(median))

#MODE

brr=[]
for i in range(n):
    count=1
    for j in range(i+1,n):
        if (arr[i]==arr[j] and arr[i]!=-1):
            arr[j]=-1
            count=count+1
            brr.append(count)
if len(brr)==0:
    print("MODE :0")
else:
    brr=sorted(brr)
    mode=brr[-1]
    print("MODE :{0}".format(mode))
arr=crr
#RANGE
arr=sorted(arr)
maximum=arr[-1]
minimum=arr[0]
range_=(maximum-minimum)/2
print("MAXIMUM :{0}\nMINIMUM:{1}\nRANGE:{2}".format(maximum,minimum,range_))
#variance
sum=0
for i in range(n):
    sum=sum+((arr[i]-mean)**2)
variance=sum/n
print("VARIANCE:{0}".format(variance))
#STANDARD-DEVIATION
print("STANDARD-DEVIATION:{0}".format(sqrt(variance)))
