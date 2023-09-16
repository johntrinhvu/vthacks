# /*
# Write a program that prints the nums from 1 - 100
# But...
# For mults of 3 print "Fizz" instead of the num
# For mults of 5 print "Buzz" instead of num
# For nums which are multiples of both 3 and 5 print "FizzBuzz"

"""

create for loop that runs 1 -> 100: # num = 3
    create empty answer string # ans = ""
    if num mod 3 # True
        add fizz
    if num mod 5
        add buzz
    if len of string is 0: # Fizz
        print out the string version of the number #print(str(ans)) == "1"
    else
        print out the answer string #print(ans) = "Fizz

"""

def fizzBuzz():
    for i in range(1, 101):
        ans = ""

        if i % 3 == 0:
            ans += "Fizz"

        elif i % 5 == 0:
            ans += "Buzz"

        if len(ans) == 0:
            print(str(i))

        else:
            print(ans)