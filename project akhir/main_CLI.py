import data_mhs as dm
from matplotlib import pyplot as plt
from tkinter import messagebox
# import time

# mengimport data dari file data_mhs.py
data = dm.data()
operator = dm.operator_func()

# fungsi untuk menghitung karakter terpanjang
def long_char():
    # global t1
    # t1 = time.time()
    global long
    long = {}
    for isi in data[0]:
        temp = []
        for baris in range(len(data)):
            temp.append(len(data[baris][isi]))
            temp2 = max(temp)
        long[isi] = temp2
    return long

# fungsi untuk menampilkan data mahasiswa
def show(long):
    for baris in range(-1,len(data)):
        if baris == -1:
            print ('+',end='')
            print ('-'*102,end='')
            print ('+')
            print ('| No  |',end='')
            for kolom in data[0]:
                for spasi in long:
                    if kolom == spasi:
                        if spasi != 'nomor handphone':
                            print (kolom.center(long[spasi]+3),end='|')
                        else:
                            print ('operator'.center(12),end='|')
            print('')
        else:
            print ('+',end='')
            print ('-'*102,end='')
            print ('+')
            if len(str(baris+1)) == 3:
                print ('|',baris+1,'|',end='')
            elif len(str(baris+1)) == 2:
                print ('|',baris+1,' |',end='')
            elif len(str(baris+1)) == 1:
                print ('|',baris+1,'  |',end='')
            for isi in data[baris]:
                for spasi in long:
                    if isi == spasi:
                        if spasi != 'nomor handphone' and spasi != 'jenis kelamin':
                            print (data[baris][isi].center(long[spasi]+3),end='|')
                        elif spasi != 'nomor handphone' and spasi == 'jenis kelamin':
                            print (data[baris][isi].center(long[spasi]+4),end='|')
                        elif spasi == 'nomor handphone':
                            for jenis in operator:
                                for rentang in range(len(operator[jenis])):
                                    if data[baris][isi][0:4] == operator[jenis][rentang]:
                                        print (jenis.center(12),end='|')  

            print('')
    print ('+',end='')
    print ('-'*102,end='')
    print ('+')
    # print ('done in :',time.time()-t1)

# fungsi untuk menambahkan data
def add():
    temp = {}
    for key_par in data[0]: 
        if key_par != 'jenis kelamin':
            stop_1 = False
            while not(stop_1):
                if key_par != 'nomor handphone':
                    inp = input('masukkan data %s : ' % (key_par))
                    inp = inp.lower()
                    list_inp = inp.split(' ')
                    list_result = []
                    for i in list_inp:
                        i = i.capitalize()
                        list_result.append(i)
                    inp = ' '.join(list_result)
                if key_par == 'nomor handphone':
                    stop_2 = False
                    while not(stop_2):
                        inp = input('masukkan data %s : ' % (key_par))
                        if inp.isnumeric() == False:
                            print ('masukkan angka saja sebagai nomer handphone')
                            stop_2 = False
                        else:
                            stop_2 = True
                if len(inp) == 0:
                    print ('data harus diisi')
                    stop_1 = False
                else:
                    temp[key_par] = inp
                    stop_1 = True
        else:
            stop = False
            while not(stop):
                inp = input('masukkan data jenis kelamin\nL : laki-laki\nP : perempuan\n-->')
                if inp.upper() == 'L':
                    temp[key_par] = 'laki-laki'
                    stop = True
                elif inp.upper() == 'P':
                    temp[key_par] = 'perempuan'
                    stop = True
                elif inp == '':
                    print ('data harus diisi')
                    stop = False
                else:
                    print ('masukkan hanya huruf L atau P')
                    stop = False
    data.append(temp)
    messagebox.showinfo('info','Data berhasil ditambahkan!')

