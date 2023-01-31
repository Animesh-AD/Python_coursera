def is_palindrome(string):
    # Strip all non-alphanumeric characters and convert to lowercase
    string = ''.join(c.lower() for c in string if c.isalnum())

    # Check if the string is a palindrome
    return string == string[::-1]
string = "coloc"
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
    
'''The for c in string part means that the code will loop through each character in the string variable.
The if c.isalnum() part means that the code will only consider alphanumeric characters (i.e. letters and numbers). Non-alphanumeric characters (such as punctuation) will be ignored.
The c.lower() part means that the code will convert each character to lowercase.
The ''.join part means that the code will create a new string by concatenating all of the characters (which have been converted to lowercase and filtered to only include alphanumeric characters) with an empty string as the separator.
The resulting string will be assigned back to the string variable, effectively replacing the original string with the modified version.
For example, if the string variable contains the value "A man, a plan, a canal: Panama", the modified string will be "amanaplanacanalpanama"'''