"""The Daily Byte - A YT channel i found who sends daily python questions to level yourself up"""

# 14th
# Q1)Given the following strings...
# “Cat”, return “taC”
# “The Daily Byte”, return "etyB yliaD ehT”
# “civic”, return “civic”

# def is_rev(s):
#     """Function returning Reverse"""
#     return s[::-1]
# inp = input('Enter the str: ')

# print(is_rev(inp))

# 15th
# Q2)Given the following strings...
# "level", return true
# "algorithm", return false
# "A man, a plan, a canal: Panama.", return true
st = input('Enter to check Palindrome:').lower()
st_clean = "".join(letter for letter in st if letter.isalnum())
st_rev = st_clean[::-1]
if st_clean == st_rev:
    print(True)
else:
    print(False)

