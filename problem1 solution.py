
age = input("enter your  or year of birth ");
flag = 0
if len(age) > 3:
    try:
        age = int(age)
        if age > 2019:
            print(" hey you not borne yet ")
            flag = 0
        else:
            a = f"you are in {age + 100} 100 years old"
            print(a)
            age = 2019 - age
            flag = 1
    except:
        print(f"please enter valid age ")
        flag = 0

    
elif len(age) < 3:
    try:
        age = int(age)
        print(f"you are in  {2019 + 100 - age } 100 year old ");
        flag = 1
    except:
        print(f"please enter valid age ")
        flag = 0
elif len(age) == 3:
    try:
        age = int(age)
        print(f"you are awesonme long live ")
    except:
        print("invalid input")
if flag != 0:
    print("would you like to know in perticuler year your age :- ")
    print("say yes or no :- ")
    ch = input().lower()

    if ch == "yes":
        try:
            year = int(input("enter year :- "))
            ages =  f"your age is {year - 2019 + age}" if year > 2019  else f"your age is {2019 - year + age} "
            print(f" {ages}")
        except:
            print("please enter valid year")
    elif ch == "no":
        print("ok !")
    else:
        print("invalid inpur proggrame exit")






