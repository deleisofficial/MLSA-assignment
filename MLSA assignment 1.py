#program to calculate student's grade based on score 
"""
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: 0-59

"""
grade= int(input("Input grade :"))
if grade < 60:
    print("Your have failed the exam with an 'F'' ")
elif grade >= 60 and grade < 70:
    print("You scaled through with a 'D' ")
elif grade >= 70 and grade < 80:
    print("Narrow through with a 'C' ")
elif grade >= 80 and grade < 90:
    print("You passed with a 'B'' ")
else :
    print("Congratulations on your 'A' ")
