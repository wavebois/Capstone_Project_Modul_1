dict_coffee = {
1 : {'Menu' : 'Americano', 'Stock' : 20, 'Harga' : 15000, 'Flavor' : 'Strong', 'Kategori' : 'Coffee' },
2 : {'Menu' : 'Cappuccino', 'Stock' : 15, 'Harga' : 20000, 'Flavor' : 'Strong', 'Kategori' : 'Coffee'},
3 : {'Menu' : 'Espresso', 'Stock' : 35, 'Harga' : 5000, 'Flavor' : 'Strong', 'Kategori' : 'Coffee'},
}

#-----------------------------------------------------------------------------------------------

# Menu_1

def menu1():
    input_menu1 = input(f'''
\t \t Selamat Datang Di Menu Coffee Shop \t \t

Silahkan Pilih:
1. Menampilkan seluruh menu
2. Pilih menu yang diinginkan
3. Kembali ke menu utama

Masukan angka menu yang ingin dijalankan:''')
    
    if input_menu1 == '1':
        menu_1_1()
    elif input_menu1 == '2':
        menu_1_2()
    elif input_menu1 == '3':
        menu_utama()
    else:
        print()
        print('Data yang anda masukan tidak sesuai')
        menu1()

# Menu_1_1

def menu_1_1():
    dict_coffee_key = list(dict_coffee.keys())
    if len(dict_coffee_key) == 0:
        print()
        print('Data Kosong')
        menu1()
    else:
        print("{: <20} {: <20} {: <20} {: <20} {: <20} {: <20}".format('Kode Item', '| Menu', ' | Stock', '  | Harga', '   | Flavor', '    | Kategori'))
        for i in dict_coffee_key:
            print(f'''{i:<20} | {dict_coffee[i]['Menu']:<20}| {dict_coffee[i]['Stock']:<20}| {dict_coffee[i]['Harga']:<20}| {dict_coffee[i]['Flavor']:<20}| {dict_coffee[i]['Kategori']:<20}''')
        menu1()

# Menu_1_2

def menu_1_2():
    dict_coffee_keys = list(dict_coffee.keys())
    if len(dict_coffee_keys) == 0:
        print()
        print('Data Kosong')
        menu1()
    else:
        print()
        input_nomor = input('Masukan Kode Item:')
        if input_nomor.isnumeric():
            input_nomor = int(input_nomor)
            if input_nomor in dict_coffee_keys:
                print("{: <20} {: <20} {: <20} {: <20} {: <20} {: <20}".format('Kode Item', '| Menu', ' | Stock', '  | Harga', '   | Flavor', '    | Kategori'))
                print(f'''{input_nomor:<20} | {dict_coffee[input_nomor]['Menu']:<20}| {dict_coffee[input_nomor]['Stock']:<20}| {dict_coffee[input_nomor]['Harga']:<20}| {dict_coffee[input_nomor]['Flavor']:<20}| {dict_coffee[input_nomor]['Kategori']:<20}''')
                menu1()
            else:
                print()
                print('Menu Tidak ada')
                menu_1_2()
        else:
            print()
            print('Data yang anda masukan tidak sesuai')
            menu_1_2()

#-----------------------------------------------------------------------------------------------

# Menu_2

