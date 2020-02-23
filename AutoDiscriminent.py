
# from tkinter import *

# window = Tk()
# window.title("Welcome to AutoDiscriminator")
# window.mainloop()
print("|These Script Is made by Antar|")

def Discriminant(num1,num2,num3):


    roots = num2*num2 - 4*num1*num3
    return(roots)

d = int(input("Enter The value of a in the quadratic equation:"))
e = int(input("Enter The value of b in the quadratic equation:"))
f = int(input("Enter The value of c in the quadratic equation:"))

a = Discriminant(d,e,f)
print("Your Discriminent is:",a)
if  a == 0:
    print("Equal Roots !!! ")
    pass
elif a > 0:
    print("Real Roots !!! ")

elif a < 0:
    print("No Real Roots !!! ")

else:
    print("Something went wrong Try again ")

print("Thank you for Using Our Script !!!! ")
exit()
 

    
  
