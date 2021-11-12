from pyemailscraper.pyemailscraper import *

URL = "http://biobiochile.cl"
file = "example.txt"

emails = FileScraper("example.txt")
print(emails.scrap())