def menu_2():
    input_menu2 = input(f'''
\t \t Selamat Datang Di Menu Coffee Shop \t \t

Silahkan Pilih:
1. Jika ingin menambahkan item pada menu
2. Kembali ke menu utama

Masukan angka menu yang ingin dijalankan:''')
    #MENAMBAH_INPUT_MENU_COFFEE
    if input_menu2 == '1':
        print()
        input_kode_item = input('Masukkan kode item yang diinginkan:')
        input_kode_item_list = list(input_kode_item)
        comp = [i.isnumeric() for i in input_kode_item_list]
        if False in comp:
            print()
            print('Data yang anda masukkan tidak sesuai')
            menu_2()
        input_kode_item = int(input_kode_item)
        if input_kode_item in dict_coffee.keys():
            print()
            print('Data Sudah Tersedia')
            menu_2()
        else:
            # INPUT_MENU
            print()
            input_menu = input('Masukkan Nama Menu:')
            input_menu_list = list(input_menu)
            comp = [i.isalpha() or i.isspace() for i in input_menu_list]
            if False in comp:
                print()
                print('Data yang anda masukkan tidak sesuai')
                menu_2()
            
            # INPUT_STOCK
            print()
            input_stock = input('Masukkan Stock Menu:')
            input_stock_list = list(input_stock)
            comp = [i.isnumeric() for i in input_stock_list]
            if False in comp:
                print()
                print('Data yang anda masukkan tidak sesuai')
                menu_2()
            check_2000 = int(input_stock) <= 2000
            if check_2000 == False:
                print()
                print('Stock yang anda masukkan terlalu banyak')
                menu_2()
            input_stock = int(input_stock)
            
            #INPUT_HARGA
            print()
            input_harga = input('Masukkan Harga Menu:')
            input_harga_list = list(input_harga)
            input_harga = int(input_harga)
            comp = [i.isnumeric() for i in input_harga_list]
            if False in comp:
                print()
                print('Data yang anda masukkan tidak sesuai')
                menu_2()
            check_150000 = 10000 <= int(input_harga) <= 150000
            if check_150000 == False:
                print()
                print('Harga yang anda masukkan tidak sesuai')
                menu_2()
            input_harga = int(input_harga)
            
            #INPUT_FLAVOR
            print()
            input_flavor = input('Masukkan Flavor Menu (Strong or Mild):').lower()
            input_flavor_list = list(input_flavor)
            comp = [i.isalpha() for i in input_flavor_list]
            if False in comp:
                print()
                print('Data yang anda masukkan tidak sesuai')
                menu_2()
            if input_flavor != 'strong' and input_flavor != 'mild':
                print()
                print('Flavor yang anda masukkan harus sesuai')
                menu_2()

            #INPUT_KATEGORI
            print()
            input_kategori = input('Masukkan Kategori Menu (Coffee or Milk):').lower()
            input_kategori_list = list(input_kategori)
            comp = [i.isalpha() for i in input_kategori_list]
            if False in comp:
                print()
                print('Data yang anda masukkan tidak sesuai')
                menu_2()
            if input_kategori != 'coffee' and input_kategori != 'milk':
                print()
                print('Kategori yang anda masukkan harus sesuai')
                menu_2()
            
            #MENAMPILKAN_MENU_YANG_DITAMBAHKAN
            dict_coffee_add = {'Menu' : input_menu.capitalize(), 'Stock' : input_stock, 'Harga' : input_harga, 'Flavor' : input_flavor.capitalize(), 'Kategori' : input_kategori.capitalize()}
            print()
            print("{: <20} {: <20} {: <20} {: <20} {: <20} {: <20}".format('Kode Item', '| Menu', ' | Stock', '  | Harga', '   | Flavor', '    | Kategori'))
            print(f'''{input_kode_item:<20} | {input_menu.capitalize() :<20}| {input_stock :<20}| {input_harga :<20}| {input_flavor.capitalize() :<20}| {input_kategori.capitalize():<20}''')
            
            #DATA_INGIN_DISIMPAN
            print()
            input_save = input('Apakah data ingin disave (y/n)?').lower()
            input_save_list = list(input_save)
            comp = [i.isalpha() for i in input_save_list]
            if False in comp:
                print()
                print('Data yang anda masukkan tidak sesuai')
                menu_2()
            if input_save == 'y':
                dict_coffee[input_kode_item] = dict_coffee_add
                print()
                print('Data telah tersimpan')
                menu_2()
            elif input_save == 'n':
                print()
                print('Data Tidak Disimpan')
                menu_2()
            else:
                print()
                print('Pilihan yang anda masukkan tidak sesuai')
                menu_2()
    elif input_menu2 == '2':
        menu_utama()
    else:
        print()
        print('Data yang anda masukkan tidak sesuai')
        menu_2()

#-----------------------------------------------------------------------------------------------

# Menu_3

