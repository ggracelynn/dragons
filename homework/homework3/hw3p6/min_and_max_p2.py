def find_min_for(numbers):
    min_value = numbers[0]
    for num in numbers[1:]:
        if num < min_value:
            min_value = num
    return min_value 
    # this function will give the minimum value using a for loop

def find_min_while(numbers):
    min_value = numbers[0]
    i = 1
    while i < len(numbers):
        if numbers[i] < min_value:
            min_value = numbers[i]
        i += 1
    return min_value
    #this function will give the minimum value using a while loop

def find_max_for(numbers):
    max_value = numbers[0]
    for num in numbers[1:]:
        if num > max_value:
            max_value = num
    return max_value
    # this function will give the maximum value using a for loop

def find_max_while(numbers):
    max_value = numbers[0]
    i = 1
    while i < len(numbers):
        if numbers[i] > max_value:
            max_value = numbers[i]
        i += 1
    return max_value
    # this function will give the maximum value using a while loop

#test case! :)
numbers = [38, 21, 8, 1, 29, 3]
print("Minimum (for loop):", find_min_for(numbers)) #should return 1
print("Minimum (while loop):", find_min_while(numbers)) #should return 1
print("Maximum (for loop):", find_max_for(numbers)) #should return 38
print("Maximum (while loop):", find_max_while(numbers)) #should return 38
