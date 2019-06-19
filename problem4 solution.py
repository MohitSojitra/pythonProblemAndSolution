

try:
    s = int(input("size:- "))
    
    numb = []
    for i in range(s):
        numb.append(int(input(f"pleae enter the {i+1} number:- ")))
    i = 0
    while(True):
        if i == s:
            break
        num = numb[i]
        if num >= 10:
            while True:
                num+=1
                string = str(num)
                if string == string[::-1]:
                    print(f"next palindrome is{numb[i]} {string}")
                    break
        else:
            print(f"next palindrome is{numb[i]} {num}")
        i+=1
except:
    print("please enter valid input ")
