#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
#Any code taken from other sources is referenced within my code solution.

#Student ID: 
#Date: 

progress = 0
trailer = 0 
retriever = 0
excluded = 0
pass_credits = 0
defer_credits = 0
fail_credits = 0
total_credits = 0

def progress_outcomes(message):                     #Used functions to check user input validations for pass, defer and fail credits
    while True:                                                                         
        flag = 0
        try:
            x = int(input(message))
            if x > 120 or x < 0 or x % 20 != 0:     #Checks the range of user input whether it's valid or invalid
                print("Out of range\n")
                flag = 1    
        except ValueError:
            flag = 1
            print("Integer required\n")    
        if flag == 0:
            return x

print("Part 1:")
while True:

    pass_credits = progress_outcomes("Please enter your credits at pass: ")         #Calling progress_outcomes function by storing it in a variable
    defer_credits = progress_outcomes("Please enter your credits at defer: ")
    fail_credits = progress_outcomes("Please enter your credits at fail: ")

    total_credits = pass_credits + defer_credits + fail_credits         #Calculate the total_credits of user inputs (pass_credits + defer_credits + fail_credits)
    
    if total_credits == 120:
        
        if pass_credits == 120:
            print("Progress\n")
            progress += 1           #Gets the total count of progress
        elif pass_credits == 100:
            print("Progress (module trailer)\n")
            trailer += 1            #Gets the total count of trailer
        elif fail_credits >= 80:
            print("Exclude\n")
            excluded += 1           #Gets the total count of excluded
        else:
            print("Module retriever\n")
            retriever += 1          #Gets the total count of retriever

    else:
        print("Total incorrect.\n")

    while True:                                                               #Loop to check whether user entered 'y' or 'q'
        print("Would you like to enter another set of data?")
        option = input("Enter 'y' for yes or 'q' to quit and view results: ")
        if option.lower() == 'y':
            check = False
            break
        elif option.lower() == 'q':
            check = True
            break
        else:
            print("Invalid input, enter 'y' for yes or 'q' to quit and view results\n\n ")
    if check == True :
        break

            
#TASK 1 - Histogram
total = progress + trailer + retriever + excluded               #total variable assigned to print out the number of outcomes
print("\n-----------------------------------------------------")
print("Histogram")
row = ["Progress", "Trailer", "Retriever", "Excluded"]          #For printing purpose, it prints the string row wise
column = [progress, trailer, retriever, excluded]
for i in range(len(column)):                                        
    print(row[i], column[i],"\t:",(column[i] * ' *'))
print()                                                         #Leave space
print(total, " outcomes in total")
print("-----------------------------------------------------")

        


    
