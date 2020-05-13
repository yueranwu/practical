"""
CP1404/CP5632 Practical
Kivy GUI program to convert miles to kilometers
Yueran Wu
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import StringProperty

CONVERSION = 1.6093


class ConvertMileKilometer(App):
    """ ConvertMileKilometer is a Kivy App for converting miles into kilometers """
    conversion = StringProperty()

    def build(self):
        Window.size = (200, 100)
        self.title = "Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            number = float(text)
        except ValueError:
            self.root.ids.output_number.text = "0.0"
            return
        result = number * CONVERSION
        self.root.ids.output_number.text = str(result)
        self.conversion = str(result)

    def handle_increment(self, text, value):
        """handle increment/decrement when button pressed"""
        try:
            number = float(text)
        except ValueError:
            number = 0

        result = number + value
        self.root.ids.input_number.text = str(result)


ConvertMileKilometer().run()
