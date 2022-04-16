#get input from user an chage it to integer

num = int(input("Enter a number: "))

if num > 1:
    #algorythm below checks if there are any factors of the given number
    for i in range(2,num):
        if (num % i) == 0:
            print(num, "Is not a prime number")
            print(i, "x", num//i, "=", num)
            break
            # If you want to find the nearest prime number higher then your number, change
            # algorithm above to:
            # if (num % i) == 0:
            #   num = num + 1
        else:
            print(num, 'Is a prime number')

else:
    print("This value is incorrect")

