#REVIEW DEMO 1: Practice 1 Solution

#Follow the documented directions to analyze and solve the below program prompt.  Make note of anything you do not feel comfortable with so you are prepared with questions for Week #2's Review Demo


#PROGRAM PROMPT
#Write a program that calculates a student's average grade.  Assume each grade has an equal weight, but the student should be able to enter as many grades as they wish.  Once they are done entering grades, print their average grade in both numerical as well as letter form.

#STEP 1: Analyze the Problem --> use in-file documentation to answer the following:

#What do you KNOW form the problem
#-looking for average ---> average = sumTotal / numItems
#-input grades, all grades are equal weight, unknown number o grades


#What information will you NEED TO KNOW (gather from user) in order to SOLVE the PROBLEM
#-user needs to provide grades (input)
#-number of grades

#What FINAL SOLUTION (describe what types of data ie miles, total money, average student grade etc) is expected for this problem
#-numeric average & letter average


#FUNCTIONS----------------------------------------------------------
#functions must be defined before they are called by the base program
#FUNCTION DEFINITION: to define a function is to write its full code (so that it is usable and callable within the program)

def goodbye(): #<-- FUNCTION HEADER

    print("\n\n\nThank you & Goodbye!")

def letterAvg(gradeA):

    if(gradeA >= 90):
    
        letter = "A"
    elif(gradeA >= 80):

        letter = "B"
    elif(gradeA >= 70):
    
        letter = "C"
    elif(gradeA >= 60):

        letter = "D"
    else: #else NEVER has a condition

        letter = "F"  

    return letter  #return value REPLACES the call to the function
                    #you should not have code after your return line (it won't work!)




#BASE PROGRAM-------------------------------------------------------

#Step 2: Initialize Variables
#INITIALIZE: assign a starting value

sumTotal = 0 #starts at 0 so grades can be added

numGrades = 0 #holds total num of grades entered

#answer = "y" #holds user's response, controls loop

answer = input("Enter 'y' to start program / 'n' to quit: ")
answer = answer.lower() #forces value to lowercase

#restrict user to only reply with y or n
while answer != 'y' and answer != 'n': 

    print("**ERROR**")
    answer = input("Enter 'y' to start program / 'n' to quit: ")
    answer = answer.lower() #forces value to lowercase
    

#Step 3: Create Control Flow Statement w/ Conditional Statement

while answer == "y":
    
    
    #Step 4: Gather data and process
    grade = float(input("\nEnter a grade: "))
    #numeric types (int/float) need to be CAST during input if you are looking to mathematically process them    

    sumTotal = sumTotal + grade #sumTotal += grade

    numGrades = numGrades + 1 #numGrades += 1

    #print(grade)
    #print(numGrades)

    #Step 5: Create a startegy to Exit Loop
    answer = input("Would you like to continue? y for yes: ")

    #lower below, unnecessary b/c of condition
    answer = answer.lower()

    #restrict user to only reply with y or n
    while answer != 'y' and answer != 'n': 

        print("**ERROR**")
        answer = input("Enter 'y' to start program / 'n' to quit: ")
        answer = answer.lower() #forces value to lowercase

        if answer == 'n':
            print("sad to see you go!")
    


#average = sumTotal / numItems
gradeAvg = sumTotal / numGrades #processing outside of loop for efficiency



#find letter grade equivalent
#moved to letterAvg(), call below
letG = letterAvg(gradeAvg)



#Step 6: Display final data
print("TOTAL GRADES ENTERED: {0} \nGRADE AVERAGE: {1} \nLETTER GRADE: {2}".format(numGrades, gradeAvg, letG))


#print("\n\n\nThank you & Goodbye!") #moved to function -> goodbye()
#FUNCTION CALL IS BELOW
goodbye()










