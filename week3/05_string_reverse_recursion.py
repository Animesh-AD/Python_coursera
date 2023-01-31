def string_reverse(str):
    if len(str) ==0:
        return str
    else:
        return string_reverse(str[1:])+ str[0]
str ="HOlA"
reverse = string_reverse(str)
print(reverse)  

''' string_reverse("OlA") + "H"
(string_reverse("lA") + "O") + "H"
((string_reverse("A") + "l") + "O") + "H"
(((string_reverse("") + "A") + "l") + "O") + "H" 
The above is the explanation of the control flow of the code'''
