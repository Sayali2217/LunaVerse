import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import random


registered_users = {"us": "pas", "user2": "password2"}
words = {
    "apple": {"French": "pomme", "Spanish": "manzana", "German": "Apfel", "image": "apple.png"},
    "dog": {"French": "chien", "Spanish": "perro", "German": "Hund", "image": "dog.png"},
    "car": {"French": "voiture", "Spanish": "coche", "German": "Auto", "image": "car.png"},
}
conversion_sentences = {
    "French": [
        ("I eat an apple", "Je mange une pomme"),
        ("He reads a book", "Il lit un livre"),
        ("She drinks water", "Elle boit de l'eau"),
        ("We watch a movie", "Nous regardons un film"),
        ("You write a letter", "Tu écris une lettre")
    ],
    "Spanish": [
        ("I eat an apple", "Yo como una manzana"),
        ("He reads a book", "Él lee un libro"),
        ("She drinks water", "Ella bebe agua"),
        ("We watch a movie", "Nosotros vemos una película"),
        ("You write a letter", "Tú escribes una carta")
    ],
    "German": [
        ("I eat an apple", "Ich esse einen Apfel"),
        ("He reads a book", "Er liest ein Buch"),
        ("She drinks water", "Sie trinkt Wasser"),
        ("We watch a movie", "Wir schauen einen Film"),
        ("You write a letter", "Du schreibst einen Brief")
    ]
}

MCQ_QUESTIONS = {
    "French": [
        ("Hello", ["bonjour", "merci", "chat"], "bonjour"),
        ("Thank you", ["maison", "merci", "chien"], "merci"),
        ("Apple", ["pomme", "chat", "chien"], "pomme"),
        ("Cat", ["chien", "chat", "bonjour"], "chat"),
        ("Dog", ["chat", "merci", "chien"], "chien"),
        ("House", ["maison", "bonjour", "pomme"], "maison")
    ],
    "German": [
        ("Hello", ["hallo", "danke", "katze"], "hallo"),
        ("Thank you", ["haus", "danke", "hund"], "danke"),
        ("Apple", ["apfel", "katze", "hund"], "apfel"),
        ("Cat", ["hund", "katze", "hallo"], "katze"),
        ("Dog", ["katze", "danke", "hund"], "hund"),
        ("House", ["haus", "hallo", "apfel"], "haus")
    ],
    "Spanish": [
        ("Hello", ["hola", "gracias", "gato"], "hola"),
        ("Thank you", ["casa", "gracias", "perro"], "gracias"),
        ("Apple", ["manzana", "gato", "perro"], "manzana"),
        ("Cat", ["perro", "gato", "hola"], "gato"),
        ("Dog", ["gato", "gracias", "perro"], "perro"),
        ("House", ["casa", "hola", "manzana"], "casa")
    ]
}

# ---------------------- CONFIG ---------------------- #
class AppConfig:
    selected_language = None
    selected_level = None

