from bs4 import BeautifulSoup
import requests

#CURRENTLY PULLING A URL PRICE CHECK AS A PROOF OF CONCEPT DUE TO THE SENSITIVE DATA IT WOULD RETREIVE FROM MY COMPANY NETWORK#
#I WILL BE ADDING A PUBLIC API KEY TO REQUEST INFORMATION FROM VIRUS TOTAL IN NEXT VERSION#
url = "https://www.newegg.com/creality-ender-3-s1-black/p/288-00B4-000E3?Item=9SIAXGKH763142&cm_sp=SP-_-1029303-_-Pers_SubCategorySponsoredProduct-_-5-_-9SIAXGKH763142-_-3266-_--_-4"

#   LOCAL FILE TEST          with open("test.html", "r") as f:
#    LOCAL FILE TEST        doc = BeautifulSoup(f, "html.parser")
#    tag = doc.find_all("b")

# FOR API TO COMAPNY DATABASE#

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(text="$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)
