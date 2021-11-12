from pyemailscraper.pyemailscraper import *

URL = "http://ubiobio.cl"
file = "example.txt"

emails = FileScraper("example.txt")
print(emails.scrap())

