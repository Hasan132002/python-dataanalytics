a=eval(input("Enter the percentage : "))
if a>=80:
    print("Your grade is A+")
elif a<=79 and a>=70:
    print("Your grade is A")
elif a<=69 and a>=60:
    print("Your grade is B")
elif a<=59 and a>=50:
    print("Your grade is C")
elif a<=49 and a>=40:
    print("Your grade is D")
    
else:
    print("Fail")