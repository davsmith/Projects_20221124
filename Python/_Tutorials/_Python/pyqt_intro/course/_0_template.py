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

Created November 20, 2022
"""

from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
from os.path import join, realpath, dirname
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

      script_path = realpath(dirname(__file__))
      app_icon = QIcon(join(script_path, "images/app_icon.png"))

      self.setWindowTitle("PyQt6 <template>")
      self.setWindowIcon(app_icon)
      self.setGeometry(500, 300, 400, 300)
      self.setStyleSheet("background-color:blue")

# *** Main ***
if __name__ == '__main__':
  app = QApplication([])
  window = Window()
  window.show()
  sys.exit(app.exec())