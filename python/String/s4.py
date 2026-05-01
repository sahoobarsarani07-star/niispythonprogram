print("Enter a string:")
s = input()

c = alp = up = lw = vw = co = dg = sp = sy = 0

for i in s:
    c += 1
    
    if i.isalpha():
        alp += 1
        
        if i.isupper():
            up += 1
        else:
            lw += 1
            
        if i in "aeiouAEIOU":
            vw += 1
        else:
            co += 1
            
    elif i.isdigit():
        dg += 1
        
    elif i.isspace():
        sp += 1
        
    else:
        sy += 1

# Word count
wd = len(s.split())

print("No of characters =", c)
print("No of alphabets =", alp)
print("No of uppercase =", up)
print("No of lowercase =", lw)
print("No of vowels =", vw)
print("No of consonants =", co)
print("No of digits =", dg)
print("No of spaces =", sp)
print("No of symbols =", sy)
print("No of words =", wd)