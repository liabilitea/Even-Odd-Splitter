# Even-Odd Splitter
***
## Description

This Python project reads a txt file containing 20 random integers. Moreover, it then separates the even and odd numbers from the list into separate variables using modulo and writes them to two different files named "even.txt" and "odd.txt", respectively.

Initially, the program utilizes the 'with' statement to open the "numbers.txt" file in read mode, which guarantees that the file will be closed correctly after it has been read. Then, it employs list comprehension to eliminate the line break character from every line and transform the string into an integer.

### Elaboration on List Comprehension

List comprehension is a concise and efficient way to create a new list from an existing list, string, or any iterable object.

The purpose of this line of code is to create a new list called "numbers" by iterating over each line in the file object "basis_file", stripping any whitespace characters, and converting the resulting string to an integer using the built-in int() function.

    
    numbers = [int(line.strip()) for line in basis_file]
   
This new list "numbers" will be used later in the code to separate the even and odd numbers and write them to separate files.

## How To Use / Run 

1. Install Python on your computer to run the code. You can download its latest version here: https://www.python.org/downloads/
2. Create a text file named "numbers.txt" and enter a list of integers, each on a separate line.
3. Place the "numbers.txt" file in the same directory as the code file.
4. Copy the code from the repository. 
5. Open an IDE and paste the code.
    + If you don't have an IDE, you can use any text editor from your computer and paste the code. 
6. Save the file with a .py extension.
7. Run the code.
    + For text-editor users, open a command prompt or terminal window and locate the folder where the Python file was saved and enter the command provided below by typing it in the command-line interface. After typing the command, press the Enter key to execute.
    
  ```
  python 'file_name'.py
  ```
8. The code will read the contents of "numbers.txt" and separate the even and odd numbers into two separate lists.
9. It will then write the even numbers to a file named "even.txt" and the odd numbers to a file named "odd.txt", both of which will be created in the same directory as the code file and "numbers.txt".
