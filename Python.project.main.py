#A small python program that converts binary and decimal



print("=== Welcome to the Number Converter ===")
print("1. Convert Decimal to Binary (e.g., 5 -> 101)")
print("2. Convert Binary to Decimal (e.g., 101 -> 5)")
choice = (input('Choose an option '))

#decimal to binary
if choice == '1':
    decimal_number = (int(input('Choose a decimal number : ')))
    binary_result = bin(decimal_number)[2:]

    print(f"Result: {decimal_number} in binary is {binary_result}")

#binary to decimal    
elif choice == '2':
    binary_number= (input('Choose a binary number : '))
    decimal_result= (binary_number, 2)

    print(f"Result: {binary_number} in binary is {decimal_result}") 
    print(str(decimal_result) + ' is the answer ')
#if none
else:
    print('Invalid choice!!')