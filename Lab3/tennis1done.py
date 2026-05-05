class TennisGame1:
    def __init__(self, player1_name, player2_name):
        self.p1_name = player1_name
        self.p2_name = player2_name
        self.p1_points = 0
        self.p2_points = 0

    def won_point(self, name):
        # 1 update punktow
        if name == self.p1_name:
            self.p1_points += 1
        else:
            self.p2_points += 1

    def score(self):
        # 2 remis
        if self.p1_points == self.p2_points:
            scores = {0: "Love-All", 1: "Fifteen-All", 2: "Thirty-All"}
            return scores.get(self.p1_points, "Deuce")

        # 3 koniec gry
        if self.p1_points >= 4 or self.p2_points >= 4:
            diff = self.p1_points - self.p2_points
            if diff == 1:
                return f"Advantage {self.p1_name}"
            if diff == -1:
                return f"Advantage {self.p2_name}"
            if diff >= 2:
                return f"Win for {self.p1_name}"
            return f"Win for {self.p2_name}"

        # 4  wyniki
        names = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
        s1 = names[self.p1_points]
        s2 = names[self.p2_points]
        return s1 + "-" + s2


# POPRAWKI:
# 1 Naprawiono bledne przypisywanie punktow dla graczy na podstawie nazw.
# 2 Dodano slowniki do tlumaczenia punktow na tekst.
# 3 Usunieto petle for generujaca wynik punktowy.
# 4 Dodano obsluge dynamicznych nazw graczy zamiast player1 i player2.
