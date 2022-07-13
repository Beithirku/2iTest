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

A = int(input("Enter an integer: "))
X = int(input("Enter the end point for the table: "))

multiplication(A, X)
