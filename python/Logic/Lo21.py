def capitalize(s):
    if not s:
        return s
    first = s[0]
    rest = s[1:]
    return upper(first) + lower(rest)
