import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner based on choices
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

# Function to handle game logic
def play_game(user_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    
    result = determine_winner(user_choice, computer_choice)
    
    # Display the result using a message box
    messagebox.showinfo("Result", f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n\n{result}")

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Label and instructions
label = tk.Label(root, text="Choose your move:")
label.pack(pady=10)

# Function to handle button click events
def handle_click(choice):
    play_game(choice)

# Buttons for rock, paper, and scissors
rock_button = tk.Button(root, text="Rock", width=10, command=lambda: handle_click("rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", width=10, command=lambda: handle_click("paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", width=10, command=lambda: handle_click("scissors"))
scissors_button.pack(pady=5)

# Run the main event loop
root.mainloop()
