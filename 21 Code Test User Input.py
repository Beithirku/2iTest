
#Accepts 2 input values for A and X
def multiplication(A, X):
    i = 1
    while i < 4:
        X = X * i
        print("A = ", i, " X = ", X, "\n")
        
        stepMulti = range(A, X+1, A)
        for n in stepMulti:
            print(n, end=" ")
        print("\n")
        
        i += 1 
#Asks the user for any integer which will be the starting times table.
A = int(input("Enter an integer: "))

#Asks the user for the end point of that table.
X = int(input("Enter the end point for the table: "))

#Calls the code.
multiplication(A, X)
