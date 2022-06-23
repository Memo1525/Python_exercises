number1= 20 
number2 = 500
def product1(number1,number2):
    if number1 * number2 >1000:
        return(f"The result is {number1 + number2}")
    return(f"The result is {number1 * number2}")
print(product1(200,100))

#provided by the book 
def multiplication_or_sum(num1, num2):
    # calculate product of two number
    product = num1 * num2
    # check if product is less then 1000
    if product <= 1000:
        return product
    else:
        # product is greater than 1000 calculate sum
        return num1 + num2

# first condition
result = multiplication_or_sum(20, 30)
print("The result is", result)

# Second condition
result = multiplication_or_sum(40, 30)
print("The result is", result)