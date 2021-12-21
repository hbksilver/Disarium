# A number is said to be Disarium if the sum of its digits raised to their respective positions is the number itself.
#
# Create a function that determines whether a number is a Disarium or not.
def NumLength(number):
    length = 0;
    while (number != 0):
        length = length + 1;
        number = number // 10;
    return length;
myNumber = input('Please enter a number:')
n = sumOfDigits = 0
myLen = NumLength(myNumber);
newNumber = myNumber;

# sum of digits processing
while (myNumber > 0):
    n = myNumber % 10;
    sumOfDigits = sumOfDigits + int(n ** myLen);
    myNumber = myNumber // 10;
    myLen = myLen - 1;

# evaluate the number and returns true or false
if (sumOfDigits == newNumber):
    print(True);

else:
    print(False);
