# random-password-generator
The Random Password Generator is a Python application featuring a user-friendly graphical interface built with Tkinter. It's designed to help users create robust passwords based on specified criteria, save them alongside the associated site name in a SQLite database, and view all saved passwords. Additional features include the ability to copy the generated password to the clipboard for easy use.

Features
Customizable Password Criteria: Generate passwords by specifying:
Total password length

Number of uppercase letters

Number of lowercase letters

Number of digits

Number of special characters

Database Storage: Save passwords along with the corresponding site names to a SQLite database.

Password Display: View saved passwords and their associated site names within the application.

Clipboard Functionality: Copy generated passwords directly to the clipboard.

Requirements
Python 3.x
Tkinter (included with Python standard library)
SQLite3 (included with Python standard library)
Setup and Usage
Clone the Repository: Download the code to your local machine.

code functionality

python password_generator.py

Interact with the GUI:

Site: Enter the site name for which the password is being created.

Password Length: Specify the total length of the password.

Uppercase Letters: Define the number of uppercase letters.

Lowercase Letters: Define the number of lowercase letters.

Numbers: Specify the number of numeric characters.

Special Characters: Define the number of special characters.

Generate Password: Click to create a new password based on the entered criteria.

Generated Password: View the generated password in this field.

Save to Database: Save the password and site name to the database.

Copy to Clipboard: Copy the generated password to the clipboard.

Saved Passwords: View the list of saved passwords and associated site names.

Code Overview

generate_password(): Generates a password based on user input and criteria.

save_password(): Saves the generated password and site name to the SQLite database.

copy_to_clipboard(): Copies the generated password to the clipboard for easy use.

create_database(): Initializes the SQLite database and creates the necessary table if it doesn't exist.

display_saved_passwords(): Displays the list of saved passwords and associated site names in the application.

Example Usage

Launch the application.

Enter your desired password criteria, including the site name.

Click "Generate Password" to create a new password.

View the generated password in the designated field.

Click "Save to Database" to store the password and site name.

The saved passwords and site names will be listed in the "Saved Passwords" section.

Click "Copy to Clipboard" to copy the password for immediate use.

Notes
This application provides a simple yet effective way to manage and generate passwords, ensuring security for various sites and services.
Regular updates and enhancements can be made to adapt to changing security requirements or user preferences.

#
I've put a lot of effort into making this tool both functional and easy to use. Feedback and contributions are always welcome. If you have any suggestions or run into any issues, don't hesitate to reach out.


