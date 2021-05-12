from matplotlib import pyplot as plt
from PyQt5.QtWidgets import QApplication, QLabel,QLineEdit, QDialog,QWidget,QPushButton, QVBoxLayout, QMainWindow, QGroupBox, QCheckBox, QHBoxLayout, QButtonGroup, QRadioButton, QSizeGrip, QFrame
import sys
from PyQt5 import QtGui
from PyQt5 import QtCore
import data_mhs as dm
data = dm.data()
operator = dm.operator_func()

class screen(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Program CRUD dan statistik data mahasiswa Teknik Informatika angkatan 2020')
        self.setGeometry(100,100,800,600)
        self.setWindowIcon(QtGui.QIcon('D:\\document\\IT\\python programming\\project\\project akhir\\inpostor.png'))

        vbox = QVBoxLayout()
        
        li = QLineEdit(self)
        vbox.addWidget(li)
        self.b = li.text()
        
        label = QLabel('hello',self)
        vbox.addWidget(label)

        label2 = QLabel(self.b,self)
        vbox.addWidget(label2)
        print (self.b)

        self.setLayout(vbox)

        self.show()




        

        

        




if __name__ == "__main__":
    App = QApplication(sys.argv)
    layar = screen()
    sys.exit(App.exec_())