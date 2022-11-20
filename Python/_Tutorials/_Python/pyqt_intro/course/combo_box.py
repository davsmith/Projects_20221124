import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QComboBox, QLabel
from PyQt6.QtGui import QIcon, QFont

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt6 QComboBox')
        self.setWindowIcon(QIcon("app_icon.png"))
        self.setGeometry(500, 200, 500, 400)

        vbox = QVBoxLayout()

        self.comboBox = QComboBox()
        self.comboBox.addItem("PyQt6")
        self.comboBox.addItem("wxPython")
        self.comboBox.addItem("Kivy")
        self.comboBox.addItem("TKinter")
        self.comboBox.addItem("PySide2")
        # self.comboBox.setStyleSheet('background-color:yellow')
        self.comboBox.currentTextChanged.connect(self.item_selected)

        self.label = QLabel("Hello")
        self.label.setFont(QFont("Sanserif", 14))

        vbox.addWidget(self.comboBox)
        vbox.addWidget(self.label)
        self.setLayout(vbox)

        self.show()

    def item_selected(self):
        value = self.comboBox.currentText()
        self.label.setText(f"You have selected {value}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = Window()
    sys.exit(app.exec())