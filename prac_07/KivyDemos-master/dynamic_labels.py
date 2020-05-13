"""
Kivy practical for CP1404, IT@JCU
Dynamically create labels based on content of list
Yueran Wu
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic label creation."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create widgets from list and add them to the GUI"""
        for name in self.names:
            label = Label(text=name, id=name)
            self.root.ids.labels_box.add_widget(label)


DynamicLabelsApp().run()
