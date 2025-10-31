import tkinter as tk
import math

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.configure(bg='black')
        self.root.geometry("300x400")
        self.memory = 0
        self.last_result = 0
        self.result_displayed = False  # Flag to track if result is currently displayed
        
        # Create display with dark theme
        self.display = tk.Entry(root, width=20, justify="right", font=('Arial', 18, 'bold'), 
                               bg='black', fg='white', insertbackground='white', 
                               relief=tk.FLAT, bd=10)
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=10, sticky="nsew")
        
        # Bind keyboard events
        self.root.bind('<Key>', self.key_press)
        self.root.focus_set()  # Set focus to root window to capture key events
        
        # Configure grid weights for responsive design
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
        for i in range(7):
            root.grid_rowconfigure(i, weight=1)
        
        # Buttons layout with dark theme (simplified)
        buttons = [
            ('MC', 'MR', 'M+', 'M-'),
            ('C', 'CE', '←', '±'),
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+')
        ]
        
        # Create buttons with dark theme
        for i, row in enumerate(buttons):
            for j, button in enumerate(row):
                cmd = lambda x=button: self.click_button(x)
                btn = tk.Button(root, text=button, command=cmd, 
                               width=5, height=2, font=('Arial', 12, 'bold'),
                               bg='#333333', fg='white', activebackground='#666666',
                               activeforeground='white', relief=tk.RAISED, bd=2)
                btn.grid(row=i+1, column=j, padx=2, pady=2, sticky="nsew")

    def key_press(self, event):
        key = event.char
        keysym = event.keysym
        
        # Handle number keys
        if key.isdigit():
            # If result is displayed, clear it before entering new number
            if self.result_displayed:
                self.display.delete(0, tk.END)
                self.result_displayed = False
            self.display.insert(tk.END, key)
        
        # Handle operator keys
        elif key in '+-*/.=':
            if key == '.':
                # If result is displayed, start new number with decimal
                if self.result_displayed:
                    self.display.delete(0, tk.END)
                    self.result_displayed = False
                self.display.insert(tk.END, '.')
            elif key == '=':
                self.click_button('=')
            else:
                # Operators should clear result flag
                self.result_displayed = False
                self.display.insert(tk.END, key)
        
        # Handle special keys
        elif keysym == 'Return' or key == '=':
            self.click_button('=')
        elif keysym == 'BackSpace':
            current = self.display.get()
            self.display.delete(len(current)-1, tk.END)
            # If display becomes empty, reset result flag
            if not self.display.get():
                self.result_displayed = False
        elif keysym == 'Escape':
            self.clear()
        
        # Prevent default behavior for handled keys
        return "break"

    def click_button(self, value):
        current = self.display.get()
        
        if value == '=':
            try:
                result = eval(current)
                self.last_result = result
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
                self.result_displayed = True  # Set flag when result is displayed
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
                self.result_displayed = False  # Reset flag on error
        elif value == 'C':
            self.clear()
        elif value == 'CE':
            self.display.delete(0, tk.END)
            self.result_displayed = False  # Reset flag when display is cleared
        elif value == '←':
            self.display.delete(len(current)-1, tk.END)
            # If display becomes empty, reset result flag
            if not self.display.get():
                self.result_displayed = False
        elif value == '±':
            try:
                if current.startswith('-'):
                    self.display.delete(0, tk.END)
                    self.display.insert(0, current[1:])
                else:
                    self.display.delete(0, tk.END)
                    self.display.insert(0, '-' + current)
                # Reset result flag when value is modified
                self.result_displayed = False
            except:
                pass
        
        # Memory functions
        elif value == 'MC':
            self.memory = 0
        elif value == 'MR':
            self.display.delete(0, tk.END)
            self.display.insert(0, str(self.memory))
            self.result_displayed = True  # Set flag when memory is recalled
        elif value == 'M+':
            try:
                self.memory += float(current)
            except:
                pass
        elif value == 'M-':
            try:
                self.memory -= float(current)
            except:
                pass
        
        else:
            # For regular digits and operators
            # If result is displayed, clear it before entering new value
            if self.result_displayed:
                self.display.delete(0, tk.END)
                self.result_displayed = False
            self.display.insert(tk.END, value)

    def clear(self):
        self.display.delete(0, tk.END)
        self.last_result = 0
        self.result_displayed = False  # Reset flag when cleared

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()