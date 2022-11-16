"""Example code from PyQt Course for Beginners tutorial (YouTube).

PyQt6 Course for Beginners - Parwiz Forogh (https://www.youtube.com/watch?v=ot94H3-d5d8)
Detailed notes: https://tinyurl.com/y5db3c5c

Minimal PyQt window app with no icon or title

Concepts introduced:
    - Importing QApplication and QWidget classes
    - Using QWidget (active)
    - Introduce QDialog and QMainWindow classes (passive)
    - Displaying a window with the .show method
    - Passing arguments using sys.argv

Created November 12, 2022
"""
from  PyQt6.QtWidgets import QApplication, QWidget

import sys


app = QApplication(sys.argv)

# Can be QWidget, QDialog, or QMainWindow
window = QWidget()
window.show()

sys.exit(app.exec())

