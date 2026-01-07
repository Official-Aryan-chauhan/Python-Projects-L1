import random
score = 0
while True:
    print("Dice Roll Game :")
    choice = input("Enter 'roll' To Play A Round 'exit' For Exit The Game: ").lower().strip()
     
    if choice =="exit":
        exit("Thanks For Playing !")
    
    elif choice == "roll":
        try:
            value = int(input("Enter Your Guess ! : "))
            if 1 > value or value > 6:
                print("Out OF range: Enter A Value Btween (1,6)")
                continue
        except ValueError:
            print("Invalid Input : Please Enter A Number")
            continue
    roll = random.randint(1,6)
    print("Dice Rolled !")
    if roll == value:
        score +=2
        print(f"Rollwd Number : {roll}")
        print(f"Correct Guess,Your Score Is : {score}")
    else:
        score -=1
        print(f"Rollwd Number : {roll}")
        print(f"Incorrect Guess ,Your Score Is : {score}")
    print("\n")

