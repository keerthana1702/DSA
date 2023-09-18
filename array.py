print("reverses the array")
# def rev(A, start, end):
#     while start < end:
#         A[start], A[end] = A[end], A[start]
#         start += 1 
#         end -= 1
        
# A=[5,9,6,1,0]
# rev(A, 0,4)
# print("Reversed list is: ",A)


print("reverse the array user input")
# n = int(input())
# my_list = [input(f"Enter element {i}: ") for i in range(1, n+1)]
# print("The entered list is:", my_list)
# length = len(my_list)
# start = 0
# end = length - 1
# while start < end:
#     my_list[start], my_list[end] = my_list[end], my_list[start]
#     start += 1
#     end -= 1
# print("Reversed list:", my_list)



print("find the maximum an min in the array")
# a=[5,9,3,10,88]
# print(max(a))
# print(min(a))


print("find the min and max in the array")
# def mimx(a):
#     a.sort()
#     minmax = {"min": a[0], "max": a[-1]}
#     return minmax
# n= int(input())
# a= [int(input({i})) for i in range(1, n+1)]
# minmax = mimx(a)
# print("min= ",minmax["min"])
# print("max= ",minmax["max"])


print("kth min and max values")
# a= list(map(int,input().split()))
# a= sorted(a)
# print(a)
# k= int(input())
# print(a[k])
    
print("sort 0, 1 and 2")
# array =[0,2,1,0,0,0,1,0,2,0,1,2]
# print(array)

# for i in range(0, len(array)):
#     for j in range(i+1, len(array)):
#         if array[i] > array[j]:
#             array[i], array[j] = array[j], array[i]
# print(array)
            

print("move all the negative to left side")
# arr=[-4,0,9,-88,66,70,-2]
# print(sorted(arr))


print("find the union of 2 list")
# def dounion(a,b):
#     return(set(a+b))
    
# a = [1,2,3,4,5]

# b = [2,7, 8,9]

# print(dounion(a,b))

print("find the intersectioon of 2 list")
# def dointer(a,b):
#     return(set(a).intersection(b))

# a=[1,8,3,5]
# a=sorted(a)
# b=[1,6,8,3,6,9]
# b=sorted(b)
# print(dointer(a,b))


print("cyclic rotate")
# def rotate(array):
#     array.insert(0,array.pop())

# arr = [2,8,6,4,8]
# rotate(arr)
# print(arr)
print("kadane's algo")
def maxSubArraySum(self,arr,N):
        a = b = arr[0]
        for i in range(1,N):
            a = max(arr[i]+a,arr[i])
            b = max(a,b)
        return b