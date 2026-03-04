ch=input("Enter a character:").lower()
print("1.Check Vowel")
print("2.Check Consonant")
choice=int(input("Enter your choice:"))
match choice:
	case 1:
		if ch in 'aeiou':
			print("Vowel")
		else:
			 print("Not a vowel")
	case 2:
		if ch.isalpha() and ch not in 'aeiou':
			print("Consonant")
		else:
			print("Not a consonant")
    case _:
     print("invalid choice")
