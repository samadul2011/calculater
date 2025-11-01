from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

# Set window size (optional, useful for desktop testing)
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '400')

class CalculatorLayout(BoxLayout):
    memory = 0
    last_result = 0
    result_displayed = False

    def click_button(self, value):
        display = self.ids.display
        current = display.text

        if value == '=':
            try:
                result = str(eval(current))
                display.text = result
                self.last_result = result
                self.result_displayed = True
            except Exception:
                display.text = "Error"
                self.result_displayed = False
        elif value == 'C':
            self.clear()
        elif value == 'CE':
            display.text = ''
            self.result_displayed = False
        elif value == '←':
            display.text = current[:-1]
            if not display.text:
                self.result_displayed = False
        elif value == '±':
            if current and current != "Error":
                if current.startswith('-'):
                    display.text = current[1:]
                else:
                    display.text = '-' + current
                self.result_displayed = False
        elif value == 'MC':
            self.memory = 0
        elif value == 'MR':
            display.text = str(self.memory)
            self.result_displayed = True
        elif value == 'M+':
            try:
                self.memory += float(current)
            except ValueError:
                pass
        elif value == 'M-':
            try:
                self.memory -= float(current)
            except ValueError:
                pass
        else:
            if self.result_displayed:
                display.text = ''
                self.result_displayed = False
            display.text += value

    def clear(self):
        self.ids.display.text = ''
        self.last_result = 0
        self.result_displayed = False

    def on_key_down(self, window, key, scancode, codepoint, modifiers):
        key_mapping = {
            'escape': 'C',
            'backspace': '←',
            'enter': '=',
            'return': '='
        }

        key_name = key_mapping.get(codepoint.lower(), codepoint)

        if codepoint.isdigit() or codepoint in '+-*/.=':
            self.click_button(codepoint)
        elif key_name in ['C', '←', '=']:
            self.click_button(key_name)

class CalculatorApp(App):
    def build(self):
        self.title = "Simple Calculator"
        layout = CalculatorLayout()
        # Listen for keyboard events
        from kivy.core.window import Window
        Window.bind(on_keyboard=layout.on_key_down)
        return layout

if __name__ == "__main__":
    CalculatorApp().run()
