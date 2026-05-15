from urllib.request import urlopen
import gzip

# Pengambilan konten
url = "http://python.org/"
page = urlopen(url)

# Decode konten
if page.info().get('Content-Encoding') == 'gzip':
    html = gzip.decompress(page.read()).decode("UTF-8")
else:
    html = page.read().decode("UTF-8")

# Mencari indeks awal dan akhir
start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")

# Mengekstrak dan mencetak judul halaman
title = html[start_index:end_index]
print(title)