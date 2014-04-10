def is_narcissistic(number, base=10):
    digits_in_base = [int(digit, base) ** len(number) for digit in number]
    return int(number, base) == sum(digits_in_base)
