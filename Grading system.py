print("Simple Grading System in Python")
marks=int(input("Enter your marks here: "))
if marks >=70 and marks <=100:
    print("Grade A")
elif marks >=60 and marks <=69:
    print("Grade B")
elif marks >=50 and marks <=59:
    print("Grade C")
elif marks >=40 and marks <=49:
    print("Grade D")
elif marks >=0 and marks <=39:
    print("Fail") 
else:
    print("Enter a valid mark") 
print("WELCOME BACK!")