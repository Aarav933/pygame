print("Helo i am AI, whats your name?")
name = input()
print(f"hello, {name}")
print("How are you? (good or bad)?")
feeling = input().lower()
if feeling == "good":
    print("Thats nice")
elif feeling == "bad":
    print("Im sorry to hear that")
else:
    print("Please enter your mood correctly")
print("Goodbye it was nice meeting you")

