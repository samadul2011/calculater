from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

class CalculatorApp(App):
    def build(self):
        # Set dark background
        Window.clearcolor = (0, 0, 0, 1)
        
        self.layout = GridLayout(cols=4, spacing=2, padding=5)
        
        # Initialize variables
        self.memory = 0
        self.last_result = 0
        self.result_displayed = False
        
        # Create display
        self.display = TextInput(
            text='0',
            font_size=32,
            multiline=False,
            readonly=True,
            background_color=(0, 0, 0, 1),
            foreground_color=(1, 1, 1, 1),
            halign='right'
        )
        self.layout.add_widget(self.display)
        self.layout.add_widget(Button())  # Empty space
        self.layout.add_widget(Button())  # Empty space
        self.layout.add_widget(Button())  # Empty space
        
        # Buttons layout
        buttons = [
            ('MC', 'MR', 'M+', 'M-'),
            ('C', 'CE', '←', '±'),
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+')
        ]
        
        # Create buttons
        for row in buttons:
            for label in row:
                button = Button(
                    text=label,
                    font_size=20,
                    background_color=(0.2, 0.2, 0.2, 1),
                    color=(1, 1, 1, 1)
                )
                button.bind(on_press=self.on_button_press)
                self.layout.add_widget(button)
        
        return self.layout

    def on_button_press(self, instance):
        current = self.display.text
        button_text = instance.text
        
        if button_text == '=':
            try:
                result = eval(current)
                self.last_result = result
                self.display.text = str(result)
                self.result_displayed = True
            except Exception:
                self.display.text = "Error"
                self.result_displayed = False
        elif button_text == 'C':
            self.display.text = '0'
            self.last_result = 0
            self.result_displayed = False
        elif button_text == 'CE':
            self.display.text = '0'
            self.result_displayed = False
        elif button_text == '←':
            if len(current) > 1:
                self.display.text = current[:-1]
            else:
                self.display.text = '0'
                self.result_displayed = False
        elif button_text == '±':
            if current != '0' and current != 'Error':
                if current.startswith('-'):
                    self.display.text = current[1:]
                else:
                    self.display.text = '-' + current
                self.result_displayed = False
        elif button_text == 'MC':
            self.memory = 0
        elif button_text == 'MR':
            self.display.text = str(self.memory)
            self.result_displayed = True
        elif button_text == 'M+':
            try:
                self.memory += float(current)
            except:
                pass
        elif button_text == 'M-':
            try:
                self.memory -= float(current)
            except:
                pass
        else:
            # For digits and operators
            if self.result_displayed and button_text not in '+-*/':
                self.display.text = button_text
                self.result_displayed = False
            else:
                if self.display.text == '0' and button_text.isdigit():
                    self.display.text = button_text
                else:
                    self.display.text += button_text
                if button_text in '+-*/':
                    self.result_displayed = False

if __name__ == '__main__':
    CalculatorApp().run()