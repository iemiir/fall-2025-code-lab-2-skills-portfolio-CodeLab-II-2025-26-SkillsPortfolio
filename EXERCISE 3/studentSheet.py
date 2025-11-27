import customtkinter as ctk
from tkinter import messagebox, simpledialog
import os

# -------------------------------
# CONFIG
# -------------------------------
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


# -------------------------------
# STUDENT MANAGER CLASS
# -------------------------------
class StudentManagerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("MIR'S Student Manager Dashboard")
        self.geometry("1100x650")
        self.configure(fg_color="#E8EEFF")

        self.students = self.load_data()

        # Sidebar + main layout
        self.create_layout()

    # ---------------------------
    # READ FILE
    # ---------------------------
    def load_data(self):
        filename = "studentMarks.txt"
        students = []

        if not os.path.exists(filename):
            messagebox.showerror("Error", "studentMarks.txt not found!")
            return []

        with open(filename, "r") as f:
            lines = f.read().strip().split("\n")

        for line in lines:
            parts = line.split(",")
            if len(parts) != 6:
                continue

            code = parts[0].strip()
            name = parts[1].strip()
            c1, c2, c3 = map(int, parts[2:5])
            exam = int(parts[5])

            students.append({
                "code": code,
                "name": name,
                "coursework": c1 + c2 + c3,
                "exam": exam,
                "total": (c1 + c2 + c3) + exam,
            })

        return students

    # ---------------------------
    # WRITE FILE
    # ---------------------------
    def save_data(self):
        with open("studentMarks.txt", "w") as f:
            for s in self.students:
                cw1 = cw2 = cw3 = s["coursework"] // 3  # simple split
                f.write(f"{s['code']},{s['name']},{cw1},{cw2},{cw3},{s['exam']}\n")

    # ---------------------------
    # UI LAYOUT
    # ---------------------------
    def create_layout(self):
        # LEFT MENU
        self.menu_frame = ctk.CTkFrame(self, width=300, corner_radius=20, fg_color="white")
        self.menu_frame.pack(side="left", fill="y", padx=20, pady=20)

        title = ctk.CTkLabel(
            self.menu_frame,
            text="Student Manager",
            font=("Segoe UI", 24, "bold"),
            text_color="#1F1F1F"
        )
        title.pack(pady=(20, 30))

        # Buttons
        self.create_menu_btn("View All Student Records", self.view_all, "#3E6FF4")
        self.create_menu_btn("View Individual Student", self.view_individual, "#8D63E6")
        self.create_menu_btn("Highest Overall Mark", self.view_highest, "#18A865")
        self.create_menu_btn("Lowest Overall Mark", self.view_lowest, "#D9534F")
        self.create_menu_btn("Add Student Record", self.add_student, "#1BAFAF")

        # RIGHT OUTPUT FRAME (kept white for nice contrast)
        self.output_frame = ctk.CTkFrame(self, fg_color="white", corner_radius=20)
        self.output_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)


        self.output_box = ctk.CTkTextbox(
            self.output_frame,
            font=("Consolas", 14),
            text_color="#FFFFFF",    # White text
            fg_color="#000000",      # Black background
            corner_radius=12,
            border_width=2,
            border_color="#333333"
        )
        self.output_box.pack(fill="both", expand=True, padx=20, pady=20)

    # ---------------------------
    # BUTTON MAKER
    # ---------------------------
    def create_menu_btn(self, text, command, color):
        btn = ctk.CTkButton(
            self.menu_frame,
            text=text,
            command=command,
            fg_color=color,
            height=55,
            corner_radius=12,
            font=("Segoe UI", 15, "bold")
        )
        btn.pack(fill="x", padx=20, pady=10)

    # ---------------------------
    # FUNCTION: VIEW ALL
    # ---------------------------
    def view_all(self):
        self.output_box.delete("1.0", "end")
        total_percent = 0

        for s in self.students:
            percent = (s["total"] / 160) * 100
            total_percent += percent

            grade = self.calculate_grade(percent)

            self.output_box.insert("end", f"Name: {s['name']}\n")
            self.output_box.insert("end", f"Code: {s['code']}\n")
            self.output_box.insert("end", f"Coursework: {s['coursework']}\n")
            self.output_box.insert("end", f"Exam: {s['exam']}\n")
            self.output_box.insert("end", f"Total %: {percent:.2f}%\n")
            self.output_box.insert("end", f"Grade: {grade}\n")
            self.output_box.insert("end", "-"*40 + "\n\n")

        if self.students:
            avg = total_percent / len(self.students)
            self.output_box.insert("end", f"\nTotal Students: {len(self.students)}")
            self.output_box.insert("end", f"\nAverage Percentage: {avg:.2f}%")

    # ---------------------------
    # FUNCTION: VIEW INDIVIDUAL
    # ---------------------------
    def view_individual(self):
        code = simpledialog.askstring("Search", "Enter student code:")
        if code is None:
            return

        for s in self.students:
            if s["code"] == code.strip():
                self.display_student(s)
                return

        messagebox.showerror("Error", "Student not found!")

    # ---------------------------
    # FUNCTION: HIGHEST
    # ---------------------------
    def view_highest(self):
        if self.students:
            s = max(self.students, key=lambda x: x["total"])
            self.display_student(s)
        else:
            self.output_box.delete("1.0", "end")
            self.output_box.insert("end", "No student records found!")

    # ---------------------------
    # FUNCTION: LOWEST
    # ---------------------------
    def view_lowest(self):
        if self.students:
            s = min(self.students, key=lambda x: x["total"])
            self.display_student(s)
        else:
            self.output_box.delete("1.0", "end")
            self.output_box.insert("end", "No student records found!")

    # ---------------------------
    # ADD STUDENT
    # ---------------------------
    def add_student(self):
        try:
            code = simpledialog.askstring("Add Student", "Enter student code:")
            if not code: return
            name = simpledialog.askstring("Add Student", "Enter student name:")
            if not name: return
            c1 = int(simpledialog.askstring("Add Student", "Coursework 1 (0-20):") or 0)
            c2 = int(simpledialog.askstring("Add Student", "Coursework 2 (0-20):") or 0)
            c3 = int(simpledialog.askstring("Add Student", "Coursework 3 (0-20):") or 0)
            exam = int(simpledialog.askstring("Add Student", "Exam Mark (0-100):") or 0)

            new = {
                "code": code.strip(),
                "name": name.strip(),
                "coursework": c1 + c2 + c3,
                "exam": exam,
                "total": (c1 + c2 + c3) + exam
            }

            self.students.append(new)
            self.save_data()
            messagebox.showinfo("Success", f"Student {name} added successfully!")
        except:
            messagebox.showerror("Error", "Invalid input! Please try again.")

    # ---------------------------
    # DISPLAY STUDENT HELPER
    # ---------------------------
    def display_student(self, s):
        self.output_box.delete("1.0", "end")
        percent = (s["total"] / 160) * 100
        grade = self.calculate_grade(percent)

        self.output_box.insert("end", f"Name: {s['name']}\n")
        self.output_box.insert("end", f"Code: {s['code']}\n")
        self.output_box.insert("end", f"Coursework: {s['coursework']}\n")
        self.output_box.insert("end", f"Exam: {s['exam']}\n")
        self.output_box.insert("end", f"Total %: {percent:.2f}%\n")
        self.output_box.insert("end", f"Grade: {grade}\n")

    # ---------------------------
    # GRADE CALCULATOR
    # ---------------------------
    def calculate_grade(self, percent):
        if percent >= 70:
            return "A"
        elif percent >= 60:
            return "B"
        elif percent >= 50:
            return "C"
        elif percent >= 40:
            return "D"
        else:
            return "F"


# -----------------------------
# RUN APP
# -----------------------------
if __name__ == "__main__":
    app = StudentManagerApp()
    app.mainloop()