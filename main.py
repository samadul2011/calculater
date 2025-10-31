from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

class CalculatorApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 1)
        self.layout = GridLayout(cols=4, spacing=2, padding=5)
        
        self.memory = 0
        self.last_result = 0
        self.result_displayed = False
        
        self.display = TextInput(
            text='0',
            font_size=32,
            multiline=False,
            readonly=True,
            background_color=(0, 0, 0, 1),
            foreground_color=(1, 1, 1, 1),
            halign='right',
            size_hint=(1, 0.2)
        )
        self.layout.add_widget(self.display)
        
        buttons = [
            ('MC', 'MR', 'M+', 'M-'),
            ('C', 'CE', '←', '±'),
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+')
        ]
        
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
                self.display.text = str(result)
                self.result_displayed = True
            except:
                self.display.text = 'Error'
        elif button_text == 'C':
            self.display.text = '0'
            self.result_displayed = False
        elif button_text == 'CE':
            self.display.text = '0'
            self.result_displayed = False
        elif button_text == '←':
            self.display.text = current[:-1] or '0'
        elif button_text == '±':
            self.display.text = str(-float(current))
        elif button_text in ['MC', 'MR', 'M+', 'M-']:
            self.handle_memory(button_text, current)
        else:
            if self.result_displayed:
                self.display.text = button_text
                self.result_displayed = False
            else:
                if self.display.text == '0':
                    self.display.text = button_text
                else:
                    self.display.text += button_text

    def handle_memory(self, operation, current):
        if operation == 'MC':
            self.memory = 0
        elif operation == 'MR':
            self.display.text = str(self.memory)
            self.result_displayed = True
        elif operation == 'M+':
            self.memory += float(current)
        elif operation == 'M-':
            self.memory -= float(current)

if __name__ == '__main__':
    CalculatorApp().run()
