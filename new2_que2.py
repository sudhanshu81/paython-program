#wap to check if a list contains a palindrome of elements.(hint:use copy() method).
list1=[1,2,3,2,1]

copy_list1=list.copy()
copy_list1.reverse()
if(copy_list1==copy_list1):
    print("this is palindrome:")
else:
    print("this is not palindrome")