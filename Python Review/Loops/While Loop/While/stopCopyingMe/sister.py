msg = input("Say Something: ")


while msg != "stop copying me":
	print(msg)
	msg = input()
print("UGH FINE YOU WIN, BROTHER!")

# while msg != "stop copying me":
# 	msg = input(f"{msg}\n")
# print("UGH FINE YOU WIN, BROTHER!")

# My solution for this problem
question = input("Hey how's it going? ")


while True:
    if (question == "stop copying me"):
        print ("Ugh fine you win")
        break
    else:
        print (question)
        question = input()
