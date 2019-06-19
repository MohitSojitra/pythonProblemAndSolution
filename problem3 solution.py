l1 = [12,13,14,15]

# l2 = [2,3,4,5]
print("1. reverse by traditional method ")
print("2. reverse by slicing method ")
print("3. reverse by swapping method ")
ch = int(input())
if ch == 1:
    l2 = l1[:]
    l2.reverse()
    print(f"reverse is  {l2}")
elif ch==2:
    print(l1[::-1])
elif ch == 3:
    for i in range(len(l1) // 2):
        l1[i] , l1[len(l1) -i-1] = l1[len(l1) -i-1] , l1[i]
    print(l1)
else:
    print("please choose 1 or 2 or 3")

