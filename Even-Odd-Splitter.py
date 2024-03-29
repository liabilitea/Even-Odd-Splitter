#Read the contents of the txt file and make it into a list
with open("numbers.txt", "r") as basis_file:

#Remove the line break character from every line and convert string to integer
#Use list comprehension
    numbers = [int(line.strip()) for line in basis_file]

#Separate even and odd numbers as variables and use modulo
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

#Write even and odd numbers to different files 
#Use loop to evaluate each integer in the txt file

#Write and separate even integers
with open("even.txt", "w") as even_file:
    for num in even_numbers:
        even_file.write(str(num) + "\n")

#Write and separate odd integers
with open("odd.txt", "w") as odd_file:
    for num in odd_numbers:
        odd_file.write(str(num) + "\n")


