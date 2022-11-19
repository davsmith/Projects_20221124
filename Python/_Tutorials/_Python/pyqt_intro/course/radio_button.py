"""Example code from PyQt Course for Beginners tutorial (YouTube).

PyQt6 Course for Beginners - Parwiz Forogh (https://youtu.be/ot94H3-d5d8?t=1326)
Detailed notes: https://tinyurl.com/y5db3c5c

Example implementation of a set of radio buttons using PyQt

Concepts introduced:
  - Using the QRadioButton class from the PyQt6.QtWidgets module

Created November 19, 2022
"""

' Minimal PyQt6 window with no icon or title, using classes '
from PyQt6.QtWidgets import QApplication, QWidget, QGroupBox, QLabel, QRadioButton, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QIcon, QFont
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

      # Set window attributes
      self.setWindowTitle("PyQt6 Radio Button")
      self.setWindowIcon(QIcon("app_icon.png"))
      self.setGeometry(500, 200, 500, 400)

      self.radio_btn()

      self.label = QLabel("Hello")
      self.label.setFont(QFont("Times New Roman", 14))

      vbox = QVBoxLayout()
      vbox.addWidget(self.grpbox)
      vbox.addWidget(self.label)


      self.setLayout(vbox)


    def radio_btn(self):
      self.grpbox = QGroupBox("Choose Programming Language", self)
      self.grpbox.setFont(QFont("Times New Roman", 15))

      hbox = QHBoxLayout()
      self.rad1 = QRadioButton("Python")
      self.rad1.setChecked(True)
      self.setFont(QFont("Times New Roman", 14))
      self.rad1.toggled.connect(self.on_selected)
      hbox.addWidget(self.rad1)

      self.rad2 = QRadioButton("C++")
      self.setFont(QFont("Times New Roman", 14))
      self.rad2.toggled.connect(self.on_selected)
      hbox.addWidget(self.rad2)

      self.rad3 = QRadioButton("Java")
      self.setFont(QFont("Times New Roman", 14))
      self.rad3.toggled.connect(self.on_selected)
      hbox.addWidget(self.rad3)

      self.rad4 = QRadioButton("C#")
      self.setFont(QFont("Times New Roman", 14))
      self.rad4.toggled.connect(self.on_selected)
      hbox.addWidget(self.rad4)


      self.grpbox.setLayout(hbox)

    def on_selected(self):
      radio = self.sender()

      if radio.isChecked():
        self.label.setText("You have selected: " + radio.text())


# *** Main ***
if __name__ == '__main__':
  app = QApplication([])
  window = Window()
  window.show()
  sys.exit(app.exec())