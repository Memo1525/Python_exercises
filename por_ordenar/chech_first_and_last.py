#Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
def validate_start_end(lista):
    if numbers_x[0] == numbers_x[-1]:
        return True
    else:
        return False
    
print(validate_start_end(numbers_x))