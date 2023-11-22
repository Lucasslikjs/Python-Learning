import tkinter as tk
from tkinter import messagebox
import webbrowser
from tkinter import PhotoImage

BACKGROUND_COLOR = "lightgrey"
BUTTON_COLLOR = "grey"
FONT = ("Open Sans", 24)
FONT_BOLD = ("Open Sans", 24, "bold")
HIGHLIGHT_SETTINGS = {"highlightbackground": "black", "highlightcolor": "black", "highlightthickness": 2}

users = {
    "admin": "admin",
    "lucas": "vanderslik",
    "test": "test",
}

def create_window():
    window = tk.Tk()
    window.title("Inlog Pagina")
    window.state('zoomed')  

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width / 2) - (500 / 2)
    y = (screen_height / 2) - (500 / 2)
    window.geometry("+%d+%d" % (x, y))

    window.configure(bg=BACKGROUND_COLOR)

    username_label = tk.Label(window, text="Gebruikersnaam:", font=FONT_BOLD, bg=BACKGROUND_COLOR)
    username_label.place(relx=0.5, rely=0.3, anchor='center')

    username_entry = tk.Entry(window, font=FONT, **HIGHLIGHT_SETTINGS)
    username_entry.place(relx=0.5, rely=0.4, anchor='center')

    password_label = tk.Label(window, text="Wachtwoord:", font=FONT_BOLD, bg=BACKGROUND_COLOR)
    password_label.place(relx=0.5, rely=0.5, anchor='center')

    password_entry = tk.Entry(window, show="*", font=FONT, **HIGHLIGHT_SETTINGS)
    password_entry.place(relx=0.5, rely=0.6, anchor='center')
    

    def login():
        username = username_entry.get()
        password = password_entry.get()
        if username in users and users[username] == password:     
            window.destroy()      
            new_page()
        else:
            retry = messagebox.askretrycancel("Foute inlog", "Wachtwoord of gebruikersnaam is onjuist. Wil je het opnieuw proberen?")
        if not retry:
            window.destroy()
    
    def new_page():
        second_window = tk.Tk()
        second_window.title("Text Editor")
        second_window.state('zoomed')


        open_website_button = tk.Button(second_window, text="Open Website", command=lambda: webbrowser.open('http://www.example.com'))
        open_website_button.place(relx=0.5, rely=0.72, anchor='center')


    login_button = tk.Button(window, text="Login", command=login, font=(FONT_BOLD), bg=BUTTON_COLLOR, fg='black', borderwidth=2, relief='solid', highlightthickness=0)
    login_button.place(anchor='center')
    window.bind('<Return>', lambda event: login())
    window.mainloop()






if __name__ == "__main__":
    create_window()