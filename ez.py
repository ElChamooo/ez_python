import time

def area(length, width):
    print("Calculating area...")
    time.sleep(2)  # Simulate a time-consuming calculation
    print("Need a bit more time...")
    time.sleep(2)  # Simulate a time-consuming calculation
    print("This is a complex calculation...")
    time.sleep(2)  # Simulate a time-consuming calculation
    print("This is a VERY complex problem you gave me...")
    time.sleep(2)  # Simulate a time-consuming calculation
    print("You have time to go get a coffee")
    time.sleep(2)  # Simulate a time-consuming calculation
    print("Oh you're back already?")
    time.sleep(2)  # Simulate a time-consuming calculation
    print("How was the coffee?")
    time.sleep(2)  # Simulate a time-consuming calculation
    print("Did you get a muffin with that?")
    time.sleep(2)  # Simulate a time-consuming calculation
    print("Sounds delicious!")
    time.sleep(2)  # Simulate a time-consuming calculation
    print("Oh Jessica was with you? I'm so jealous of you")
    time.sleep(2)  # Simulate a time-consuming calculation
    print("Was I working on the calculation this whole time?")
    time.sleep(2)  # Simulate a time-consuming calculation
    print("Nah my men I was talking with you the whole time")
    time.sleep(2)  # Simulate a time-consuming calculation
    print("I'll get back to it but first allow me to smoke a cigarette")
    time.sleep(2)  # Simulate a time-consuming calculation
    print("Almost there...")
    time.sleep(2)  # Simulate a time-consuming calculation
    print("Got it now!")
    time.sleep(2)  # Simulate a time-consuming calculation
    print("Oh you want the result now?")
    time.sleep(2)  # Simulate a time-consuming calculation
    print("My bad I'm just joking with you")
    time.sleep(2)  # Simulate a time-consuming calculation
    print("The result is "+str(length * width))
    time.sleep(2)  # Simulate a time-consuming calculation
    print("Oh you forgot what was the question?")
    time.sleep(2)  # Simulate a time-consuming calculation

def onetotwenty():
    for i in range(20):
        print(i+1)


def multipleofthree():
    print([i for i in range(1, 21) if i % 3 == 0])


classroom ={
    "students": [("John", 21, 60), ("Jane", 22, 50), ("Doe", 20, 40)]
}

print (classroom)
classroom["students"].append(("Alice", 23, 12))
print (classroom)
classroom["students"].remove(("Doe", 20, 40))
print (classroom)
max=0
for student in classroom["students"]:
    if student[2]>max:
        max=student[2]
        name=student[0]
print("The student with the highest score is "+name+" with a score of "+str(max))
classroom["students"].sort(key=lambda x: x[2], reverse=True)
print (classroom)