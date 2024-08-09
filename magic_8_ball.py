import tkinter as tk
import random

def shake_ball(event=None):
    question = entry_question.get()
    if question == "":
        label_answer.config(text="There is no question for me")
        return

    # Simulate shaking effect
    for i in range(10):  # Number of shake frames
        offset = random.randint(-10, 10)  # Random offset to create shaking effect
        canvas.delete("ball")
        draw_ball(offset)
        window.update_idletasks()
        window.after(50)  # Delay between frames

    # Clear the ball and show the answer after shaking
    canvas.delete("ball")
    draw_ball()
    window.after(100, display_answer)

def display_answer():
    random_number = random.randint(1, 11)
    if random_number == 1:
        answer = "Yes - definitely"
    elif random_number == 2:
        answer = "It is decidedly so"
    elif random_number == 3:
        answer = "Without a doubt"
    elif random_number == 4:
        answer = "Reply hazy, try again"
    elif random_number == 5:
        answer = "Ask again later"
    elif random_number == 6:
        answer = "Better not tell you now"
    elif random_number == 7:
        answer = "My sources say no"
    elif random_number == 8:
        answer = "Outlook not so good"
    elif random_number == 9:
        answer = "Very doubtful"
    elif random_number == 10:
        answer = "Is that even a question?"
    elif random_number == 11:
        answer = name + " is already manifesting it."
    else:
        answer = "Error"

    label_answer.config(text=answer)

def draw_ball(offset=0):
    # Draw the ball with an optional offset for shaking effect
    canvas.create_oval(50 + offset, 50 + offset, 250 + offset, 250 + offset, fill="black", outline="white", tags="ball")
    canvas.create_text(150 + offset, 150 + offset, text="8", font=("Arial", 60), fill="white", tags="ball")

# Main application window
window = tk.Tk()
window.title("Magic 8-Ball")

name = "Malashree"

# Create canvas for ball drawing
canvas = tk.Canvas(window, width=300, height=300, bg="white")
canvas.pack(pady=10)

# Draw the initial ball
draw_ball()

# Bind mouse click event to the ball
canvas.tag_bind("ball", "<Button-1>", shake_ball)

# Create widgets
label_title = tk.Label(window, text="Magic 8-Ball", font=("Arial", 24))
label_question = tk.Label(window, text="Ask a question:")
entry_question = tk.Entry(window, width=40)
button_ask = tk.Button(window, text="Shake the Magic 8-Ball", command=shake_ball)
label_answer = tk.Label(window, text="", font=("Arial", 14), wraplength=300)

# Place widgets in the window
label_title.pack(pady=10)
label_question.pack()
entry_question.pack(pady=5)
button_ask.pack(pady=20)
label_answer.pack(pady=10)

# Run the application
window.mainloop()
