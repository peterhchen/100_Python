import string  
punctuation_except_decimal = string.punctuation.replace('.', '')

def TotalText(text, total=0):
    """Returns the sum of all the numbers in the text."""
    words = text.split()
    for word in words:
        word = word.strip(punctuation_except_decimal)
        word = word.rstrip('.')
        try:
            num = float(word)
            #print ('num, word: ', num, word)
        except ValueError:
            pass
        else:
            total += num
    return total