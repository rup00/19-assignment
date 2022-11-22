def num_check(n,lower,upper):
    if n in range(lower,upper+1):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
num_check(5,4,7)