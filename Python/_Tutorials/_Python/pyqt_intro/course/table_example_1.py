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

        vbox = QVBoxLayout()

        # add table 
        tableWidget = QTableWidget(self)
        tableWidget.setColumnCount(3)
        tableWidget.setRowCount(3)

        tableWidget.setItem(0, 0, QTableWidgetItem("FName"))
        tableWidget.setItem(0, 1, QTableWidgetItem("LName"))
        tableWidget.setItem(0, 2, QTableWidgetItem("Email"))

        tableWidget.setItem(1, 0, QTableWidgetItem("Parwiz"))
        tableWidget.setItem(1, 1, QTableWidgetItem("Forogh"))
        tableWidget.setItem(1, 2, QTableWidgetItem("parwiz@gmail.com"))

        tableWidget.setItem(2, 0, QTableWidgetItem("John"))
        tableWidget.setItem(2, 1, QTableWidgetItem("Doe"))
        tableWidget.setItem(2, 2, QTableWidgetItem("john_doe@gmail.com"))

        vbox.addWidget(tableWidget)
        self.setLayout(vbox)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = Window()
    sys.exit(app.exec())