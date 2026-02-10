marks1 = int(input("Enter marks 1 = "))
marks2 = int(input("Enter marks 2 = "))
marks3 = int(input("enter marks 3 = "))

total_percentage = (marks1+marks2+marks3)/3
if(total_percentage>=40 and marks1>20 and marks2>20 and marks3>20):
    print("YOU ARE PASSED!")

else:
    print ("YOU ARE FAILED!!!")