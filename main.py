# filepath: calculator-app/main.py
import math
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout

# Load the KV file (you could also embed the KV string here)
Builder.load_file('calculator.kv')


class CalcLogic(BoxLayout):
    # UI bindings
    display_text = StringProperty("")
    result_displayed = BooleanProperty(False)

    # Memory
    memory = NumericProperty(0)

    # ------------------------------------------------------ #
    # Helper methods – keep the same semantics you had in Tk #
    # ------------------------------------------------------ #
    def _clear(self):
        self.display_text = ""
        self.result_displayed = False

    def _backspace(self):
        self.display_text = self.display_text[:-1]
        if not self.display_text:
            self.result_displayed = False

    def _toggle_sign(self):
        if self.display_text.startswith('-'):
            self.display_text = self.display_text[1:]
        elif self.display_text:
            self.display_text = '-' + self.display_text
        self.result_displayed = False

    # ------------------------------------------------------ #
    # Public callbacks from the KV file (buttons, keys)     #
    # ------------------------------------------------------ #
    def on_button(self, value):
        """Callback for all calculator buttons."""
        if value == 'C':
            self._clear()
        elif value == 'CE':
            self._clear()
        elif value == '←':
            self._backspace()
        elif value == '±':
            self._toggle_sign()
        elif value == 'MC':
            self.memory = 0
        elif value == 'MR':
            self.display_text = str(self.memory)
            self.result_displayed = True
        elif value == 'M+':
            try:
                self.memory += float(self.display_text)
            except ValueError:
                pass
        elif value == 'M-':
            try:
                self.memory -= float(self.display_text)
            except ValueError:
                pass
        elif value == '=':
            self._evaluate()
        else:                                   # digits, '.' and operators
            if self.result_displayed:
                self.display_text = ""
                self.result_displayed = False
            self.display_text += value

    def _evaluate(self):
        """Evaluate the expression shown in the display."""
        try:
            # NOTE: eval is dangerous – you may want a safer parser.
            result = eval(self.display_text, {"__builtins__": {}}, {})
            self.display_text = str(result)
            self.result_displayed = True
        except Exception:
            self.display_text = "Error"
            self.result_displayed = False

    # ------------------------------------------------------ #
    # Keyboard handling (optional – works on desktop)       #
    # ------------------------------------------------------ #
    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        """Map desktop keyboard keys to button presses."""
        key = keycode[1]
        if key.isdigit() or key in '+-*/.':
            self.on_button(key)
        elif key in ('enter', 'numpadenter'):
            self.on_button('=')
        elif key == 'backspace':
            self.on_button('←')
        elif key == 'escape':
            self.on_button('C')
        return True


class CalculatorApp(App):
    def build(self):
        root = CalcLogic()
        # Bind keyboard only on desktop (not on Android)
        from kivy.core.window import Window
        Window.bind(on_key_down=root.keyboard_on_key_down)
        return root


if __name__ == '__main__':
    CalculatorApp().run()
