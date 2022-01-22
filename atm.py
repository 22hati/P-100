class ATM(object):
    card_ID = ""
    balance = 0
    pin_number = ""

    def __init__(self, card_ID, balance, pin_number):
        self.card_ID = card_ID
        self.balance = balance
        if card_ID == "00001":
            self.pin_number = "1234"
        elif card_ID == "00002":
            self.pin_number = "4321"

    def withdraw(self, card_ID, pin_number, amount):
        self.card_ID = card_ID

        temp = ""
        if card_ID == "00001":
            temp = "1234"
        elif card_ID == "00002":
            temp = "4321"

        self.pin_number = pin_number
        if pin_number != temp:
            print("pin number does not exist!")
        else:
            self.amount = amount
            self.balance = int(self.balance)-int(self.amount)
            print("transaction complete")

    def check(self):
        print(self.balance)

p1 = ATM("00001", 10000, "1234")
p2 = ATM("00002", 10000, "4321")

