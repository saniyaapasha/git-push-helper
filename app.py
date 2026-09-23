import tkinter as tk

def add_numbers():
    result = int(num1.get()) + int(num2.get())
    answer.config(text=f"Result: {result}")

app = tk.Tk()
app.title("My Calculator")
app.geometry("300x200")

tk.Label(app, text="First number").pack()
num1 = tk.Entry(app)
num1.pack()

tk.Label(app, text="Second number").pack()
num2 = tk.Entry(app)
num2.pack()

tk.Button(app, text="Add", command=add_numbers).pack()

answer = tk.Label(app, text="Result:")
answer.pack()

app.mainloop()