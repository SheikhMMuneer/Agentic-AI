# ----------------------------------
# TASK 1- CONDITIONAL STATEMENTS
# ----------------------------------

# 1.1- Divisibility Checker
# - Ask the user to enter an integer number.
# - Check if the number is divisible by 3.
# If divisible, print: "<number> is divisible by 3".
# Otherwise, print: "<number> is NOT divisible by 3".
# This tests your understanding of basic if/else logic

def Divisibility():
    if (user_number := input("Enter an Integer number: ")) and user_number.isdigit():
        if int(user_number) % 3 ==0:
            print(f"{user_number} is divisible by 3")
        else:
            print(f"{user_number}  is NOT divisible by 3")
    else:
        print("Invalid input. Please enter an Integer number Only.")

Divisibility()

# 1.2-Even/Odd with Sign Detection
# - Ask the user to enter any integer.
# - If the number is greater than zero:
# - Determine whether the number is even or odd.
# - Print: "Positive Even Number" or "Positive Odd Number".
# If the number is exactly zero, print: "The number is zero".
# - If less than zero, print: "Negative Number".
# This tests conditional nesting and number classification.

def Get_Even_Odd_Number():
    num: int = int(input("Enter any Integer number for knowing Even or Odd Number: "))
    if num > 0:
        if num%2==0:
            print("Positive Even Number.")
        else:
            print("Positive Odd Number.")
    elif num < 0:
        print("Negative Number.")
    else:
        print("The number is zero.")

Get_Even_Odd_Number()


# 1.3-Grade Evaluator
# - Ask the user to enter a score between 0 and 100.
# - Use if/elif/else to assign a grade:
# -A: 90-100
# -B: 75-89
# C: 50-74
# -D: 35-49
# - Fail: below 35
# Print L a message like "Excellent", "Good", "Needs Improvement", etc.
# Demonstrates multi-condition evaluation.


def GradeEvaluator():
    score: int = int(input("Enter enter a score between 0 and 100: "))
    grade: str = None
    remarks: str = None

    if score >= 90:
        grade = "A"
        remarks="Excellent"
    elif score >= 75:
        grade = "B"
        remarks = "Good"
    elif score >= 50:
        grade = "C"
        remarks = "Fair"
    elif score >= 35:
        grade = "D"
        remarks = "Needs Improvement"
    else:
        grade = "F"
        remarks = "Fail"

    print(f"you got grade \"{grade}\" - \"{remarks}\"")

GradeEvaluator()

# 1.4-Leap Year Checker
# Ask the user to enter a year.
# - Apply leap year rules:
# - Year divisible by 4'n possible leap year
# - But if divisible by 100'n must ALSO be divisible by 400
# Print whether the year is leap or not.
# This tests compound conditions.

def LeapYearChecker():
    year: int = int(input("Enter enter a year: "))

    if year%100==0:
        if year%400==0:
            print(f"The year {year} is leap year")
        else:
            print(f"The year {year} is not leap year")
    elif  year%4==0:
        print(f"The year {year} is  leap year")
    else:
      print(f"The year {year} is not leap year")

LeapYearChecker()

# ------------------------------------
# TASK 2- BASIC LOOPS (FOR + WHILE)
# ------------------------------------

# 2.1-Print Numbers 1 to 10
# - Use a for loop.
# - Print each number on a new line.

def Print_Numbers():
    for num in range(1,11):
        print(num)

Print_Numbers()


# 2.2-Sum of First N Natural Numbers
# - Ask the user for a positive integer N.
# - Use a while loop to calculate the sum from 1 to N.
# Print the result.
# This tests accumulators and loop iteration.

def Sum_Of_Natural_Numbers():
    i: int = 1
    total: int = 0
    positive_number: int = int(input("Enter positive integer: "))

    while(i<= positive_number):
        total = total+i
        i = i+1

    print(f"Sum is {total}")

