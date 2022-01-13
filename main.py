import time
import pdgaRequests
from bs4 import BeautifulSoup
from pdgaRequests import pdgaRequests
from database import Database
from htmlParsing import HtmlParser
from utils import ingestNewMembers
from models import RatedRound

# pdgaNumber = 1
# playerInfo = pdgaRequests.getPlayerInfoPage(pdgaNumber)

conn = Database.createConnection("./pdga.db")

start_time = time.time()
numberOfPlayersToIngest = 150000
ingestNewMembers(conn, numberOfPlayersToIngest)
print("--- %s seconds ---" % (time.time() - start_time))
print((time.time() - start_time) / numberOfPlayersToIngest)
