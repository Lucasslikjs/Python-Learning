import tkinter as tk
from tkinter import messagebox
import webbrowser

def create_window():
    window = tk.Tk()
    window.title("Inlog Pagina")
    window.geometry("500x500")

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width / 2) - (500 / 2)
    y = (screen_height / 2) - (500 / 2)
    window.geometry("+%d+%d" % (x, y))

    window.configure(bg='white')

    username_label = tk.Label(window, text="Gebruikersnaam", font=("Open Sans", 24), bg='white')
    username_label.place(relx=0.5, rely=0.3, anchor='center')

    username_entry = tk.Entry(window, font=("Open Sans", 24))
    username_entry.place(relx=0.5, rely=0.4, anchor='center')

    password_label = tk.Label(window, text="Wachtwoord", font=("Open Sans", 24), bg='white')
    password_label.place(relx=0.5, rely=0.5, anchor='center')

    password_entry = tk.Entry(window, show="*", font=("Open Sans", 24))
    password_entry.place(relx=0.5, rely=0.6, anchor='center')

    def login():
        username = username_entry.get()
        password = password_entry.get()
        if username == "admin" and password == "admin":
            messagebox.showinfo("Welkom", "Je bent succesvol ingelogd")
            webbrowser.open('http://www.vanderslik.online')
        else:
            messagebox.showinfo("Error", "Wachtwoord of gebruikersnaam is onjuist")

    login_button = tk.Button(window, text="Login", command=login, font=("Open Sans", 24), bg='lightgray')
    login_button.place(relx=0.5, rely=0.7, anchor='center')

    window.mainloop()

if __name__ == "__main__":
    create_window()