
#Sets the default value of i to 1 for iteration.
i = 1

#While i is lower than 4 it will loop the code
while i < 4:
    
    #A is set to the value of i, this makes iteration cleaner.
    A = i
    
    #X is set to the first initial value of 10, and then multiplied by i, this is for the later loops mostly.
    X = 10 * i
    
    #Prints the current values of A, and what the final value should be for that iteration of the loop.
    print("A = ", i, " X = ", X, "\n")
    
    #Uses a range with a step of the value of A.
    #X is X+1 so it'll print the final value otherwise it would only print up to 9, not 10.
    stepMulti = range(A, X+1, A)
    for n in stepMulti:
        
        #Mostly for tidiness but the end=" " makes it so it prints the numbers on the same line.
        print(n, end=" ")
    print("\n")
    
    #Iterates to the next number so it isn't forever looping.
    i += 1 
