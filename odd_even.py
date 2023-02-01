n = int(input("Please enter your number: "))

if n % 2 == 0 and n > 0:
    print("{} is even number".format(n))
elif n % 2 != 0 and n > 0:
    print("{} is odd number".format(n))
else:
    print('zero is untouchable')