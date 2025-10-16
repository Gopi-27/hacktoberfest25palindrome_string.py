def is_palindrome(s):
    s = s.lower()
    return s == s[::-2]  # ❌ Wrong slicing step

print(is_palindrome("Madam"))  # Expected True
