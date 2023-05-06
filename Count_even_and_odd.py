sample_numbers = ()

lst = list(sample_numbers)

even_count = 0
odd_count = 0

size = int(input("enter the total no.of elements"))

for x in range (size):
    element = int(input(f"enter the {x+1} element"))
    lst.append(element)


for x in (lst):

    if(x%2==0):
        even_count+=1
    else:
        odd_count+=1

print("odd numbers count are : ",odd_count)
print("even numbers count are : ",even_count)
