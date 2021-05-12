from matplotlib import pyplot as plt
from PyQt5.QtWidgets import QApplication, QLabel,QLineEdit, QDialog,QWidget,QPushButton, QVBoxLayout, QComboBox,QMainWindow, QGroupBox, QCheckBox, QHBoxLayout, QButtonGroup, QRadioButton, QSizeGrip, QFrame, QTableWidget, QTableWidgetItem
import sys
from PyQt5 import QtGui
from PyQt5 import QtCore
import data_mhs as dm
data = dm.data()
operator = dm.operator_func()

class window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = 'PyQt5 QTable Widget'
        self.left = 200
        self.top = 200
        self.width = 400
        self.height = 250
        self.iconname = "D://document//IT//python programming//pyqt5//Parwiz forogh//image.jpg"

        self.InitUi()
        self.creatingTables()

        self.show()
    def InitUi(self):
        self.setWindowIcon(QtGui.QIcon(self.iconname))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)

        vbox = QVBoxLayout()


        show = QPushButton('show',self)
        show.setGeometry(20,20,100,30)
        show.clicked.connect(self.button_click)
        vbox.addWidget(show)

        Add = QPushButton('Add',self)
        Add.setGeometry(130,20,100,30)
        # Add.clicked.connect(self.button_click)
        vbox.addWidget(Add)

        update = QPushButton('update',self)
        update.setGeometry(240,20,100,30)
        # update.clicked.connect(self.button_click)
        vbox.addWidget(update)

        delete = QPushButton('delete',self)
        delete.setGeometry(350,20,100,30)
        # delete.clicked.connect(self.button_click)
        vbox.addWidget(delete)


        combo = QComboBox(self)
        for item in data[0]:
            if item != 'nama':
                combo.addItem(item)
        combo.setGeometry(463,20,120,30)
        vbox.addWidget(combo)

    def button_click(self):
        self.creatingTables()
        


    def creatingTables(self):
        vbox = QVBoxLayout()
        wid = QWidget(self)
        wid.setGeometry(20,70,668,650)
        table = QTableWidget()
        table.setRowCount(len(data))
        table.setColumnCount(len(data[0]))
        headers = []
        for header in data[0]:
            if header != 'nomor handphone':
                headers.append(header)
            elif header == 'nomor handphone':
                headers.append('operator')



        table.setHorizontalHeaderLabels(headers)
        table.move(40,40)

        for baris in range(len(data)):
            for kolom in range(len(headers)):
                if headers[kolom] != 'operator' and headers[kolom] == 'nama':
                    table.setItem(baris,kolom,QTableWidgetItem(data[baris][headers[kolom]]))
                    table.setColumnWidth(kolom,200)
                elif headers[kolom] != 'operator' and headers[kolom] != 'nama':
                    table.setItem(baris,kolom,QTableWidgetItem(data[baris][headers[kolom]]))
                elif headers[kolom] == 'operator':
                    for jenis in operator:
                        for rentang in range(len(operator[jenis])):
                            if data[baris]['nomor handphone'][0:4] == operator[jenis][rentang]:
                    
                                table.setItem(baris,kolom,QTableWidgetItem(jenis))

        vbox.addWidget(table)

        wid.setLayout(vbox)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = window()
    sys.exit(App.exec_())
