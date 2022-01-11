import pdgaRequests
from bs4 import BeautifulSoup
from pdgaRequests import pdgaRequests
from database import Database
from htmlParsing import HtmlParser

# pdgaNumber = 1
# playerInfo = pdgaRequests.getPlayerInfoPage(pdgaNumber)

conn = Database.createConnection("./pdga.db")
# Database.dropPlayersTable(conn)
# Database.createPlayersTable(conn)

for i in range(1, 250):
    html = pdgaRequests.getPlayerInfoPage(i)
    htmlInside = html.find("div", {"class", "inside"})
    player = HtmlParser.getPlayerStatusFromInfoPage(html)
    print(player)
    Database.addPlayerToDb(conn, player)
