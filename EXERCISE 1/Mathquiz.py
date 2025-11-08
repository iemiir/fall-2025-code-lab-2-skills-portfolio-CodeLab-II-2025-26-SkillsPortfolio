import tkinter as tk
from tkinter import messagebox
import random


class MathQuizGame:
    """MIRS Math Quiz - Professional and Stylish"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("MIRS Math Quiz")
        
        # Make fullscreen
        self.root.state('zoomed')
        
        # Color Scheme For The Quiz
        self.colors = {
            'bg': '#0a0e27',
            'bg_card': '#1a1f3a',
            'primary': '#ff0080',
            'secondary': '#00d4ff',
            'success': '#00ff88',
            'warning': '#ffa500',
            'danger': '#ff0055',
            'text': '#ffffff',
            'text2': "#000000",
            'text_dim': '#a0a0a0'
        }
        
        # Game variables
        self.difficulty = None
        self.score = 0
        self.question_count = 0
        self.total_questions = 10
        self.current_num1 = 0
        self.current_num2 = 0
        self.current_operation = ''
        self.correct_answer = 0
        self.attempts = 0
        
        self.displayMenu()
    
    def clear_screen(self):
        """Clear all widgets"""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def create_gradient_label(self, parent, text, font_size, fg_color):
        """Create a styled label"""
        label = tk.Label(
            parent,
            text=text,
            font=('Arial Black', font_size, 'bold'),
            fg=fg_color,
            bg=self.colors['bg']
        )
        return label
    
    def create_styled_button(self, parent, text, command, bg_color, width=25):
        """Create a beautiful 3D-style button"""
        button = tk.Button(
            parent,
            text=text,
            command=command,
            font=('Arial', 16, 'bold'),
            bg=bg_color,
            fg=self.colors['text2'],
            activebackground=bg_color,
            activeforeground='white',
            width=width,
            height=2,
            relief='flat',
            cursor='hand2',
            borderwidth=0
        )
        
        # Hover effects
        def on_enter(e):
            button.config(bg=self._lighten_color(bg_color))
        
        def on_leave(e):
            button.config(bg=bg_color)
        
        button.bind('<Enter>', on_enter)
        button.bind('<Leave>', on_leave)
        
        return button
    
    def _lighten_color(self, color):
        """Lighten a hex color for hover effect"""
        color = color.lstrip('#')
        r, g, b = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
        r = min(255, r + 30)
        g = min(255, g + 30)
        b = min(255, b + 30)
        return f'#{r:02x}{g:02x}{b:02x}'
    
    def add_background_math_symbols(self, parent):
        """Add decorative math symbols in the background"""
        symbols = ['+', '-', '×', '÷', '=', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        positions = [
            (50, 50), (150, 100), (250, 80), (100, 200), (200, 250),
            (1400, 50), (1300, 150), (1450, 200), (1350, 300),
            (50, 600), (150, 700), (100, 500),
            (1400, 600), (1300, 700), (1450, 500)
        ]
        
        for i, (x, y) in enumerate(positions):
            symbol = random.choice(symbols)
            label = tk.Label(
                parent,
                text=symbol,
                font=('Arial Black', 80, 'bold'),
                fg='#1a2345',  # Very dark, subtle color
                bg=self.colors['bg']
            )
            label.place(x=x, y=y)
    
    def displayMenu(self):
        """Display the main menu"""
        self.clear_screen()
        self.root.config(bg=self.colors['bg'])
        self.add_background_math_symbols(self.root)
        
        # Main container
        main_frame = tk.Frame(self.root, bg=self.colors['bg'])
        main_frame.pack(expand=True)
        
        # Title - MIRS
        title_mirs = tk.Label(
            main_frame,
            text="MIR'S",
            font=('Impact', 90, 'bold', 'underline'),
            fg=self.colors['primary'],
            bg=self.colors['bg']
        )
        title_mirs.pack(pady=(50, 0))
        
        # Subtitle - MATH QUIZ
        title_math = tk.Label(
            main_frame,
            text="MATH QUIZ",
            font=('Impact', 50, 'bold'),
            fg=self.colors['secondary'],
            bg=self.colors['bg']
        )
        title_math.pack(pady=(0, 10))
        
        # Tagline
        tagline = tk.Label(
            main_frame,
            text="✨ Test Your Brain Power! ✨",
            font=('Arial', 16),
            fg=self.colors['text_dim'],
            bg=self.colors['bg']
        )
        tagline.pack(pady=(0, 50))
        
        # Buttons
        btn_start = self.create_styled_button(
            main_frame,
            "▶  START GAME",
            self.showDifficultyMenu,
            self.colors['success']
        )
        btn_start.pack(pady=12)
        
        btn_instructions = self.create_styled_button(
            main_frame,
            "📖  INSTRUCTIONS",
            self.showInstructions,
            self.colors['secondary']
        )
        btn_instructions.pack(pady=12)
        
        btn_exit = self.create_styled_button(
            main_frame,
            "✕  EXIT",
            self.root.quit,
            self.colors['danger']
        )
        btn_exit.pack(pady=12)
    
    def showInstructions(self):
        """Display instructions screen"""
        self.clear_screen()
        self.root.config(bg=self.colors['bg'])
        self.add_background_math_symbols(self.root)
        
        # Main container
        main_frame = tk.Frame(self.root, bg=self.colors['bg'])
        main_frame.pack(expand=True)
        
        # Title - smaller
        title = tk.Label(
            main_frame,
            text="HOW TO PLAY",
            font=('Impact', 35, 'bold', 'underline'),
            fg=self.colors['secondary'],
            bg=self.colors['bg']
        )
        title.pack(pady=15)
        
        # Instructions Card - more compact
        card_frame = tk.Frame(main_frame, bg=self.colors['bg_card'], relief='flat', bd=0)
        card_frame.pack(padx=80, pady=10)
        
        instructions = """
        GAME RULES:
        1) Select your difficulty level (Easy, Moderate, or Advanced)
        2) Answer 10 math questions (addition and subtraction)
        3) You get 2 attempts for each question
        
        SCORING SYSTEM:
        1) Correct on 1st attempt: 10 points
        2) Correct on 2nd attempt: 5 points
        3) Wrong on both attempts: 0 points
        
        DIFFICULTY LEVELS:
        1) Level 1 (Easy): Single-digit (0-9)
        2) Level 2 (Moderate): Two-digit (10-99)
        3) Level 3 (Advanced): Four-digit (1000-9999)
        
        TIP: Return to menu or change difficulty anytime!
        """
        
        instructions_label = tk.Label(
            card_frame,
            text=instructions,
            font=('Impact', 15),
            fg=self.colors['text'],
            bg=self.colors['bg_card'],
            justify='left',
            anchor='w'
        )
        instructions_label.pack(padx=30, pady=25, anchor='w')
        
        # Back button
        btn_back = self.create_styled_button(
            main_frame,
            "🏠  BACK TO MENU",
            self.displayMenu,
            self.colors['warning'],
            width=30
        )
        btn_back.pack(pady=15)
    
    def showDifficultyMenu(self):
        """Display difficulty selection menu"""
        self.clear_screen()
        self.root.config(bg=self.colors['bg'])
        self.add_background_math_symbols(self.root)
        
        # Main container
        main_frame = tk.Frame(self.root, bg=self.colors['bg'])
        main_frame.pack(expand=True)
        
        # Title
        title = tk.Label(
            main_frame,
            text="SELECT DIFFICULTY",
            font=('Impact', 50, 'bold'),
            fg=self.colors['warning'],
            bg=self.colors['bg']
        )
        title.pack(pady=50)
        
        # Level buttons
        btn_level1 = self.create_styled_button(
            main_frame,
            "LEVEL 1 - EASY",
            lambda: self.startQuiz(1),
            self.colors['success'],
            width=35
        )
        btn_level1.pack(pady=15)
        
        btn_level2 = self.create_styled_button(
            main_frame,
            "LEVEL 2 - MODERATE",
            lambda: self.startQuiz(2),
            self.colors['warning'],
            width=35
        )
        btn_level2.pack(pady=15)
        
        btn_level3 = self.create_styled_button(
            main_frame,
            "LEVEL 3 - ADVANCED",
            lambda: self.startQuiz(3),
            self.colors['danger'],
            width=35
        )
        btn_level3.pack(pady=15)
        
        # Back button
        btn_back = self.create_styled_button(
            main_frame,
            "🏠  BACK TO MENU",
            self.displayMenu,
            '#444466',
            width=30
        )
        btn_back.pack(pady=30)
    
    def startQuiz(self, difficulty):
        """Start the quiz with selected difficulty"""
        self.difficulty = difficulty
        self.score = 0
        self.question_count = 0
        self.attempts = 0
        self.displayProblem()
    
    def randomInt(self):
        """Generate random integers based on difficulty"""
        if self.difficulty == 1:
            return random.randint(0, 9), random.randint(0, 9)
        elif self.difficulty == 2:
            return random.randint(10, 99), random.randint(10, 99)
        else:
            return random.randint(1000, 9999), random.randint(1000, 9999)
    
    def decideOperation(self):
        """Randomly decide between addition or subtraction"""
        return random.choice(['+', '-'])
    
    def displayProblem(self):
        """Display the current math problem"""
        if self.question_count >= self.total_questions:
            self.displayResults()
            return
        
        self.question_count += 1
        self.attempts = 0
        
        # Generate problem
        self.current_num1, self.current_num2 = self.randomInt()
        self.current_operation = self.decideOperation()
        
        if self.current_operation == '+':
            self.correct_answer = self.current_num1 + self.current_num2
        else:
            self.correct_answer = self.current_num1 - self.current_num2
        
        self.clear_screen()
        self.root.config(bg=self.colors['bg'])
        self.add_background_math_symbols(self.root)
        
        # Header with score and question count
        header_frame = tk.Frame(self.root, bg=self.colors['bg_card'], height=80)
        header_frame.pack(fill='x', pady=(0, 30))
        header_frame.pack_propagate(False)
        
        score_label = tk.Label(
            header_frame,
            text=f"💰 Score: {self.score}/100",
            font=('Arial', 18, 'bold'),
            fg=self.colors['success'],
            bg=self.colors['bg_card']
        )
        score_label.pack(side='left', padx=50, pady=20)
        
        question_label = tk.Label(
            header_frame,
            text=f"📝 Question: {self.question_count}/{self.total_questions}",
            font=('Arial', 18, 'bold'),
            fg=self.colors['secondary'],
            bg=self.colors['bg_card']
        )
        question_label.pack(side='right', padx=50, pady=20)
        
        # Main problem container
        main_frame = tk.Frame(self.root, bg=self.colors['bg'])
        main_frame.pack(expand=True)
        
        # Problem display
        problem_card = tk.Frame(main_frame, bg=self.colors['bg_card'], relief='flat')
        problem_card.pack(pady=30, padx=100, ipadx=100, ipady=60)
        
        problem_text = tk.Label(
            problem_card,
            text=f"{self.current_num1}  {self.current_operation}  {self.current_num2}  =  ?",
            font=('Courier New', 60, 'bold'),
            fg=self.colors['primary'],
            bg=self.colors['bg_card']
        )
        problem_text.pack(pady=30)
        
        # Answer section
        answer_label = tk.Label(
            main_frame,
            text="Your Answer:",
            font=('Arial', 20, 'bold'),
            fg=self.colors['text'],
            bg=self.colors['bg']
        )
        answer_label.pack(pady=10)
        
        self.answer_entry = tk.Entry(
            main_frame,
            font=('Courier New', 28, 'bold'),
            width=20,
            justify='center',
            bg=self.colors['bg_card'],
            fg=self.colors['text'],
            insertbackground=self.colors['primary'],
            relief='flat',
            bd=5
        )
        self.answer_entry.pack(pady=15, ipady=15)
        self.answer_entry.focus()
        self.answer_entry.bind('<Return>', lambda e: self.checkAnswer())
        
        # Buttons
        button_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        button_frame.pack(pady=30)
        
        btn_submit = self.create_styled_button(
            button_frame,
            "✓  SUBMIT",
            self.checkAnswer,
            self.colors['success'],
            width=15
        )
        btn_submit.pack(side='left', padx=10)
        
        btn_menu = self.create_styled_button(
            button_frame,
            "🏠  MENU",
            self.displayMenu,
            '#444466',
            width=15
        )
        btn_menu.pack(side='left', padx=10)
        
        btn_change = self.create_styled_button(
            button_frame,
            "🔄  CHANGE LEVEL",
            self.showDifficultyMenu,
            self.colors['warning'],
            width=18
        )
        btn_change.pack(side='left', padx=10)
    
    def isCorrect(self, user_answer):
        """Check if answer is correct"""
        return user_answer == self.correct_answer
    
    def checkAnswer(self):
        """Check the user's answer"""
        try:
            user_answer = int(self.answer_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number!")
            return
        
        if self.isCorrect(user_answer):
            if self.attempts == 0:
                self.score += 10
                messagebox.showinfo(
                    "🎉 Correct!",
                    f"Excellent! First try!\n\n+10 points\n\nCurrent Score: {self.score}"
                )
            else:
                self.score += 5
                messagebox.showinfo(
                    "👍 Correct!",
                    f"Good job! Second try!\n\n+5 points\n\nCurrent Score: {self.score}"
                )
            self.displayProblem()
        else:
            if self.attempts == 0:
                self.attempts = 1
                messagebox.showwarning(
                    "❌ Incorrect",
                    "Wrong answer!\n\nYou have one more attempt."
                )
                self.answer_entry.delete(0, tk.END)
                self.answer_entry.focus()
            else:
                messagebox.showinfo(
                    "❌ Wrong Answer",
                    f"Incorrect!\n\nThe correct answer was: {self.correct_answer}\n\nMoving to next question..."
                )
                self.displayProblem()
    
    def displayResults(self):
        """Display final results"""
        self.clear_screen()
        self.root.config(bg=self.colors['bg'])
        self.add_background_math_symbols(self.root)
        
        # Main container
        main_frame = tk.Frame(self.root, bg=self.colors['bg'])
        main_frame.pack(expand=True)
        
        # Trophy icon (using text) - smaller
        trophy = tk.Label(
            main_frame,
            text="🏆",
            font=('Arial', 60),
            bg=self.colors['bg']
        )
        trophy.pack(pady=10)
        
        # Title - smaller
        title = tk.Label(
            main_frame,
            text="QUIZ COMPLETE!",
            font=('Impact', 40, 'bold'),
            fg=self.colors['warning'],
            bg=self.colors['bg']
        )
        title.pack(pady=10)
        
        # Score card - more compact
        score_card = tk.Frame(main_frame, bg=self.colors['bg_card'], relief='flat')
        score_card.pack(pady=15, padx=100, ipadx=60, ipady=30)
        
        score_title = tk.Label(
            score_card,
            text="FINAL SCORE",
            font=('Arial', 16, 'bold'),
            fg=self.colors['text_dim'],
            bg=self.colors['bg_card']
        )
        score_title.pack(pady=5)
        
        score_value = tk.Label(
            score_card,
            text=f"{self.score}/100",
            font=('Impact', 50, 'bold'),
            fg=self.colors['secondary'],
            bg=self.colors['bg_card']
        )
        score_value.pack(pady=5)
        
        # Calculate grade
        if self.score >= 90:
            grade, message, color = "A+", "OUTSTANDING! 🌟", self.colors['success']
        elif self.score >= 80:
            grade, message, color = "A", "EXCELLENT! 🎉", self.colors['secondary']
        elif self.score >= 70:
            grade, message, color = "B", "GREAT JOB! 👍", '#9d4edd'
        elif self.score >= 60:
            grade, message, color = "C", "GOOD EFFORT! 📚", self.colors['warning']
        else:
            grade, message, color = "F", "KEEP TRYING! 💪", self.colors['danger']
        
        grade_label = tk.Label(
            score_card,
            text=f"Grade: {grade}",
            font=('Impact', 35, 'bold'),
            fg=color,
            bg=self.colors['bg_card']
        )
        grade_label.pack(pady=5)
        
        message_label = tk.Label(
            score_card,
            text=message,
            font=('Arial', 18, 'bold'),
            fg=color,
            bg=self.colors['bg_card']
        )
        message_label.pack(pady=5)
        
        # Buttons - more compact
        btn_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        btn_frame.pack(pady=15)
        
        # Show "Next Level" button only if not on max difficulty
        if self.difficulty < 3:
            btn_next_level = self.create_styled_button(
                btn_frame,
                f"⬆  NEXT LEVEL ({['MODERATE', 'ADVANCED'][self.difficulty - 1]})",
                lambda: self.startQuiz(self.difficulty + 1),
                self.colors['primary'],
                width=30
            )
            btn_next_level.pack(pady=8)
        
        btn_play_again = self.create_styled_button(
            btn_frame,
            "🔄  PLAY SAME LEVEL AGAIN",
            lambda: self.startQuiz(self.difficulty),
            self.colors['success'],
            width=30
        )
        btn_play_again.pack(pady=8)
        
        btn_menu = self.create_styled_button(
            btn_frame,
            "🏠  HOME PAGE",
            self.displayMenu,
            self.colors['secondary'],
            width=30
        )
        btn_menu.pack(pady=8)
        
        btn_change_level = self.create_styled_button(
            btn_frame,
            "🎯  CHOOSE DIFFERENT LEVEL",
            self.showDifficultyMenu,
            self.colors['warning'],
            width=30
        )
        btn_change_level.pack(pady=8)
        
        btn_exit = self.create_styled_button(
            btn_frame,
            "✕  EXIT",
            self.root.quit,
            self.colors['danger'],
            width=25
        )
        btn_exit.pack(pady=8)


def main():
    """Main function to run the application"""
    root = tk.Tk()
    app = MathQuizGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()