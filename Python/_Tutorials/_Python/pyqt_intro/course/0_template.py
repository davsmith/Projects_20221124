"""Example code from PyQt Course for Beginners tutorial (YouTube).

PyQt6 Course for Beginners - Parwiz Forogh (https://youtu.be/ot94H3-d5d8)
Detailed notes: https://tinyurl.com/y5db3c5c
Relative link: <You Tube link relative to topic>

Minimal PyQt window app with no icon or title

Concepts introduced:
    - <Concept 1>



Created November 12, 2022
"""
from  PyQt6.QtWidgets import QApplication, QWidget

import sys


app = QApplication(sys.argv)

# Can be QWidget, QDialog, or QMainWindow
window = QWidget()
window.show()

sys.exit(app.exec())

