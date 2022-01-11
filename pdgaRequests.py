import requests
from bs4 import BeautifulSoup

baseUrl = "https://www.pdga.com/"


class pdgaRequests:
    @staticmethod
    def getPlayerInfoPage(pdgaNumber):
        url = baseUrl + "player/" + str(pdgaNumber)
        r = requests.get(url)
        html = BeautifulSoup(r.content, 'html.parser')
        return html

    @staticmethod
    def getPlayerYearlyStats(pdgaNumber, year):
        url = f"{baseUrl}player/{pdgaNumber}/stats/{year}"
        r = requests.get(url)
        html = BeautifulSoup(r.content, 'html.parser')
        return html

    @staticmethod
    def getPlayerDetails(pdgaNumber):
        url = baseUrl + f"player/{pdgaNumber}/stats"
        r = requests.get(url)
        html = BeautifulSoup(r.content, 'html.parser')
        return html

    @staticmethod
    def getPlayerHistory(pdgaNumber):
        url = f"{baseUrl}/player/{pdgaNumber}/history"
        r = requests.get(url)
        html = BeautifulSoup(r.content, 'html.parser')
        return html

    @staticmethod
    def getPlayerCareerWins(pdgaNumber):
        url = f"{baseUrl}/player/{pdgaNumber}/wins"
        r = requests.get(url)
        html = BeautifulSoup(r.content, 'html.parser')
        return html

    @staticmethod
    def getEventtInfoPage(eventNumber):
        url = baseUrl + "tour/event/" + str(eventNumber)
        r = requests.get(url)
        html = BeautifulSoup(r.content, 'html.parser')
        return html
