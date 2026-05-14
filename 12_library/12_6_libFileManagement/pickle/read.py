import pickle

pickle_masuk = open("dict.pickle", "rb")     # Buka file mode read binary
contohDictionary = pickle.load(pickle_masuk) # Load object dari file
pickle_masuk.close()                         # Tutup file

print(contohDictionary)  # Output: {1:"6", 2:"2", 3:"f"}
