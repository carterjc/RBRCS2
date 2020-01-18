class Client:

    count = 0

    def __init__(self, citizen):
        self.name = citizen["f_name"] + " " + citizen["l_name"]
        self.occupation = citizen["occupation"]
        self.family = citizen["family"]
        self.income = citizen["income"]
        self.money = citizen["asset_v"]
        self.risk = citizen["risk"]
        self.d_loan = citizen["d_loan"]
        self.d_invest = citizen["d_invest"]
        Client.count -= -1

    def req_loan(self):
        pass

    def req_invest(self, banker):
        pass


class Banker:

    def __init__(self):
        self.strikes = 0
        self.money = 1000

    def give_loan(self):
        pass

    def c_invest(self):
        pass

    def s_invest(self):
        pass

    def appraise(self):
        pass

