# wap to print the element of a list in a single line.(list is the parameter)
cities=["delhi","mumbai","gurugram ","noida","kolkata","simla"]
heroes=["superman ","thor","ironman"]

def print_len(list):
    print(len(list))

    print_len(cities)
    print_len(heroes)

    #print a list in single line
    def print_list(list):
        for item in list:
            print(item,end="")