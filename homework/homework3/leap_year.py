def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else: return False  
    
#test cases!
print(is_leap_year(1900)) #false
print(is_leap_year(2000)) #true
print(is_leap_year(2021)) #false