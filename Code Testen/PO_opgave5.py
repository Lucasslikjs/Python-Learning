import tkinter as tk
from tkinter import messagebox
import webbrowser

BACKGROUND_COLOR = "pink"
BUTTON_COLLOR = "lightblue"
FONT = ("Open Sans", 24)
HIGHLIGHT_SETTINGS = {"highlightbackground": "black", "highlightcolor": "black", "highlightthickness": 2}

users = {
    "admin": "admin",
    "lucas": "vanderslik",
    "test": "test",
}

def create_window():
    window = tk.Tk()
    window.title("Inlog Pagina")
    window.geometry("500x500")

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width / 2) - (500 / 2)
    y = (screen_height / 2) - (500 / 2)
    window.geometry("+%d+%d" % (x, y))

    window.configure(bg=BACKGROUND_COLOR)

    username_label = tk.Label(window, text="Gebruikersnaam", font=FONT, bg=BACKGROUND_COLOR)
    username_label.place(relx=0.5, rely=0.3, anchor='center')

    username_entry = tk.Entry(window, font=FONT, **HIGHLIGHT_SETTINGS)
    username_entry.place(relx=0.5, rely=0.4, anchor='center')

    password_label = tk.Label(window, text="Wachtwoord", font=FONT, bg=BACKGROUND_COLOR)
    password_label.place(relx=0.5, rely=0.5, anchor='center')

    password_entry = tk.Entry(window, show="*", font=FONT, **HIGHLIGHT_SETTINGS)
    password_entry.place(relx=0.5, rely=0.6, anchor='center')

    def login():
        username = username_entry.get()
        password = password_entry.get()
        if username in users and users[username] == password:
            messagebox.showinfo("Welkom", "Je bent succesvol ingelogd")
            webbrowser.open('http://www.vanderslik.online')
            webbrowser.open('https://admin.microsoft.com/#/homepage')
            window.destroy()
        retry = messagebox.askretrycancel("Foute inlog", "Wachtwoord of gebruikersnaam is onjuist. Wil je het opnieuw proberen?")
        if not retry:
            window.destroy()


    login_button = tk.Button(window, text="Login", command=login, font=(FONT, 24), bg=BUTTON_COLLOR, fg='black', borderwidth=2, relief='solid', highlightthickness=0)
    login_button.place(relx=0.5, rely=0.72, anchor='center')
    window.mainloop()

if __name__ == "__main__":
    create_window()