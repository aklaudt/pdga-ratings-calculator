import pdgaRequests
from bs4 import BeautifulSoup
from pdgaRequests import pdgaRequests
from database import Database
from htmlParsing import HtmlParser
from utils import ingestNewMembers

# pdgaNumber = 1
# playerInfo = pdgaRequests.getPlayerInfoPage(pdgaNumber)

conn = Database.createConnection("./pdga.db")
# Database.dropPlayersTable(conn)
# Database.createPlayersTable(conn)

pdga = 97510
html = pdgaRequests.getPlayerDetails(pdga)
htmlInside = html.find("div", {"class", "inside"})

rows = htmlInside.find_all("tr")
print(rows)