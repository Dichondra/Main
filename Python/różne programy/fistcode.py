from urllib.request import urlopen
from urllib.error import HTTPError
try:
    html = urlopen('http://www.dupadupa.com')
except HTTPError as e:
    print(e)
else:
    print("dupa")