# fungsi untuk mengupdate data
def update():
    long = long_char()
    # show(long)
    global daftar_nomer
    daftar_nomer = []
    for nomer in range(1,len(data)+1,1):
        daftar_nomer.append(nomer)
    stop_main = False
    while not(stop_main):
        try:
            inp_update = int(input('masukkan nomer yang ingin diupdate : '))
            if inp_update not in daftar_nomer:
                print ('masukkan nomer yang benar')
                stop_main = False
            else:
                stop_main = True
        except:
            print ('masukkan angka')
    def show_spec_num(long):
        print ('+',end='')
        print ('-'*102,end='')
        print ('+')
        print ('| No  |',end='')
        for kolom in data[0]:
            for spasi in long:
                if kolom == spasi:
                    if spasi != 'nomor handphone':
                        print (kolom.center(long[spasi]+3),end='|')
                    else:
                        print ('operator'.center(12),end='|')
        print('')
        print ('+',end='')
        print ('-'*102,end='')
        print ('+')
        if len(str(inp_update)) == 3:
            print ('|',inp_update,'|',end='')
        elif len(str(inp_update)) == 2:
            print ('|',inp_update,' |',end='')
        elif len(str(inp_update)) == 1:
            print ('|',inp_update,'  |',end='')
        for isi in data[inp_update-1]:
            for spasi in long:
                if isi == spasi:
                    if spasi != 'nomor handphone' and spasi != 'jenis kelamin':
                        print (data[inp_update-1][isi].center(long[spasi]+3),end='|')
                    elif spasi != 'nomor handphone' and spasi == 'jenis kelamin':
                        print (data[inp_update-1][isi].center(long[spasi]+4),end='|')
                    elif spasi == 'nomor handphone':
                        for jenis in operator:
                            for rentang in range(len(operator[jenis])):
                                if data[inp_update-1][isi][0:4] == operator[jenis][rentang]:
                                    print (jenis.center(12),end='|')
        print('')
        print ('+',end='')
        print ('-'*102,end='')
        print ('+')
    show_update = show_spec_num(long)   

    stop_part = False
    while not(stop_part):
        part_update = input('masukkan bagian data yang ingin diupdate\n1. nama\n2. jenis kelamin\n3. kota\n4. provinsi\n5. nomor handphone\n--> : ')
        if part_update not in ['1','2','3','4','5']:
            print ('masukkan angka diantara 1,2,3,4,5')
            stop_part = False
        else:
            theKeys = ('nama','jenis kelamin','kota','provinsi','nomor handphone')
            inp_update = int(inp_update)
            part_update = int(part_update)
            if part_update != 2:
                if part_update != 5:
                    stop_1 = False
                    while not(stop_1):
                        print ('data %s lama anda adalah : %s'% (theKeys[part_update-1],data[inp_update-1][theKeys[part_update-1]]))
                        update_new = input('masukkan data %s anda yang baru : ' % (theKeys[part_update-1]))
                        if len(update_new) == 0:
                            print ('data harus diisi')
                            stop_1 = False
                        else:
                            stop_1 = True
                    update_new = update_new.lower()
                    list_update = update_new.split(' ')
                    list_update_result = []
                    for i in list_update:
                        i = i.capitalize()
                        list_update_result.append(i)
                    update_new = ' '.join(list_update_result)
                    data[inp_update-1][theKeys[part_update-1]] = update_new
                stop_part = True
                if part_update == 5:
                    stop_2 = False
                    while not(stop_2):
                        print ('data %s lama anda adalah : %s'% (theKeys[part_update-1],data[inp_update-1][theKeys[part_update-1]]))
                        update_new = input('masukkan data %s anda yang baru : ' % (theKeys[part_update-1]))
                        if update_new.isnumeric() == False:
                            print ('masukkan angka saja sebagai nomer handphone')
                            stop_2 = False
                        else:
                            stop_2 = True
                    data[inp_update-1][theKeys[part_update-1]] = update_new
                    
            else:
                stop = False
                while not(stop):
                    print ('data %s lama anda adalah : %s'% (theKeys[part_update-1],data[inp_update-1][theKeys[part_update-1]]))
                    inp = input('masukkan data jenis kelamin anda yang baru\nL : laki-laki\nP : perempuan\n-->')
                    if inp.upper() == 'L':
                        data[inp_update-1][theKeys[part_update-1]] = 'laki-laki'
                        stop = True
                    elif inp.upper() == 'P':
                        data[inp_update-1][theKeys[part_update-1]] = 'perempuan'
                        stop = True
                    elif inp == '':
                        print ('data harus diisi')
                        stop = False
                    else:
                        print ('masukkan hanya huruf L atau P')
                        stop = False
                stop_part = True

    messagebox.showinfo('info','Data berhasil update!')

