question = input("Hey how's it going? ")


while True:
    if (question == "stop copying me"):
        print ("Ugh fine you win")
        break
    else:
        print (question)
        question = input()
        