# Palindrome Checker (Beginner Project)
# Part of Sukruth Reddy's Python Developer Roadmap

def is_palindrome(text: str) -> bool:
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

user_input = input("Enter a word or sentence: ")

if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome.")
else:
    print(f"'{user_input}' is NOT a palindrome.")
