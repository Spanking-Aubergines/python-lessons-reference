
questions= ("How many buttons does a mouse have ?",
            "What side do Europeans drive on ?",
            "How many wheels does a bike have ?")
options= (("A. 2", "B. 9", "C. 1"),
          ("A. left", "B. right", "C. middle"),
          ("A. three", "B. none", "C. two"))
answers= ("A","B","C")
guesses = []
score = 0
question_num=0

# for x in range (len(questions)):
#     print(questions[x])
#     print (options[x])
#     resp=input("Choose an option (A - B - C) :")
#     if resp == answers[x]:
#         print("Correct answer")
#     else:
#         print("Incorrect answer")

for question in questions:
    print("---------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = str(input("Guess: ").upper())
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct answer")
    else:
        print("Incorrect answer")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("*------------------------*")
print("*         RESULTS        *")
print("*------------------------*")

print("Answers: ",end="")
for answer in answers:
    print(answer, end=" ")
print()
print("Guesses: ",end="")
for guess in guesses:
    print(guess, end=" ")

score = int(score /len(questions) * 100)
print(f"Your socre is: {score}%")