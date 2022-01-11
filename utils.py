from database import Database
from htmlParsing import HtmlParser

def ingestNewMembers(numberToIngest):
    startingPdgaNumber = Database.getHighestPdgaNumberInDb(conn) + 1

    for i in range(startingPdgaNumber, startingPdgaNumber + 25):
        html = pdgaRequests.getPlayerInfoPage(i)
        htmlInside = html.find("div", {"class", "inside"})
        player = HtmlParser.getPlayerStatusFromInfoPage(html)
        print(player)

    if player is not None:
        Database.addPlayerToDb(conn, player)