#Read the contents of the txt file and make it into a list
with open("numbers.txt", "r") as basis_file:

#Remove the line break character from every line and convert string to integer
    numbers = []
for line in basis_file:
    number = int(line.strip())
    numbers.append(number)

#Separate even and odd numbers as variables and use modulo
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

#Write even and odd numbers to different files 
#Use loop to evaluate each integer in the txt file

