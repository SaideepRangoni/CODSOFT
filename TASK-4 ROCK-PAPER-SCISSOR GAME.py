import random
user_score=0
computer_score=0
while True:
  print("Do u want to play: ")
  response = input().lower()
  if response == "yes":
    while True:
      user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
      if user_choice in ['rock', 'paper', 'scissors']:
        break
      else:
        print("Enter valid choice")
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print("Computer choice : ", computer_choice)
    if computer_choice == user_choice:
      print("Tie!")
    elif computer_choice == "rock":
      if user_choice == "paper":
        print("User wins!")
        user_score += 1
      if user_choice == "scissors":
        print("Computer wins!")
        computer_score += 1
    elif computer_choice == "paper":
      if user_choice == "scissors":
        print("User wins!")
        user_score += 1
      if user_choice == "rock":
        print("Computer wins!")
        computer_score += 1
    elif computer_choice == "scissors":
      if user_choice == "rock":
        print("User wins!")
        user_score += 1
      if user_choice == "paper":
        print("Computer wins!")
        computer_score += 1
  if response == "no":
    print("Thank you!")
    if user_score > computer_score:
      print("User wins!, user_score = ", user_score, "computer score = ", computer_score)
    if user_score == computer_score:
      print("Tied!")
    if user_score < computer_score:
      print("Computer wins!, computer_score = ", computer_score, "user_score = ", user_score)
    break
   
  
  
    
