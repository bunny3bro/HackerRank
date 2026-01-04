
def art_opr(a,b):
    if 1<=a and a<=1010 and 1<=b and b<=1010:
        print("Sum of a and b :",a+b)
        print("Difference between a and b :",a-b)
        print("Multiplication of a and b :",a*b)
        print("Division of a and b :",a/b)
    else:
        print("Enter the value of a and b in the range.")
if __name__ == '__main__':
    a = int(input("Enter the vlaue of a :"))
    b = int(input("Enter the valueof b :"))
    art_opr(a,b)