"""Example code from PyQt Course for Beginners tutorial (YouTube).

PyQt6 Course for Beginners - Parwiz Forogh (https://youtu.be/ot94H3-d5d8?t=10388)
Detailed notes: https://tinyurl.com/y5db3c5c

Demonstrates drawing shapes using the QPainter class

Concepts introduced:
    - Drawing rectangles
    - Differences between PyQt5 and PyQt6

Module/Class/Methods:
    QApplication    See detailed notes (linked above)
    QWidget         See detailed notes (linked above)
    QLabel          See detailed notes (linked above)
    QIcon           See detailed notes (linked above)
    QFont           See detailed notes (linked above)

    QPainter        Draws shapes in a window (canvas)
        paintEvent  Callback for 
    QPainter This show the longest line allowed by Python style conventions (99 characters)


Created November 22, 2022
"""

from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon, QFont, QPainter, QPen, QBrush
from PyQt6.QtCore import Qt

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

      # Set window attributes
      self.setWindowTitle("PyQt6 Drawing Shapes QPainter()")
      self.setWindowIcon(app_icon)
      self.setGeometry(500, 300, 500, 300)

    #   self.create_widgets()

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.GlobalColor.blue, 5, Qt.PenStyle.DashDotDotLine))

        painter.drawRect(100, 15, 300, 100)


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