# ---------------------- MAIN WINDOW ---------------------- #
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Luna Verse")
        self.geometry("400x400")

        self.bg_image = Image.open("Moon.png")
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = tk.Label(self, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.get_started_btn = tk.Button(self,text="Get Started",command=self.open_login_window,width=20,height=2,font=("Helvetica", 14, "bold"))
        self.get_started_btn.place(x=630, y=650) 

    def open_login_window(self):
        self.destroy()  
        LoginPage().mainloop()  

# ---------------------- SIGNUP WINDOW ---------------------- #
class SignupPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Signup Page")
        self.geometry("400x300")
       
        tk.Label(self, text="Create Username:").pack(pady=10)
        self.entry_username = tk.Entry(self)
        self.entry_username.pack(pady=5)
        
        tk.Label(self, text="Create Password:").pack(pady=10)
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack(pady=5)

        tk.Button(self, text="Sign Up", command=self.register_user).pack(pady=20)
        tk.Button(self, text="Go to Login", command=self.open_login_window).pack()

    def register_user(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if not username or not password:
            messagebox.showwarning("Error", "All fields are required!")
            return

        if username in registered_users:
            messagebox.showerror("Error", "Username already exists!")
        else:
            registered_users[username] = password
            messagebox.showinfo("Success", "Account created successfully!")
            self.destroy()
            LoginPage().mainloop()

    def open_login_window(self):
        self.destroy()
        LoginPage().mainloop()

# ---------------------- LOGIN WINDOW ---------------------- #
class LoginPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login Page")
        self.geometry("400x300")
        
        tk.Label(self, text="Username:").pack(pady=10)
        self.entry_username = tk.Entry(self)
        self.entry_username.pack(pady=5)

        tk.Label(self, text="Password:").pack(pady=10)
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack(pady=5)

        tk.Button(self, text="Login", command=self.login).pack(pady=20)
        tk.Button(self, text="Go to Sign Up", command=self.open_signup_window).pack()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if registered_users.get(username) == password:
            messagebox.showinfo("Success", "Login successful!")
            self.destroy()
            HomePage().mainloop()
        else:
            messagebox.showerror("Error", "Invalid username or password!")

    def open_signup_window(self):
        self.destroy()
        SignupPage().mainloop()

# ---------------------- HOME PAGE ---------------------- #
class HomePage(tk.Tk):
    def __init__(self):
        
        super().__init__()
        self.title("Home Page")
        self.geometry("400x400")
      
        tk.Label(self, text="Welcome to the Home Page!", font=("Arial", 16)).pack(pady=20)
        tk.Label(self, text="Choose a Language").pack(pady=10)

        self.language_var = tk.StringVar()
        self.language_dropdown = ttk.Combobox(self, textvariable=self.language_var,
                                              values=["French", "German", "Spanish"],
                                              state="readonly")
        self.language_dropdown.pack(pady=10)

        tk.Label(self, text="Choose Proficiency Level").pack(pady=10)
        self.profi_var = tk.StringVar()
        self.profi_dropdown = ttk.Combobox(self, textvariable=self.profi_var,
                                           values=["Beginner", "Basic", "Intermediate", "Advanced"],
                                           state="readonly")
        self.profi_dropdown.pack(pady=10)

        tk.Button(self, text="Confirm Information", command=self.show_info).pack(pady=20)
        tk.Button(self, text="Start Learning", command=self.next_page).pack(pady=10)
        tk.Button(self, text="Logout", command=self.logout).pack(pady=20)

    def show_info(self):
        selected_language = self.language_var.get()
        selected_level = self.profi_var.get()
        if selected_language and selected_level:
            messagebox.showinfo("Language Selected",
                                f"You have selected {selected_language} Language and {selected_level} level")
        else:
            messagebox.showwarning("Incomplete Information", "Please fill the information completely!")

    def next_page(self):
        selected_language = self.language_var.get()
        selected_level = self.profi_var.get()
        if selected_language and selected_level:
            AppConfig.selected_language = selected_language
            AppConfig.selected_level = selected_level
            self.destroy()
            GameSelectionPage().mainloop()
        else:
            messagebox.showwarning("Incomplete", "Please select both Language and Level!")

    def logout(self):
        self.destroy()
        LoginPage().mainloop()

# ---------------------- GAME SELECTION ---------------------- #
class GameSelectionPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Select a Game")
        self.geometry("400x300")
        
        lang = AppConfig.selected_language
        level = AppConfig.selected_level
        tk.Label(self, text=f"Choose a Game for {lang} - {level}").pack(pady=10)

        tk.Button(self, text="Start Match Game", command=self.start_match_game).pack(pady=10)
        tk.Button(self, text="Image Game", command=self.start_simple_game).pack(pady=10)
        tk.Button(self, text="Fill in the Blanks", command=self.open_sentence_game).pack(pady=10)
        tk.Button(self, text="MCQ Translation", command=self.start_MCQ_game).pack(pady=10)
        tk.Button(self, text="Logout", command=self.logout).pack(pady=20)

    def start_match_game(self):
        self.destroy()
        MatchGame().mainloop()

    def start_simple_game(self):
        self.destroy()
        SimpleGame().mainloop()
        
    def open_sentence_game(self):
        self.destroy()
        SentenceConversionGame().mainloop()
        
    def start_MCQ_game(self):
        self.destroy()
        MCQTranslateGame().mainloop()
        
    def logout(self):
        self.destroy()
        LoginPage().mainloop()
      
    
        
# ---------------------- MATCH GAME ---------------------- #

class MatchGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Match Game")
        self.geometry("500x600")
        
        lang = AppConfig.selected_language
        self.word_pairs = {
            "French": {"I": "je", "July": "juillet", "seven": "sept"},
            "Spanish": {"I": "yo", "July": "julio", "seven": "siete"},
            "German": {"I": "ich", "July": "Juli", "seven": "sieben"},
        }

        self.pairs = list(self.word_pairs[lang].items())
        self.buttons = []
        self.selected_buttons = []
        self.matched_pairs = set()

        self.setup_game()

    def setup_game(self):
        lang = AppConfig.selected_language
        tk.Label(self, text=f"Match the words - {lang}", font=("Arial", 16)).pack(pady=20)

        english_words = [eng for eng, _ in self.pairs]
        foreign_words = [trans for _, trans in self.pairs]
        random.shuffle(english_words)
        random.shuffle(foreign_words)

        frame = tk.Frame(self)
        frame.pack(pady=20)

        self.left_frame = tk.Frame(frame)
        self.left_frame.pack(side="left", padx=10)

        self.right_frame = tk.Frame(frame)
        self.right_frame.pack(side="right", padx=10)

        for word in english_words:
            btn = tk.Button(self.left_frame, text=word, width=15, command=lambda b=word: self.select_word(b))
            btn.pack(pady=2)
            self.buttons.append((word, btn))

        for word in foreign_words:
            btn = tk.Button(self.right_frame, text=word, width=15, command=lambda b=word: self.select_word(b))
            btn.pack(pady=2)
            self.buttons.append((word, btn))

    def select_word(self, word):
        if len(self.selected_buttons) < 2:
            for w, btn in self.buttons:
                if w == word and btn['state'] != 'disabled' and (w, btn) not in self.selected_buttons:
                    btn.config(relief="sunken")
                    self.selected_buttons.append((w, btn))
                    break

        if len(self.selected_buttons) == 2:
            self.after(500, self.check_match)

    def check_match(self):
        word1, btn1 = self.selected_buttons[0]
        word2, btn2 = self.selected_buttons[1]

        is_match = any((word1 == eng and word2 == trans) or (word1 == trans and word2 == eng)
                       for eng, trans in self.pairs)

        if is_match:
            messagebox.showinfo("Correct", "Yay! Correct Pair!")
            btn1.config(state="disabled")
            btn2.config(state="disabled")
            self.matched_pairs.add(frozenset([word1, word2]))
        else:
            messagebox.showinfo("Wrong", "Oops! Not a Match!")
            btn1.config(relief="raised")
            btn2.config(relief="raised")

        self.selected_buttons.clear()

        if len(self.matched_pairs) == len(self.pairs):
            self.show_game_over()

    def show_game_over(self):
        game_over_label = tk.Label(self, text="🎉 Game Over! You've matched all pairs!", font=("Arial", 14), fg="green")
        game_over_label.pack(pady=20)

        back_btn = tk.Button(self, text="Back to Menu", font=("Arial", 12), command=self.return_to_menu)
        back_btn.pack(pady=10)

    def return_to_menu(self):
        self.destroy()
        GameSelectionPage().mainloop()


# ---------------------- IMAGE GAME ---------------------- #

class SimpleGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Game")
        self.geometry("400x400")
        
        self.language = AppConfig.selected_language
        self.score = 0
        self.words_list = list(words.keys())
        random.shuffle(self.words_list)
        self.index = 0

        self.start_game()

    def start_game(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.show_question()

    def show_question(self):
        for widget in self.winfo_children():
            widget.destroy()

        if self.index >= len(self.words_list):
            tk.Label(self, text=f"🎉 Game Over! Score: {self.score}", font=("Arial", 16)).pack(pady=20)
            
            # ✅ ADD: Back to Menu button
            tk.Button(self, text="Back to Menu", command=self.return_to_menu).pack(pady=10)
            return

        word = self.words_list[self.index]
        correct = words[word][self.language]
        options = [correct]
        others = [words[w][self.language] for w in words if w != word]
        options += random.sample(others, 2)
        random.shuffle(options)

        img = Image.open(words[word]["image"])
        img = img.resize((150, 150))
        self.tk_img = ImageTk.PhotoImage(img)

        tk.Label(self, image=self.tk_img).pack(pady=10)
        tk.Label(self, text="What is this in " + self.language + "?", font=("Arial", 12)).pack(pady=5)

        for opt in options:
            tk.Button(self, text=opt, width=20,
                      command=lambda o=opt, c=correct: self.check_answer(o, c)).pack(pady=3)

    def check_answer(self, selected, correct):
        for widget in self.winfo_children():
            widget.destroy()

        if selected == correct:
            self.score += 10
            result = "✅ Correct!"
        else:
            result = f"❌ Wrong! Correct: {correct}"

        tk.Label(self, text=result, font=("Arial", 14)).pack(pady=10)
        tk.Label(self, text=f"Score: {self.score}", font=("Arial", 12)).pack(pady=5)
        tk.Button(self, text="Next", command=self.next_question).pack(pady=10)

    def next_question(self):
        self.index += 1
        self.show_question()

    def return_to_menu(self):  # ✅ NEW FUNCTION
        self.destroy()
        GameSelectionPage().mainloop()


# ---------------------- SENTENCE CONVERSION GAME ---------------------- #

class SentenceConversionGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sentence Conversion Game")
        self.geometry("500x400")
        
        self.sentences = conversion_sentences.get(AppConfig.selected_language, [])
        random.shuffle(self.sentences)
        self.current_index = 0
        self.user_selection = []
        self.word_buttons = []
        self.correct_words = []

        self.eng_label = tk.Label(self, text="", font=("Arial", 14))
        self.eng_label.pack(pady=10)

        self.buttons_frame = tk.Frame(self)
        self.buttons_frame.pack()

        self.answer_label = tk.Label(self, text="", font=("Arial", 14), fg="blue")
        self.answer_label.pack(pady=10)

        self.next_button = tk.Button(self, text="Next Sentence", command=self.next_sentence)
        self.next_button.pack(pady=5)

        self.back_button = None  # ✅ NEW: Placeholder for back button

        self.load_sentence()

    def load_sentence(self):
        self.user_selection.clear()
        for widget in self.buttons_frame.winfo_children():
            widget.destroy()
        self.answer_label.config(text="")

        eng, fr = self.sentences[self.current_index]
        self.eng_label.config(text=f"Translate: {eng}")
        self.correct_words = fr.split()
        shuffled = random.sample(self.correct_words, len(self.correct_words))

        self.word_buttons = []
        for word in shuffled:
            btn = tk.Button(self.buttons_frame, text=word, font=("Arial", 12))
            btn["command"] = lambda w=word, b=btn: self.select_word(w, b)
            btn.pack(side="left", padx=5)
            self.word_buttons.append(btn)

    def select_word(self, word, button):
        if len(self.user_selection) < len(self.correct_words):
            self.user_selection.append(word)
            self.answer_label.config(text=" ".join(self.user_selection))
            button.config(state="disabled")

        if len(self.user_selection) == len(self.correct_words):
            self.check_answer()

    def check_answer(self):
        if self.user_selection == self.correct_words:
            messagebox.showinfo("Correct", "✅ Well done!")
        else:
            correct = " ".join(self.correct_words)
            messagebox.showerror("Wrong", f"❌ Correct answer: {correct}")

    def next_sentence(self):
        self.current_index += 1
        if self.current_index >= len(self.sentences):
            self.eng_label.config(text="🎉 Game Over!")
            for widget in self.buttons_frame.winfo_children():
                widget.destroy()
            self.answer_label.config(text="")
            self.next_button.config(state="disabled")

            self.back_button = tk.Button(self, text="Back to Menu", command=self.return_to_menu)  # ✅ NEW
            self.back_button.pack(pady=10)  # ✅ NEW
        else:
            self.load_sentence()

    def return_to_menu(self):  # ✅ NEW METHOD
        self.destroy()
        GameSelectionPage().mainloop()

# ---------------------- MCQ GAME ---------------------- #          

class MCQTranslateGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MCQ Translate Game")
        self.geometry("400x350")
        
        self.questions = MCQ_QUESTIONS.get(AppConfig.selected_language, [])
        random.shuffle(self.questions)

        self.question_index = 0
        self.score = 0

        self.label = tk.Label(self, text="Choose the correct translation:", font=("Arial", 14))
        self.label.pack(pady=10)

        self.word_label = tk.Label(self, text="", font=("Arial", 18, "bold"))
        self.word_label.pack(pady=5)

        self.var = tk.StringVar()

        self.options = []
        for _ in range(3):
            rb = tk.Radiobutton(self, text="", variable=self.var, value="", font=("Arial", 12))
            rb.pack(anchor='w', padx=50)
            self.options.append(rb)

        self.submit_btn = tk.Button(self, text="Submit", command=self.check_answer)
        self.submit_btn.pack(pady=10)

        self.progress = ttk.Progressbar(self, length=200, maximum=len(self.questions))
        self.progress.pack(pady=10)

        self.result_label = tk.Label(self, text="", font=("Arial", 14))
        self.result_label.pack()

        self.back_button = tk.Button(self, text="Back to Menu", command=self.return_to_menu)  # ✅ INITIALLY HIDDEN
        self.load_question()

    def load_question(self):
        if self.question_index < len(self.questions):
            question, choices, answer = self.questions[self.question_index]
            self.word_label.config(text=question)
            self.var.set("")
            for rb, choice in zip(self.options, choices):
                rb.config(text=choice, value=choice, state="normal")
            self.result_label.config(text=f"Question {self.question_index + 1} of {len(self.questions)}")
            self.progress["value"] = self.question_index
            self.submit_btn.config(state="normal")
            self.back_button.pack_forget()  # ✅ HIDE BUTTON IF RESTARTED
        else:
            for rb in self.options:
                rb.config(state="disabled")
            self.word_label.config(text="✅ Quiz Completed!")
            self.label.config(text=f"Your Score: {self.score} / {len(self.questions)}")
            self.result_label.config(text="")
            self.submit_btn.config(state="disabled")
            self.back_button.pack(pady=10)  # ✅ SHOW BACK BUTTON

    def check_answer(self):
        selected = self.var.get()
        if not selected:
            messagebox.showwarning("No selection", "Please select an option before submitting.")
            return

        _, _, correct = self.questions[self.question_index]
        if selected == correct:
            self.score += 1
            messagebox.showinfo("Correct", "✅ That's correct!")
        else:
            messagebox.showerror("Incorrect", f"❌ Wrong! Correct answer was: {correct}")

        self.question_index += 1
        self.load_question()

    def return_to_menu(self):  # ✅ NEW METHOD
        self.destroy()
        GameSelectionPage().mainloop()

# ---------------------- MAIN ---------------------- #
if __name__ == "__main__":
    MainWindow().mainloop()
