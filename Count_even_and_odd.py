sample_numbers = (2,8,9,45,67,4,10,5,34,56,99)
even_count = 0
odd_count = 0

for x in (sample_numbers):

    if(x%2==0):
        even_count+=1
    else:
        odd_count+=1

print("odd numbers count are : ",odd_count)
print("even numbers count are : ",even_count)
