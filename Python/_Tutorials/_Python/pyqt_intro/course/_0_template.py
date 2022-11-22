"""Example code from PyQt Course for Beginners tutorial (YouTube).

PyQt6 Course for Beginners - Parwiz Forogh (https://youtu.be/ot94H3-d5d8?t=0)
Detailed notes: https://tinyurl.com/y5db3c5c

Concepts introduced:
    - Concept 1
    - Concept 2

Module/Class/Methods:
    QApplication    Provides interface with OS for command line args and exit codes
        __init__    Pass sys.argv or []
        exec        Runs the application and returns exit code

    QWidget         Base application form with no menus
        __init__
        show        Displays the form

    QIcon           Loads an image file and provides an instance of a PyQt icon class
        __init__    Receives an image file as an argument (e.g. .png)

    QFont           Loads a font, sets the font size and provides an instance of a PyQt font class
    CLongestClassAB This show the longest line allowed by Python style conventions (99 characters)


Created November 20, 2022
"""

from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont
from os.path import join, realpath, dirname
import sys

class Window(QWidget):
    """Single line summary of the class with a period at the end.
 
    Methods:
        __init__(self, arg1, arg2)
        method2()
    """

    def __init__(self):
      """This method multiplies the given two numbers.
  
      Input Arguments: a, b must be numbers.
      Returns: Multiplication of a and b.
      """
      super().__init__()

      script_path = realpath(dirname(__file__))
      app_icon = QIcon(join(script_path, "images/app_icon.png"))

      self.setWindowTitle("PyQt6 <template>")
      self.setWindowIcon(app_icon)
      self.setGeometry(500, 300, 400, 300)
      self.setStyleSheet("background-color:blue")

      self.create_widgets()

    def create_widgets(self):
      """This method multiplies the given two numbers.

      Input Arguments: a, b must be numbers.
      Returns: Multiplication of a and b.
      """

      # Create a widget for something, set some attributes
      widget1 = QWidget("Click Me", self)

      # widget1.move(100,100)
      widget1.setGeometry(100, 100, 100, 100)
      widget1.setStyleSheet('background-color:red')
      widget1.setIcon(QIcon('button_icon.png'))

      # Create a widget for something, set some attributes
      label = QLabel("My Label", self)
      label.move(100,200)
      label.setStyleSheet('color:green')
      label.setFont(QFont("Times New Roman", 15))

# *** Main ***
if __name__ == '__main__':
  app = QApplication([])
  window = Window()
  window.show()
  sys.exit(app.exec())