# fungsi untuk menghapus data
def delete():
    stop = False
    long = long_char()
    show(long)
    while not(stop):
        try:
            inp_del = int(input('masukkan nomer yang ingin dihapus : '))
            stop = True
        except:
            print('masukkan angka saja')
            stop = False

    sure = messagebox.askyesno('konfirmasi','apakah anda yakin ingin menghapus data nomor %i atas nama %s ?' % (inp_del,data[inp_del-1]['nama']))
    if sure == 1:
        data.remove(data[inp_del-1])
    else:
        pass

# fungsi untuk menganalisis dan mengelompokkan data
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

# fungsi menampilkan statistik data mahasiswa berdasarkan jenis kelamin
def jk():
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
    plt.pie(jk_jum,labels = jk_list,explode=explode,autopct='%1.1f%%')
        
    plt.title('Statistik Mahasiswa Teknik Informatika Angkatan 2020\n Berdasarkan Jenis kelamin')
    plt.tight_layout()
    plt.show()

# fungsi menampilkan statistik data mahasiswa berdasarkan kota asal
def kota_asal():
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

# fungsi menampilkan statistik data mahasiswa berdasarkan provinsi asal
def provinsi_asal():
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

 # fungsi menampilkan statistik data mahasiswa berdasarkan operator yang digunakan   
def operator_stat():
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

# main program  
stop = False
while not(stop):
    # melakukan percobaan eksekusi program, jika gagal maka akan menampilkan exception
    try:
        print ('+',end='')
        print ('-'*106,end='')
        print ('+')
        print ('|',end='')
        print ('PROGRAM CRUD (CREATE,READ,UPDATE,DAN DELETE) DAN STATISTIK DATA MAHASISWA TEKNIK INFORMATIKA ANGKATAN 2020',end='')
        print('|')
        print ('+',end='')
        print ('-'*106,end='')
        print ('+')
        choose = int(input('Masukkan pilihan anda:\n1. tampilkan data\n2. tambah data\n3. update data \n4. hapus data\n5. tampilkan statistik\n6. keluar\n --> ' ))
        if choose == 1:
            long = long_char()
            show(long)
        elif choose == 2:
            add()
        elif choose == 3:
            update()
        elif choose == 4:
            delete()
        elif choose == 5:
            stop_2 = False
            while not(stop_2):
                inp_stat = int(input('masukkan pilihan statistik yang ingin anda lihat:\n1. jenis kelamin\n2. Kota asal\n3. Provinsi asal\n4. Operator seluler yang digunakan\n5. keluar\n(masukkan angkanya saja) : '))
                if inp_stat == 1:
                    analisis()
                    jk()
                elif inp_stat == 2:
                    analisis()
                    kota_asal()
                elif inp_stat == 3:
                    analisis()
                    provinsi_asal()
                elif inp_stat == 4:
                    analisis()
                    operator_stat()
                elif inp_stat == 5:
                    stop_2 = True
                else:
                    print ('masukkan angka yang benar')
                    stop_2 = False
        elif choose == 6:
            stop = True
        else:
            print ('masukkan hanya antara 1,2,3,4')
            stop = False
    except:
        print ('--hanya boleh memasukkan angka saja!!--')
        stop = False 
# thank you   
messagebox.showinfo('info','Thank you!')   