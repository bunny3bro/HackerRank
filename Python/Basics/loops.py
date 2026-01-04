if __name__ == '__main__':
    n = int(input("Enter the number : "))
    i=0
    if n>=1 and n<=20:
        while i in range(0,n):
            print(f"Square of {i} :",i*i)
            i=i+1
    else:
        print("Enter the value of n in range 1 to 20.")

