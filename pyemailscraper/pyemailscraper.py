# pyemailscraper.py
# Autor: Alejandro (farias@8loop.cl)
# Esta librería scrapea todos los emails de las páginas
"""
import pyemailscraper

emails = EmailScraper("https://8loop.cl")
print("mails %s" % emails.scrap())
"""

import re
import requests
RE = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}\b"

class EmailScraper(object):
    def __init__(self, url):
        self.url = url
        
    
    def scrap(self):
        r = requests.get(self.url)
        contenido = r.content
        return re.findall(u"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}", f"{contenido}")
