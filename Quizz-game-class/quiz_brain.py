class QuizzBrain:
    def __init__(self, qlist):
        self.qlist = qlist
        self.qnu = 0
        self.score = 0

    def still_has_qn(self):
        return self.qnu < len(self.qlist)

    def check_ans(self, uans, cans):
        if uans == cans.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"The correct answer is {cans}")

    def next_qns(self):
        uans = input(f"Q {self.qnu + 1}. {self.qlist[self.qnu].qns} (True/False) --> ").lower()
        self.check_ans(uans, self.qlist[self.qnu].ans)
        self.qnu += 1

