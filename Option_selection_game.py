import os


print("Welcome to KBC ")

intiate = int(input("Press 1 to begin /n Press 0 to exit"))

Answers = ["Joe Biden", "Narendra Modi", "7", "1947", "26 January", "18"]

Questions = {0: "who is the current United States President",
             1: "Who is the current President of India",
             2: "How many wonders of the world are there",
             3: "When did India gain independence",
             4: "When is republic day celebrated",
             5: "What is the legal age to vote"}


total_prizemon = 0


def check_answer(ans, i):

    global total_prizemon
    if ans.lower() == Answers[i].lower():
        print("your answer is correct .You get additional 5k")
        total_prizemon+=5000


    else:
        print("Answer is incorrect.Sorry")



if (intiate == 0):
    print("Goodbye")

if (intiate == 1):

    print(f"There are {len(Questions)} questions ")

    for i in range(len(Questions)):
        match i:
            case 0:
                print(Questions[0])
                dict1 = {1: "donald trump", 2: "joe biden", 3: "Barack Obama"}
                print("Options are ", dict1)
                a1 = int(input("Select correct option"))

                check_answer(dict1[a1], 0)

            case 1:
                print(Questions[1])
                dict2 = {1: "Atalbihari Vajpayee", 2: "Manmohan singh", 3: "Narendra Modi"}
                print("Options are ", dict2)
                a2 = int(input("Select correct option"))

                check_answer(dict2[a2], 1)

            case 2:
                print(Questions[2])
                dict3 = {1: "7", 2: "3", 3: "9"}
                print("Options are ", dict3)
                a3 = int(input("Select correct option"))

                check_answer(dict3[a3], 2)

            case 3:
                print(Questions[3])
                dict4 = {1: "1947", 2: "1946", 3: "1987"}
                print("Options are ", dict4)
                a4 = int(input("Select correct option"))

                check_answer(dict4[a4], 3)

            case 4:
                print(Questions[4])
                dict5 = {1: "26 august", 2: "27 september", 3: "26 January"}
                print("Options are ", dict5)
                a5 = int(input("Select correct option"))

                check_answer(dict5[a5], 4)

            case 5:
                print(Questions[5])
                dict6 = {1: "26 ", 2: "20", 3: "18"}
                print("Options are ", dict6)
                a5 = int(input("Select correct option"))

                check_answer(dict6[a5], 5)


    print("total prizemoney won is ",total_prizemon)

