def isPalindrome(str,str2):
    if str == str2:
        # Output:
        print(str,"is a palindrome.")   # radar is a palindrome.
    else:
        # Output:
        print(str,"is not a palindrome.")   # Hand is not a palindrome.

# Input:
str = input("Enter a string: ")   # Enter a string: radar  or  Enter a string: Hand
str2 = str[::-1]
isPalindrome(str,str2)