def menu_3():

    input_menu3 = input(f'''
\t \t Selamat Datang Di Menu Coffee Shop \t \t

Silahkan Pilih:
1. Jika ingin mengupdate data
2. Kembali ke menu utama

Masukan angka menu yang ingin dijalankan:''')
    
    # INPUT_MENU
    if input_menu3 == '1':
        dict_coffee_key = dict_coffee.keys()
        print()
        input_nomor = input('Masukan Kode Item:')
        if input_nomor.isnumeric():
            input_nomor = int(input_nomor)
            if input_nomor in dict_coffee_key:
                print("{: <20} {: <20} {: <20} {: <20} {: <20} {: <20}".format('Kode Item', '| Menu', ' | Stock', '  | Harga', '   | Flavor', '    | Kategori'))
                print(f'''{input_nomor:<20} | {dict_coffee[input_nomor]['Menu']:<20}| {dict_coffee[input_nomor]['Stock']:<20}| {dict_coffee[input_nomor]['Harga']:<20}| {dict_coffee[input_nomor]['Flavor']:<20}| {dict_coffee[input_nomor]['Kategori']:<20}''')
                
                # PERTANYAAN
                print()
                input_save = input('Apakah data ingin dirubah (y/n)?').lower()
                input_save_list = list(input_save)
                comp = [i.isalpha() for i in input_save_list]
                if False in comp:
                    print()
                    print('Data yang anda masukkan tidak sesuai')
                    menu_3()
                if input_save == 'y':
                    # INPUT_KOLOM
                    print()
                    input_kolom = input('Pilih kolom yang ingin dirubah:').capitalize()
                    input_kategori_list = list(input_kolom)
                    comp = [i.isalpha() for i in input_kategori_list]
                    if comp == False:
                        print()
                        print('Mohon untuk memilih kolom yang benar')
                        menu_3()
                    else:
                        # KOLOM_MENU
                        if input_kolom == 'Menu':
                            print()
                            input_value_baru = input('Masukkan menu baru anda:').lower()
                            input_value_list = list(input_value_baru)
                            comp = [i.isalpha() or i.isspace() for i in input_value_list]
                            if False in comp:
                                print()
                                print('Data yang anda masukkan tidak sesuai')
                                menu_3()
                            else:
                                print()
                                input_save = input('Apakah data ingin disave (y/n)?').lower()
                                input_save_list = list(input_save)
                                comp = [i.isalpha() for i in input_save_list]
                                if False in comp:
                                    print()
                                    print('Data yang anda masukkan tidak sesuai')
                                    menu_3()
                                if input_save == 'y':
                                    dict_coffee[input_nomor][input_kolom] = input_value_baru.capitalize()
                                    print()
                                    print('Data telah tersimpan')
                                    menu_3()
                                elif input_save == 'n':
                                    print()
                                    print('Data Tidak Disimpan')
                                    menu_3()
                                else:
                                    print()
                                    print('Data yang anda masukkan tidak sesuai')
                                    menu_3()
                        
                        # KOLOM_STOCK
                        elif input_kolom == 'Stock':
                            print()
                            input_value_baru = input('Masukkan stock baru anda:')
                            input_value_list = list(input_value_baru)
                            comp = [i.isnumeric() for i in input_value_list]
                            if False in comp:
                                print()
                                print('Data yang anda masukkan tidak sesuai')
                                menu_3()
                            check_2000 = int(input_value_baru) <= 2000
                            if check_2000 == False:
                                print()
                                print('Data yang anda masukkan tidak sesuai')
                                menu_3()
                            else:
                                print()
                                input_save = input('Apakah data ingin disave (y/n)?').lower()
                                input_save_list = list(input_save)
                                comp = [i.isalpha() for i in input_save_list]
                                if False in comp:
                                    print()
                                    print('Data yang anda masukkan tidak sesuai')
                                    menu_3()
                                if input_save == 'y':
                                    input_value_baru = int(input_value_baru)
                                    dict_coffee[input_nomor][input_kolom] = input_value_baru
                                    print()
                                    print('Data telah tersimpan')
                                    menu_3()
                                elif input_save == 'n':
                                    print()
                                    print('Data Tidak Disimpan')
                                    menu_3()
                                else:
                                    print()
                                    print('Data yang anda masukkan tidak sesuai')
                                    menu_3()

                        # KOLOM_HARGA
                        elif input_kolom == 'Harga':
                            print()
                            input_value_baru = input('Masukkan harga baru anda:')
                            input_value_list = list(input_value_baru)
                            comp = [i.isnumeric() for i in input_value_list]
                            if False in comp:
                                print()
                                print('Data yang anda masukkan tidak sesuai')
                                menu_3()
                            check_150000 = 10000 <= int(input_value_baru) <= 150000
                            if check_150000 == False:
                                print()
                                print('Data yang anda masukkan tidak sesuai')
                                menu_3()
                            else:
                                print()
                                input_save = input('Apakah data ingin disave (y/n)?').lower()
                                input_save_list = list(input_save)
                                comp = [i.isalpha() for i in input_save_list]
                                if False in comp:
                                    print()
                                    print('Data yang anda masukkan tidak sesuai')
                                    menu_3()
                                if input_save == 'y':
                                    input_value_baru = int(input_value_baru)
                                    dict_coffee[input_nomor][input_kolom] = input_value_baru
                                    print()
                                    print('Data telah tersimpan')
                                    menu_3()
                                elif input_save == 'n':
                                    print()
                                    print('Data Tidak Disimpan')
                                    menu_3()
                                else:
                                    print()
                                    print('Data yang anda masukkan tidak sesuai')
                                    menu_3()

                        # KOLOM_FLAVOR
                        elif input_kolom == 'Flavor':
                            print()
                            input_value_baru = input('Masukkan flavor baru anda (Strong or Mild):').lower()
                            input_value_list = list(input_value_baru)
                            comp = [i.isalpha() for i in input_value_list]
                            if False in comp:
                                print()
                                print('Data yang anda masukkan tidak sesuai')
                                menu_3()
                            if input_value_baru != 'strong' and input_value_baru != 'mild':
                                print()
                                print('Data yang anda masukkan tidak sesuai')
                                menu_3()
                            else:
                                print()
                                input_save = input('Apakah data ingin disave (y/n)?').lower()
                                input_save_list = list(input_save)
                                comp = [i.isalpha() for i in input_save_list]
                                if False in comp:
                                    print()
                                    print('Data yang anda masukkan tidak sesuai')
                                    menu_3()
                                if input_save == 'y':
                                    dict_coffee[input_nomor][input_kolom] = input_value_baru.capitalize()
                                    print()
                                    print('Data telah tersimpan')
                                    menu_3()
                                elif input_save == 'n':
                                    print()
                                    print('Data Tidak Disimpan')
                                    menu_3()
                                else:
                                    print()
                                    print('Data yang anda masukkan tidak sesuai')
                                    menu_3()

                        # KOLOM_KATEGORI
                        elif input_kolom == 'Kategori':
                            print()
                            input_value_baru = input('Masukkan kategori baru anda (Coffee or Milk):').lower()
                            input_value_list = list(input_value_baru)
                            comp = [i.isalpha() for i in input_value_list]
                            if False in comp:
                                print()
                                print('Data yang anda masukkan tidak sesuai')
                                menu_3()
                            if input_value_baru != 'coffee' and input_value_baru != 'milk':
                                print()
                                print('Data yang anda masukkan tidak sesuai')
                                menu_3()
                            else:
                                input_save = input('Apakah data ingin disave (y/n)?').lower()
                                input_save_list = list(input_save)
                                comp = [i.isalpha() for i in input_save_list]
                                if False in comp:
                                    print()
                                    print('Data yang anda masukkan tidak sesuai')
                                    menu_3()
                                if input_save == 'y':
                                    
                                    dict_coffee[input_nomor][input_kolom] = input_value_baru.capitalize()
                                    print()
                                    print('Data telah tersimpan')
                                    menu_3()
                                elif input_save == 'n':
                                    print()
                                    print('Data Tidak Disimpan')
                                    menu_3()
                                else:
                                    print()
                                    print('Data yang anda masukkan tidak sesuai')
                                    menu_3()
                        else:
                            print()
                            print('Data yang anda masukkan tidak sesuai')
                            menu_3()
                elif input_save == 'n':
                        print()
                        print('Data Tidak Diupdate')
                        menu_3()   
                else:
                    print()
                    print('Data yang anda masukkan tidak sesuai')
                    menu_3()  
            else:
                print()
                print('Menu tidak ada')
                menu_3()
        else:
            print()
            print('Data yang anda masukkan tidak sesuai')
            menu_3()
    elif input_menu3 == '2':
        menu_utama()
    else:
        print()
        print('Data yang anda masukkan tidak sesuai')
        menu_3()

