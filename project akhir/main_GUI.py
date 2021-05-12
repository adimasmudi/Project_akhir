"""
Ini adalah source code dari program untuk menampilkan table daftar mahasiswa teknik informatika beserta dengan
statistik dari kota asal, provinsi, jenis kelamin, operator seluler yang digunakan
"""
# import modul matplotlib 
from matplotlib import pyplot as plt

# import beberapa komponen data QtWidgets di PyQt5
from PyQt5.QtWidgets import QApplication,QLineEdit, QDialog,QWidget,QPushButton,QDialogButtonBox,QLabel, QGroupBox,QFormLayout,QVBoxLayout, QMainWindow, QHBoxLayout, QButtonGroup, QRadioButton, QComboBox, QTableWidget, QTableWidgetItem, QMessageBox

# import system
import sys

# import tambahan dari komponen PyQt5
from PyQt5 import QtGui
from PyQt5 import QtCore

# import data deklarasikan variabel untuk menyimpan data dari file data_mhs.py
import data_mhs as dm
data = dm.data()
operator = dm.operator_func()

# class untuk layar utama
class screen(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Program CRUD dan statistik data mahasiswa Teknik Informatika angkatan 2020')
        self.setGeometry(100,100,800,600)
        self.setWindowIcon(QtGui.QIcon('D:\\document\\IT\\python programming\\project\\project akhir\\inpostor.png'))
        self.setFont(QtGui.QFont('helvetica',10))
        self.setStyleSheet('screen{background-color : rgb(31, 31, 31)}')

        vbox = QVBoxLayout()


        Add = QPushButton('Add',self)
        Add.setGeometry(20,20,100,30)
        Add.setStyleSheet('background-color:rgb(0, 79, 170);color:white')
        Add.clicked.connect(self.new_window)
        vbox.addWidget(Add)

        update = QPushButton('update',self)
        update.setGeometry(130,20,100,30)
        update.setStyleSheet('background-color:rgb(0, 79, 170);color:white')
        update.clicked.connect(self.update_window)
        vbox.addWidget(update)

        delete = QPushButton('delete',self)
        delete.setGeometry(240,20,100,30)
        delete.setStyleSheet('background-color:rgb(0, 79, 170);color:white')
        delete.clicked.connect(self.delete_window)
        vbox.addWidget(delete)


        self.combo = QComboBox(self)
        for item in data[0]:
            if item != 'nama':
                if item != 'nomor handphone':
                    self.combo.addItem(item)
                elif item == 'nomor handphone':
                    self.combo.addItem('operator')
            
        self.combo.setGeometry(350,20,120,30)
        self.combo.setStyleSheet('background-color:rgb(0, 79, 170);color:white')
        self.combo.currentTextChanged.connect(self.choice)
        vbox.addWidget(self.combo)

        self.creatingTables()
        
        self.setLayout(vbox)

        self.show()

    # fungsi untuk membuat tabel
    def creatingTables(self):
        vbox = QVBoxLayout()
        wid = QWidget(self)
        wid.setGeometry(20,70,820,650)
        global table
        table = QTableWidget()
        table.setRowCount(len(data))
        table.setColumnCount(len(data[0]))
        global headers
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
                    table.setColumnWidth(kolom,150)
                elif headers[kolom] == 'operator':
                    for jenis in operator:
                        for rentang in range(len(operator[jenis])):
                            if data[baris]['nomor handphone'][0:4] == operator[jenis][rentang]:                   
                                table.setItem(baris,kolom,QTableWidgetItem(jenis))

        vbox.addWidget(table)

        wid.setLayout(vbox)

    def new_window(self,checked):
        self.new = Another_window()
        self.new.show()

    def update_window(self,checked):
        self.updt = update_data()

    def delete_window(self,checked):
        self.delete = delete_data()

    def choice(self):
        def analisis():
            global hasil_akhir
            global hasil
            global pembanding
            hasil_akhir = {
                'jenis kelamin':{},'provinsi':{},'nomor handphone':{},'kota':{}
                }
            key_list = []
            hasil = []
            for key in data[0]:
                if key != 'nama':
                    for baris in range(len(data)):
                        key_list.append(key)
            hasil.append(list(set(key_list)))
            for dat in hasil[0]:
                temp = []
                for row in range(len(data)):
                    temp.append(data[row][dat])
                hasil.append(temp)
            pembanding = []
            for banding in hasil:
                temp = []
                p = list(set(banding))
                temp = p
                pembanding.append(temp)
            return hasil
            return pembanding
            return hasil_akhir

        text = self.combo.currentText()
        if text == 'jenis kelamin':
            analisis()
            jk = {}
            for a in pembanding:
                if 'laki-laki' in a:
                    b = list(set(a))
            for c in b:
                jk[c] = 0
            for d in jk:
                for e in hasil:
                    if 'laki-laki' in e:
                        temp = e.count(d)
                        jk[d] = temp
            plt.style.use('fivethirtyeight')
            jk_list = []
            jk_jum = []
            jk_gab = []
            explode = [0.01,0.01]
            for i in jk:
                jk_list.append(i+'('+str(jk[i])+')')
                jk_jum.append(jk[i])
            plt.pie(jk_jum,explode = explode,labels = jk_list,autopct='%1.1f%%')
                
            plt.title('Statistik Mahasiswa Teknik Informatika Angkatan 2020\n Berdasarkan Jenis kelamin')
            plt.tight_layout()
            plt.show()
        
        elif text == 'kota':
            analisis()
            for i in range(len(pembanding)):
                if 'Bangkalan' in pembanding[i]:
                    hasil_akhir['kota'] = pembanding[i]
            hit_list = []
            for cari in range(len(hasil)):
                for ini in range(len(hasil_akhir['kota'])):
                    hitung = hasil[cari].count(hasil_akhir['kota'][ini])
                    if hitung != 0:
                        hitungan = (hasil_akhir['kota'][ini],hitung)
                        if hasil_akhir['kota'][ini] not in hit_list:
                            hit_list.append(hitungan)
            hasil_akhir['kota'] = hit_list
            kota_x = []
            kota_y = []
            for j in range(len(hasil_akhir['kota'])):
                kota_x.append(str(hasil_akhir['kota'][j][0]))
                kota_y.append(str(hasil_akhir['kota'][j][1]))
            copyan = []
            for k in kota_y:
                temp = int(k)
                copyan.append(temp)
            kota_y = copyan.copy()
            for l in range(len(kota_y)):
                for m in range(l+1,len(kota_y)):
                    if l < m :
                        if kota_y[l] > kota_y[m]:
                            temp = kota_y[l]
                            temp2 = kota_x[l]
                            kota_y[l] = kota_y[m]
                            kota_x[l] = kota_x[m]
                            kota_y[m] = temp
                            kota_x[m] = temp2
            for x in range(len(kota_y)):
                plt.barh(kota_x,kota_y,color = 'blue')
                plt.text(kota_y[x],x,str(kota_y[x]))
            plt.style.use('classic')
            plt.title('Data kota asal Mahasiswa Teknik Informatika 2020')
            plt.xlabel('jumlah')
            plt.ylabel('kota asal')
            plt.tight_layout()
            plt.show()
        elif text == 'provinsi':
            analisis()
            key_prov = []
            hasil_akhir2 = {}
            for a in range(len(pembanding)):
                if 'Jawa Timur' in pembanding[a]:
                    for b in range(len(pembanding[a])):
                        key_prov.append(pembanding[a][b])
            for b in key_prov:
                hasil_akhir2[b] = 0
            prov_x = []
            prov_y = []
            for c in hasil_akhir2:
                for d in range(len(hasil)):
                    if 'Jawa Timur' in hasil[d]:
                        temp = hasil[d].count(c)
                        prov_x.append(c)
                        prov_y.append(temp)
            for f in range(len(prov_x)):
                prov_x[f] = prov_x[f]+'('+str(prov_y[f])+')'
            plt.style.use('seaborn')
            for d in range(len(prov_y)):
                plt.bar(prov_x,prov_y,color = 'green')
            plt.style.use('seaborn')
            plt.title('Data Provinsi Asal Mahasiswa Teknik Informatika Angkatan 2020')
            plt.tight_layout()
            plt.show()

        elif text == 'operator':
            analisis()
            operator_list = []
            operator_dict = {}
            for h in range(len(pembanding)):
                if '0878' in pembanding[h]:
                    for i in pembanding[h]:
                        for j in operator:
                            for k in range(len(operator[j])):
                                if i == operator[j][k]:
                                    operator_list.append(j)
            op_set = set(operator_list)
            operator_list2 = list(op_set)
            for c in range(len(operator_list2)):
                operator_dict[operator_list2[c]] = 0
            dict_op = []
            for h in range(len(hasil)):
                if '0878' in hasil[h]:
                    for i in hasil[h]:
                        for j in operator:
                            for k in range(len(operator[j])):
                                if i[0:4] == operator[j][k]:
                                    dict_op.append(j)
            nama_operator = []
            jumlah = []
            for m in operator_dict:
                tempx = dict_op.count(m)
                nama_operator.append(m)
                jumlah.append(tempx)
            for g in range(len(nama_operator)):
                nama_operator[g] = nama_operator[g]+'('+str(jumlah[g])+')'
            colors = ['yellow','blue','purple','red','green','cyan']
            plt.style.use('fivethirtyeight')
            plt.pie(jumlah,labels = nama_operator,colors = colors,autopct='%1.1f%%')
            plt.title('Statistik Operator nomor telepon yang digunakan\nMahasasiswa Teknik Informatika Angkatan 2020')
            plt.tight_layout()
            plt.show()

# class untuk menambahkan data
class Another_window(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Tambahkan data')
        self.setGeometry(800,130,300,300)
        self.setWindowIcon(QtGui.QIcon('D:\\document\\IT\\python programming\\project\\project akhir\\inpostor.png'))
        self.setFont(QtGui.QFont('helvetica',10))

        self.input_Add()

    def input_Add(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        wid = QWidget()

        form = QFormLayout()

        self.groupbox = QGroupBox('TAMBAHKAN DATA')

        
        self.nama = QLineEdit(self)


        self.laki = QRadioButton('laki-laki')
        self.laki.setChecked(True)
        self.perempuan = QRadioButton('perempuan')
        hbox.addWidget(self.laki)
        hbox.addWidget(self.perempuan)

        self.kota = QLineEdit(self)

        self.provinsi = QLineEdit(self)

        self.nomor_handphone = QLineEdit(self)

        form.addRow(QLabel('Nama'),self.nama)
        form.addRow(QLabel('Jenis kelamin'),hbox)
        form.addRow(QLabel('Kota Asal'),self.kota)
        form.addRow(QLabel('Provinsi'),self.provinsi)
        form.addRow(QLabel('Nomor handphone'),self.nomor_handphone)

        self.groupbox.setLayout(form)

        self.buttonbox = QDialogButtonBox(QDialogButtonBox.Save|QDialogButtonBox.Cancel)
        self.buttonbox.accepted.connect(self.Action)
        self.buttonbox.rejected.connect(self.close)
        
        vbox.addWidget(self.groupbox)
        vbox.addWidget(self.buttonbox)

        self.setLayout(vbox)

    def Action(self):
        def toCapital(value):
            if len(value) <= 3:
                value = value.upper()
            elif len(value) > 3:
                value = value.lower()
                value_list = value.split(' ')
                value_2 = []
                for kata in value_list:
                    if len(kata) <= 3:
                        kata = kata.upper()
                    elif len(kata) > 3:
                        kata = kata.capitalize()
                    value_2.append(kata)
                value = ' '.join(value_2)

            return value

        nama = self.nama.text()
        nama = toCapital(nama)
        if self.laki.isChecked():
            jk = self.laki.text()
        elif self.perempuan.isChecked():
            jk = self.perempuan.text()
        kota = self.kota.text()
        kota = toCapital(kota)
        provinsi = self.provinsi.text()
        provinsi = toCapital(provinsi)
        no_hp = self.nomor_handphone.text()
        operator_name = ''
        for jenis in operator:
            for rentang in range(len(operator[jenis])):
                if no_hp[0:4] == operator[jenis][rentang]:
                    operator_name = jenis
                
        temp = {}
        row = len(data)
        table.setRowCount(row)
        
        table.insertRow(row)
        
        for kolom in range(len(headers)):
            if headers[kolom] == 'nama':
                table.setItem(row,kolom,QTableWidgetItem(nama))
                table.setColumnWidth(kolom,200)
                temp['nama'] = nama
            elif headers[kolom] == 'jenis kelamin':
                table.setItem(row,kolom,QTableWidgetItem(jk))
                table.setColumnWidth(kolom,150)
                temp['jenis kelamin'] = jk
            elif headers[kolom] == 'kota':
                table.setItem(row,kolom,QTableWidgetItem(kota))
                table.setColumnWidth(kolom,150)
                temp['kota'] = kota
            elif headers[kolom] == 'provinsi':
                table.setItem(row,kolom,QTableWidgetItem(provinsi))
                table.setColumnWidth(kolom,150)
                temp['provinsi'] = provinsi
            elif headers[kolom] == 'operator':
                table.setItem(row,kolom,QTableWidgetItem(operator_name))
                temp['nomor handphone'] = no_hp

        data.append(temp)
        QMessageBox.about(self,'info','Data berhasil ditambahkan')
        self.close()

# class untuk update data     
class update_data(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Masukkan nomer')
        self.setGeometry(600,130,300,300)
        self.setWindowIcon(QtGui.QIcon('D:\\document\\IT\\python programming\\project\\project akhir\\inpostor.png'))
        self.setFont(QtGui.QFont('helvetica',10))

        self.nomer_update()

        self.show()

    def nomer_update(self):
        vbox = QVBoxLayout()
        self.judul = QLabel('Masukkan nomor yang ingin diupdate!')
        vbox.addWidget(self.judul)

        global inp_no
        inp_no = QLineEdit(self)
        
        vbox.addWidget(inp_no)

        tombol = QPushButton('update')
        tombol.clicked.connect(self.update)
        vbox.addWidget(tombol)

        self.setLayout(vbox)

    def update(self):
        self.upd = update_the_data()
        self.close()
        
# class untuk window baru pada update data
class update_the_data(QDialog):
    def __init__(self):
        super().__init__()
        # self.setModal(True)
        # self.exec()

        self.setWindowTitle('Update data')
        self.setGeometry(950,130,300,300)
        self.setWindowIcon(QtGui.QIcon('D:\\document\\IT\\python programming\\project\\project akhir\\inpostor.png'))
        self.setFont(QtGui.QFont('helvetica',10))

        self.update()


    def update(self):
        daftar_nomer = []
        for nomer in range(1,len(data)+1,1):
            daftar_nomer.append(str(nomer))

        if inp_no.text() in daftar_nomer:
            global no
            no = int(inp_no.text())
            vbox = QVBoxLayout()
            hbox = QHBoxLayout()
            wid = QWidget()

            form = QFormLayout()

            self.groupbox = QGroupBox('UPDATE DATA')

            
            self.nama = QLineEdit(data[no-1]['nama'])

            if data[int(no-1)]['jenis kelamin'] == 'laki-laki':
                self.laki = QRadioButton('laki-laki')
                self.laki.setChecked(True)
                self.perempuan = QRadioButton('perempuan')
            elif data[int(no-1)]['jenis kelamin'] == 'perempuan':
                self.laki = QRadioButton('laki-laki')
                self.perempuan = QRadioButton('perempuan')
                self.perempuan.setChecked(True)
            hbox.addWidget(self.laki)
            hbox.addWidget(self.perempuan)

            self.kota = QLineEdit(data[no-1]['kota'])

            self.provinsi = QLineEdit(data[no-1]['provinsi'])

            self.nomor_handphone = QLineEdit(data[no-1]['nomor handphone'])

            form.addRow(QLabel('Nama'),self.nama)
            form.addRow(QLabel('Jenis kelamin'),hbox)
            form.addRow(QLabel('Kota Asal'),self.kota)
            form.addRow(QLabel('Provinsi'),self.provinsi)
            form.addRow(QLabel('Nomor handphone'),self.nomor_handphone)

            self.groupbox.setLayout(form)

            self.buttonbox = QDialogButtonBox(QDialogButtonBox.Save|QDialogButtonBox.Cancel)
            self.buttonbox.accepted.connect(self.update_Action)
            self.buttonbox.rejected.connect(self.close)

            
            vbox.addWidget(self.groupbox)
            vbox.addWidget(self.buttonbox)

            self.setLayout(vbox)
            self.show()

        else:
            message = QMessageBox.warning(self,'warning','Harap masukkan hanya angka yang ada di tabel')
            self.close()
        
    def update_Action(self):
        table.removeRow(no-1)
        table.insertRow(no-1)
        def toCapital(value):
            if len(value) >= 0:
                value = value.lower()
                value_list = value.split(' ')
                value_2 = []
                for kata in value_list:
                
                    kata = kata.capitalize()
                    value_2.append(kata)
                value = ' '.join(value_2)

            return value

        def toCapital_prov(value):
            if len(value) <= 3:
                value = value.upper()
            elif len(value) > 3:
                value = value.lower()
                value_list = value.split(' ')
                value_2 = []
                for kata in value_list:
                    if len(kata) <= 3:
                        kata = kata.upper()
                    elif len(kata) > 3:
                        kata = kata.capitalize()
                    value_2.append(kata)
                value = ' '.join(value_2)

            return value

        nama = self.nama.text()
        nama = toCapital(nama)
        if self.laki.isChecked():
            jk = self.laki.text()
        elif self.perempuan.isChecked():
            jk = self.perempuan.text()
        kota = self.kota.text()
        kota = toCapital(kota)
        provinsi = self.provinsi.text()
        provinsi = toCapital_prov(provinsi)
        no_hp = self.nomor_handphone.text()
        operator_name = ''
        for jenis in operator:
            for rentang in range(len(operator[jenis])):
                if no_hp[0:4] == operator[jenis][rentang]:
                    operator_name = jenis
        for kolom in range(len(headers)):
            if headers[kolom] == 'nama':
                table.setItem(no-1,kolom,QTableWidgetItem(nama))
                table.setColumnWidth(kolom,200)
                data[no-1]['nama'] = nama
            elif headers[kolom] == 'jenis kelamin':
                table.setItem(no-1,kolom,QTableWidgetItem(jk))
                table.setColumnWidth(kolom,150)
                data[no-1]['jenis kelamin'] = jk
            elif headers[kolom] == 'kota':
                table.setItem(no-1,kolom,QTableWidgetItem(kota))
                table.setColumnWidth(kolom,150)
                data[no-1]['kota'] = kota
            elif headers[kolom] == 'provinsi':
                table.setItem(no-1,kolom,QTableWidgetItem(provinsi))
                table.setColumnWidth(kolom,150)
                data[no-1]['provinsi'] = provinsi
            elif headers[kolom] == 'operator':
                table.setItem(no-1,kolom,QTableWidgetItem(operator_name))
                data[no-1]['nomor handphone'] = no_hp

        QMessageBox.about(self,'info','Data berhasil di update')
        self.close()

# class untuk menghapus data
class delete_data(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Delete data')
        self.setGeometry(800,130,300,300)
        self.setWindowIcon(QtGui.QIcon('D:\\document\\IT\\python programming\\project\\project akhir\\inpostor.png'))
        self.setFont(QtGui.QFont('helvetica',10))

        self.nomer_delete()

        self.show()

    def nomer_delete(self):
        vbox = QVBoxLayout()
        self.judul = QLabel('Masukkan nomor yang ingin didelete!')
        vbox.addWidget(self.judul)

        
        self.inp_no = QLineEdit(self)
        
        vbox.addWidget(self.inp_no)

        tombol = QPushButton('delete')
        tombol.clicked.connect(self.delete)
        vbox.addWidget(tombol)

        self.setLayout(vbox)

    def delete(self):
        try:
            no = self.inp_no.text()
            confirm = QMessageBox.question(self,'konfirmasi','apakah anda yakin ingin menghapus data no %i atas nama %s ?' % (int(no),data[int(no)-1]['nama']))
            if confirm == 16384:
                table.removeRow(int(no)-1)
                data.remove(data[int(no)-1])
                self.close()
                QMessageBox.about(self,'info','data berhasil dihapus')
            else:
                QMessageBox.about(self,'info','anda membatalkan untuk menghapus data tersebut')
                self.close()
        except:
            QMessageBox.warning(self,'kesalahan','harap masukkan angka yang benar')

# main field atau main program            
if __name__ == "__main__":
    App = QApplication(sys.argv)
    layar = screen()
    sys.exit(App.exec_())