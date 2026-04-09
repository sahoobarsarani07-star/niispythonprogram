min_val = int(input("Enter minimum value: "))
max_val = int(input("Enter maximum value: "))

for no in range(min_val, max_val + 1, 1):
    c = 0
    d = 2
    
    if no == 0 or no == 1:
        continue
    
    while d <= no // 2:
        if no % d == 0:
            c = c + 1
            break
        d = d + 1
    
    if c == 0:
        print(no, "is prime number")