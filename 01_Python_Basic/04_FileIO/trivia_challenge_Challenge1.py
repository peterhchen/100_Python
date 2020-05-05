# Trivia Challenge
# Trivia game that reads a plain text file
"""
Challenge 1: Improve the Trivia Challenge game so that each question has a
unique point value associated with it. The player's score should be the total
of all the point values of the questions he or she answers correctly.

Steps:
    - Generate a simpler trivia.txt file with 1 question
    - Add a new line at the end of the question with point value
    - Adjust the next_block() routine to to read the extra line
    - Convert the value to an integer (NOTE: need to add an error check)
    - Return it as a new value from calls to next_block
    - Track it in the return variables from next_block calls
    - Define a new variable in main to track total difficulty across questions
    - If answer is correct, in addition to incrementing score, increment tot Difficulty
    - At the end, print out value of total difficulty score 
"""
import sys

def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    print("Starting next_block")
    """Return the next block of data from the trivia file."""
    category = next_line(the_file)
    
    question = next_line(the_file)
    
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
        
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
        
    explanation = next_line(the_file)
    
    
    # WF - Adding a weight to each question to reflect difficulty
    diff = next_line(the_file)
    if diff:                               # IF we read a line, then convert/save
        difficulty = int(diff)             # amake sure it's an int
    else:
        difficulty = 0                     # If line wasn't valid set to 0
   
    # WF - print out all the question fields to make sure each is clean
    """
    print("\n")
    print("category=",category)
    print("category=",question)
    print("answers=",answers)
    print("explanation",explanation)
    print("diff=",diff,"difficulty=",difficulty,"\n")
    """
    
    # WF - Return new difficulty value
    return category, question, answers, correct, explanation, difficulty

def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to Trivia Challenge!\n")
    print("\t\t", title, "\n")
 
def main():
    # WF, change the file name to one we have updated
    trivia_file = open_file("trivia_challenge_challenge1.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0
    
    # WF Track difficulty separately as a local scope variable in main()
    total_difficulty = 0

    # get first block
    
    # WF Update return list from next_block to include new difficulty value
    category, question, answers, correct, explanation, difficulty = next_block(trivia_file)
    while category:
        # ask a question
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # get answer
        answer = input("What's your answer?: ")

        # check answer
        if answer == correct:
            print("\nRight!", end=" ")
            score += 1
            
            # WF increment total_difficulty to reflect new answer 
            total_difficulty += difficulty
        else:
            print("\nWrong.", end=" ")
        print(explanation)
        print("Score:", score, "\n\n")

        # get next block
        
        # WF Update return list from next_block to include new difficulty value
        category, question, answers, correct, explanation, difficulty = next_block(trivia_file)

    trivia_file.close()

    print("That was the last question!")
    print("You're final score is", score)
    
    # WF print out the final value of total difficulty score
    print("You're total difficulty score is", total_difficulty)
 
main()  
input("\n\nPress the enter key to exit.")
