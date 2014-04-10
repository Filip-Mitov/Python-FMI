def is_perfect(number):
    sbor = 0
    maxi = int (number / 2) + 1
    for x in range(1, maxi):
        if number % x == 0:
            sbor += x

    return number == sbor