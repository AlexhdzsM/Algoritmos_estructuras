def factorial(num):

    if num > 1:
        num = num * factorial(num - 1)
    return num

print(factorial(6))
