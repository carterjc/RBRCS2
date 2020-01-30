import random


class Client:

    count = 0

    def __init__(self, citizen):
        self.name = citizen["f_name"] + " " + citizen["l_name"]
        self.age = citizen["age"]
        self.gender = citizen["gender"]
        self.occupation = citizen["occupation"]
        self.family = citizen["family"]
        self.income = citizen["income"]
        self.asset_v = citizen["asset_v"]
        self.risk = citizen["risk"]
        self.d_loan = citizen["d_loan"]
        self.d_invest = citizen["d_invest"]
        Client.count -= -1

    def give_info(self, loan):
        job_sentiment = "fun" if random.randint(0, 1) == 0 else "eh - a little annoying"
        pay_sentiment = "good" if self.income > 80000 else "alright, but it could be better"
        gender = "male" if self.gender == 1 else "female"
        risk = "high" if self.risk == 3 else ("medium" if self.risk == 2 else "low")
        print(f"""
Hey there. I'm {self.name}. I guess I'll tell you a little about myself.
So, I'm {self.age} and a {self.occupation}. It's pretty {job_sentiment}. It pays {pay_sentiment}.
Anyways, I'm looking to make some more money and here are my financials.\n\n
Income: ${self.income:,d}
Asset Value: ${self.asset_v:,d}
Risk Tolerance: {risk.capitalize()}""")
        if loan:
            print(f"Requested Loan: ${self.d_loan:,d}")
        else:
            print(f"Requested Investment: ${self.d_invest:,d}")
        print("\nSo, what are you thinking? I really want the money.\n\n----")


class Banker:

    def __init__(self):
        self.strikes = 0
        self.money = 1000


