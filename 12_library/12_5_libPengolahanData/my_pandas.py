import pandas as pd

# Membuat DataFrame dari Dictionary
data = {
    'Nama': ['John', 'Jane', 'Bob', 'Alice'],
    'Usia': [25, 30, 22, 28],
    'Pekerjaan': ['Engineer', 'Teacher', 'Designer', 'Doctor']
}

df = pd.DataFrame(data)

# Menampilkan DataFrame
print(df)