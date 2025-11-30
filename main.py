import sys
import sqlite3
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QTableWidgetItem


class CoffeeApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(CoffeeApp, self).__init__()
        uic.loadUi('main.ui', self)
        self.load_data()

    def load_data(self):
        connection = sqlite3.connect('coffee.sqlite')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM coffee")
        records = cursor.fetchall()
        self.tableWidget.setRowCount(len(records))
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels([
            "ID", "Название сорта", "Степень обжарки",
            "Молотый/в зернах", "Описание вкуса", "Цена", "Объем упаковки"
        ])
        for i, row in enumerate(records):
            for j, value in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(value)))
        connection.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec())
