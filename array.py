# reverses the array
# def rev(A, start, end):
#     while start < end:
#         A[start], A[end] = A[end], A[start]
#         start += 1 
#         end -= 1
        
# A=[5,9,6,1,0]
# rev(A, 0,4)
# print("Reversed list is: ",A)


#reverse the array user input
n = int(input())
my_list = [input(f"Enter element {i}: ") for i in range(1, n+1)]
print("The entered list is:", my_list)
length = len(my_list)
start = 0
end = length - 1
while start < end:
    my_list[start], my_list[end] = my_list[end], my_list[start]
    start += 1
    end -= 1
print("Reversed list:", my_list)
