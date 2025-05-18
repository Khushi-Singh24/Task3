# 1. Check if a number is prime using a loop.
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# num = int(input("Enter a number: "))
# if is_prime(num):
#     print(f"{num} is a prime number.")
# else:
# print(f"{num} is not a prime number.")
    
    
# 2. factorial of a number using while loop.
# def factorial(num):
#     if num < 0:
#         return "Factorial is not defined for negative numbers."
#     elif num == 0 or num == 1:
#         return 1
#     else:
#         fact=1
#         while num > 0:
#             fact *= num
#             num -=1
#         return fact
# num = int(input("Enter a number: "))
# result = factorial(num)
# print(f"The factorial of {num} is {result}")

# 3. Sum of digits of a number using loop.
# num = int(input("Enter a number: "))
# sum_of_digits = 0
# while num > 0:
#     digit = num % 10
#     sum_of_digits += digit
#     num //= 10  
# print(f"The sum of the digits is: {sum_of_digits}")


# 4. checck if a number is palindrome using loop.
# def is_palindrome(num):
#     original_num = num    
#     reversed_num = 0
#     while num > 0:    
#         digit = num % 10
#         reversed_num = reversed_num * 10 + digit
#         num //= 10
#     return original_num == reversed_num
# num = int(input("Enter a number: "))
# if is_palindrome(num):
#     print(f"{num} is a palindrome.")
# else:
#     print(f"{num} is not a palindrome.")


# 5. LCM of two numbers using loop.
# def lcm(a, b):
#     max_num = max(a, b)
#     while True:
#         if max_num % a == 0 and max_num % b == 0:
#             return max_num
#         max_num += 1
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# result = lcm(a, b)
# print(f"The LCM of {a} and {b} is {result}")


# 6. Square matrix with diagonal 0.
# -----------------------


# 7. Continuous numbers in triangle.
# 1
# 2 3
# 4 5 6
# 7 8 9 10

def print_triangle(n):
    num = 1
    for i in range(1, n + 1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()
        
n = int(input("Enter the number of rows: "))
print_triangle(n)
