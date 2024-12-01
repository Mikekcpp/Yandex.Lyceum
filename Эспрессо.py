from PyQt6.QtWidgets import QApplication, QMainWindow, QTableView
from PyQt6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt6 import QtWidgets, QtGui, QtCore
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connectToDatabase()
        self.displayData()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Coffee Database')
        self.table_view = QTableView(self)
        self.table_view.setGeometry(10, 10, 780, 580)
        self.setCentralWidget(self.table_view)

    def connectToDatabase(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("coffee.sqlite")
        if not self.db.open():
            print("Error: Unable to connect to database")
            return False
        return True

    def displayData(self):
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable("coffee")
        self.model.select()
        self.table_view.setModel(self.model)
        self.table_view.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
