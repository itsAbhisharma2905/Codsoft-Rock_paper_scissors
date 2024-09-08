import tkinter as tk
from PIL import Image, ImageTk
import random

# Initialize main window
window = tk.Tk()
window.title("Rock-Paper-Scissors Game")
window.geometry("500x500")

# Global variables for scores
user_score = 0
computer_score = 0

# Load Images using Pillow (Ensure that images are in the same directory)
rock_img = Image.open("rock.jpeg")
paper_img = Image.open("paper.jpeg")
scissors_img = Image.open("scissors.jpeg")

# Resize images to fit the display

# Convert images to PhotoImage for Tkinter
rock_photo = ImageTk.PhotoImage(rock_img)
paper_photo = ImageTk.PhotoImage(paper_img)
scissors_photo = ImageTk.PhotoImage(scissors_img)

# Function to get computer choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'You win!'
    else:
        return 'You lose!'

# Function to update scores and display result
def play_game(user_choice):
    global user_score, computer_score
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    # Update result text
    result_label.config(text=f"Computer chose {computer_choice}. {result}")

    # Update images based on choices
    user_image_label.config(image=images[user_choice])
    computer_image_label.config(image=images[computer_choice])

    # Update scores
    if 'win' in result:
        user_score += 1
    elif 'lose' in result:
        computer_score += 1

    user_score_label.config(text=f"User Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

# Function to reset game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="")
    user_score_label.config(text="User Score: 0")
    computer_score_label.config(text="Computer Score: 0")
    user_image_label.config(image='')
    computer_image_label.config(image='')

# Create Labels
result_label = tk.Label(window, text="", font=('Arial', 14))
result_label.pack(pady=20)

user_score_label = tk.Label(window, text="User Score: 0", font=('Arial', 12))
user_score_label.pack()

computer_score_label = tk.Label(window, text="Computer Score: 0", font=('Arial', 12))
computer_score_label.pack()

# Create frames for images
image_frame = tk.Frame(window)
image_frame.pack(pady=20)

user_image_label = tk.Label(image_frame, image='')
user_image_label.grid(row=0, column=0, padx=20)

computer_image_label = tk.Label(image_frame, image='')
computer_image_label.grid(row=0, column=1, padx=20)

# Dictionary to map choices to images
images = {
    'rock': rock_photo,
    'paper': paper_photo,
    'scissors': scissors_photo
}

# Create buttons for user choices
button_frame = tk.Frame(window)
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", font=('Arial', 12), command=lambda: play_game('rock'))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", font=('Arial', 12), command=lambda: play_game('paper'))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", font=('Arial', 12), command=lambda: play_game('scissors'))
scissors_button.grid(row=0, column=2, padx=10)

# Reset button to start a new game
reset_button = tk.Button(window, text="Reset Game", font=('Arial', 12), command=reset_game)
reset_button.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
