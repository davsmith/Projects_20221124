import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QTableWidget,QTableWidgetItem
from PyQt6.QtGui import QIcon

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt6 TableWidget')
        self.setWindowIcon(QIcon("app_icon.png"))
        self.setGeometry(500, 200, 500, 400)

        self.vbox = QVBoxLayout()

        # add table 
        self.table = QTableWidget(self)
        self.table.setColumnCount(3)
        self.table.setRowCount(3)

        self.table.setItem(0, 0, QTableWidgetItem("FName"))
        self.table.setItem(0, 1, QTableWidgetItem("LName"))
        self.table.setItem(0, 2, QTableWidgetItem("Email"))

        self.table.setItem(1, 0, QTableWidgetItem("Parwiz"))
        self.table.setItem(1, 1, QTableWidgetItem("Forogh"))
        self.table.setItem(1, 2, QTableWidgetItem("parwiz@gmail.com"))

        self.table.setItem(2, 0, QTableWidgetItem("John"))
        self.table.setItem(2, 1, QTableWidgetItem("Doe"))
        self.table.setItem(2, 2, QTableWidgetItem("john_doe@gmail.com"))

        self.vbox.addWidget(self.table)
        self.setLayout(self.vbox)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = Window()
    sys.exit(app.exec())