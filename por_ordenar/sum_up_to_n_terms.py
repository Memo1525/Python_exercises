#Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690
terms=10
number_temp=2
sumatoria=0
number=2
#reverse_number = (reverse_number * 10) + reminder 
for i in range(terms-1):
    number = number*10 + number_temp
    sumatoria += number
print(sumatoria + 2)

#provided by the book 
n = 5
# first number of sequence
start = 2
sum_seq = 0

# run loop n times
for i in range(0, n):
    print(start, end="+")
    sum_seq += start
    # calculate the next term
    start = start * 10 + 2
print("\nSum of above series is:", sum_seq)