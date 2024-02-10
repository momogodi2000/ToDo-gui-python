from tkinter import *
from tkinter import messagebox, simpledialog

# Global list for storing tasks
tasks_list = []
# Global variable for counting tasks
counter = 1

# Function for checking input error when empty input is given in task field
def inputError():
    if enterTaskField.get() == "":
        messagebox.showerror(language['error_title'], language['error_message'])
        return False
    return True

# Function for clearing the contents of task number text field
def clear_taskNumberField():
    taskNumberField.delete(0.0, END)

# Function for clearing the contents of task entry field
def clear_taskField():
    enterTaskField.delete(0, END)

# Function for inserting the contents from the task entry field to the text area
def insertTask():
    global counter

    # Check for input error
    if not inputError():
        return

    content = enterTaskField.get() + "\n"
    tasks_list.append(content)

    TextArea.insert('end -1 chars', "[ " + str(counter) + " ] " + content)
    counter += 1
    clear_taskField()

# Function for deleting the specified task
def delete():
    global counter

    if len(tasks_list) == 0:
        messagebox.showerror(language['no_task_title'], language['no_task_message'])
        return

    number = taskNumberField.get(1.0, END)

    if number == "\n":
        messagebox.showerror(language['input_error_title'], language['input_error_message'])
        return
    else:
        task_no = int(number)

    clear_taskNumberField()
    tasks_list.pop(task_no - 1)
    counter -= 1

    TextArea.delete(1.0, END)
    for i in range(len(tasks_list)):
        TextArea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + tasks_list[i])

# Function for displaying a reminder alert
def setReminder():
    reminder_time = simpledialog.askstring(language['reminder_title'], language['reminder_message'])
    if reminder_time:
        messagebox.showinfo(language['reminder_alert_title'], language['reminder_alert_message'] + reminder_time)

# Create a GUI window
gui = Tk()
gui.configure(background="#94d3f7")
gui.title("ToDo App")
gui.geometry("250x350")

# Create a language selection dialog
language = simpledialog.askstring("Language Selection", "Select your preferred language (English, Spanish, French, German, Italian):")
if language not in ["English", "Spanish", "French", "German", "Italian"]:
    language = "English"

# Language dictionary for different languages
language_dict = {
    "English": {
        "title": "ToDo App",
        "enter_task": "Enter Your Task",
        "submit": "Submit",
        "delete_task_number": "Delete Task Number",
        "delete": "Delete",
        "exit": "Exit",
        "error_title": "Input Error",
        "error_message": "Please enter a task.",
        "no_task_title": "No Task",
        "no_task_message": "No tasks available.",
        "input_error_title": "Input Error",
        "input_error_message": "Please enter a valid task number.",
        "reminder_title": "Set Reminder",
        "reminder_message": "Enter the reminder time (e.g., 10:30 AM):",
        "reminder_alert_title": "Reminder Alert",
        "reminder_alert_message": "Reminder set for "
    },
    "Spanish": {
        # Add Spanish translations here
    },
    "French": {
        # Add French translations here
    },
    "German": {
        # Add German translations here
    },
    "Italian": {
        # Add Italian translations here
    }
}

# Set the language dictionary based on the selected language
language = language_dict[language]

# Create labels and buttons with the translated text
enterTask = Label(gui, text=language['enter_task'], background="#94d3f7")
enterTaskField = Entry(gui, background="#e8e9ed")
Submit = Button(gui, text=language['submit'], fg="Black", bg="#fafcfc", command=insertTask)
TextArea = Text(gui, height=5, width=25, font="lucida 13", background="#e8e9ed")
taskNumber = Label(gui, text=language['delete_task_number'], bg="#94d3f7")
taskNumberField = Text(gui, height=1, width=2, font="lucida 13", background="#e8e9ed")
delete = Button(gui, text=language['delete'], fg="Black", bg="#fafcfc", command=delete)
Exit = Button(gui, text=language['exit'], fg="Black", bg="#f25f49", command=exit)
Reminder = Button(gui, text="Set Reminder", fg="Black", bg="#fafcfc", command=setReminder)

# Grid placement for labels and buttons
enterTask.grid(row=0, column=2)
enterTaskField.grid(row=1, column=2, ipadx=50)
Submit.grid(row=3, column=2)
TextArea.grid(row=5, column=2, padx=10, sticky=W)
taskNumber.grid(row=6, column=2, pady=5)
taskNumberField.grid(row=7, column=2)
delete.grid(row=8, column=2, pady=5)
Exit.grid(row=9, column=2)
Reminder.grid(row=10, column=2)

# Function to update the tasks display in the selected language
def updateTasksDisplay():
    TextArea.delete(1.0, END)
    for i in range(len(tasks_list)):
        TextArea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + tasks_list[i])

# Start the GUI
gui.mainloop()