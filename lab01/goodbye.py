num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
num1  # what is in num1? placeholder for first value input
num2  # what is in num2? placeholder for second value input
result1= int(num1) + int(num2)  # what happens if we add? Sums them arithmetically
result2= num1 + num2  # what happens without int? Concatenates them
print("Their arithmetic sum is {}".format(result1))
print("The concatenation of both inputs is {}".format(result2))
