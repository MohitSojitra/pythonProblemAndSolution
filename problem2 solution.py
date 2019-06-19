

try:
    nA = int(input("enter the number of apples:- "))
    minN = int(input("please enter the min number:- "))
    maxN = int(input("please enter the max number:- "))

    if minN == maxN:
        a =f"it is complete divided by {minN}" if nA % minN == 0 else f"it is complete not divided by {minN}"
        print(f"hear minimum number and maximum number is equal and ans is \n {a}")
    elif minN < maxN:
        for i in range(minN , maxN + 1):
            a =f"it is complete divided by {i}" if nA % i == 0 else f"it is complete not divided by {i}"
            print(a)
    else:
        print("its not in range")
except:
    print("invalid input")

    