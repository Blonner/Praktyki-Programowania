class TennisGame3:
    def __init__(self, p1_name, p2_name):
        # 1
        self.name1 = p1_name
        self.name2 = p2_name
        self.pts1 = 0
        self.pts2 = 0

    def won_point(self, name):
        # 2
        if name == self.name1:
            self.pts1 += 1
        else:
            self.pts2 += 1

    def score(self):
        # 3
        if self.pts1 < 4 and self.pts2 < 4 and (self.pts1 + self.pts2 < 6):
            txt = ["Love", "Fifteen", "Thirty", "Forty"]
            s1 = txt[self.pts1]
            if self.pts1 == self.pts2:
                return s1 + "-All"
            return s1 + "-" + txt[self.pts2]

        # 4 przewaga
        if self.pts1 == self.pts2:
            return "Deuce"
        leader = self.name1 if self.pts1 > self.pts2 else self.name2
        diff = self.pts1 - self.pts2
        if abs(diff) == 1:
            return "Advantage " + leader
        return "Win for " + leader

# POPRAWKI:
# 1 Zamieniono operatory trzyargumentowe na bloki if.
# 2 Zmieniono nazwy zmiennych p1, p2 na bardziej czytelne.
# 3 Poprawiono warunek logiczny w won_point.
# 4 Uproszczono budowanie napisow wynikowych dla fazy poczatkowej.