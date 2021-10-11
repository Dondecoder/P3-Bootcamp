times = input("How many times do I have to tell you? ")
times = int(times)

# Simplest Version
for time in range(times):
	print("CLEAN UP YOUR ROOM")

# Version 2
for time in range(times):
	print(f"time {time+1}:CLEAN UP YOUR ROOM")

# Version 3
cleanRoom = int(input("How many time do I have to tell you? "))

for c in range (cleanRoom):
    print ("Clean up your room!")