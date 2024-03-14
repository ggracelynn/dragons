def vowels(statement):
    v="aeiouAEIOU"
    total= 0 #starting number of vowels before counting 
    for letter in statement:
        if letter in v:
            total += 1
    return total 


#testing function time! 
statement = "UC Berkeley" #we should get 4 in return! 
print(vowels(statement))
