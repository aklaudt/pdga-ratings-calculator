from database import Database
from htmlParsing import HtmlParser
from models import RatedRound
from pdgaRequests import pdgaRequests


def ingestNewMembers(conn, numberToIngest):
    startingPdgaNumber = Database.getHighestPdgaNumberInDb(conn) + 2

    for i in range(startingPdgaNumber, startingPdgaNumber + numberToIngest):
        html = pdgaRequests.getPlayerInfoPage(i)
        htmlInside = html.find("div", {"class", "inside"})
        player = HtmlParser.getPlayerStatusFromInfoPage(html)
        print(player)

        if player is not None:
            Database.addPlayerToDb(conn, player)


def ingestRatedRoundsForActiveMembers(conn):
    tuples = Database.getActivePdgaNumbers(conn)
    pdgaNumbers = list(map(lambda x: x[0], tuples))

    for pdga in pdgaNumbers:
        print(pdga)
        html = pdgaRequests.getPlayerDetails(pdga)

        tableBody = html.find("tbody")

        if tableBody is not None:
            rows = tableBody.find_all("tr")
            for row in rows:
                cells = row.find_all("td")
                tournament = row.find(
                    "td", {"class", "tournament"}).find("a").text
                tier = row.find("td", {"class", "tier"}).text
                date = row.find("td", {"class", "date"}).text

                division = row.find("td", {"class", "division"}).text
                roundNumber = row.find("td", {"class", "round"}).text
                score = row.find("td", {"class", "score"}).text
                rating = row.find("td", {"class", "round-rating"}).text
                evaluated = row.find("td", {"class", "evaluated"}).text
                included = row.find("td", {"class", "included"}).text

                ratedRound = RatedRound(pdga, tournament, tier, date, division,
                                        roundNumber, score, rating, evaluated, included)

                Database.addRatedRoundToDb(conn, ratedRound)
