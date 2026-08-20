class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total = 0 
        scoreboard = []
        for x in operations:
            if x not in {"C","D","+"}:
                scoreboard.append(int(x))
                total += int(x)
            elif x == "+":
                if len(scoreboard) > 1:
                    y = scoreboard[-1]  + scoreboard[-2]
                    scoreboard.append(y)
                    total += y
            elif x == "D":
                if len(scoreboard) > 0:
                    doub = 2 * scoreboard[-1]
                    scoreboard.append(doub)
                    total += doub
            elif x == "C":
                if len(scoreboard) > 0:
                    total -= scoreboard.pop()
        return total