#Week 4: Introduction to Lists

#Lists can hold multiple points of data and store them to "memory" to be used later on in our program

#below is a hand-populated list (not from file)
#list1 holds a series of names

list1 = ["Sam", "Mary", "Bill", "Adam", "Betty"]

#print full list - looks like print(rec) in data import demo
print(list1)

#LIST: store multiple data values (of the same type!) to RAM (memory) ie our program can remember a group of values, as long as they have a position (index) in the list
print() #for spacing in console

#print the list each data point at a time
#0 --> FIRST INDEX!
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])

num_records = len(list1) #len() is a LENGTH FUNCTION
#len() returns the length of the list/item you pass it
print("\nNUM RECORDS in LIST1: ", num_records)
#the LENGTH of a list is always +1 more than the highest index # (position in the list! starts at 0)

print()#for console space
print()

#a BETTER way to print (and PROCESS) a full list w contents is using the . . . F O R  L O O P !
#for loops were made for lists :]
print("Printing from a FOR LOOP!\n")

for index in range(0, num_records):
    #the loop starts at index 0 ( [0] ) and it will run for num_records # of times (includes 0)
    #IE the loop will run num_records number of times, or for each position held by a list item

    print("INDEX#", index, "\t", list1[index])
    #index MUST be used in combo with list1 (or other list names) in order to find specific value in list at that position
    #index is the position of the stored values
    #each index reps a different value position in the list

#-----------------------------------------------------

#three new lists, now with DIFFERENT types of data...
list2 = ["Sam", "18", "32000"]
list3 = ["Mary", "21", "34000"]
list4 = ["Tom", "24", "38000"]
#lists above look like a RECORD as opposed to a FIELD when considering a text file

#RECORD --> multiple data values, all different kinds
#FILED  --> multiple data values, all same kind

#to store a data file's records (which are read as lists) into actual lists (values stored to RAM):

#STEP 1: CREATE EMPTY LISTS
#each FIELD should have its own list
name = [] #empty list called 'name'
age = [] #empty list called 'age'
salary = [] #empty list called 'salary'
#the above lists are EMPTY -- they have no values stored in them

#STEP 2: ADD ELEMENTS TO THE LIST (POPULATING THE LISTS)
name.append(list2[0]) #adds index0 of list2 to 'name'
name.append(list3[0])
name.append(list4[0])

print()
print("Array 'name' contents: ", name)
print("name[1]: ", name[1])

#REMEMBER: it's easier/more efficient to do this in a FOR LOOP
for index in range(0, 3):
        print(name[index])

print("Part 1 of demo complete ... \n\n")

#PART 2 -------- FILE IMPORT REVIEW / APPENDING DATA FROM FILES TO LISTS!---------------------------------
print("----------------------------------------------")
print("\n\n")

#BEFORE STARTING: CHECK THE TEXT/CSV FILE!
#STEP 1: import CSV library
import csv 

#STEP 2: initialize num_records to 0
num_records = 0 

#STEP 3: create empty lists to populate with text file data
name = []
age = []
salary = []
#NOTE: there is an array for each field in the text file

#STEP 4: connect to data file
with open("C:/Users/KTRUCHON/Downloads/example.csv") as csvfile: #SCHOOL
#with open("C:/Desktop/SE126/example.csv") as csvfile: #HOME

    #STEP 5: allow data to be "read"
    file = csv.reader(csvfile)

    #STEP 6: process data in a for loop
    for rec in file:

        #STEP 7: increment (+1) num_records
        num_records += 1 #num_records = num_records + 1

        #STEP 8: append (add) values from each field to its corresponding list
        name.append(rec[0]) #name is held in 1st field
        age.append(int(rec[1])) #age is held in 2nd field
        salary.append(float(rec[2])) #salary is held in 3rd field

        #rec[1] and rec[2] have been CAST as they are appended for easier numeric processing

        #rec[#] represents the FIELD of data, rec is one full record of data
print("Finished processing file.\n\n")

#once values have been stored into the lists, now you can process them as many times as you'd like!
#when you hear "process" in relation to lists think FOR LOOP!

#processing of the lists should happen AFTER the with open() statement (no longer indented)

#process the lists to print:
for index in range(0, num_records):

    print("INDEX: ", index, "\t", name[index], "\t", age[index], "\t $", salary[index])

print("Finished processing lists for: printing.\n\n")

#process the age list to find the avg age:
age_total = 0 #need a sum total var for averages

for index in range(0, num_records):

    age_total += age[index] #age_total = age_total + age[index]
    #adds each value of age stored in list to age_total
print("Finished processing age list for: avg age.\n")
avg_age = age_total / num_records
print("AVG AGE IN FILE: ", avg_age, "yrs\n\n")

#process the salary list to find average salary:
sal_total = 0

for index in range(0, num_records):

    sal_total += salary[index]

print("Finished processing for: avg salary.\n")

avg_sal = sal_total / num_records

print("AVG SALARY IN FILE: ${:.2f}".format(avg_sal))


#FINAL 2 FOR LOOPS COULD HAVE BEEN DONE AT THE SAME TIME:
age_total = 0
sal_total = 0
for index in range(0, num_records):

    age_total += age[index] #age_total = age_total + age[index]
    #adds each value of age stored in list to age_total

    sal_total += salary[index]
    #adds each value of salary stored in list to sal_total

print("Finished processing for: avg age, avg salary.\n")

avg_age = age_total / num_records
avg_sal = sal_total / num_records
print("AVG AGE: {0} | AVG SALARY: ${1:.2f}".format(avg_age, avg_sal))






