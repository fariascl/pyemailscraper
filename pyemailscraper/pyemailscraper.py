# pyemailscraper.py
# Autor: Alejandro (farias@8loop.cl)
# Esta librería scrapea todos los emails disponibles en una URL
"""
from pyemailscraper import *

emails = WebScraper("https://8loop.cl") # Instancia para scrapear desde URLs
emails_2 = FileScraper("/path/file.txt") # Instancia para scrapear archivo .txt
print("mails %s" % emails.scrap())
"""
import re
import requests

class WebScraper:
    def __init__(self, url):
        self.url = url
        
    def scrap(self):
        r = requests.get(self.url)
        contenido = r.content
        return re.findall(u"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}", f"{contenido}")

class FileScraper:
    def __init__(self, file):
        self.file = file

    def scrap(self):
        with open(self.file) as file:
            emails = re.findall(u"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}", f"{file.read()}")
        return emails
    
