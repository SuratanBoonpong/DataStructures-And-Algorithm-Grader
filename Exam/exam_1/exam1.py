print(" *** BMI ***")
w,h = input("Enter your weight(kg) and height(m) : ").split(" ")
w = float(w)
h = float(h)
BMI = w/(h*h)
print("Your status is : ",end="")
if BMI < 18.5:
    print("Below normal weight.")
elif BMI < 25:
    print("Normal weight.")
elif BMI < 30:
    print("Overweight.")
elif BMI < 35:
    print("Case I Obesity.")
elif BMI < 40:
    print("Case II Obesity.")
else:
    print("Case III Obesity.")