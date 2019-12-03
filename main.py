"""
quizzes of what I have learned in COP1500 by chapter (activity number)
__author__ = Rylie Hurley
"""


def intro(fname):
    """
    Combines the string with the users input to greet them to the program
    :param fname:
    :return: Greets the user using the name they input
    """

    print("Hello, " + fname)


intro(input("Please enter your name: "))
q = input("Would you like to take a COP1500 quiz?: ")
chapter_quiz = 0
if q == "yes":
    bad_input = True
    while bad_input:
        try:
            chapter_quiz = int(input("Which chapter quiz would you like to "
                                     "take?(1-10): "))
            bad_input = False
        except ValueError:
            print("This is not a chapter number, please enter a NUMBER.")
    print("Okay! Let's start with chapter", chapter_quiz)

    # CHAPTER 1 QUIZ
    if chapter_quiz == 1:
        def chapter_one():
            """
            Tests the users knowledge of basic python functions
            :return: The calculated score of all questions answered correctly
            """

            question_one = input(
                "What is the output of print(2+5) in python: ")
            question_two = input("True or False, print(Hello my name is Pat) "
                                 "is a string literal: ")
            print(
                "What does a comma do in a print statement? \n a.) it outputs"
                " a comma after the print statement\n b.) It prevents the"
                " print from ending with a newline, allowing you to append a "
                "new print to the end of the line\n c.) nothing")
            question_three = input("The answer is: ")
            print(
                "What does a '#' do when placed in front of any code? \n a.) "
                "makes the code a comment and doesn't print it \n b.) makes "
                "the code a comment and prints it \n c.) nothing")
            question_four = input("The answer is: ")
            question_five = input("What does the function '*' mean?: ")
            score = 0
            if question_one == "7":
                score = score + 1
            else:
                score = score
            if question_two == "False" or question_two == "false":
                score = score + 1
            else:
                score = score
            if question_three == "b" or question_three == "B":
                score = score + 1
            else:
                score = score
            if question_four == "a" or question_four == "A":
                score = score + 1
            else:
                score = score
            if question_five == "multiplication" or question_five == \
                    "Multiplication":
                score = score + 1
            else:
                score = score
            print('Your score is: ', score, '/5!')
            print("Thanks for taking my quiz! Good Bye.")


        chapter_one()
    # CHAPTER 2 QUIZ
    elif chapter_quiz == 2:
        def chapter_two():
            """
            Tests the users knowledge of acceptable variable names in python
            :return: The calculated score of all questions answered correctly
            """

            question_one = input("Is costoffirstitem a GOOD variable name?: ")
            question_two = input("Is '1st_name' a valid variable name?: ")
            question_three = input(
                "State the output for this line of code: \n print('your name"
                " is' + 'Pat.') \nThe output is: ")
            score = 0
            if question_one == "no":
                score = score + 1
            else:
                score = score
            if question_two == "yes":
                score = score + 1
            else:
                score = score
            if question_three == "your name isPat.":
                score = score + 1
            else:
                score = score
            print('Your score is: ', score, '/3!')
            print("Thanks for taking my quiz! Good Bye.")


        chapter_two()
    # CHAPTER 3 QUIZ
    elif chapter_quiz == 3:
        def chapter_three():
            """
            Tests the users knowledge of basic math and formatting operators in
            python
            :return: The calculated score of all questions answered correctly
            """

            question_one = input(
                "State the arithmetic operation each symbol represents."
                "\n*\n**\n/\n//\n%\nUse a comma to seperate your answers: ")
            question_two = input("What is the one word that defines the '='"
                                 " symbol in a line of code: ")
            question_three = input(
                "Evaluate the following line of code.\nage = 15\nprint('your"
                " age is', age)\nWhat does the assignment statement 'age = 15'"
                " do?\na.) nothing\nb.) assigns the variable age to 15\nc.) "
                "assigns 15 to the variable age\nYour answer is: ")
            question_four = input(
                "What does it mean when the '+' sign is put in between two "
                "strings?\na.) it outputs the sum the number of letters up in"
                " the strings\nb.) it's invalid\nc.) it concatenates the two"
                " strings stored in the variables into one string.\nYour"
                " answer is: ")
            score = 0
            if question_one == "multiplication, exponent, division, " \
                               "quotient, modulus" or question_one == \
                    "Multiplication, Exponent, Division, Quotient, Modulus":
                score = score + 1
            else:
                score = score
            if question_two == "assignment" or question_two == "Assignment":
                score = score + 1
            else:
                score = score
            if question_three == "C" or question_three == "c":
                score = score + 1
            else:
                score = score
            if question_four == "c" or question_four == "C":
                score = score + 1
            else:
                score = score
            print('Your score is: ', score, '/4!')
            print("Thanks for taking my quiz! Good Bye.")


        chapter_three()
    # CHAPTER 4 QUIZ
    elif chapter_quiz == 4:
        def chapter_four():
            """
            Tests the users knowledge of main operations in python
            :return: The calculated score of all questions answered correctly
            """

            print(
                "Enter and Execute the following code\n\nnumLaptops"
                " = 7\nlaptopCost = 599.50\nprice = numLaptops * "
                "laptopCost\nprint('Total cost of Laptops: ', price)")
            question_one = input(
                "\nIf the last line of code was replaced with "
                "the following\n  print('Total cost of laptops:',format"
                "(price,'.2f'))\nWhat would the output be?: ")
            question_two = input(
                "How would you add a dollar sign to the number that was "
                "output previously?\na.) you cant\nb.) add it IN the string "
                "literal in the fourth line\nc.) add it after the string"
                " literal in teh fourth line, before price\n Your Answer: ")
            question_three = input("What will be the output if you change .2"
                                   " with .4 in the last line of code?:")
            question_four = input(
                "Computers perform four main operations on data, what are "
                "they? Seperate your answers with commas: ")
            score = 0
            if question_one == "Total cost of Laptops:  4196.50":
                score = score + 1
            else:
                score = score
            if question_two == "b" or question_two == "B":
                score = score + 1
            else:
                score = score
            if question_three == "Total cost of Laptops:  4196.5000":
                score = score + 1
            else:
                score = score
            if question_four == "input, output, process, store" or \
                    question_four == "Input, Output, Process, Store":
                score = score + 1
            else:
                score = score
            print('Your score is: ', score, '/4!')
            print("Thanks for taking my quiz! Good Bye.")


        chapter_four()
    # CHAPTER 5 QUIZ
    elif chapter_quiz == 5:
        def chapter_five():
            """
            Tests the users basic knowledge of conditional operators in python
            :return: The calculated score of all questions answered correctly
            """

            question_one = input("What operators are used to compare the "
                                 "relationship between two operands?: ")
            question_two = input("Expressions whose result can only be true "
                                 "or false are known as _____________:")
            question_three = input(
                "Assume:   word1 = 'hello' and word2 = 'good-bye'\nWhat is"
                " the result of the following expression?\nword1 < word2\nYour"
                " answer: ")
            question_four = input(
                "How do the conditional operators work when the operands"
                " are strings?\na.) it won't work because the operands need"
                " to be integers\nb.)they evaluate the first values inside "
                "the strings\nYour answer: ")
            score = 0
            if question_one == "conditional operators":
                score = score + 1
            else:
                score = score
            if question_two == "boolean expressions" or question_two == \
                    "Boolean Expressions":
                score = score + 1
            else:
                score = score
            if question_three == "false" or question_three == "False":
                score = score + 1
            else:
                score = score
            if question_four == "b" or question_four == "B":
                score = score + 1
            else:
                score = score
            print('Your score is: ', score, '/4!')
            print("Thanks for taking my quiz! Good Bye.")


        chapter_five()
    # CHAPTER 6 QUIZ
    elif chapter_quiz == 6:
        def chapter_six():
            """
            Tests the users knowledge of basic conditional formatting
            :return: The calculated score of all questions answered correctly
            """

            question_one = input(
                "What is the output of the program listed below?\n\ngrade "
                "= 95\nif grade >= 94:\nprint('Excellent!')\n\nYour answer: ")
            question_two = input("In the first question, what would be the "
                                 "output if 95 was changed to 90?: ")
            question_three = input(
                "What function is used to return a floating point number"
                " from a number or a string?: ")
            question_four = input(
                "What function allows multiple substitutions and value "
                "formatting and lets us concatenate elements within a string "
                "through positional formatting?: ")
            score = 0
            if question_one == "Excellent!":
                score = score + 1
            else:
                score = score
            if question_two == "nothing" or question_two == "Nothing":
                score = score + 1
            else:
                score = score
            if question_three == "float" or question_three == "Float":
                score = score + 1
            else:
                score = score
            if question_four == "format" or question_four == "Format":
                score = score + 1
            else:
                score = score
            print('Your score is: ', score, '/4!')
            print("Thanks for taking my quiz! Good Bye.")


        chapter_six()
    # CHAPTER 7 QUIZ
    elif chapter_quiz == 7:
        def chapter_seven():
            """
            Tests the users knowledge of function 'elif'
            :return:The calculated score of all questions answered correctly
            """

            question_one = input(
                "What is a Python keyword that represents else if and allows"
                " you to test for one of several options?: ")
            question_two = input(
                "True or False? As soon as an elif statement is tested as "
                "true, the rest of the elif statements are ignored.: ")
            question_three = input(
                "How many elif statements can there be with in"
                " an if statement?\na.) 10\nb.) 1\nc.) infinite\nd.) "
                "0\nYour answer: ")
            question_four = input(
                "Does it matter where an elif is placed within an if "
                "statement?\na.) No, they are all evaluated so they can be "
                "placed anywhere.\nb.) Yes, the first true elif statement is"
                " outputted and the rest are ignored.\nYour answer: ")
            score = 0
            if question_one == "elif":
                score = score + 1
            else:
                score = score
            if question_two == "true" or question_two == "True":
                score = score + 1
            else:
                score = score
            if question_three == "c" or question_three == "C":
                score = score + 1
            else:
                score = score
            if question_four == "b" or question_four == "B":
                score = score + 1
            else:
                score = score
            print('Your score is: ', score, '/4!')
            print("Thanks for taking my quiz! Good Bye.")


        chapter_seven()
    # CHAPTER 8 QUIZ
    elif chapter_quiz == 8:
        def chapter_eight():
            """
            Tests the users knowledge of loops and short cut operators
            :return: The calculated score of all questions answered correctly
            """

            question_one = input(
                "How does the Python interpreter know what lines of code "
                "belong to the loop body?\na.) anything after the loop is "
                "considered in the loop body\nb.) nothing\nc.) indentation\n "
                "Your answer: ")
            question_two = input(
                "State the output of the code below.\nnumber = 1\nwhile"
                " number <= 10:\n   if number % 2 == 0:\n      print(number, "
                "end = ' ')\nnumber = number + 1\n\n Your Answer:")
            question_three = input(
                "What structure is where you know the number of times it"
                " will execute is known as a count-controlled loop: ")
            question_four = input(
                "____________  _______ provide a concise way of creating"
                " assignment statements when the variable on the left-hand "
                "side of the assignment statement is also on the right-hand"
                " side.\nThe addition short-cut operator (+=) is usually "
                "used for incrementing a variable.: ")
            score = 0
            if question_one == "c" or question_one == "C":
                score = score + 1
            else:
                score = score
            if question_two == "2 4 6 8 10":
                score = score + 1
            else:
                score = score
            if question_three == "looping structure" or question_three == \
                    "Looping Structure":
                score = score + 1
            else:
                score = score
            if question_four == "short-cut operators" or question_four == \
                    "Short-Cut Operators":
                score = score + 1
            else:
                score = score
            print('Your score is: ', score, '/4!')
            print("Thanks for taking my quiz! Good Bye.")


        chapter_eight()
    # CHAPTER 9 QUIZ
    elif chapter_quiz == 9:
        def chapter_nine():
            """
            Tests the users knowledge of intermediate functions and FOR loops
            :return: The calculated score of all questions answered correctly
            """

            question_one = input("What is a python function that is used to"
                                 " define a series of numbers and can be "
                                 "used\nin a FOR loop to determine the number"
                                 " of times the loop is executed.: ")
            question_two = input("What function converts what is in"
                                 " parentheses ( ) to a String, if it is "
                                 "not a string already?: ")
            question_three = input("What is a variable that stores the sum "
                                   "of a group of values?: ")
            question_four = input("What loop can you include a list of values"
                                  " in place of the range() function?: ")
            score = 0
            if question_one == "range" or question_one == "Range":
                score = score + 1
            else:
                score = score
            if question_two == "str()":
                score = score + 1
            else:
                score = score
            if question_three == "accumulator" or question_three == \
                    "Accumulator":
                score = score + 1
            else:
                score = score
            if question_four == "for" or question_four == "FOR" or \
                    question_four == "for loop" or question_four == "FOR loop":
                score = score + 1
            else:
                score = score
            print('Your score is: ', score, '/4!')
            print("Thanks for taking my quiz! Good Bye.")


        chapter_nine()
    # CHAPTER 10 QUIZ
    elif chapter_quiz == 10:
        def chapter_ten():
            """
            Tests the users knowledge of FOR loops
            :return: The calculated score of all questions answered correctly
            """

            question_one = input("A loop within another loop is known as...: ")
            print("Use the following informtion to answer questions 2-4")
            print("name = input('What is your name: ')")
            print("for x in range(5):")
            print("   for x in range(3): ")
            print("     print(name + ' ', end = ' '")
            print("   print()")
            question_two = input("How many FOR loops are in this code?: ")
            question_three = input("Is one loop completely executed before "
                                   "the next loop begins?: ")
            question_four = input(
                "print(name + ' ', end = ' ')\nHow many times is the following"
                " line of code executed in the program?: ")
            score = 0
            if question_one == "nest loop" or question_one == "nest":
                score = score + 1
            else:
                score = score
            if question_two == "2":
                score = score + 1
            else:
                score = score
            if question_three == "yes" or question_three == "Yes":
                score = score + 1
            else:
                score = score
            if question_four == "5":
                score = score + 1
            else:
                score = score
            print('Your score is: ', score, '/4!')
            print("Thanks for taking my quiz! Good Bye.")


        chapter_ten()

else:
    print("Thanks for trying my quiz!")
