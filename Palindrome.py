def is_palindrome(text):
    text1="".join(c for c in text if c.isalpha())
    text1 = text1.lower()
    text2 = text1[::-1]

    if text2 == text1:
        return True
    else:
        return False

txt = input('Your text: ')

print(is_palindrome(txt))



# The is_palindrome(text) function takes the string text as an argument and returns True if the specified text is a palindrome and False otherwise.

# True: 
# ΝΙΨΟΝ ΑΝΟΜΗΜΑΤΑ ΜΗ ΜΟΝΑΝ ΟΨΙΝ
# Madam, I'm Adam.
# Sit on a potato pan, Otis. 
# Able was I, ere I saw Elba.

# False:
# Jesus travels toward Jerusalem 
# The disciples ask about the future
# the Christ, the son of the living God
# When Jesus had finished...
