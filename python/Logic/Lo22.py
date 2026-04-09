def title(s):
    result = ''
    new_word = True
    for char in s:
        if char == ' ':
            result += char
            new_word = True
        elif new_word:
            result += upper(char)
            new_word = False
        else:
            result += lower(char)
    return result