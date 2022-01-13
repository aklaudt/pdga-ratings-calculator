class Player:
    def __init__(self, pdgaNo, name, status, yearStarted, classifaction, officialStatus, officialStatusExpiration, currentRating, careerEvents, careerEarnings, location, membershipExpired):
        self.pdgaNumber = pdgaNo
        self.name = name
        self.status = status
        self.membershipExpired = membershipExpired
        self.yearStarted = yearStarted
        self.classification = classifaction
        self.officialStatus = officialStatus
        self.officialStatusExpiration = officialStatusExpiration
        self.currentRating = currentRating
        self.careerEvents = careerEvents
        self.careerEarnings = careerEarnings
        self.location = location

    def __str__(self):
        return f"{self.pdgaNumber}: {self.name}"


class RatedRound:
    def __init__(self, pdgaNumber, tournament, tier, date, division, roundNumber, score, rating, evaluated, included):
        self.pdgaNumber = pdgaNumber
        self.tournament = tournament
        self.tier = tier
        self.date = date
        self.division = division
        self.roundNumber = roundNumber
        self.score = score
        self.rating = rating
        self.evaluated = evaluated
        self.included = included

    def __str__(self):
        return f"{self.tournament} {self.date}"
