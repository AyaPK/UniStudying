import random
import baseconvert

base = input("What base are you working in? (Answer ? to have a random one generated)")
charcount = int(input("How many digits do you want?"))

def generate(charcount):
    output = ''
    global base
    if base == "?":
        base = int(random.randint(2, 9))
    for x in range(0, charcount):
        if x == 0:
            num = random.randint(1, int(base) - 1)
        else:
            num = random.randint(0, int(base) - 1)
        output = output+str(num)
    return output

quiz = generate(int(charcount))
answer = baseconvert.base(quiz, int(base), 10)

ansout = ""
for x in range(0,len(answer)):
    ansout = ansout+str(answer[x])

answer = int(ansout)


trying = True
while trying:
    print(f"Convert base {base} {quiz} to base 10")
    userAns = input(">> ")

    if int(userAns) == int(answer):
        print(f"Correct!! base {base} {quiz} in base 10 is {answer}!")
        trying = False
    else:
        print(f"Incorrect. base {base} {quiz} in base 10 is not {userAns}.")
        tryAgain = input(f"Try again? ")
        if tryAgain.lower() == "no":
            trying = False
            print(f"That's too bad. base {base} {quiz} in base 10 is {answer}!")
        if tryAgain.lower() == "yes":
            continue
        else:
            break