A=int(input("Enter your marks 1: "))
B=int(input("Enter your marks 2: "))
C=int(input("Enter your marks 3: "))
D=int(input("Enter your marks 4: "))
E=int(input("Enter your marks 5: "))
total = A + B + C + D + E
print(total)
percentage = total / 5
print(percentage)
if percentage >= 90:
    print("Grade: A")
elif percentage >= 80:
    print("Grade: B")
elif percentage >= 70:
    print("Grade: C")
elif percentage >= 60:
    print("Grade: D")
else:
    print("fail")