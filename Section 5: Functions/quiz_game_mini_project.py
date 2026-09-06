def ask_ques(question,correct_ans):
    print(question)
    user_ans=input("Your answer:")
    if user_ans.lower()==correct_ans:
        print("Correct! \n")
        return True
    else:
        print("Wrong, The correct answer is",correct_ans)
        return False

def cal_per(score,total):
    per=(score/total)*100
    return per
def get_result_msg(per):
    if per==100:
        return "Perfect Score! Outstanding"
    elif per>=80:
        return "Excellent! You are a Python expert! 🌟"
    elif per>=60:
        return "Good job! Keep practising! 👍"
    elif per>=40:
        return "Not bad! Review the basics! 📚"
    else:
        return "Keep learning! You will get better! 💪"
def run_quiz():
    print("========================================")
    print("         PYTHON QUIZ GAME               ")
    print("========================================")
    print("Answer each question correctly!")
    print("Type your answer and press Enter.\n")

    score=0
    total_ques=5

    if ask_ques("Q1. What keyword defines a function?", "def"):
        score+=1
    if ask_ques("Q2. What does print() do?", "displays output"):
        score += 1
    if ask_ques("Q3. Which loop uses range()?", "for"):
        score += 1
    if ask_ques("Q4. What keyword stops a loop?", "break"):
        score += 1
    if ask_ques("Q5. Comment symbol in Python?", "#"):
        score += 1

    print("========================================")
    print("           QUIZ COMPLETE!")
    print("========================================")
    print("Your Score : " + str(score) + " out of " + str(total_ques))
    
    percentage = cal_per(score, total_ques)
    print("Percentage : " + str(percentage) + "%")
    
    message = get_result_msg(percentage)
    print("Result     : " + message)
    print("========================================")
    print("Thank you for playing Python Quiz Game!")
    print("========================================")
run_quiz()




    
    

    