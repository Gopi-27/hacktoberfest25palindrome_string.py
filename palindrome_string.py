def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]  # ✅ Proper reversal

print(is_palindrome("Madam"))  # Output: True
