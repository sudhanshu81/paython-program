# write a recursive function to print all element in a list.
# hint:use list & index as parametrs.
def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list(idx))
    print_list(list,idx+1)
    fruits=["mango","litchi","apple","banana"]
    print_list(fruits)