
def fibonacci(a):
    result = 1
    preview_number = 1
    next_number = 1
    if a == 1 or a == 2:
        return result
    if a == 0:
        return 0
    for i in range(3, a + 1):
        result = preview_number + next_number
        preview_number = next_number
        next_number = result

    return result

a = int(input("Enter the number You Want His Fibo :"))

print(fibonacci(a))