import pdgaRequests
from bs4 import BeautifulSoup
from pdgaRequests import pdgaRequests

pdgaNumber = 97510
playerInfo = pdgaRequests.getPlayerInfoPage(pdgaNumber)
print(playerInfo)