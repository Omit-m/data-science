score = float(input("Enter the student's score: "))
if(score <= 100):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    elif score >= 50:
        grade = "E"
    elif score >= 40:
        grade = "E-"
    else:
        grade = "f"

    print("Student's grade is : ",grade)
else :
    print(" This is 100(+) score ,its not possible")