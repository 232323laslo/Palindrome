# объявление функции
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

# ΝΙΨΟΝ ΑΝΟΜΗΜΑΤΑ ΜΗ ΜΟΝΑΝ ΟΨΙΝ
