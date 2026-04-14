class TennisGame2:
    def __init__(self, player1_name, player2_name):
        self.p1_name = player1_name
        self.p2_name = player2_name
        self.p1_points = 0
        self.p2_points = 0

    def won_point(self, name):
        # 1 dodany punkt
        if name == self.p1_name:
            self.p1_points += 1
        else:
            self.p2_points += 1

    def score(self):
        # 2 remis
        if self.p1_points == self.p2_points:
            if self.p1_points < 3:
                names = ["Love", "Fifteen", "Thirty"]
                return names[self.p1_points] + "-All"
            return "Deuce"

        # 3 wygrana/przewaga
        if self.p1_points >= 4 or self.p2_points >= 4:
            diff = self.p1_points - self.p2_points
            if diff == 1: return "Advantage " + self.p1_name
            if diff == -1: return "Advantage " + self.p2_name
            if diff >= 2: return "Win for " + self.p1_name
            return "Win for " + self.p2_name

        # 4 wyniki
        res = ["Love", "Fifteen", "Thirty", "Forty"]
        return res[self.p1_points] + "-" + res[self.p2_points]

# POPRAWKI:
# 1 Polaczono warunki if sprawdzajace kazdy punkt z osobna.
# 2 Wykorzystano listy do mapowania wartosci punktowych.
# 3 Usunieto zbedne metody p1_score i p2_score.
# 4 Zastapiono sztywne teksty player1 nazwami z konstruktora.