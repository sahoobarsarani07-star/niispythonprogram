marks=int(input("Enter your marks(0-100):"))
print("1.Check Grade")
choice=int(input("Enter your choice:"))
match choice:
	case 1:
		match marks:
		case_if marks>=90:
print("Grade:A")
        case_if marks>=75:
print("Grade:B")
        case_if marks>=60:
print("Grade:C")
        case_if marks>=40:
print("Grade:D")
        case_if marks>=0:
print("Grade:"F)
        case_:print("invalid marks")
    case_:
     print("invalid choice")