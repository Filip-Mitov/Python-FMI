def is_happy(number):
    if number <= 0:
        return False
    new_number = sum([int(digit) ** 2 for digit in str(number)])

    if new_number == 4:
       return False

    return is_happy(new_number) if not new_number == 1 else True

def is_number_prime(number):
    divisor_range = range(2, int(number/2) + 1)
    is_divisor = [number % divisor == 0 for divisor in divisor_range]
    return False if number < 2 else not any(is_divisor)

def happy_primes(check_range):
    return [number for number in check_range if is_happy(number) \
                                            and is_number_prime(number)]