#-----------------------------------------------------------------------------------------------

# Menu_4

def menu_4():

    input_menu4 = input(f'''
    \t \t Selamat Datang Di Menu Coffee Shop \t \t

Silahkan Pilih:
1. Menghapus item pada menu
2. Kembali ke menu utama

Masukan angka menu yang ingin dijalankan:''')
    
    if input_menu4 == '1':
        dict_keys = list(dict_coffee.keys())
        if len(dict_keys) == 0:
            print()
            print('Data sudah kosong')
            menu_4()
        else:
            print("{: <20} {: <20} {: <20} {: <20} {: <20} {: <20}".format('Kode Item', '| Menu', ' | Stock', '  | Harga', '   | Flavor', '    | Kategori'))
            for i in dict_keys:
                print(f'''{i:<20} | {dict_coffee[i]['Menu']:<20}| {dict_coffee[i]['Stock']:<20}| {dict_coffee[i]['Harga']:<20}| {dict_coffee[i]['Flavor']:<20}| {dict_coffee[i]['Kategori']:<20}''')
            input_kode_item = input('Silahkan masukkan kode item yang dipilih:')
            input_kode_item_list = list(input_kode_item)
            comp = [i.isnumeric() for i in input_kode_item_list]
            input_kode_item = int(input_kode_item)
            if False in comp:
                print()
                print('Data yang anda masukkan tidak sesuai')
                menu_4()
            else:
                input_save = input('Apakah anda yakin data ingin dihapus (y/n)?').lower()
                input_save_list = list(input_save)
                comp = [i.isalpha() for i in input_save_list]
                if False in comp:
                    print()
                    print('Data yang anda masukkan tidak sesuai')
                    menu_4()
                if input_save == 'y':
                    if input_kode_item in dict_coffee:
                        del dict_coffee[input_kode_item]
                        print()
                        print('Data telah terhapus')
                        menu_4()
                    else:
                        print()
                        print('Data tidak ada')
                        menu_4()
                elif input_save == 'n':
                    print()
                    print('Data tidak dihapus')
                    menu_4()
                else:
                    print()
                    print('Data yang anda masukkan tidak sesuai')
                    menu_4()

    elif input_menu4 == '2':
        menu_utama()

    else:
        print()
        print('Data yang anda masukkan tidak sesuai')
        menu_4()