Sum_Of_Natural_Numbers()

# 2.3-Print Even Numbers Up To N
# Ask the user for integer N.
# Use a for loop to print all even numbers up to N.
# This checks conditional checking inside loops.

def Even_Numbers():
    user_number: int = int(input("Enter any integer number: "))
    for num in range(1,user_number+1):
        if num%2==0:
            print(num,end='\n')


Even_Numbers()

# 2.4-Countdown Timer
# - Ask user for a starting number.
# - Use a while loop to count down to 1.
# - After the countdown ends, print "Liftoff!".
# - This tests decrementing loops.

def CountdownTimer():
    user_number: int = int(input("Enter any starting number: "))
    while(user_number>=1):
        print(user_number)
        user_number-=1

    print( "Liftoff!")

CountdownTimer()

# ------------------------------------------------
# TASK 3- LOOP CONTROL (break, continue, else)
# ------------------------------------------------

# 3.1-Divisibility Search with break
# - Ask user for a list of numbers.
# -Ask for a number K.
# -Loop through the list.
# - Find the first number divisible by K.
# - Stop the loop using break.
# - Print result. If no number matches, print a "not found" message.

def Divisibility_Search_With_Break():
    numbers_list: list = list(map(int,input("Enter list of number seperated by space: ").split()))
    k: int = int(input("Enter any  number K:"))

    while k==0:
        print("K value cannot be 0")
        k: int = int(input("Enter any  number K other than 0:"))

    for number in numbers_list:
        if number%k==0:
            print(f"Number found:{number}")
            break
    else:
        print("not found")

Divisibility_Search_With_Break()

# 3.2-Skip Negative Numbers using continue
# -Ask user for a list of integers.
# - Loop through them.
# - Print only non-negative numbers.
# - Skip negatives with continue.
# - Tests selective execution inside loops.

def Non_Negative_Numbers():
    numbers_list: list = list(map(int,input("Enter list of number seperated by space: ").split()))
    for num in numbers_list:
        if num < 0:
            continue
        else:
            print(num)

Non_Negative_Numbers()


# 3.3-Loop with else Clause
# - Ask user for a list and a target K.
# - Search for K in the list.
# - If found, print index and break.
# - If loop completes normally, execute loop's else: print "Not found".
# - Tests understanding of Python's special loop-else behavior.

def Loop_With_Else_Clause():
    numbers_list: list = list(map(int, input("Enter list of number seperated by space: ").split()))
    k: int = int(input("Enter any  number K:"))

    for index, num in enumerate(numbers_list):
        if num == k:
            print(f"{k} found at Index {index}")
            break
    else:
        print("Not found")

Loop_With_Else_Clause()



# --------------------------------
# TASK 4- NESTED & MIXED LOGIC
# --------------------------------

# 4.1 - Multiplication Table (Nested Loops)
# - Ask user for integer N.
# Print full multiplication tables from 1 to N.
# - Demonstrates nested for loops.

def Multiplication_Table():
    last_table_number: int = int(input("Enter any  number for Multiplication Tables Run :"))
    for outer in range(1,last_table_number+1):
        print(f"Multiplication table for {outer}:")
        for inner in range(1, 11):
            print(f"{outer} * {inner} = {outer * inner}")
        print()

Multiplication_Table()


# 4.2-Prime Number Checker
# - Ask for a number greater than 1.
# - Use a loop to test whether it has any divisor.
# - Print "Prime" or "Not Prime".
# - Encourages algorithmic thinking.

def Check_Prime_Number():
    prime_number: int = int(input("Enter any  number greater than 1 :"))
    is_prime: bool = True
    while prime_number==1:
        print("Number cannot be 1")
        prime_number: int = int(input("Please Enter any number greater than 1 :"))

    for number in range(2,prime_number+1):
        if (prime_number%number==0 and number!=prime_number):
            is_prime = False
            break

    print("Not Prime" if not is_prime else "Prime")

