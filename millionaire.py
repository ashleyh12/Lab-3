# Lab-3
Conditionals &amp; String Functions

# Solving "Who wants to be a millionaire?" 

# Who wants to be a Millionaire??
 
# The progression in this "short" version of millionaire should be:
# 1 answer correct: $500
# 2 answers correct: $1000
# 3 answers correct: $5000
# 4 answers correct: $20000 
# 5 answers correct: $50000
# 6 answers correct: $250000
# 7 answers correct: $500000
# 8 answers correct: $1000000

# Your code here!
name = input("Welcome to Millionaire! What is your name? ")
money_made = 0 
print("Currently you have made" + " $" + str(money_made))
question_1 = input("Mount Killimanjaro is the tallest summit on which continent?  a. Asia  b. Africa  c. Europe d. Australia   Your answer: ")

while True: 
  if question_1 == "b": 
    print("Correct!")
    money_made = 500
    print("Currently you have made" + " $" + str(int(money_made)))
  else:
    print("I'm sorry, that is incorrect")
    print(money_made)
    break

 
  question_2 = input("Which of these US presidents appeared on the television series Laugh in?  a. Lyndon Johnson b. Jimmy Carter c. Richard Nixon  d. Gerald Ford   Your answer: ")

  if question_2 == "c":
    print("Correct!")
    money_made = 1000
    print("Currently you have made" + " $" + str(int(money_made)))
  else:
    print("I'm sorry, that is incorrect")
    print(money_made)
    break


  question_3 = input("The Earth is approximately how many miles away form the sun? a. 9.3 million b. 39 million c.  93 million, d. 193 million   Your answer: ")

  if question_3 == "a":
    print("Correct!")
    money_made = 5000
    print("Currently you have made" + " $" + str(int(money_made)))
  else:
    print("I'm sorry, that is incorrect")
    print(money_made)
    break

  question_4 = input("What insect was found inside the computer of scientist Grace Hopper? a. fly b. Japanese beetle c. moth d. roach    Your answer: ")

  if question_4 == "c":
    print("Correct!")
    money_made = 20000
    print("Currently you have made" + " $" + str(int(money_made)))
  else:
    print("I'm sorry, that is incorrect")
    print(money_made)
    break

  question_5 = input("Which of the following men does not have a chemical element named after him? a. Albert Einstein b. Niels Bohr c. Isaac Newton d. Enrico Fermi   Your answer: ")

  if question_5 == "c":
    print("Correct!")
    money_made = 50000
    print("Currently you have made" + " $" + str(int(money_made)))
  else:
    print("I'm sorry, that is incorrect")
    print(money_made)
    break

  question_6 = input("In the children's book, where is Paddington Bear originally from? a. India b. Peru c. Canada d. Iceland   Your answer: ")

  if question_6 == "b":
    print("Correct!")
    money_made = 250000
    print("Currently you have made" + " $" + str(int(money_made)))
  else:
    print("I'm sorry, that is incorrect")
    print(money_made)
    break

  question_7 = input("Who invented the first mass-produced helicopter? a. Igor Sikorsky b. Elmer Sperry c. Ferdinand von Zepplin d. Gottlieb Daimler   Your answer: ")

  if question_7 == "a":
    print("Correct!")
    money_made = 500000
    print("Currently you have made" + " $" + str(int(money_made)))
  else:
    print("I'm sorry, that is incorrect")
    print(money_made)
    break

  question_8 = input("What is the approximate number of people who have ever lived on earth? a. 50 billion b. 100 billion c. 1 trillion d. 5 trillion   Your answer: ")

  if question_8 == "b":
    print("Correct! You are a millionaire")
    money_made = 1000000000
    break

  else:
    print("I'm sorry, that is incorrect")
    print(money_made)
    break
  