#-----------------------------------------------------------------------------------------------

# MENU_5

def menu_5():
        
        input_menu5 = input(f'''
\t \t Selamat Datang Di Menu Coffee Shop \t \t

Silahkan Pilih:
1. Jika ingin membeli menu
2. Kembali ke menu utama

Masukan angka menu yang ingin dijalankan:''')
        
        if input_menu5 == '1':
            # MENDEFINISIKAN
            dict_coffee_key = list(dict_coffee.keys())
            cart = {}
            cart_counter = 1
            
            # MEMBUAT LOOP PEMBELIAN
            while True:
                if len(dict_coffee_key) == 0:
                    print()
                    print('Data Kosong')
                    break
                else:
                    print()
                    print("{: <20} {: <20} {: <20} {: <20} {: <20} {: <20}".format('Kode Item', '| Menu', ' | Stock', '  | Harga', '   | Flavor', '    | Kategori'))
                    for i in dict_coffee_key:
                        print(f'''{i:<20} | {dict_coffee[i]['Menu']:<20}| {dict_coffee[i]['Stock']:<20}| {dict_coffee[i]['Harga']:<20}| {dict_coffee[i]['Flavor']:<20}| {dict_coffee[i]['Kategori']:<20}''')

            # INPUT_ITEM_YANG_INGIN_DIBELI
                dict_coffee_key = list(dict_coffee.keys())
                if len(dict_coffee_key) == 0:
                    print()
                    print('Data Kosong')
                    break

                print()
                item = input("Masukan kode item yang ingin dibeli: ")
                if item.isnumeric():
                    item = int(item)
                    if item in dict_coffee:
                        print()
                        print("{: <20} {: <20} {: <20} {: <20} {: <20} {: <20}".format('Kode Item', '| Menu', ' | Stock', '  | Harga', '   | Flavor', '    | Kategori'))
                        print(f'''{item:<20} | {dict_coffee[item]['Menu']:<20}| {dict_coffee[item]['Stock']:<20}| {dict_coffee[item]['Harga']:<20}| {dict_coffee[item]['Flavor']:<20}| {dict_coffee[item]['Kategori']:<20}''')
                    else:
                        print()
                        print('Menu tidak ada')
                        menu_5()
                else:
                    print()
                    print('Data yang anda masukkan tidak sesuai')
                    menu_5()
                
                # MENDEFINISIKAN
                stok = dict_coffee[item]['Stock']
                stok = int(stok)
                nama = dict_coffee[item]['Menu']

                #INPUT_QUANTITY
                print()
                quantity = input('Berapa banyak yang ingin anda beli? ')
                if quantity.isnumeric():
                    quantity = int(quantity)
                    cart_key = list(cart.keys())
                    harga = dict_coffee[item]['Harga']
                    total_harga = harga*quantity
                    if stok < quantity:
                        print()
                        print(f'''Stock {nama} {stok}''')
                        menu_5()
                    else:
                        if item in cart_key:
                            cart[item]['Quantity'] = cart[item]['Quantity'] + quantity
                            dict_coffee[item]['Stock'] = dict_coffee[item]['Stock'] - quantity
                        else:
                            belanja_add = {'Menu' : dict_coffee[item]['Menu'], 'Quantity' : quantity, 'Harga' : harga, 'Harga' : total_harga}
                            cart[cart_counter] = belanja_add
                            cart_counter += 1
                            dict_coffee[item]['Stock'] = dict_coffee[item]['Stock'] - quantity
                    cart_key = list(cart.keys())
                    print()
                    print("{: <20} {: <20} {: <20} {: <20}".format('Menu', ' | Quantity', ' | Harga', '  | Total Harga'))
                    for i in cart_key:
                        print(f'''{cart[i]['Menu']:<20}  |{cart[i]['Quantity']:<20}| {dict_coffee[i]['Harga']:<20}| {cart[i]['Harga']:<20}''')
                    print()
                else:
                    print()
                    print('Data yang anda masukkan tidak sesuai')
                    menu_5()

                # HARGA_TOTAL
                total_belanja = 0
                for i in cart_key:
                    harga_total = cart[i]['Harga']
                    total_belanja = total_belanja+harga_total
                print(f'''Total Harga {total_belanja}''')

                # LOOPING_PEMBAYARAN
                while True:
                    masukanUang = input('Masukan Jumlah Uang:')
                    input_masukanUang_list = list(masukanUang)
                    comp = [i.isnumeric() for i in input_masukanUang_list]
                    if False in comp:
                        dict_coffee[item]['Stock'] = dict_coffee[item]['Stock'] + quantity
                        print()
                        print('Data yang anda masukkan tidak sesuai')
                        menu_5()
                    masukanUang = int(masukanUang)
                    kembalian = (masukanUang-total_belanja)
                    kurang = (total_belanja-masukanUang)
                    if masukanUang > total_belanja:
                        print(f'''
        Terimakasih
        Uang kembali anda: {kembalian} Rupiah'''
                        )
                        break
                    elif masukanUang < total_belanja:
                        print(f'''
        Transaksi anda dibatalkan
        Uang anda kurang sebesar {kurang} Rupiah'''
                            )
                        
                    else:
                        print('Terimakasih')
                        break
                break

            menu_5()

        elif input_menu5 == '2':
            menu_utama()
        
        else:
            print()
            print('Data yang anda masukkan tidak sesuai')
            menu_5()

#-----------------------------------------------------------------------------------------------


# Menu_Utama

def menu_utama():

    input_menu = input(f'''

\t \t Selamat Datang Di Menu Cofee Shop \t \t

List Menu:
1. Menampilkan daftar menu
2. Menambahkan item
3. Mengubah item
4. Menghapus item
5. Membeli menu
6. Exit program

Masukan angka menu yang ingin dijalankan:''')


    if input_menu == '1':
        menu1()
    elif input_menu == '2':
        menu_2()
    elif input_menu == '3':
        menu_3()
    elif input_menu == '4':
        menu_4()
    elif input_menu == '5':
        menu_5()
    elif input_menu == '6':
        print('Terimakasih sudah berbelanja')
        exit()
    else:
        menu_utama()

menu_utama()