Check_Prime_Number()


# 4.3- Fibonacci Sequence Generator
# - Ask for N terms.
# - Generate Fibonacci sequence using a loop.
# - Print the complete series.

def Fabonacci_Series():
    series_number: int = int(input("Enter any number for Fabonacci Series term :"))
    a: int = 0
    b: int = 1
    count: int = 0

    while(count < series_number):
        print(a , end= ' ')
        a,b = b, a+b
        count+=1

Fabonacci_Series()


# 4.4- Menu-Driven Program
# Display menu:
# 1) Greet me
# 2) Multiplication table
# 3) Exit
# Use a loop to keep showing the menu.
# - Use conditionals to run selected actions.
# - Exit only when user chooses option 3.
# - Tests control flow in a practical scenario.

def InfiniteInputCalling():
    while True:
        menu: int = int(input("""Enter the Number: 
        1 for Greeting  
        2 for Multiplication Table  
        3 for exit from Program :"""))

        if menu == 1:
            print("Greet me")
        elif menu == 2:
            Multiplication_Table()
        elif menu == 3:
            break

InfiniteInputCalling()

# ____________________________________
# TASK 5- CHALLENGE/ADVANCED PROBLEMS
# ____________________________________

# 5.1- Number Guessing Game
# - Randomly generate a number between 1 and 100.
# - Ask the user to guess.
# - Give hints: "Too high" /"Too low".
# - Continue until correct guess.
# - Tests loops + conditions + interaction.

from random import randint
def Guessing_Game():

    rand_number = randint(1, 10)
  # print(rand_number)

    while True:
        user_guess: int = int(input("Enter the Number to match with Random Number:"))
        if user_guess > rand_number:
            print("Too high")
        elif user_guess < rand_number:
            print("Too low")
        elif user_guess == rand_number:
            print("You guess correctly Yahooo")
            break

Guessing_Game()

# 5.2- Star Pyramid Pattern
# Ask for N.
# - Print a centered pyramid of stars of height N.
# - Requires nested loops and spacing logic.


def PyramidStarPattern():
    user_height: int = int(input("Enter the Number for Height of Star Pyramid:"))
    star = '*'

    for i in range(1,user_height+1):
                str_string: str = star * (2*i-1)
                strspace: int =  user_height - i

                print(' '*strspace, end = '')
                print(str_string)

PyramidStarPattern()


# 5.3-Odd-Even Counter from List
# Ask for a list of integers.
# - Count:
# - Total evens
# - Total odds
# - Positives/ negatives/zeros
# - Print results.

def Odd_Even_Counter():
    numbers_list: list = list(map(int, input("Enter list of Integers seperated by space: ").split()))
    numers_count = len(numbers_list)
    even_counter,odd_counter,positive_counter,negative_counter,zero_counter = 0,0,0,0,0

    for number in numbers_list:
        if number < 0:
            negative_counter+=1
        elif number > 0:
            positive_counter+=1
            if number%2==0:
                even_counter+=1
            else:
                odd_counter+=1
        else:
            zero_counter+=1

    print(f" - Count:{numers_count} \n - Total evens : {even_counter} \n - Total odds : {odd_counter} \n - Positives/ negatives/zeros : {positive_counter}/{negative_counter}/{zero_counter}")

Odd_Even_Counter()


# 5.4-Collatz Sequence
# - Ask for integer N.
# Apply:
# - If even: n = n/2
# - If odd: n = 3n+1
# - Continue until n becomes 1.
# Print sequence.


def Collatz_Sequence():
    user_number: int = int(input("Enter the Number for Collatz Sequence:"))
    list_seq = []

    list_seq.append(user_number)

    while(user_number!=1):
        if user_number%2==0:
            user_number = user_number/2
        elif user_number%2== 1:
            user_number = 3*user_number+1

        list_seq.append(user_number)

    print(list_seq)

Collatz_Sequence()