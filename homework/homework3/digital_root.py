def digital_root(n):
    while n >= 10:
        # take digits and add them
        sum_of_digits = 0
        for digit in str(n):
            sum_of_digits += int(digit)
        # Update n with the sum_of_digits so we keep going until we get digital root!
        n = sum_of_digits
        
    return sum_of_digits

# Example usage:
n = 12345
print(digital_root(n))