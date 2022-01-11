from player import Player


class HtmlParser:
    @staticmethod
    def getYearsPlayedFromInfoPage(html):
        mainHeader = html.findAll("h1")[0]

        if(mainHeader.text != "Page not found" and mainHeader.text != "Access denied"):

            yearLink = html.findAll("ul", {"class", "tabs secondary"})[0]
            yearsTags = yearLink.find_all("li")
            years = []

            for yearTag in yearsTags:
                years.append(yearTag.find("a").text)
            return years


    @staticmethod
    def getPlayerStatusFromInfoPage(html):
        mainHeader = html.findAll("h1")[0]

        if(mainHeader.text != "Page not found" and mainHeader.text != "Access denied"):
            (name, pdgaNumber) = mainHeader.text.split("#")
            playerInfoList = html.find("ul", {"class", "player-info"})

            listItem = playerInfoList.find(
                "li", {"class", "location"}).find("a")

            if listItem is not None:
                location = listItem.text.split(": ")[0]
            else:
                location = None

            listItem = playerInfoList.find("li", {"class", "classification"})

            if listItem is not None:
                classification = listItem.text.split(" ")[2]
            else:
                classification = None

            listItem = playerInfoList.find("li", {"class", "join-date"})

            if listItem is not None:
                memberSince = listItem.text.split(" ")[2]
            else:
                memberSince = None

            listItem = playerInfoList.find(
                "li", {"class", "membership-status"})

            if listItem is not None:
                membershipStatus = listItem.text.split(" ")[3]

                if(membershipStatus == "Eagle"):
                    membershipStatus = "Eagle Club"
                    membershipExpired = listItem.text.split(" ")[6][:-1]
                else:
                    membershipExpired = listItem.text.split(" ")[5][:-1]
            else:
                membershipStatus = None
                membershipExpired = None

            listItem = playerInfoList.find("li", {"class", "official"})

            if listItem is not None:
                officialStatus = listItem.text.split(" ")[3]
                officialStatusExpiration = listItem.text.split(" ")[5][:-1]
            else:
                officialStatus = None
                officialStatusExpiration = None

            listItem = playerInfoList.find("li", {"class", "current-rating"})

            if listItem is not None:
                currentRating = listItem.text.split(" ")[3]
            else:
                currentRating = None

            listItem = playerInfoList.find("li", {"class", "career-events"})

            if listItem is not None:
                careerEvents = listItem.text.split(" ")[2]
            else:
                careerEvents = None

            listItem = playerInfoList.find("li", {"class", "career-earnings"})

            if listItem is not None:
                careerEarnings = listItem.text.split(" ")[2]
            else:
                careerEarnings = None

            player = Player(pdgaNumber, name, membershipStatus,
                            memberSince, classification, officialStatus, officialStatusExpiration, currentRating, careerEvents, careerEarnings, location, membershipExpired)
            return player
