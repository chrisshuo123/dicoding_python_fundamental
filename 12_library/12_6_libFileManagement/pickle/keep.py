import pickle
contoh_dictionary = {1:"6", 2:"2", 3:"f"}  # Dictionary yang akan disimpan
pickle_keluar = open("dict.pickle","wb")    # Buka file mode write binary
pickle.dump(contoh_dictionary, pickle_keluar) # Simpan object
pickle_keluar.close()                        # Tutup file
