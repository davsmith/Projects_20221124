"""Example code from PyQt Course for Beginners tutorial (YouTube).

PyQt6 Course for Beginners - Parwiz Forogh (https://youtu.be/ot94H3-d5d8?t=410)
Detailed notes: https://tinyurl.com/y5db3c5c

Minimal PyQt app to demonstrate use of the SpinBox control

Concepts introduced:

Created November 19, 2022
"""

' Minimal PyQt6 window with no icon or title, using classes '
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QHBoxLayout, QTableWidgetItem, QVBoxLayout
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

      # Set title and appearance of the app
      self.setWindowTitle("PyQt6 TableWidget")
      self.setWindowIcon(QIcon("app_icon.png"))
      self.setGeometry(500, 200, 500, 400)
      
      vbox = QVBoxLayout()

      tableWidget = QTableWidget()
      tableWidget.setRowCount = 3
      tableWidget.setColumnCount = 3

      tableWidget.setItem(0, 0, QTableWidgetItem("FName"))
      tableWidget.setItem(0, 1, QTableWidgetItem("LName"))
      tableWidget.setItem(0, 2, QTableWidgetItem("Email"))

      tableWidget.setItem(1, 0, QTableWidgetItem("Parwiz"))
      tableWidget.setItem(1, 1, QTableWidgetItem("Forogh"))
      tableWidget.setItem(1, 2, QTableWidgetItem("parwiz@gmail.com"))

      vbox.addWidget(tableWidget)
      self.setLayout(vbox)
      self.setGeometry(20,20,200,200)
      # self.setStyleSheet("background-color:blue")


# *** Main ***
if __name__ == '__main__':
  app = QApplication([])
  window = Window()
  window.show()
  sys.exit(app.exec())