from tkinter import *

def calculate_percentage():
    try:
        subject1 = float(entry_subject1.get())
        subject2 = float(entry_subject2.get())
        subject3 = float(entry_subject3.get())

        total_marks = subject1 + subject2 + subject3
        percentage = (total_marks / 300) * 100

        grade = grade_var.get()
        pass_status = "Pass" if percentage >= 40 else "Fail"

        result_label.config(text=f"Percentage: {percentage:.2f}%\nGrade: {grade}\nStatus: {pass_status}")

    except ValueError:
        result_label.config(text="Please enter valid numeric values for all subjects.")

root = Tk()
root.title("Percentage Calculator")


entry_subject1 = Entry(root, width=10)
entry_subject1.grid(row=0, column=1, padx=10, pady=10)
label_subject1 = Label(root, text="Subject 1:")
label_subject1.grid(row=0, column=0)

entry_subject2 = Entry(root, width=10)
entry_subject2.grid(row=1, column=1, padx=10, pady=10)
label_subject2 = Label(root, text="Subject 2:")
label_subject2.grid(row=1, column=0)

entry_subject3 = Entry(root, width=10)
entry_subject3.grid(row=2, column=1, padx=10, pady=10)
label_subject3 = Label(root, text="Subject 3:")
label_subject3.grid(row=2, column=0)


grades = ["Grade 3", "Grade 5", "Grade 10"]
grade_var = StringVar(root)
grade_var.set(grades[0]) 
grade_dropdown = OptionMenu(root, grade_var, *grades)
grade_dropdown.grid(row=3, column=0, columnspan=2, pady=10)

calculate_button = Button(root, text="Calculate", command=calculate_percentage)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

result_label = Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
