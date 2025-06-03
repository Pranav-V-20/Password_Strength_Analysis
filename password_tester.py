import re
import tkinter as tk
from tkinter import messagebox

def analyze_password(password):
    strength = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Lowercase check
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Add lowercase letters.")

    # Uppercase check
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Add uppercase letters.")

    # Digit check
    if re.search(r'\d', password):
        strength += 1
    else:
        feedback.append("Include digits.")

    # Special character check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Use special characters (e.g., !, @, #, $).")

    # Evaluate strength
    if strength == 5:
        feedback.append("Strong password!")
    elif strength >= 3:
        feedback.append("Moderate password. Consider adding more diversity.")
    else:
        feedback.append("Weak password. Improve based on feedback.")

    return strength, feedback

def check_password():
    password = entry.get()
    strength, suggestions = analyze_password(password)
    result = f"Password Strength: {strength}/5\n\n" + "\n".join(suggestions)
    messagebox.showinfo("Password Analysis", result)

# Create the GUI
root = tk.Tk()
root.title("Password Analyzer")
root.geometry("400x200")

# Widgets
label = tk.Label(root, text="Enter your password:")
label.pack(pady=10)

entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=5)

analyze_button = tk.Button(root, text="Analyze", command=check_password)
analyze_button.pack(pady=10)

# Run the application
root.mainloop()

