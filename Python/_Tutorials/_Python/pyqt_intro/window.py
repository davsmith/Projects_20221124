"""Example code from PyQt Course for Beginners tutorial (YouTube).

PyQt6 Course for Beginners - Parwiz Forogh (https://www.youtube.com/watch?v=ot94H3-d5d8)
Detailed notes: https://tinyurl.com/y5db3c5c

Minimal PyQt window app with no icon or title

Created November 12, 2022
"""
from  PyQt6.QtWidgets import QApplication, QWidget

import sys


app = QApplication(sys.argv)

window = QWidget()
window.show()

sys.exit(app.exec())

