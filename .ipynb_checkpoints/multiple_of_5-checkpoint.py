# write a function to find if the number is multiple of 5
def multiple_of_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

print(multiple_of_five(10))  
print(multiple_of_five(7))   
