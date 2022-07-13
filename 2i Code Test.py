i = 1
while i < 4:
    A = i
    X = 10 * i
    print("A = ", i, " X = ", X, "\n")
    
    stepMulti = range(A, X+1, A)
    for n in stepMulti:
        print(n, end=" ")
    print("\n")
    
    i += 1 
