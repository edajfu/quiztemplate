from questions import quiz


def check_ans(question, ans, attempts, score):

    if quiz[question]['answer'].lower() == ans.lower():
        print(f"Correct Answer! \nYour score is {score + 1}!")
        return True
    else:
        print(f"The answer is {quiz[question]['answer']}, not {answer!r}")
        return False


def print_dictionary():
    for question_id, ques_answer in quiz.items():
        for key in ques_answer:
            print(key + ':', ques_answer[key])


def intro_message():

    print("Welcome to the quiz! \nAre you ready?")
    print("There are a total of 20 questions. \nEach question is one point. \nYou can skip a question anytime by typing 'skip'")
    input("Let's start! Hit any key")
    return True


intro = intro_message()
while True:
    score = 0
    for question in quiz:
        attempts = 3
        while attempts > 0:
            print(quiz[question]['question'])
            answer = input("Enter Answer: ")
            if answer == "skip":
                break
            check = check_ans(question, answer, attempts, score)
            if check:
                score += 1
                break
            attempts -= 1

    break

print(f"Your final score is {score}!\n\n")
print("Thanks for playing! 💜")
