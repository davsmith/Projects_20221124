"""Example code from PyQt Course for Beginners tutorial (YouTube).

PyQt6 Course for Beginners - Parwiz Forogh (https://youtu.be/ot94H3-d5d8?t=2410)
Detailed notes: https://tinyurl.com/y5db3c5c

PyQt app for use with layout management example

Concepts introduced:
  - Layout classes (QHBoxLayout)

Created November 13, 2022
"""

' Minimal PyQt6 window with no icon or title, using classes '
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    """Basic app window class extending the QWidget base class from PyQT.

    Longer class information...
    Longer class information...

    Attributes:
      none
    """
    def __init__(self):
      """Extends the init function on the QWidget class.

      Sets up the application window, setting up icons, dimensions, etc.

      Args:
        none

      Returns:
        none

      Raises:
        none
    """
      super().__init__()

      self.setWindowTitle("PyQt6 HBox Layout")
      self.setWindowIcon(QIcon("app_icon.png"))
      self.setGeometry(500, 300, 400, 300)

      hbox = QHBoxLayout()

      btn1 = QPushButton("Button One")
      btn2 = QPushButton("Button Two")
      btn3 = QPushButton("Button Three")
      btn4 = QPushButton("Button Four")

      hbox.addWidget(btn1)
      hbox.addWidget(btn2)
      hbox.addWidget(btn3)
      hbox.addWidget(btn4)

      self.setLayout(hbox)

# *** Main ***
if __name__ == '__main__':
  app = QApplication([])
  window = Window()
  window.show()
  sys.exit(app.exec())