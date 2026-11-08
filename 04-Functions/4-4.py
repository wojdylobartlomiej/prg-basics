#
def sum_digits(number):
    str_num = str(number)  
    total_sum = 0          
    
    for char in str_num:   
        total_sum += int(char)
        
    return total_sum

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')