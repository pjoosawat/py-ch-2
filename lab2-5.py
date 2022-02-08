mid = int(input("midterm"))
final = int(input("final"))
homework = int(input("homework"))
total = (mid*40/100)+(final*50/100)+(homework*10/100)
print("รวม", total)

x = total
if x >= 90 and x <=100:
    print("Grade A")
elif x >= 85 and x <=90:
    print("Grade B+")
elif x >= 80 and x <=85:
    print("Grade B")
elif x >= 70 and x <=80:
    print("Grade C+")
elif x >= 60 and x <=70:
    print("Grade C")
elif x >= 55 and x <=60:
    print("Grade D+")
elif x >= 50 and x <=55:
    print("Grade D")
elif x >= 0 and x <=50:
    print("Grade F")