import tkinter as tk
from tkinter import messagebox
import random

class JokeTellerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Alexa Joke Teller")
        self.root.geometry("700x550")
        self.root.resizable(False, False)
        
        # Darker color scheme
        self.bg_color = "#0a0a0a"
        self.secondary_bg = "#1a1a1a"
        self.accent_color = "#1e1e1e"
        self.highlight_color = "#ff6b6b"
        self.text_color = "#ffffff"
        self.subtitle_color = "#888888"
        
        self.root.configure(bg=self.bg_color)
        
        # Load jokes
        self.jokes = []
        self.current_joke_index = -1
        self.punchline_shown = False
        self.load_jokes()
        
        # Header Frame
        self.header_frame = tk.Frame(root, bg=self.secondary_bg, height=140)
        self.header_frame.pack(fill="x", pady=0)
        self.header_frame.pack_propagate(False)
        
        # Title
        self.title_label = tk.Label(
            self.header_frame,
            text="ALEXA",
            font=("Segoe UI", 32, "bold"),
            bg=self.secondary_bg,
            fg=self.highlight_color
        )
        self.title_label.pack(pady=(25, 0))
        
        # Subtitle
        self.subtitle_label = tk.Label(
            self.header_frame,
            text="J O K E   T E L L E R",
            font=("Segoe UI", 11),
            bg=self.secondary_bg,
            fg=self.subtitle_color
        )
        self.subtitle_label.pack(pady=(5, 15))
        
        # Decorative line
        self.line = tk.Frame(self.header_frame, bg=self.highlight_color, height=2)
        self.line.pack(fill="x", padx=150)
        
        # Main content frame
        self.content_frame = tk.Frame(root, bg=self.bg_color)
        self.content_frame.pack(fill="both", expand=True, padx=40, pady=30)
        
        # Joke display card
        self.joke_card = tk.Frame(self.content_frame, bg=self.accent_color, relief="flat", bd=0)
        self.joke_card.pack(fill="both", expand=True)
        
        # Setup Label
        self.setup_label = tk.Label(
            self.joke_card,
            text="Ready to laugh?\n\nClick 'Tell Me a Joke' to begin",
            font=("Segoe UI", 16, "bold"),
            bg=self.accent_color,
            fg=self.text_color,
            wraplength=600,
            justify="center",
            pady=40
        )
        self.setup_label.pack(fill="both", expand=True, padx=20)
        
        # Punchline Label
        self.punchline_label = tk.Label(
            self.joke_card,
            text="",
            font=("Segoe UI", 15),
            bg=self.accent_color,
            fg="#ffd93d",
            wraplength=600,
            justify="center",
            pady=30
        )
        self.punchline_label.pack(fill="both", expand=True, padx=20)
        
        # Button container
        self.button_container = tk.Frame(root, bg=self.bg_color)
        self.button_container.pack(side="bottom", fill="x", padx=40, pady=(0, 30))
        
        # Top row buttons
        self.top_button_frame = tk.Frame(self.button_container, bg=self.bg_color)
        self.top_button_frame.pack(fill="x", pady=(0, 10))
        
        # Tell me a Joke button
        self.joke_button = tk.Button(
            self.top_button_frame,
            text="Tell Me a Joke",
            font=("Segoe UI", 12, "bold"),
            bg="#ff6b6b",
            fg="white",
            activebackground="#ff5252",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            height=2,
            bd=0,
            command=self.tell_joke
        )
        self.joke_button.pack(side="left", fill="x", expand=True, padx=(0, 5))
        
        # Show Punchline button
        self.punchline_button = tk.Button(
            self.top_button_frame,
            text="Show Punchline",
            font=("Segoe UI", 12, "bold"),
            bg="#4ecdc4",
            fg="white",
            activebackground="#3db8af",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            height=2,
            bd=0,
            state="disabled",
            command=self.show_punchline
        )
        self.punchline_button.pack(side="left", fill="x", expand=True, padx=(5, 0))
        
        # Bottom row buttons
        self.bottom_button_frame = tk.Frame(self.button_container, bg=self.bg_color)
        self.bottom_button_frame.pack(fill="x")
        
        # Next Joke button
        self.next_button = tk.Button(
            self.bottom_button_frame,
            text="Next Joke",
            font=("Segoe UI", 12, "bold"),
            bg="#a29bfe",
            fg="white",
            activebackground="#8b83eb",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            height=2,
            bd=0,
            state="disabled",
            command=self.next_joke
        )
        self.next_button.pack(side="left", fill="x", expand=True, padx=(0, 5))
        
        # Exit button
        self.exit_button = tk.Button(
            self.bottom_button_frame,
            text="Exit",
            font=("Segoe UI", 12, "bold"),
            bg="#2d3436",
            fg="white",
            activebackground="#1e2021",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            height=2,
            bd=0,
            command=self.exit_app
        )
        self.exit_button.pack(side="left", fill="x", expand=True, padx=(5, 0))
        
    def load_jokes(self):
        """Load jokes from randomJokes.txt file"""
        import os
        
        # Debug: Show current working directory
        current_dir = os.getcwd()
        print(f"Current directory: {current_dir}")
        print(f"Files in directory: {os.listdir(current_dir)}")
        
        try:
            with open("randomJokes.txt", "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    if line and "?" in line:
                        parts = line.split("?", 1)
                        if len(parts) == 2:
                            setup = parts[0].strip() + "?"
                            punchline = parts[1].strip()
                            self.jokes.append((setup, punchline))
            
            if not self.jokes:
                messagebox.showerror("Error", "No jokes found in randomJokes.txt")
                self.root.destroy()
        except FileNotFoundError as e:
            error_msg = f"File not found!\n\nLooking in: {current_dir}\n\nPlease make sure 'randomJokes.txt' is in the same folder as your Python script."
            messagebox.showerror("Error", error_msg)
            print(f"Error details: {e}")
            self.root.destroy()
    
    def tell_joke(self):
        """Display a random joke"""
        if not self.jokes:
            return
        
        # Pick a random joke
        self.current_joke_index = random.randint(0, len(self.jokes) - 1)
        joke = self.jokes[self.current_joke_index]
        
        self.setup_label.config(text=joke[0])
        self.punchline_label.config(text="")
        self.punchline_shown = False
        
        # Enable punchline and next buttons
        self.punchline_button.config(state="normal", bg="#4ecdc4")
        self.next_button.config(state="normal", bg="#a29bfe")
    
    def show_punchline(self):
        """Display the punchline of the current joke"""
        if self.current_joke_index >= 0 and not self.punchline_shown:
            joke = self.jokes[self.current_joke_index]
            self.punchline_label.config(text=joke[1])
            self.punchline_shown = True
            self.punchline_button.config(state="disabled", bg="#555555")
    
    def next_joke(self):
        """Display the next random joke"""
        if not self.jokes:
            return
        
        # Pick a new random joke
        self.current_joke_index = random.randint(0, len(self.jokes) - 1)
        joke = self.jokes[self.current_joke_index]
        
        self.setup_label.config(text=joke[0])
        self.punchline_label.config(text="")
        self.punchline_shown = False
        
        # Enable punchline button
        self.punchline_button.config(state="normal", bg="#4ecdc4")
    
    def exit_app(self):
        """Exit the application"""
        self.root.destroy()

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = JokeTellerApp(root)
    root.mainloop()