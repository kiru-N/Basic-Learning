
# Palindrome
# -------------

word = input('Enter the word to check for palindrome: ')
reverse_word = word[::-1]
if word == reverse_word:
    print(f'{word} is a Palindrome')
else:
    print(f'{word} is not a Palindrome')