*Password Generator*
Description
This Python script generates a random password based on user-defined length and complexity level.

*Requirements*
Python 3.x
Usage
Run the Script

*bash*
Copy code
python password_generator.py
Follow the Prompts

Enter the password length (positive integer).
Enter the complexity level (1 for easy, 2 for medium, 3 for hard).
Example
bash
Copy code
$ python password_generator.py
Length of the pass: 12
Pass complexity level (1/2/3): 3
Your Password: aB3$eF6@hJ9!

*Code Overview*
generate_password(length, level): Generates the password based on length and complexity level.
main(): Handles user input and displays the password.
