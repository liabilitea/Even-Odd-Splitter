#Read the contents of the txt file and make it into a list
with open("numbers.txt", "r") as basis_file:

#Remove the line break character from every line and convert string to integer
    numbers = []
for line in basis_file:
    number = int(line.strip())
    numbers.append(number)

#Write even and odd numbers to different files 

#Use loop to evaluate each integer in the txt file