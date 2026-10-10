"""Simple two pointer function to check to see if a string is a palindrom
    should i return true if the string is empty?
        yes
    should i skip over non alphanumeric
        yes
Keyword arguments:
argument -- description
Return: return_description
"""

def is_palindrome(string: str) -> bool:
    left, right = 0, len(string) - 1
    while left < right:
        # this is where i will check to see if it is alphanumeric on the left side
        while left < right and not string[left].isalnum():
            left += 1
        # this is where i will check to see if it is alphanumeric on the right side
        while left < right and not string[right].isalnum():
            right -= 1
        if string[left].lower() != string[right].lower():
            return False
        left += 1
        right -= 1  
    return True

# Test cases
assert is_palindrome("mom") == True
assert is_palindrome("A man, a plan, a canal: Panama") == True
assert is_palindrome("racecar") == True
assert is_palindrome("hello") == False
assert is_palindrome("") == True
assert is_palindrome(" ()^&()*&^*()^") == True
assert is_palindrome("12345678900987654321") == True
assert is_palindrome("mom m o m") == True
assert is_palindrome("Mom") == True

