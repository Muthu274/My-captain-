
def print_positive_numbers(lst):
   
    for num in lst:
      
        if num > 0:
           
            print(num, end=", ")


list1 = [12, -7, 5, 64, -14]
print_positive_numbers(list1)

list2 = [12, 14, -95, 3]
print_positive_numbers(list2)
