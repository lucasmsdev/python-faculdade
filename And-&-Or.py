#1 -Write a program that asks the user to input three numbers and then determines whether one of the three numbers is greater than the sum of the other two.

#First solution:
num1 = float(input('Enter with a number: \n'))
num2 = float(input('Enter with a number: \n'))
num3 = float(input('Enter with a number: \n'))

num1_bigger = num1 > num2 + num3
num2_bigger = num2 > num1 + num3
num3_bigger = num3 > num1 + num2

if num1_bigger == True:
    print("There's a number bigger than the sum of the two others. This number is: ", num1 )

elif num2_bigger == True:
    print("There's a number bigger than the sum of the two others. This number is: ", num2 )

elif num3_bigger == True:
    print("There's a number bigger than the sum of the two others. This number is: ", num3 )

else:
    print("There's no number bigger than the sum of the two others.")

#Second solution:
num1 = float(input('Enter with a number: \n'))
num2 = float(input('Enter with a number: \n'))
num3 = float(input('Enter with a number: \n'))

num1_bigger = num1 > num2 + num3
num2_bigger = num2 > num1 + num3
num3_bigger = num3 > num1 + num2

if num1_bigger or num2_bigger or num3_bigger:
    print("There's a number bigger than the sum of the two others.")
else:
    print("There's no number bigger than the sum of the two others.")


#2 - Write a program that asks the user to enter two grades (between 0 and 100) and determine if the student passed or not. A student passes if the sum of the grades is greater than or equal to 60 and no grade is less than 40.

firstGrade = float(input())
secondGrade = float(input())

finalGrade = firstGrade + secondGrade
isItTrue = firstGrade >= 40 and secondGrade >=40

if finalGrade >= 60 and isItTrue:
    print('Congratulations! You passed.')

elif finalGrade < 60:
    print('You didnt passed! :c')

else:
    print('Enter with a grade between 0-100')


#3 -Check if a person is 18 years or older or if they have parental authorization.
age = int(input())

if age < 18:
    print("You're ", age, " years old! So you need a permission to get in here.")
    permission = input("Do you have one? Type Y if you have, and N if you don't. \n")

    if permission == 'Y' or permission == 'y':
        print('Get in there and have a good night!')
    elif permission == 'N' or permission == 'n':
        print("Sorry! You can't enter today. Try when you get 18 or get a permission.")
    else:
        print('ERROR! Type Y or N, any value different will let us here.')
else:
    print("You're 18 years old! Don\'\t worry")

#4 - Write a code that checks if a number is even or divisible by 3.

number = float(input())

isAnEvenNumber = number % 2
div_by_three = number % 3

if isAnEvenNumber == 0:
    print("It's a even number!")
if div_by_three == 0: 
    print("It's a number divisible for 3")

#5 -Write a code that verifies that a person is literate (knows how to read and write) and is over 25 years old.

print("Hello! Welcome to our forms. Could you answer this questions?")
print('')

write = int(input("Do you know how to write? \n 1 - YES \n 2 - NO "))
read = int(input("Do you know how to read? \n 1 - YES \n 2 - NO "))
age = int(input("What's your age? \n"))

if write == 1 and read == 1 and age >= 25:
    print('Verified!')
else: 
    print('Iliterate.')

#6 - Create a program that checks if a person has a discount on a product, based on age and category (student, retired, etc.) and on the day of the week. (Use as many categories as you like)

#First solution (Simple with no library, just an def.)

def weekday_discount(weekday):
    weekdays = ['Monday', 'monday', 'Tuesday', 'tuesday', 'Wednesday', 'wednesday', 'Thursday', 'thursday']
    weekend = ['Friday', 'friday', 'Saturday', 'saturday', 'Sunday', 'sunday']

    if weekday in weekdays:
        print('During the week we give 10% off in the tickets.')
    elif weekday in weekend:
        print('We are on the weekend, so our tickets receive 15% up in price.')
    else:
        print("ERROR! Enter with a weekday.")


print("Welcome to CineTicket!")
print('')

age = int(input('Enter with your age: \n'))

weekday = input("Wich day of the week today is? \n")

print('')
print('-----------------------------')
print('')

print("Wich category are you in?")
print('')

print('1- Student') 
print('2- People with Disabilities')
print('3- Elderly') 
print('4- Blood Donor')
print('5- Low Income') 
print('6 - No one')

print('')

category = input('Enter with the category: \n')


if category == 1 or category == '1- Student':
    print('So you are a student! Remember to bring yourcome of up to two minimum wages.')
    print("")
    print(weekday_discount(weekday))

elif category == 2 or category == "2- People with Disabilities":
    print('Okay! have a good night.')
    print('')
    print(weekday_discount(weekday))

elif category == 3 or category == '3- Elderly':
    
    if age >= 65:
        print('You can use this discount. And remember to bring your doc.')
        print("")
        print(weekday_discount(weekday))
    else:
        print("You can't use this discount. Sorry! Try to use another discount.")
        print('')
        print(weekday_discount(weekday))

elif category == 4 or '4- Blood Donor':
    print('You can use this discount but remember to bring your doc to valide.')
    print('')
    print(weekday_discount(weekday))


elif category == 5 or '5- Low Income' or '5- low income' or '5- Low income':

    print('Ok, now to use this discount you need to valide some informations.') 

    age = int(input("First at all, what's your age? \n "))
    register = input("Do you have a register in Cadastro Único (CadÚnico)? Type Y if it's true or type N if it's not true. \n")

    if age <= 14 and  register != 'Y' or register != 'y':
        print("You can't use this discount. Sorry try to look for another.")
        print('')
        print(weekday_discount(weekday))

    if age >= 15 and register == 'Y' or register == 'y':
        print("You have acess at this discount. Remember to bring your card to valide.")
        print('')
        print(weekday_discount(weekday))

elif category == 6 or category == '6- No one':
    print("You do not have category. Let's search for the ticket in the convenient price.")
    print('')
    print(weekday_discount(weekday))
else:
    ('Try to type a valide category.')
    print('')
    print(weekday_discount(weekday))


#Second solution - I don't know if its works.

#from datetime import datetime

#currently_datatime = datetime.now()

#def weekday_discount(currently_datatime):
#    weekdays = ['Monday', 'monday', 'Tuesday', 'tuesday', 'Wednesday', 'wednesday', 'Thursday', 'thursday']
#    weekend = ['Friday', 'friday', 'Saturday', 'saturday', 'Sunday', 'sunday']

#    if currently_datatime in weekdays:
#        print('During the week we give 10% off in the tickets.')
#    elif currently_datatime in weekend:
#        print('We are on the weekend, so our tickets receive 15% up in price.')
#    else:
#        print("ERROR! Enter with a weekday.")
                     
    