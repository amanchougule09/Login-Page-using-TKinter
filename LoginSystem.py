import tkinter as tk
from tkinter import messagebox

# ====== Authentication Logic ======
def login():
    email = entry_email.get().strip()
    password = entry_password.get().strip()
    
    if email == "" or password == "":
        messagebox.showwarning("Input Error", "Please enter both Email and Password.")
    elif email == "aman@gmail.com" and password == "12345":
        messagebox.showinfo("Login Success", f"Welcome, {email}!")
    else:
        messagebox.showerror("Login Failed", "Invalid email or password.")

# ====== Hover Effects ======
def on_enter(e):
    login_btn.config(bg="#1A73E8")

def on_leave(e):
    login_btn.config(bg="#4285F4")

# ====== Main Window ======
root = tk.Tk()
root.title("Enterprise Login")
root.geometry("480x450")  # slightly taller for button visibility
root.configure(bg="#F5F5F5")

# ====== Center Login Card ======
card = tk.Frame(root, bg="white", bd=1, relief="solid", highlightbackground="#B2DFDB", highlightthickness=2)
card.place(relx=0.5, rely=0.5, anchor="center", width=380, height=380)  # increased height

# ====== Title ======
title = tk.Label(card, text="Sign in", font=("Segoe UI", 20, "bold"), bg="white", fg="#202124")
title.pack(pady=(25, 10))

subtitle = tk.Label(card, text="to continue to MyApp", font=("Segoe UI", 11), bg="white", fg="#5F6368")
subtitle.pack(pady=(0, 20))

# ====== Email Field ======
email_label = tk.Label(card, text="Email", font=("Segoe UI", 10), bg="white", fg="#202124")
email_label.pack(anchor="w", padx=30)
entry_email = tk.Entry(card, font=("Segoe UI", 11), bd=1, relief="solid", width=30)
entry_email.pack(pady=(2, 15), padx=30, ipady=5)

# ====== Password Field ======
password_label = tk.Label(card, text="Password", font=("Segoe UI", 10), bg="white", fg="#202124")
password_label.pack(anchor="w", padx=30)
entry_password = tk.Entry(card, font=("Segoe UI", 11), bd=1, relief="solid", show="*", width=30)
entry_password.pack(pady=(2, 10), padx=30, ipady=5)

# ====== Forgot Password Link ======
forgot_link = tk.Label(card, text="Forgot password?", font=("Segoe UI", 9, "underline"),
                       bg="white", fg="#1A73E8", cursor="hand2")
forgot_link.pack(anchor="e", padx=30, pady=(0,15))

# ====== Login Button ======
login_btn = tk.Button(card, text="Login", font=("Segoe UI", 12, "bold"), bg="#4285F4", fg="white",
                      activebackground="#1A73E8", activeforeground="white", relief="flat",
                      cursor="hand2", width=28, pady=8, command=login)  # visible button
login_btn.pack(pady=10)

login_btn.bind("<Enter>", on_enter)
login_btn.bind("<Leave>", on_leave)

# ====== Footer ======
footer = tk.Label(root, text="© 2025 MyApp. Designed by Aman", font=("Segoe UI", 9), bg="#F5F5F5", fg="#5F6368")
footer.pack(side="bottom", pady=10)

# ====== Run App ======
root.mainloop()
