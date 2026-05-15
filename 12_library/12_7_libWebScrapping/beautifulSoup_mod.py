from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import gzip

# Pengambilan Konten
url = "http://python.org/"
req = Request(url, headers={'Accept-Encoding': 'identity'}) # Minta tanpa kompresi
page = urlopen(url)

# Jika tetap menerima gzip, harus di-decode dulu:
if page.info().get('Content-Encoding') == 'gzip':
    html = gzip.decompress(page.read()).decode("UTF-8")
else:
    html = page.read().decode("UTF-8")
    
# Membuat objek BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Mencetak judul halaman
print(soup.title)