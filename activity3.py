num = int(input("Enter a number: "))
t = num
numLen = 0
while t > 0:
    numLen = numLen + 1
    t = int(t / 10)

if numLen < 4:
    numLen = int(numLen/2)
    chk = 0
    mid0ne = midTwo = 0  # Initialize mid0ne and midTwo
    while num > 0:
        rem = num % 10
        if chk == numLen:
            mid0ne = rem
        elif chk == (numLen - 1):
            midTwo = rem
        num = int(num / 10)
        chk = chk + 1
    prod = mid0ne * midTwo
    print("\nProduct of Mid digits(" + str(mid0ne) + "*" + str(midTwo) + ") = " + str(prod))