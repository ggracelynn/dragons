def rotate_digits(n):
    if n < 10:
        return n  # If the number has only one digit, rotation won't change it
    last_digit = n % 10  # Get the last digit of the number
    rest_of_digits = n // 10  # Get the remaining digits of the number

    #we need to multiply the last digit of the number properly to get it to the front!
    multiplier = 1
    while n >= 10:
        n //= 10
        multiplier *= 10

    # Rotate the digits to the right by one position
    rotated_number = last_digit * multiplier + rest_of_digits


    return rotated_number
print(rotate_digits(965438)) #should return 896543
    