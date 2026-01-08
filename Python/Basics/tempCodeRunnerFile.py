a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

# Check if a and b are between 1 and 1010
if 1 <= a <= 1010 and 1 <= b <= 1010:
    print("Addition of a and b:", a + b)          # add a and b
    print("Subtraction of a and b:", a - b)       # subtract b from a
    print("Multiplication of a and b:", a * b)   # multiply a and b
else:
    print("Please enter numbers between 1 and 1010")

## ### #### ###### ####### ###### Alterneavitv ## ### ##### ###### #######

a = int(input("Enter the value for a:"))
b = int(input("enter the value for b:"))

1 <= a <=1010 and 1<= b <=1010
print("""
    1.add
    2.sub
    3.multi
    4.divid
""")

z = int(input("Enter the number to perform the operasion:"))

if z == int(1):
    print(f"addacation of {a} and {b}:",a+b)
elif z == int(2):
    print(f"suberasation of {a} and {b}:",a-b)
elif z == int(3):
    print(f"multiplacation of {a} nad {b}:",a*b)
elif z == int(4):
    if b == 0:
        print("you divide by 0 ")
    else:
        print(f"divided {a} and {b}:",a/b)
else:
    print("curret number")
