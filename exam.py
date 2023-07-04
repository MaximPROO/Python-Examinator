Максим Орлов, [03.07.2023 19:13]
import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedStyle
import time


class ExaminatorGUI:
    def init(self, questions):
        self.questions = questions
        self.current_question = 0
        self.score = 0
        self.start_time = None
        self.name = None

        self.window = tk.Tk()
        self.window.title("Python Examinator")
        self.window.attributes('-fullscreen', True)
        self.window.attributes('-topmost', True)
        self.window.configure(bg="black")

        self.style = ThemedStyle(self.window)
        self.style.set_theme("black")

        self.name_label = ttk.Label(self.window, text="Enter your Name:", font=('Arial', 20, 'bold'),
                                    foreground='white', background='black')
        self.name_label.pack(pady=50)

        self.name_entry = ttk.Entry(self.window, font=('Arial', 16))
        self.name_entry.pack(pady=10)
        self.name_entry.focus()

        self.start_button = ttk.Button(self.window, text="Start", command=self.display_welcome_screen,
                                       style="StartButton.TButton")
        self.start_button.pack(pady=10)

        self.style.configure("StartButton.TButton", font=('Arial', 16, 'bold'), foreground='white', background='green',
                             width=20, padding=10)

        self.question_label = ttk.Label(self.window, wraplength=600, font=('Arial', 20, 'bold'), foreground='white',
                                        background='black')
        self.answer_var = tk.StringVar()
        self.answer_entry = ttk.Entry(self.window, textvariable=self.answer_var, font=('Arial', 16), foreground='gray')
        self.submit_button = ttk.Button(self.window, text="Submit", command=self.check_answer,
                                        style="SubmitButton.TButton")

    def display_name_input(self):
        self.name_label.config(text="Enter your Name:")
        self.start_button.config(text="Start", command=self.display_welcome_screen)
        self.question_label.pack_forget()
        self.answer_entry.pack_forget()
        self.submit_button.pack_forget()

    def display_welcome_screen(self):
        self.name = self.name_entry.get()
        if self.name:
            self.name_label.config(text=f"Welcome, {self.name}!")
            self.start_button.config(text="Start Test", command=self.start_test)
            self.name_entry.pack_forget()
        else:
            messagebox.showwarning("Name Required", "Please enter your name.")

    def start_test(self):
        self.start_time = time.time()
        self.name_label.pack_forget()
        self.start_button.pack_forget()
        self.display_question()

    def display_question(self):
        if self.current_question < len(self.questions):
            question = list(self.questions.keys())[self.current_question]
            self.question_label.config(text=question)
            self.question_label.pack(pady=50)
            self.answer_entry.pack(pady=10)
            self.submit_button.pack(pady=10)
            self.answer_var.set("")
            self.answer_entry.focus()
        else:
            self.display_score()

    def check_answer(self):
        user_answer = self.answer_var.get()
        correct_answer = list(self.questions.values())[self.current_question]
        if user_answer.lower() == correct_answer.lower():
            self.score += 1

        self.current_question += 1
        self.display_question()

    def display_score(self):
        total_questions = len(self.questions)
        percentage = (self.score / total_questions) * 100
        elapsed_time = round(time.time() - self.start_time, 2)
        messagebox.showinfo("Exam Completed",
                            f"{self.name}, you scored {self.score}/{total_questions} ({percentage}%) in {elapsed_time} seconds.")
        self.window.destroy()

Максим Орлов, [03.07.2023 19:13]
questions = {
    "Q1: Qaysi metod qatorni barcha belgilarini kichik qilib beradi": "lower",
    "Q2: Qatorni listga ajratuvchi metod": "split",
    "Q3: Qatordagi malum bir belgini boshgasiga aylantiruvchi metod": "replace",
    "Q4: Qatorni belgilarini KATTA qilivchi metod": "upper",
    "Q5 Birinchi belgini katta harfga aylantiradigan metod": "capitalize",
    "Q6 Belgilangan qiymat qatorda necha marta qaytarilganini sanuvchi metod": "count",
    "Q7 Belgi nechanchi o'rinda ekanligini aniqlovchi metod": "index",
    "Q8 Agar satrdagi barcha belgilar alifboda bo'lsa, True qiymatini qaytaradigan metod": "isalpha",
    "Q9 Listga element qo'shuvchi metod": "append",
    "Q10 Roʻyxatdagi barcha elementlarni olib tashlaydigan metod": 'clear',
    "Q11 Listdan mustaqil nusxa oladigan metod": 'copy',
    "Q12 Ikkta lisni birlashriruvchi metod": 'extend',
    "Q13 Lisning malum bir indexiga elemnt qo'shuvchi metod": 'insert',
    "Q14 Index berilmaganda oxirgi elementni o'chiruvchi metod": 'pop',
    "Q15 Belgilangan qiymatni listan ochirish": 'remove',
    "Q16 Darajaga ko'taruvchi arifmetik amal": "**",
    "Q17 Darajaga ko'taruvchi modul": "pow",
    "Q18 Ildiz xisoblovchi funksiya": "sqrt",
    "Q20 Manfiy sonni musbat qilib beruvchi funksiya": "fabs",
    "Q21 Bo'linmaning butun qismini oluvchi arifmetik belgi": "//",
    "Q22 Kasr sonni butun songa o'zgartiradigan funksiya": "floor",
    "Q23 Unikal ro'yxat bu": 'set',
    "Q24 Tuple malumot turini necha metodi mavjud": '2',
    "Q25 Lug'atda barcha kalitlarni qaytaruvchi metod": 'keys',
    "Q26 Har bir kalit qiymat juftligi uchun tuple qaytaradigan metod": "items",
    "Q27 Lug'atga malumot qo'shuvchi metod": 'update',
    "Q28 List elementlarni bir ma bir olish qaysi ichki funksiya ishlatiladi": 'for',
    "Q29 Qatorni chappa teskari qiluvchi indexni kiriting": '[-1::-1]',
    "Q30 O'zgaruvchini qaysi turga mansub ekanligini aniqlovchi ichki funksiya": 'type',
    "Q31 Katta yoki teng belgisni kiriting": '>=',
    "Q32 Teng emas belgisini kiriting": "!=",
    "Q33 Ikki qator bir xil ekanligi tekshirmoqchi bo'lsangiz, qanaqa ichki funksiyani ishlatasiz": 'is',
    "Q34 Qator ichida malum bir belgi mavjud ekanligini tekshiruvchi ichki funksiya": 'in',
    "Q35 Mantiqiy malumot turi nma deb ataladi": 'bool',

}

examinator_gui = ExaminatorGUI(questions)
examinator_gui.window.mainloop()
