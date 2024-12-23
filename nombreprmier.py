def prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

num = int(input("Enter an integer: "))
if prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")