#task1
def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True
#masalan:
print(is_prime(4))  # Natija: False
print(is_prime(7))  # Natija: True


#task2
def digit_sum(k):
    return sum(int(digit) for digit in str(k))
  
#masalan:
print(digit_sum(24))   # Natija: 6 (2 + 4)
print(digit_sum(502))  # Natija: 7 (5 + 0 + 2)


#task3
def print_powers_of_two(N):
    power = 1
    while True:
        power *= 2
        if power > N:
            break
        print(power, end=' ')

#masalan:
print_powers_of_two(10)


